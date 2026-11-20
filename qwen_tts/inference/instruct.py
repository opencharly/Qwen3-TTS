# Copyright 2026 opencharly
# SPDX-License-Identifier: Apache-2.0
"""Instruction policy for the Qwen3-TTS checkpoints (opencharly fork).

Kept dependency-free so the policy is unit-testable without torch/sox.
"""

import warnings
from typing import Any


def resolve_instruct(tts_model_size: str, instruct: Any) -> Any:
    """Return the instruction to use, warning when the 0.6B checkpoint cannot honour it.

    Modified by opencharly, 2026: upstream silently set ``instruct = None`` for the
    0.6B model. The value is still discarded (that checkpoint does not honour it), but
    the caller is told instead of being left believing the style was applied.
    """
    if instruct and tts_model_size in "0b6":
        warnings.warn(
            "instruct is not supported by the 0.6B Qwen3-TTS checkpoint; the supplied "
            "instruction is ignored. Use a 1.7B CustomVoice checkpoint for instruction control.",
            UserWarning,
            stacklevel=3,
        )
        return None
    return instruct
