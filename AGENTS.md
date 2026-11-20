# AGENTS.md — opencharly/Qwen3-TTS (fork)

This is the OpenCharly fork of `QwenLM/Qwen3-TTS`. The authoritative rulebook is the
umbrella `AGENTS.md` in [opencharly/opencharly](https://github.com/opencharly/opencharly):
Part I (R0–R11) and Part II. This file adds only the rules specific to this fork.

## Read first

- `FORK.md` — why the fork exists, what diverges, and how upstream is synced.
- `NOTICE` — the modified-file list required by Apache-2.0 §4(b).
- The umbrella `/charly-internals:git-workflow` before any git/PR action.

## Rules specific to this repo

- **Do not reformat upstream files.** Changes stay minimal and localized; an unrelated
  formatting sweep makes the next upstream merge a conflict.
- **Mark every modified upstream file** with a `Modified by opencharly, <year>: <what>`
  notice, and add it to `NOTICE`.
- **Never open a PR or issue against `QwenLM/Qwen3-TTS`.** Everything lands inside the
  `opencharly` org. Upstream sync is a merge PR inside this fork.
- **Keep the package import surface stable** (`qwen_tts`, `qwen-tts`,
  `qwen_tts.inference.qwen3_tts_model.Qwen3TTSModel`, `generate_custom_voice`) — the
  consumer `opencharly/pod-qwen3-tts` depends on it.
- **Tests are part of the change.** The CI workflow runs the unit tests; a behaviour
  claim without a test that can fail is not landable.
- **The org ruleset applies here** (it targets this fork), so `main` is protected and
  `validate / validate` is required. The CalVer tag is minted by the per-repo
  `tag-on-merge.yml` caller.
- **License discipline:** Apache-2.0 `LICENSE` verbatim, no Qwen/Alibaba endorsement,
  new files carry a charly copyright + SPDX header.

## Landing

PR-only. A `feat/` branch off fresh `origin/main`; the org `charly/pr-validator` is the
gate and arms native auto-merge on a PASS. History lives in `CHANGELOG/` (written by
tag-on-merge from the PR body) — the PR body IS the changelog.
