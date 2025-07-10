import random

print("Errate die zufällige Zahl zwischen 1 und 100")
print("Du hast insgesamt 10 Versuche")


counter = 1


while True:
    
    randomNum = random.randint(1,100)
    

    try:
        guess = int(input(f"Das ist dein {counter}. Versuch: "))
    except ValueError:
        print("Abgebrochen, weil Eingabe falsch ist!")
    
    if guess == randomNum:
        print("Du hast gewonnen")
    elif guess > randomNum:
        print("Dein Guess ist größer")
    elif guess < randomNum:
        print("Dein Guess ist kleienr")
    else:
        print("Falsche Eingabe")

    if counter == 10:
        print("Du hast verloren, weil du 10 Versuche benutzt hast")
        counter = 1
        continue
    
    counter = counter +1 
