import sys 
from math import *
def numLen(num):
  return len(str(abs(num)))
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return floor(n * multiplier) / multiplier

def main2():
    # creating an empty list 
    inputlst = [] 
    outputList=[]
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
    for i in range(0, n): 
        ele = int(input()) 
        inputlst.append(ele) # adding the element 
        if (i==0):
            outputList.append(ele)  
        else:
            temp= outputList[-1]
            lenOftemp =numLen(temp)
            lenOfele =numLen(ele)
            newtemp =temp/(10**lenOftemp)
            newele =ele/(10**lenOfele)
            if(lenOftemp== lenOfele ):
                if(ele> temp):                
                    outputList.pop()
                    outputList.append(ele)
                    outputList.append(temp)
                else:
                    outputList.append(ele)
            elif lenOftemp>lenOfele :
               
                if (newtemp >= newele):
                    outputList.pop()
                    outputList.append(ele)
                    outputList.append(temp) 
                else:
                    outputList.append(ele)
            else:
                if (newtemp >= newele):
                    outputList.pop()
                    outputList.append(ele)
                    outputList.append(temp) 
                else:
                    outputList.append(ele)
    print(*outputList)
   

def main():
    # creating an empty list 
    inputlst = [] 
    outputList=[]
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
    for i in range(0, n): 
        ele = int(input()) 
        inputlst.append(ele) # adding the element 
        if (i==0):
            outputList.append(ele)  
        else:
            compareele =ele
            for j in range(len(outputList)):
                temp= outputList[j]
                lenOftemp =numLen(temp)
                lenOfele =numLen(compareele)
                newtemp =temp/(10**lenOftemp)
                newele =compareele/(10**lenOfele)
                if(lenOftemp== lenOfele and compareele> temp ) or (lenOftemp>lenOfele and  newele<=round_down(newtemp)) or (lenOftemp<lenOfele and newtemp < round_down(newele,1)):
                    tempswap = temp
                    outputList[j]=compareele
                    compareele= tempswap                 
            outputList.append(compareele)
    print (*outputList)




main()


