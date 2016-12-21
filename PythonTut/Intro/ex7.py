def isLeapYear(theYear):
    ans = False

    if(theYear % 4 == 0):

        if(theYear % 100 != 0):
            ans = True
        elif(theYear % 100 == 0 and theYear % 400 ==0):
            ans = True    

    return ans

inp = int(input())
print(isLeapYear(inp))
