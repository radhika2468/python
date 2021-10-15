import string
import os
import math
# Complete the solve function below.
def solve(s):
    count=0
    m=0
    listi=[]
    mylist=list(s)
    k=s[0].upper()
    for letter in mylist:
       count=count+1
    for i in range(0,count):
         if i==0:
            r=mylist[0].upper()
            listi.append(r)
         elif mylist[i]==" ":
            listi.append(mylist[i])
            m=i+1
         elif i==m:
            listi.append(mylist[i].upper())
         else:
            listi.append(mylist[i])
    s="".join(listi) 
    return s

