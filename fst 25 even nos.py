# find the first 25 even numbers that not divisible by 10 or not ending the values with 0.
num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the second value: "))
count = 0
if num1 < num2:

    for i in range(num1, num2):
        if i % 2 == 0:
            if i % 10 == 0:
                continue


            print(i)
            count += 1
            if count == 25:
                break
else:
    print("invalid order")








