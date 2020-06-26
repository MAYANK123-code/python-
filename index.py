secret=7
guess=int(input("guess any number: "))
while guess!=secret:
    if guess<secret:
        print("you need to guess high bruh")
        guess=int(input("guess any number: "))
    else:
        print("you need to trhink low bruh")
        guess=int(input("guess any number: "))
print("you guessed the number correctly")
