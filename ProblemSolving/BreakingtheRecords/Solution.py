#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    
    minimum = scores[0]
    maximum = scores[0]
    minct = 0
    maxct = 0
    
    for i in range(1, len(scores)):
        if scores[i] < minimum:
            minimum = scores[i]
            minct += 1
        if scores[i] > maximum:
            maximum = scores[i]
            maxct += 1
    
    x = [maxct, minct]
    return x
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
