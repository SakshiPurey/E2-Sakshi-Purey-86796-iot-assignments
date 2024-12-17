#accept 4 digit num from user
num = int(input("Enter 4 digit number : "))

Dig1 = num // 1000
Dig2 = (num // 100)%10
Dig3 = (num // 10)%10
Dig4 = num%10

#a.face value
print(f"a : face value of num = {Dig1} {Dig2} {Dig3} {Dig4} ")

#b.place value
print(f"b : place value of num = {Dig1*1000} {Dig2*100} {Dig3*10} {Dig4} ")

#c.rev num
rev = Dig4*1000 + Dig3*100 + Dig2*10 + Dig1
print(f"reverse value = {rev}")