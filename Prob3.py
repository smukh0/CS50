## 18 Fuel gauge


# i = 0
# cda = 4
        
# def main():
#     while True:
#         try:
#             Fraction = get_input("Fraction: ")
#             Checked = check(Fraction)
#         else:
#             print(checked)
#         break
        
# def get_input(prompt):
#     while i <= 4:   
#         try:
#             prompt = int(input(prompt).split("/"))
#             i += 1
#         except ValueError:
#             print("Invalid input, try another fraction: ")
#         continue

#         if i == cda:
#             print("Too many attempts. Program closed.")
#             break
#         except ZeroDivisionError:
#             if input1 
#             print("You can't divide the number by 0. Try another: ")

# def check():

#### FUEL CORRECT

# def main():
#     while True:
#         try:
#             result = get_frac("Fraction: ")
#             fuel_gauge = check_max_min(result)
#         except ValueError:
#             pass
#         except ZeroDivisionError:
#             pass
#         except NameError:
#             pass
#         else:
#             print(fuel_gauge)
#             break


# def get_frac(prompt):
#     fraction = input(prompt).split("/")
#     return abs(round(int(fraction[0]) / int(fraction[1]) * 100))


# def check_max_min(number):
#     if 99 <= number <= 100 :
#         return "F"
#     if number <= 1:
#         return "E"
#     if number > 100:
#         return Error
#     else:
#         return f"{number}%"


# main()

### 19 Felipe Taqueria

# menu = {
#     "Baja Taco": 4.00,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
# }


# def main():
#     get_order()


# def get_order():
#     total = 0
#     while True:
#         try:
#             order = input("Item: ").title()
#             total = total + menu[order]
#             print("Total: ", "$","{:.2f}".format(total), sep="")
#         except (ValueError,NameError,KeyError):
#             pass
#         except EOFError:
#             return None


# main()

# 20 GROCERY

# def main():
#     g_list = []    
#     shop()


# def shop():
#     while True:
#         try:
#             user_input = input().upper().strip()
#             g_list.append(user_input)
#         except (EOFError, KeyError):
#             sorted_list = sorted(set(g_list))
#             for i in sorted_list:
#                 print(g_list.count(i),i)
#             quit()


# main()

    

## 22 EMOJI

# import emoji as Em
# input_user = input("input: ")
# print(Em.emojize(f"output: {input_user}"))

## 23 FIGLET

# import sys
# import random
# from pyfiglet import Figlet

# figlet = Figlet()

# x = ['-f', '--font']

# def main():
#     # check command line arguments
#       if len(sys.argv) == 1:
#         figlet.setFont(font = random.choice(figlet.getFonts()))
#         print("Output: ", figlet.renderText(input("Input: ")), sep="\n")
#       elif len(sys.argv) == 3 and sys.argv[1] in x and sys.argv[2] in figlet.getFonts():
#         figlet.setFont(font = sys.argv[2])
#         print("Output: ", figlet.renderText(input("Input: ")), sep="\n")
#       else:
#         sys.exit("Error: ")
# main()        


## 24


# import inflect

# p = inflect.engine()

# names = []

# while True:
#     try:
#         x = input("Name: ")
#         if x != "":
#             names.append(x)
#         else:
#             continue
#     except EOFError:
#         print("Adieu, adieu, to " + p.join(names))
#         break 

# import inflect

# p = inflect.engine()
# names = []

# while True:
#     cda=4
#     try:
#         name = input("Enter your name: ")
#         if name != "":
#             names.append(name)
#             cda -= 1
#     except EOFError:
#         pass
#     else:
#         print("Adieu, adieu, to " + p.join(names))
        
## 25

# import random

# def main():
#     number = level()
#     guess = positive()
#     if guess > number:
#         print ("too much")
#     elif guess == number:
#         print ("Thats right")
#     else:
#         print("Too low")

# def positive():
#     cda = 4
#     while True:
#         try:
#             number = int(input("Enter the number: "))
#         except ValueError:
#             print("It's not an integer. Try again:")
#             cda -= 1
#             if cda == 0:
#                 print("too many attempts")
#                 break
#         else:
#             if number < 0:
#                 print("Please enter positive integer!")
#                 cda -= 1
#                 if cda == 0:
#                     print("too many attempts")
#                     break  
#             else:
#                 break
#     return number
            
