from math import sqrt

print("What do you want to find out?")
print("A. Height")
print("B. Base")
print("C. Hypotenuse")

x = input("Enter your choice (A, B, C): ").upper()

def pg():
    if x == "A":
        c = int(input("Enter the hypotenuse value: "))
        b = int(input("Enter the base value: "))
        a = c ** 2 - b ** 2
        if a < 0 :
            print("Height can not be negative!")
            return
        result = sqrt(a)
        print(f"Your height value is {result}")

    elif x == "B":
        c = int(input("Enter the hypotenuse value: "))
        a = int(input("Enter the height value: "))
        b = c ** 2 - a ** 2
        if b < 0 :
            print("Base can not be negative!")
            return
        result = sqrt(b)

        print(f"Your base value is {result}")

    elif x == "C":
        a = int(input("Enter the height value: "))
        b = int(input("Enter the base value: "))
        c = a ** 2 + b ** 2
        result = sqrt(c)
        print(f"Your hypotenuse value is {result}")

    else:
        print("Value error! Please input a valid choice.")

pg()
