'''
Input integer 1 to infinite

Follows these 4 rules: 
1. The first minion gets 1 Lamb and there will always be at least one team member.
2. The next minion in line cannot be given more than double the amount the  previous minion received.
3. A minion cannot be given less than the sum for the previous two minions (this rule doesn’t affect the first minion and the second minion only needs to make equal or more than minion 1).
4. You must always add better paid minions, as long as you follow the previous rules.

Returns the differecne between how many are paid on the most stingy payment scheme and the most generous

'''
import math

def answer(integer):
    geoCounter = 1
    fibCounter = 1

#geometric counter
    geoCounter = int(math.log2(integer+1))
    geoSum = 2**geoCounter - 1
    remainder = integer - geoSum
    prev1 = 2**(geoCounter - 1) -1
    prev2 = 2**(geoCounter - 2) -1
    if (remainder >= prev1 + prev2):
        geoCounter += 1


#fibonacci counter
    current = 1
    previous = 0
    fibSum = current + previous
    fibCounter = 1
    
    while (fibSum <= integer):
        future = current + previous
        fibSum += future

        if (fibSum <= integer):
            fibCounter += 1

        previous = current
        current = future

    difference = fibCounter - geoCounter

    return difference

print(answer(13))
