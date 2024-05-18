import random
#List of cars in India
cars=["Ford Endeavour", "Volckswagon Virtus GT","Land Rover Defender", "Mahindra Scorpion Z8L"]
#choose a random car from the list
car_to_guess=random.choice(cars)
word_length=len(car_to_guess) 
display=['_']* word_length
guessed_letters=[]
remaining_lives=6
print("Welcome to the hangman game....let's rollin with Cars")
print(f"the car name has a {word_length} letters.")

while True:
    print(f"\nLives remaining: (remaining_lives)")
    print(''.join(display))
    
    if '_' not in display:
        print(f"congratulations! You guessed the car right '{car_to_guess}'.")
        break

    if remaining_lives == 0:
        print(f"Game Over! The Car was '{Car_to_guess}'.")
        break

    guess=input("Guess a letter: ").upper()

    if len(guess) !=1 or not guess.isalpha():
        print("invalid input. Please Enter a single value.")
        continue

    guessed_letters.append(guess)
    if len(guess) != 1 or not guess.isalpha():
        print("invalid input. Please Enter a single value.")
        continue
    
    guessed_letters.append(guess)

    if guess in car_to_guess.upper():
        indices=[i for i, letter in enumerate(car_to_guess.upper()) if letter == guess]
        for index in indices:
            display[index]=car_to_guess [index]
    else:
        remaining_lives -=1
        print(f" '{guess}' is not in the car name")

