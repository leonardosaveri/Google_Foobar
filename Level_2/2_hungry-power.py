# Hungry Power
def solution(x):
    if len(x) == 1:
        return str(x[0])

    max_neg = max([i for i in x if i < 0]) if len([i for i in x if i < 0]) != 0 else 1 # find the greatest negative number
    count_neg = len([i for i in x if i < 0])  # find the number of negative numbers
    count_zero = x.count(0)  # count the zeroes

    # If all elements are 0
    if count_zero == len(x):
        return 0

    prod = 1
    for i in range(len(x)):
        if x[i] == 0:
            continue

        prod = prod * x[i]

    if count_neg % 2 != 0:
        # if all zeroes but one element (negative)
        if count_neg == 1 and count_zero > 0 and count_zero + count_neg == len(x):
            return 0
        # else we divide the total product by the maximum negative value
        prod = prod // max_neg

    return str(prod)
