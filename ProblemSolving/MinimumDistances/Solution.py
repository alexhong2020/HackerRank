#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    min_dist = 1000
    
    thisdict = {}
    
    for i in range(len(a)):
        if not a[i] in thisdict:
            thisdict[a[i]] = i
        else:
            dist = i - thisdict[a[i]]
            
            if dist < min_dist:
                min_dist = dist
                
    if min_dist == 1000:
        return -1
    
    return min_dist
                  
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

