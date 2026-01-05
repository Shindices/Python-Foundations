total = 0

while True:
    num = input("Enter number: ")

    if num == "done":
        break

    try:
        num = float(num)
    except:
        print("Invalid input")
        continue

    total = total + num

print(total)
