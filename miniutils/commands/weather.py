"""Weather command — pretend to fetch weather (mock data)."""

MOCK = {
    "beijing": "Sunny, 25°C",
    "shanghai": "Cloudy, 22°C",
    "shenzhen": "Rainy, 28°C",
}

def register(subparsers):
    p = subparsers.add_parser("weather", help="Show mock weather for a city")
    p.add_argument("city", help="City name, e.g. beijing")
    p.set_defaults(handler=run)

def run(args):
    city = args.city.lower()
    print(MOCK.get(city, f"No data for {args.city}"))
    return 0
