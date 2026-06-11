"""Smoke test — make sure the CLI parser at least builds."""
from miniutils.cli import build_parser


def test_parser_builds():
    parser = build_parser()
    assert parser.prog == "miniutils"
