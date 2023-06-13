#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    a,b,c,d,e,f,g = [None]*7
    sumx = None
    for i in range(len(arr)-2):
        row1 = arr[i]
        row2 = arr[i+1]
        row3 = arr[i+2]
        for var in range(len(arr[i])-2):
            a = row1[var]
            b = row1[var+1]
            c = row1[var+2]
            d = row2[var+1]
            e = row3[var]
            f = row3[var+1]
            g = row3[var+2]
            if sumx == None:
                sumx = a+b+c+d+e+f+g
            if a+b+c+d+e+f+g > sumx:
                sumx=a+b+c+d+e+f+g
    return sumx
         
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
