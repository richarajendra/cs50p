# yName=input("what is your name: ")
# print("Your name is ", yName)



# Ask the user for their name
# Store their name in a variable
# name = input("what is your name?").strip().title()

# split users name into first and last name
# first, last=name.split(" ")



# # Ask the user for their age
# # Store their age in a variable
# age = input("what is your age?")

# # Display "Hello" followed by their name
# # Display their age
# print("Hello ", name, "Age: ",age )
# print ("Hello ", end="")
# print(name)
# print("Hello ,\"friend\"",name)
# name=name.strip()
# name=name.title()  # Remove any leading/trailing whitespace and capitalize the first letter
# name = name.strip().title()

# print(f"Hello, {first}")

def main():
    name = input("What is your name? ").strip().title()
    hello(name)




def hello(name):
    print(f"Hello,",name)

main()