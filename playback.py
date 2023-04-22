# a = input("write a phrase")

# newa = a.replace(" ", "...")
# print(newa)

## 4

# a = input("Say hello to us").strip()

# emojia = a.replace(":)", "🙂")

# print(emojia)

## 5

# c=300000000
# ask = int(input("Enter mass in kgs: "))

# output = ask * c **2
# print(output)

## 6

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    dollarfloat = float(d)
    return dollarfloat

def percent_to_float(p):
    p.replace("%", "")
    floatpercent = int(float(p))/100.0
    return floatpercent

main()

## testi

# d = input("number: ")
# d = d.replace("$","")
# d = float(d)
# print(d)

## 7

# if input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower() in ["90", "ninety", "ninety"]:
#     print("Yes")
# else:
#     print("No")

## 8

# greeting = input("Greeting ")
# if  greeting.title()[0:5] == "Hello" :
#     print("0$")
# elif greeting.title()[0] == "H":
#     print("20$")
# else:
#     print("100$")
    
## 9

# expression = input("calculate: ")
# x, y, z = expression.split(" ")

# x = float(x)
# z = float(z)

# if y == "+":
#     result = x+z
# elif y == "-":
#     result = x-z
# elif y == "*":
#     result = x*z
# elif y == "/":
#     result = x/z

# print("{:.1f}".format(result))

## 10

# fileformat = input("Input file name: ").lower()
# filetype = fileformat[fileformat.find("."):]
# match filetype:
#     case ".gif":
#         print("image/gif")
#     case ".jpg" | ".jpeg":
#         print("image/jpeg")
#     case ".png":
#         print("image/png")
#     case ".pdf":
#         print("application/pdf")
#     case ".txt":
#         print("text/plain")
#     case ".zip":
#         print("application/zip")
        
## 11

# def main():
#     current_time = convert(input("What time is it?"))
#     if 7 <= current_time <= 8:
#         print("breakfeast time")
#     elif 12 <= current_time <= 13:
#         print("dinner time")
#     elif 18 <= current_time <= 19:
#         print("supper time")
#     else:
#         print("finish meal time")


# def convert(time):
#     hours, minutes = time.split(":")
#     convert_time = float(minutes) / 60
#     return float(hours) + convert_time


# if __name__ == "__main__":
#     main()
    
## 11

# def main():
#     textinput = input("Tell me something: ")
#     if textinput != "":
#         print(textinput + " has "+ str(len(textinput)) + " characters")
#     else:
#         print("Don't be shy")
#         main()

# main()

## GUI

# # Import the required libraries
# from tkinter import *
# # Create an instance of tkinter window
# win=Tk()
# # Set the size of the tkinter window
# win.title("Characters Counter")
# win.geometry("700x350")
# #Ask users to write text
# label2=Label(text="Please, write some text", justify=RIGHT, font=('11'))
# label2.pack()
# # Define a function to get the length of the current text
# def update(event):
#    label.config(text="Total Characters: "+str(len(text.get("1.0", 'end-1c'))))

# # Create a text widget
# text=Text(win, width=50, height=10, font=('Calibri 14'))
# text.pack()

# # Create a Label widget
# label=Label(win, text="", justify=CENTER, font=('11'))
# label.pack()


# # Bind the buttons with the event
# text.bind('<KeyPress>', update)
# text.bind('<KeyRelease>', update)

# win.mainloop()

## 12

# quote = input("What is the quote? ")
# name = input("Who said it? ").title()

# quotes=[
#         "\"We are a way for the cosmos to know itself.\"",
#         "\"No space of regret can make amends for one life's opportunity misused.\"",
#         "\"But in ya heeeeaad.\"",
#         "\"Mars is there, waiting to be reached.\"",
#         "\"Hips don\'t lie.\"",
#         ]
# match name:
#     case "Carl Sagan":
#         print(name + " said: " + quotes[0])
#     case "Charles Dickens":
#         print(name + " said: " + quotes[1])
#     case "The Cranberries" :
#         print(name + " said: " + quotes[2])
#     case "Buzz Aldrin":
#         print(name + " said: " + quotes[3])
#     case "Shakira":
#         print(name + " said: " + quotes[4])
#     case _:
#         print("Try again")







