name = input("What's your name?\n\t")
age = input("How old are you?\n\t")

# got bored
for i in range(5):
    print("hello " + name)
if int(age) < 8:
    print("Go read a book or something")
elif int(age) > 80:
    print("Damn, thats unexpected")
else:
    print("Alright")
