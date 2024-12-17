#Accept 3 int num and find its average

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

if num1 > num2:
    if num1 > num3:
        print(f"Max num = {num1}")
    else:
        print(f"Max num = {num3}")
else:
    if num2 > num3:
        print(f"Max num = {num2}")
    else:
        print(f"Max num = {num3}")