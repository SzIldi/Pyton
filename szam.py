szam = 1
while szam <= 10:
    print szam
    szam = szam +1

print "vege"

secret = 22

while True:
    guess = int(raw_input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print "You guessed it - congratulations! It's number 22 :)"
        break
    elif guess > secret:
        print "Your guess is not correct... try something smaller"
    elif guess < secret:
        print "Your guess is not correct... try something bigger"