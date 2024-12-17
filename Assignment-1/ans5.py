sub1 = int(input("Enter subject 1 marks [0-100]: "))
sub2 = int(input("Enter subject 2 marks [0-100]: "))
sub3 = int(input("Enter subject 3 marks [0-100]: "))

average = (sub1+sub2+sub3) // 3
print(f"avg = {average}")

if 90 <= average <= 100:
    print("grade = A")
elif 80 <= average <= 89:
    print("grade = B")
elif 70 <= average <= 79:
    print("grade = C")
elif 60 <= average <= 69:
    print("grade = D")
else:
    print("grade = F")

