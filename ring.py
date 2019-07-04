while True:
    try:
        number = int(input("enter a number: "))
    except ValueError:
        print("That's not a number.")
        continue
    if number == 1:
        message = "ring to rule them all."
    else:
        message = "rings to rule them all."
    if number > 20:
        print("Invalid number. Only 20 rings have been made.")
        continue
    if number <= 0:
        print("Invalid number. A ring can't rule the others if it doesn't exist.")
        continue
    print(number , message)
