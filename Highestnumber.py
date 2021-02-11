
import math as math
def ArrangeIt(lst):
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

def main():
    # creating an empty list 
    inputlst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
    for i in range(0, n): 
            number = int(input()) 
            inputlst.append(round(number))
    Ans=ArrangeIt(inputlst)
    print(Ans)

main()