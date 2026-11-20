# Copyright 2026 opencharly
# SPDX-License-Identifier: Apache-2.0
"""Exercises the generate_custom_voice CALL SITE, not only the policy helper.

Reverting the call site to the upstream `instruct = None` makes this test fail.
"""

import importlib.machinery
import sys
import types
import warnings
from unittest.mock import MagicMock

import pytest

# The tokenizer's import chain imports sox/onnxruntime; this test never touches the
# tokenizer, so stub them when the environment lacks the audio stack. The stub carries a
# real ModuleSpec because torch's dynamo trace_rules calls find_spec on installed modules.
for _name in ("sox", "onnxruntime"):
    try:
        __import__(_name)
    except Exception:
        _stub = types.ModuleType(_name)
        _stub.__spec__ = importlib.machinery.ModuleSpec(_name, loader=None)
        sys.modules[_name] = _stub

import qwen_tts.inference.qwen3_tts_model as model_module  # noqa: E402


class _StopAfterGuard(Exception):
    """Raised by the patched validator once the changed call site has run."""


def _fake_instance(size: str):
    obj = object.__new__(model_module.Qwen3TTSModel)
    model = MagicMock()
    model.tts_model_type = "custom_voice"
    model.tts_model_size = size
    model.tokenizer_type = "qwen3-tts-tokenizer-v2"
    obj.model = model
    return obj


def _stop_at_validation(monkeypatch):
    monkeypatch.setattr(
        model_module.Qwen3TTSModel,
        "_validate_languages",
        lambda self, languages: (_ for _ in ()).throw(_StopAfterGuard()),
    )


def test_generate_custom_voice_warns_at_the_call_site(monkeypatch):
    _stop_at_validation(monkeypatch)
    with pytest.warns(UserWarning, match="0.6B"):
        with pytest.raises(_StopAfterGuard):
            _fake_instance("0b6").generate_custom_voice(
                text="hi", speaker="vivian", instruct="angry"
            )


def test_generate_custom_voice_does_not_warn_for_larger_models(monkeypatch):
    _stop_at_validation(monkeypatch)
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        with pytest.raises(_StopAfterGuard):
            _fake_instance("1b7").generate_custom_voice(
                text="hi", speaker="vivian", instruct="angry"
            )
