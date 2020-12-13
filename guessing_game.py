secretWord = "żyrafa"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuesses = False

while guess != secretWord and not(outOfGuesses):
    if guessCount<guessLimit:
        guess = input("Wprowadź słowo: ")
        guessCount += 1
    else:
        outOfGuesses = True

if outOfGuesses:
    print("Przegrałeś")
else:
    print("Wygrałeś!")