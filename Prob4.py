## 32 Lines of code

# import sys


# def files():
#     if len(sys.argv) < 2:
#         sys.exit("Too few arguments")  
#     elif len (sys.argv) > 2:
#         sys.exit("Too many arguments")
#     elif not sys.argv[1].endswith(".py"):
#         sys.exit("It's not a Python file")

#     try:
#         with open(sys.argv[1]) as file:
#             count = 0 
#             for line in file:
#                 line = line.strip()
#                 if line.startswith("#") or not line:
#                     continue
#                 count += 1
#     except FileNotFoundError:
#         sys.exit("File not found.")
#     else:
#         print("Line numbers:", count)

# files()


## 33 Pizza py

import sys
import csv
from tabulate import tabulate

def line_arguments(arguments):
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    
    if arguments[1].split(".")[1] != "csv":
        sys.exit("Not a csv file")

    try:
        open(arguments[1], "r")
    except:
        sys.exit("File does not exist")

    return arguments[1]  

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        header = next(reader)
except FileNotFoundError:
    sys.exit("File does not exist")

# Check if file  is correct  format
if header != ["Sicilian Pizza", "Small", "Large"]:
    sys.exit("isn't correct format")

# Read file and print formatted table
with open(sys.argv[1], "r") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    rows = [[item.strip() for item in row] for row in reader]
    print(tabulate(rows, headers=["Sicilian Pizza", "Small", "Large"], tablefmt="grid"))
