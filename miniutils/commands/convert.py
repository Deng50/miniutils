"""Unit converter — distance only, for demo."""

RATES = {
    ("km", "mile"): 0.621371,
    ("mile", "km"): 1.609344,
    ("m", "ft"): 3.28084,
    ("ft", "m"): 0.3048,
}

def register(subparsers):
    p = subparsers.add_parser("convert", help="Convert units, e.g. 10 km mile")
    p.add_argument("value", type=float)
    p.add_argument("src")
    p.add_argument("dst")
    p.set_defaults(handler=run)

def run(args):
    rate = RATES.get((args.src, args.dst))
    if rate is None:
        print(f"Unsupported: {args.src} -> {args.dst}")
        return 1
    print(f"{args.value} {args.src} = {args.value * rate:.4f} {args.dst}")
    return 0