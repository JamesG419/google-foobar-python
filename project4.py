'''
Applies solution to Bomb Baby

M and F are arbitrarily large integers. Returns string with number of generations it took.
Otherwise returns Impossible



'''

def answer(M,F):

    M = int(M)
    F = int(F)
    gen = 0
    
    #counter function
    def counter(larger,smaller):

        count = int(larger/smaller)
        
        if (smaller == 1):
            count = count - 1

        return count

    def remainder(larger,smaller,cou):

        rem = larger - smaller*cou
        
        #if (smaller == 1):
        #    rem = rem + 1

        return rem
    
    while (M >= 1 and F >= 1):
        if (M == 1 and F == 1):
            return str(gen)
        elif (M == 0 or F == 0):
            return 'impossible'

        else:
            if (M > F):
                count = counter(M,F)
                M = remainder(M,F,count)
                gen += count
                
            else:
                count = counter(F,M)
                F = remainder(F,M,count)
                gen += count
        
print(answer('2','4'))
