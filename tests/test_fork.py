# Copyright 2026 opencharly
# SPDX-License-Identifier: Apache-2.0
"""Tests for the opencharly fork's changes (see NOTICE)."""

import warnings

import pytest

import qwen_tts
from qwen_tts.inference.instruct import resolve_instruct


def test_version_is_defined():
    assert isinstance(qwen_tts.__version__, str)
    assert qwen_tts.__version__


def test_public_classes_are_exported():
    for name in ("Qwen3TTSModel", "VoiceClonePromptItem", "Qwen3TTSTokenizer", "__version__"):
        assert name in qwen_tts.__all__, f"{name} missing from __all__"


def test_instruct_warns_on_the_0b6_model():
    with pytest.warns(UserWarning, match="0.6B"):
        assert resolve_instruct("0b6", "an angry voice") is None


def test_instruct_is_unchanged_off_the_0b6_model():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert resolve_instruct("1b7", "an angry voice") == "an angry voice"
        assert resolve_instruct("0b6", None) is None
