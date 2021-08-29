rows = 5
s = 2 * rows - 2
for i in range(0, rows):
    for a in range(0, s):
        print(end=" ")
    s = s - 2
    for a in range(0, i + 1):
        print("* ", end="")
    print("")