# def level():
#     n = int(input("Enter your level: "))
#     randomize = random.randint(1, n)
#     return randomize



# main()


## 26 EEE PROFESSOR

# import random


# def main():
#     n = get_level()
#     i=10
#     while i>0:
#         i-=1
#         x = generate_integer(n)
#         y = generate_integer(n)
#         solution = generate_equation_solution(x, y)
#         j=3
#         while j>0:
#             j-=1
#             try:
#                 print(x, "+", y, "= ", end="")
#                 if check_user_input(solution):
#                     break
#                 elif j==0:
#                     print("EEE")
#                     print(x, "+", y, "= ", solution)
#                 else:
#                     print("EEE")
#             except ValueError:
#                 pass


# def get_level():
#     while True:
#         try:
#             lvl = int(input("Enter your level: "))
#             if lvl > 0 and < 4:
#                 break
#         else:
#             pass

#     return lvl


# def generate_integer(level):
#     numberList =[]
#     if level == 1:
#         numberList = range(1, 10)
#     elif level == 2:
#         numberList = range(10, 100)
#     elif level == 3:
#         numberList = range(100, 1000)

#     number = random.choice(numberList)
#     return number

# def generate_equation_solution(num1, num2):
#     sum = num1+num2
#     return sum

# def check_user_input(solution):
#      userInput = int(input())
#      if userInput == solution:
#         return True

# if __name__ == "__main__":
#     main()


## 27 BITCOIN
# import requests
# import sys


# if len(sys.argv) !=2:
#     print("Missing command-line argument")
#     sys.exit()
    
# try:
#     response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#     rate = response.json()["bpi"]["USD"]["rate"]
#     rate = rate.replace(",", "")
#     userAmount = float(sys.argv[1])
#     amount = float(rate)*userAmount
#     print(f"${amount:,.4f}")
# except ValueError:
#     print("Command-line argument is not number")
#     sys.exit()

## 28
# from twttr import shorten

# def test_shorten_no_vowels():
#     assert shorten("ghtrk") == "ghtrk"

# def test_shorten_only_vowels():
#     assert shorten("aeiouAEIOU") == ""
# def test_shorten_mixed():
#     assert shorten("hello world") == "hll wrld"

# def test_shorten_single_vowels():
#     assert shorten("a") == ""
#     assert shorten("e") == ""
#     assert shorten("i") == ""
#     assert shorten("o") == ""
#     assert shorten("u") == ""

# def test_shorten_empty():
#     assert shorten("") == ""


## 29 BANK TESTING

# from bank import value

# def test_value_hello():
#     assert value("hello world! ") == 0
#     assert value("hi there! ") == 20
#     assert value("good morning! ") == 100

## 30 PLATES TESTING

# from plates import is_valid

# def test_valid_plate():
#     assert is_valid("PLATE") == True

# def test_invalid_plate():
#     assert is_valid("PLATE12") == False
#     assert is_valid("PLATE14") == False
#     assert is_valid("PLATE16") == False
#     assert is_valid("PLATE18") == False

# def test_lowercase_digit():
#     assert is_valid("plate123") == False


## 31 FUEL TESTING

# from fuel import convert, gauge

# def test_convert_valid_fraction():
#     assert convert("5/10") == 50
#     assert convert("1/4") == 25
#     assert convert("3/5") == 60
#     assert convert("50/100") == 50
#     assert convert("1/100") == 1
#     assert convert("99/100") == 99

# def test_convert_invalid_franction():
#     try:
#         convert("5/0")
#         return False
#     except ZeroDivisionError:
#         pass

#     try:
#         convert("10/5")
#         assert False
#     except ValueError:
#         pass

#     try:
#         convert("-1/10")
#         assert False
#     except ValueError:
#         pass

# def test_gauge():
#     assert gauge(0) == "E"
#     assert gauge(1) == "E"
#     assert gauge(99) == "F"
#     assert gauge(100) == "F"
#     assert gauge(-1) == "E"
#     assert gauge(101) == "F"