# print("hello, world.")
#
# name = input("What is your name? ")
# name = name.strip().title()
# print(f"Hello, {name}!")


# first, last = name.split()
# print(f"Hello, {first}!")

def hello(to):
    print("hello,", to)

name = input("What's your name? ").title()
hello(name)