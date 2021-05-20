#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    totpairs = 0
    
    
    for i in range(n - 1):
        count = 1
        if ar[i] != 0:
            for j in range(i + 1, n):
                if ar[j] == ar[i]:
                    count += 1
                    #flag to not double count it
                    ar[j] = 0
                
        totpairs += count // 2
        
    return totpairs
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

