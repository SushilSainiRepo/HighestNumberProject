
from math import * 

def ArrangeIT(inputlst):
    outputList=[]
    for i in range(len(inputlst)): 
        ele = inputlst[i]
        if (i==0):
            outputList.append(ele)  
        else:
            compareele =ele
            for j in range(len(outputList)):
                temp= outputList[j]
                lenOftemp =numLen(temp)
                lenOfele =numLen(compareele)
                newtemp =int(str(temp)+ str(compareele))
                newele =int(str(compareele)+ str(temp))
                if(  newele>=newtemp):
                    tempswap = temp
                    outputList[j]=compareele
                    compareele= tempswap                 
            outputList.append(compareele)
    result= ''
    for element in outputList:
        result += str(element)
    return result
def main():
    # creating an empty list 
    inputlst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
    for i in range(0, n): 
            number = int(input()) 
            inputlst.append(round(number))
    # Ans=ArrangeDigits(inputlst)
    outputlist= ArrangeIT(inputlst)
    print(outputlist)
    # print(Ans)

main()



def ArrangeAllDigits(lst):
    ilst = [] 
    for i in range(len(lst)): 
        number = lst[i] 
        while (number >= 10):
            digit = math.remainder(number, 10)
            ilst.append(digit)
            number = (number-digit) / 10 
            # adding the element 
        ilst.append(round(number))
    ilst.sort()
    answer=0
    for j in range(len(ilst)):
        answer=answer+ilst[j] * 10**j 
    return (round(answer))

def numLen(num):
  return len(str(abs(num)))
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return floor(n * multiplier) / multiplier
