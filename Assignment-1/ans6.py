def factorial_num(number):
    if number < 0:
        print("enter valid number")
    else:
        factorial = 1
        i = number
        while i > 1:
            factorial = factorial * i
            i = i-1
        return factorial
        

number = int(input(f"Enter num : ")) 
result = factorial_num(number)

print(f"Factorial of given number = {result}")


