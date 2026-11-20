# OpenCharly fork of Qwen3-TTS

This repository is `opencharly/Qwen3-TTS`, a fork of
[`QwenLM/Qwen3-TTS`](https://github.com/QwenLM/Qwen3-TTS). It exists for the reasons
below and is consumed by `opencharly/pod-qwen3-tts` as a pinned git source.

## Why a fork

- Upstream publishes **no tags and no releases**, so PyPI `0.1.1` is the only version
  handle it offers. A fork gives the org an owned, taggable source handle.
- `Qwen3TTSModel.generate_custom_voice` silently sets `instruct = None` when the
  checkpoint is the 0.6B model. The pod's default checkpoint is the 0.6B CustomVoice
  model, so the style-control feature is a no-op that looks applied. The fork warns
  instead of discarding silently (it still discards — the 0.6B model does not honour it).

## What differs from upstream

See [`NOTICE`](NOTICE) for the file-by-file list. In short:

- `__version__` is defined and the public classes are exported from `qwen_tts`; they are
  resolved lazily, so importing the package does not pull torch/sox (upstream imported them
  eagerly).
- The instruction policy lives in `qwen_tts/inference/instruct.py`: supplying `instruct`
  to the 0.6B checkpoint now warns that the value is ignored.
- `py.typed` ships (upstream's `package-data` declared it but the file was absent).
- Project URLs point at this fork, with an `Upstream` link.
- The fork version is `0.1.1.post1`.
- Tests and CI are added (upstream has no build/test CI).

## Syncing upstream

- Keep the `upstream` remote: `git remote add upstream https://github.com/QwenLM/Qwen3-TTS.git`.
- Because this fork diverges, sync by a **local merge PR inside this fork**: branch
  `feat/sync-upstream-<YYYY-MM>`, merge `upstream/main`, run CI, land through the org
  gate. Do **not** use `gh repo sync` (the org ruleset's `workflows` rule blocks it).
- Never open a PR or issue against `QwenLM/Qwen3-TTS`; this fork is the only place for
  changes. Upstream gaps are recorded here.

## License

Apache-2.0. The upstream `LICENSE` and all copyright notices are retained verbatim;
modified files carry a change notice, and `NOTICE` records the divergence.
