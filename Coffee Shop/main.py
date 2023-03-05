menu = "Black Coffee ($3), Espresso ($5), Latte ($10), Cappuccino ($8), Vanilla Latte ($10)"

print("Hello, welcome to NetCoffee!")

name = input("What is your name?\n")

if name == "Ben" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("You are not welcome here " + name + "!! Get OUT!")
        exit()
    else:
        print("Oh, you are one of those good " + name + " thats great, come on in.")
else:
    print("Hello " + name + ", thank you for coming in today.\n\n\n")

print(name + ", what would you like from our fine cafe today? Here is what we are serving.\n" + menu)

order = input()

if order not in menu:
    print("Sorry, " + order + " is not on the menu.")
    exit()

if order == "Vanilla Latte":
    price = 10
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 10
elif order == "Cappuccino":
    price = 8

print("Sounds good " + name + ", I will have that " + order + " ready for you in one moment.")

amount = input("How many " + order + " would you like?\n")

tip_amount = input("Enter a percentage or dollar amount for the tip (e.g. 10 or $2.50):\n")

if tip_amount[0] == "$":
    tip = float(tip_amount[1:])
else:
    tip = float(tip_amount) / 100

total = price * int(amount) * 1.13 * (1 + tip)

formatted_total = "{:.2f}".format(total)

print("That will be $" + formatted_total)
