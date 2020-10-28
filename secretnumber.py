max = 100
min = 0
number = 50
def math():
    global max
    global min
    global number
    choice = input("is your secret number higher1 or lower2 or equal3 to " + str(number) +"?: ")
    if choice == "hi":
        min = number
        number = int((number + max)/2)
        print(number)
        math()
    elif choice == "lo":
         max = number
         number = int((number + min)/2)
         print(number)
         math()
    elif choice == "eq":
        print("your secret number is " + str(number))

    else:
        print("bru")
        math()











math()
