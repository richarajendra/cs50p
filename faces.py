def main():
    smile= str(input("Enter a smiley face after text:"))
    print(convert(smile))

def convert(n):
    n = n.replace(":)","🙂")
    n = n.replace(":(","🙁")
    return(n)

main()