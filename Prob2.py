## camel

def main():
    get_input = getinput()
    snake_case = convert_input(get_input)
    print("case snake: ", snake_case)


def getinput():
    input1 = input("Camel case: ")
    return input1

def convert_input(txt):
    for letter in txt:
        if letter.isupper():
            txt = txt.replace(letter, "_" + letter.lower())
    return txt


main()

## coke

def main():
    coke()

def coke():
    coins = [5, 10, 25]
    price = 50
    while price > 0:
        print("Amount due: ", price)
        coin = int(input("Insert coin: "))
        if coin in coins:
            price -= coin
        else:
            print("change owed: ", abs(price))

main()


## twitter

def main():
    tweet = input1()
    shortened_tweet = shortened(tweet)
    print(shortened_tweet)

def input1():
    phrase = str(input("Tweet anything: "))
    return phrase

def shortened(tweet):
    vowels = ["a", "e", "i", "o", "u"]
    for i in tweet:
        if i.lower() in vowels:
            tweet = tweet.replace(i, "")
    return tweet
        
main()


## Plates

plate = ""

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    digit_count = 0
    for char in plate:
        if char.isdigit():
            digit_count += 1
        elif not char.isalpha():
            return False
    if plate[0:2].isalpha() and plate[-2:].isdigit() and int(plate[-2]) != 0 and len(plate)>= 0 and len(plate)<=6 and digit_count == 2:
        return True
    else:
        return False

main()

# Nutritions 17

calories = {
    "Apple" : 130,
    "Avocado" : 50,
    "Sweet cherries" : 100,
    "Banana" : 140,
    "Strawberries" : 30,
    "Lemon" : 25,
    "Orange" : 15
}

print(f"Calories: ", calories[input("Items: ").title()])






