"""Todo command — in-memory todo (resets each run; demo only)."""
import json
from pathlib import Path

STORE = Path.home() / ".miniutils_todo.json"

def _load():
    if STORE.exists():
        return json.loads(STORE.read_text(encoding="utf-8"))
    return []

def _save(items):
    STORE.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")

def register(subparsers):
    p = subparsers.add_parser("todo", help="Manage a tiny todo list")
    p.add_argument("action", choices=["add", "list", "done"])
    p.add_argument("text", nargs="?", help="Todo text (for add) or index (for done)")
    p.set_defaults(handler=run)

def run(args):
    items = _load()
    if args.action == "add":
        if not args.text:
            print("Need text to add.")
            return 1
        items.append({"text": args.text, "done": False})
        _save(items)
        print(f"Added: {args.text}")
    elif args.action == "list":
        if not items:
            print("(empty)")
        for i, it in enumerate(items):
            mark = "x" if it["done"] else " "
            print(f"[{mark}] {i}. {it['text']}")
    elif args.action == "done":
        idx = int(args.text)
        items[idx]["done"] = True
        _save(items)
        print(f"Done: {items[idx]['text']}")
    return 0