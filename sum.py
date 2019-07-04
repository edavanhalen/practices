while True:
    try:
        n = int(input(" Please enter a number : "))
        even_total = 0
        odd_total = 0
    except ValueError:
        print("This is not a number. Please enter a number.")
        continue

    for number in range(1, n + 1):
        if(number %2 == 0):
            even_total = even_total + number
        else:
            odd_total = odd_total + number
        
    print("The sum of even numbers from 1 to {0} = {1}".format(number, even_total))
    print("The sum of odd numbers from 1 to {0} = {1}".format(number, odd_total))        
