# coding=utf-8
# Copyright 2026 The Alibaba Qwen team.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
qwen_tts: Qwen-TTS package.

Modified by opencharly, 2026: define ``__version__``, export the public classes, and
resolve those classes lazily so importing the package does not pull torch/sox. The
upstream file named a nonexistent ``__version__`` in ``__all__`` and omitted the
public classes from it.
"""

from importlib import import_module
from importlib.metadata import PackageNotFoundError, version as _dist_version
from typing import Any

try:
    __version__ = _dist_version("qwen-tts")
except PackageNotFoundError:  # running from a source tree without an install
    __version__ = "0.1.1.post1"

__all__ = [
    "Qwen3TTSModel",
    "VoiceClonePromptItem",
    "Qwen3TTSTokenizer",
    "__version__",
]

_LAZY = {
    "Qwen3TTSModel": (".inference.qwen3_tts_model", "Qwen3TTSModel"),
    "VoiceClonePromptItem": (".inference.qwen3_tts_model", "VoiceClonePromptItem"),
    "Qwen3TTSTokenizer": (".inference.qwen3_tts_tokenizer", "Qwen3TTSTokenizer"),
}


def __getattr__(name: str) -> Any:
    target = _LAZY.get(name)
    if target is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    value = getattr(import_module(target[0], __name__), target[1])
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(__all__))