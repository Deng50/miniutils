"""miniutils CLI entry point.

Each contributor adds their command between the REGISTER markers below.
"""
import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="miniutils",
        description="A small CLI toolbox.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # === REGISTER:BEGIN ===
    from miniutils.commands import weather
    weather.register(subparsers)

    from miniutils.commands import todo
    todo.register(subparsers)
    from miniutils.commands import convert
    convert.register(subparsers)
    # === REGISTER:END ===

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handler = getattr(args, "handler", None)
    if handler is None:
        parser.print_help()
        return 1
    return handler(args) or 0


if __name__ == "__main__":
    sys.exit(main())
