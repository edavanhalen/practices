count = 0
sum = 0
n = int(input("please enter a number.: "))

while n > 0:
    d = n%10
    n = n//10
    count += 1 
    sum += d
	
print("Number of digits:",count)
print("The sum of digits:",sum)
