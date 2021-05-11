#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minv = 1000000000
    maxv = 1
    totsum = 0
    minsum = 0
    maxsum = 0
    
    
    for k in range(len(arr)):
        if (arr[k] < minv):
            minv = arr[k]
        
        if (arr[k] > maxv):
            maxv = arr[k]
        
        totsum += arr[k]
    

    minsum = totsum - maxv
    maxsum = totsum - minv
        
    print(minsum, maxsum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

