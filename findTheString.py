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
    # Here we are getting the length of the input string
    n_length = len(lcp)
   
    # Forming a string array, by the length of input
    string_array = [""] * n_length
   
    # Setting index for loop
    index = 0
    # Assuming only checking for lowercase characters
    lowercase_characters = "abcdefghijklmnopqrstuvwxyz"

    # when this question was posed, it was asked to output "Impossible" on failing conditions
    # I am storing this message under the variable return_message
    return_message = "Impossible"
   
    for char in lowercase_characters:
        while index < n_length and string_array[index]:
            index += 1
        if index == n_length:
            break
        for j_index in range(index, n_length):
            if lcp[index][j_index]:
                string_array[j_index] = char    
   
    if "" in string_array:
        return return_message
   
    for i_index in range(n_length - 1, -1, -1):
        for j_index in range(n_length - 1, -1, -1):
            if string_array[i_index] == string_array[j_index]:
                if i_index == n_length - 1 or j_index == n_length - 1:
                    if lcp[i_index][j_index] != 1:
                        return return_message
                elif lcp[i_index][j_index] != lcp[i_index + 1][j_index + 1] + 1:
                    return return_message
            elif lcp[i_index][j_index]:
                return return_message
    if "".join(string_array):
        return "".join(string_array)
    else:
        return return_message               

lcp_test_cases = [
    [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]],
    [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]],
    [[8,5,4,8],[7,7,9,1],[4,5,8,1],[9,9,1,7]],
]

for test_case in lcp_test_cases:
    result = findTheString(test_case)
    print("For this test case: ", test_case, "\nThe result is: ", result)
