word = input("Enter a word: ")

try:
    times = int(input("How many times should it repeat? "))
except:
    print("Invalid input")
    quit()

for i in range(times):
    print(word)
