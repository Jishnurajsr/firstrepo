# # #Revers the each word in the sentance
# #
# #
# # # def reverse(x):
# # #     str = ""
# # #     for i in x:
# # #         str = i + str
# # #     return str
# # x="Hello How are you bro"
# # z=x[0:5]
# # c=z[::-1]
# # print(c)
# #
# # n1 = int(input("Enter the first value: "))
# # n2 = int(input("Enter tne second value: "))
# # for i in range(n1, n2):
# #     if i % 2 != 0:
# #         print(i)
#
#
# # *
# # **
# # ***
# # ****
# # *****
# for i in range(1, 10):
#         print("*" * i)
#
# def add(a,b):
#     return a+b
#
# print(add(2,3))


rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print("* ", end="")
        k += 1

    k = 0
    print()


