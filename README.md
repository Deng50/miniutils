# miniutils

A small Python CLI toolbox — built as a hands-on demo for multi-person Git workflow (branches, PRs, code review, conflict resolution).

## Install (dev)

```bash
pip install -e .
```

## Usage

```bash
miniutils --help
```

## Available commands

<!-- COMMANDS:BEGIN -->
- `miniutils weather <city>` — show mock weather (by Alice)
- `miniutils todo add|list|done` — tiny todo list (by Bob)
- `miniutils convert <value> <src> <dst>` — unit converter (by Carol)
<!-- COMMANDS:END -->

## Contributing

1. Create a feature branch: `git checkout -b feature/<your-module>`
2. Add your command in `miniutils/commands/<name>.py`
3. Register it in `miniutils/cli.py`
4. Add a line under "Available commands" above
5. Open a PR against `main`
