"""Quote command."""
import random

q = [
    "Stay hungry, stay foolish.",
    "Talk is cheap. Show me the code.",
    "Premature optimization is the root of all evil.",
]

def register(s):
    p = s.add_parser("quote", help="Print a random quote")
    p.set_defaults(handler=r)

def r(a):
    print(random.choice(q))