## 18 Fuel gauge


i = 0
cda = 4
        
def main():
    while True:
        try:
            Fraction = get_input("Fraction: ")
            Checked = check(Fraction)
        else:
            print(checked)
        break
        
def get_input(prompt):
    while i <= 4:   
        try:
            prompt = int(input(prompt).split("/"))
            i += 1
        except ValueError:
            print("Invalid input, try another fraction: ")
        continue

        if i == cda:
            print("Too many attempts. Program closed.")
            break
        except ZeroDivisionError:
            if input1 
            print("You can't divide the number by 0. Try another: ")

def check():


### 19 Felipe Taqueria

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    get_order()


def get_order():
    total = 0
    while True:
        try:
            order = input("Item: ").title()
            total = total + menu[order]
            print("Total: ", "$","{:.2f}".format(total), sep="")
        except (ValueError,NameError,KeyError):
            pass
        except EOFError:
            return None


main()

# 20 GROCERY

def main():
    g_list = []    
    shop()


def shop():
    while True:
        try:
            user_input = input().upper().strip()
            g_list.append(user_input)
        except (EOFError, KeyError):
            sorted_list = sorted(set(g_list))
            for i in sorted_list:
                print(g_list.count(i),i)
            quit()


main()

    

## 22 EMOJI

import emoji as Em
input_user = input("input: ")
print(Em.emojize(f"output: {input_user}"))


        
## 25

import random

def main():
    number = level()
    guess = positive()
    if guess > number:
        print ("too much")
    elif guess == number:
        print ("Thats right")
    else:
        print("Too low")

def positive():
    cda = 4
    while True:
        try:
            number = int(input("Enter the number: "))
        except ValueError:
            print("It's not an integer. Try again:")
            cda -= 1
            if cda == 0:
                print("too many attempts")
                break
        else:
            if number < 0:
                print("Please enter positive integer!")
                cda -= 1
                if cda == 0:
                    print("too many attempts")
                    break  
            else:
                break
    return number
            
def level():
    n = int(input("Enter your level: "))
    randomize = random.randint(1, n)
    return randomize



main()


