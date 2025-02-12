#!/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'findTheString' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY lcp as parameter.


def findTheString(lcp):
    # Write your code here
   
    # here we are getting the length of the input string
    n_length = len(lcp)
   
    # forming a string array, by the length of input
    string_array = [""] * n_length
   
    # setting index for loop
    index = 0
    # assuming only checking for lowercase characters
    lowercase_characters = "abcdefghijklmnopqrstuvwxyz"
   
    for char in lowercase_characters:
        while index < n_length and string_array[index]:
            index += 1
        if index == n_length:
            break
        for j_index in range(index, n_length):
            if lcp[index][j_index]:
                string_array[j_index] = char    
   
    if "" in string_array:
        return ""
   
    for i in range(n_length - 1, -1, -1):
        for j in range(n_length - 1, -1, -1):
            if string_array[i] == string_array[j]:
                if i == n_length - 1 or j == n_length - 1:
                    if lcp[i][j] != 1:
                        return ""
                elif lcp[i][j] != lcp[i + 1][j + 1] + 1:
                    return ""
            elif lcp[i][j]:
                return ""
    if "".join(string_array):
        return "".join(string_array)
    else:
        return "Impossible"                
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')


    lcp_rows = int(input().strip())
    lcp_columns = int(input().strip())


    lcp = []


    for _ in range(lcp_rows):
        lcp.append(list(map(int, input().rstrip().split())))


    result = findTheString(lcp)


    fptr.write(result + '\n')


    fptr.close()
