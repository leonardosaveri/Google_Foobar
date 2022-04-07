# The greatest staircase of them all
def solution(n):
    staircases = [1] + [0] * n
    for brick in range(1, n+1):
        for height in range(n, brick-1, -1):
            staircases[height] += staircases[height-brick]
    return staircases[n] - 1
