# Bunny prisoner location
def solution(x, y):
	return x + [(x + y - 2) * (x + y - 1) ] / 2
