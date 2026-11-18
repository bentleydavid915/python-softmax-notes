import math

def solve(value):
    return (lambda e: [x/math.fsum(e) for x in e])([math.exp(x-max(value)) for x in value]) if value else []
