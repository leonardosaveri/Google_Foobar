# Find the access codes
def solution(l):
    # first I want to check if there are at least 3 numbers
    if len(l) < 3:
        return 0
    count = 0
    for i in range(1, len(l) - 1):
        '''
        I compute the numbers of elements on the left
        that are divisors of a given element l[i]
        '''
        countX = len([x for x in l[:i] if l[i] % x == 0])
        '''
        I compute the numbers of elements on the right
        that are divisible by the given element l[i]
        '''
        countZ = len([z for z in l[i + 1:] if z % l[i] == 0])
        '''
        To count the total, we multiply them.
        If either the left (countX) or the right count(Z)
        are 0, count will not be updated (no lucky triplets)
        If they are not 0, the multiplication gives the total
        number of lucky triplets given an element l[i]
        '''
        count += countX * countZ
    return count
