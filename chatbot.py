print("Hey there, what's your name?")
name = input()
print(f"Nice to meet you, {name}, how old are you?")
age = input()
print("How can I help you?")
print("1. Tell a joke")
print("2. Do nothing")
print("3. Exit conversation")
option = input("Choice: ")

if option == "1":
    print("What do you call a well-balanced horse?")
    empty = input() #yeah this doesn't store anything it's supposed to be the part where user says "what?" or something like that
    print("Stable!")
elif option == "2":
    pass #i know i don't need anything for menus but ran out of ideas sorry
elif option == "3":
    print("Thanks, have a good day!")
