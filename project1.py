'''
Translating project 1 of the google-foobar challenge from Java to python
Takes a list of sorted integers and an integer as input

returns a final string that ignores any number that shows up more than the integer number of times
'''

def answer(numbers, integer):

    numberCounts = {}
#count number of times a number appears in list
    for number in numbers:
        numberCounts.setdefault(number,0)
        numberCounts[number] +=1

    
    final = []
#create final list ignoring any number that appears more than number times
    for number in numbers:
        currentCount = numberCounts[number]
        if (currentCount <= integer):
            final.append(number)

    return final


print(answer([1,2,3,3,4,5],1))
