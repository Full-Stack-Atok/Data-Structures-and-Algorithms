import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input("Enter a string: ")
    
    read = {} # Create a dictionary to store the characters and their frequencies
    for char in s: # for each character in the string
        if char in read: # if the character is already in the dictionary
            read[char] += 1 # increment the frequency of the character
        else:
            read[char] = 1 # add the character to the dictionary with a frequency of 1
        sorted_read = sorted(read.items(), key=lambda item: (-item[1], item[0]))
    
    for char, freq in sorted_read[:3]:
        print(f"{char}, {freq}") # print the dictionary