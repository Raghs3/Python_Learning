activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():  # casefold converts str to lowercase
    print("But I want to go to the cinema")
