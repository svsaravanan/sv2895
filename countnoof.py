string = input("enter your commend: ")
length = len(string)
for row in range(length):
    for col in range(row + 1):
        print(string[col], end="")
    print()
