# x = input("enter a number: ")
# y = input("enter another number: ")
# print("Value of z:", int(x) + int(y))

# x = float(input("enter a number: "))
# y = float(input("enter another number: "))
# z= x/y

# print(f"{z:.2f}")

def main():
    x= int(input("enter a number: "))
    print("x squared is", square(x))


def square(n):
    return n**2

main()

