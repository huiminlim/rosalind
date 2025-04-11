import os
import sys

# Set directory path of current code folder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#print(ROOT_DIR)

# Data file name
data_file = "data.txt"

# Parse input strings
input = ""
with open(f"{ROOT_DIR}/{data_file}", "r") as f:
    input = f.readline().strip()
# print(input)

# data_file = open(sys.argv[1])
# input = data_file.read() #You can also put the text from the file into the code as a variable

## ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ##

# Count the number of ATCG each
num_a = input.count('A')
num_t = input.count('T')
num_c = input.count('C')
num_g = input.count('G')

print(num_a, num_c, num_g, num_t)