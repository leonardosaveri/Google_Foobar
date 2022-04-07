# Bomb, Baby
def solution(m, f):
    m, f = int(m), int(f)
    if max(m, f) % min(m, f) == 0 and min(m, f) != 1:
        return "impossible"
    t = 0
    while m != 1 or f != 1:
        if f <= 0 or m <= 0:
            return "impossible"
        if min(m, f) == 1:
            return str(t + max(m, f) - 1)
        else:
            t += m//f
            m, f = f, m % f
    return str(t)
