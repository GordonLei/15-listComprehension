'''
Write a function that uses list comprehension to return whether a password meets a minimum threshold: 
it contains a mixture of upper- and lowercase letters, and at least one number

Write a function that uses list comprehension to return a password's strength rating. 
This function should return a lower integer for a weak password and a higher integer for a stronger password. (Suggested scale: 1-10) Consider these criteria:
mixture of upper- and lower-case
inclusion of numerals
inclusion of these non-alphanumeric chars: . ? ! & # , ; : - _ *
'''
def isMinimum(password):
    newList = [1 if x.islower() else 2 if x.isupper() else 3 if x.isdigit() else 0 for x in str(password)]
    return (1 in newList and 2 in newList and 3 in newList)

print isMinimum("abc")
print isMinimum("12132")
print isMinimum("dsads12132")
print isMinimum("123AbC123")

def strength(password):
    if not(isMinimum(password)):
        return 0
    else:
        characterList = [x for x in ". ? ! & # , ; : - _ *" if x != " "]
        newList = [1 if x.islower() else 2 if x.isupper() else 3 if x.isdigit() else 4 if x in characterList else 0 for x in str(password)]
        # Max score would be 4 points in one space (so max score is 4points * lenght of password + other required chars)
        # Multiply 10 by that fraction to hit a max of 10 (sum is always less than 4*len(password))
        return (11 * sum(newList)/(4*len(password)))
print strength("1aB.")
print strength("1Ab..........DSADDA.")
print strength("1Ab........................")
print strength("1Abccccccccc")
print strength("InsertMyPasswordHere404")