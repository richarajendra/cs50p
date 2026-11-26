def main():
    mass = int(input("Enter Mass in kilogram:"))
    print(einstein(mass))

def einstein(mass):
    c = 300000000
    E = mass * (c**2)
    return E

main()


