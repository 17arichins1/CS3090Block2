# CS3090Block2
This is just for a simple class assignment.
I made it using Python3 from a terminal, you just need the interpreter to run it.
It uses Python's hash library to demonstrate the principle of hashing passwords. It also demonstrates standard/suggested password selection practices.
Given some password, it hashes it, and then makes a short list of 'guesses' that are 12-16 characters long, each one being randomly an upper- or lower-case letter, number digit, or symbol.
Then it runs a function that takes each of these 'guesses' and to see if any are the correct password, hashes them and compares them to the hash of the original given password.

This file is for educational purposes only. It doesn't really do anything in its current state, other than showing simple exercises in manipulating strings that could be used as passwords.
It just uses the .sha256() function from Python's hashlib, and encode().hexdigest() functions to hash those strings that could be passwords. If you ran it an infinite number of times, at some point it would 'guess' the current hardcoded, given password.
It doesn't really offer any help for anyone to make something more secure, and wouldn't really be able to be modified to make something less secure.
