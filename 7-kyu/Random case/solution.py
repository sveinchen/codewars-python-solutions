def random_case(x):
    import random
    s = ''
    for c in x:
        if random.choice([True, False]):
            s += c.upper()
        else:
            s += c.lower()
    return s
