
import string
import math
def wrap(string,max_width):
    m=0
    r=0
    k=""
    for i in range(max_width,max_width+len(string),max_width):
       k=k+string[m:i]+"\n"
       m=m+max_width
    return k 