import hashlib
import random
import string

givenPassword = "N0rm13P@$$w0rd"
hashedPassword = hashlib.sha256(givenPassword.encode()).hexdigest()

def cheatcodeAttack(target, guesses):
    for guess in guesses:
        hashedGuess = hashlib.sha256(guess.encode()).hexdigest()
        if hashedGuess == target:
            print(f"Guess was correct, the password is: {guess}")
            return
    print("None of the guesses were correct")

def makeGuess(len):
    choices = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(choices) for _ in range(len))

numOfGuesses = 7
guesses = []
for _ in range(numOfGuesses):
    n = random.randint(12,16)
    guesses.append(makeGuess(n))
print(f"The guesses we're gonna try are: {guesses}")

cheatcodeAttack(hashedPassword, guesses)