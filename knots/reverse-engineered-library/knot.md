---
name: Reverse Engineered Library
slug: reverse-engineered-library
origin: [F43L22]
---

# Reverse Engineered Library

An index of reverse-engineered and opened-up software: game decompilations, recompilations,
emulators, official source releases, and specs — with what each project needs to move forward.

Wyrd **links**; the code lives in each project's own repository.

## What belongs here

| type | what |
|---|---|
| `decomp` | rebuilt as source that compiles to the original binary |
| `recomp` | binary translated to run natively on another platform |
| `emulator` | hardware emulation |
| `source-release` | creator published their own code or weights |
| `spec` | file formats, protocols, hardware documentation |

## Rules

Fylgja removes anything that breaks these — no vote needed.

1. **Code only.** No ROMs, game assets, BIOS files or keys. Users **bring their own copy**.
2. **No leaked or stolen source.** Clean-room work or official releases only.
3. **No copy-protection circumvention tools.**
4. **Link, don't host.** Point to the project's own repo.
5. **Credit the original project and its authors** in every Thread.

## Thread fields

Required: `title`, `knot`, `status`, `needs`, plus:

- `type` — one of the types above
- `platform` — e.g. N64, PS2, Switch, x86
- `legal` — e.g. `clean-room, bring-your-own-rom` or `official-release`
- `progress` — 0–100, if the project tracks it
