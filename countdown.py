try:
    num = int(input("Enter a number: "))
except:
    print("Invalid input")
    quit()

if num < 0:
    print("Done!")
else:
    for i in range(num, -1, -1):
        print(i)
    print("Done!")
