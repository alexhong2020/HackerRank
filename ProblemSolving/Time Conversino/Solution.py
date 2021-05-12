#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    str0 = ""
    
    if s[-2] == "P" and s[0:2] < "12":
        str0 = str(int(s[0:2]) + 12) + s[2:-2]
        
    elif s[-2] == "A" and s[0:2] == "12":
        str0 = "00" + s[2:-2]
    
    else:
        str0 = s[0:-2]
    
    return str0
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

