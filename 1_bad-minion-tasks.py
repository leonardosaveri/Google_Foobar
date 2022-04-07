# Bad minion tasks
def solution(data, n):
    return [i for i in data if data.count(i) <= n]
