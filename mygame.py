def movie_guessing_game():
    # Player 1 inputs the movie name
    movie = input("Player 1, enter the movie name: ").lower().replace(" ", "")
    
    # Display the masked movie for Player 2
    hidden_movie = ['_' if char.isalpha() else char for char in movie]
    
    # Maximum chances for guessing
    chances = 5
    guessed_letters = set()
    
    print("\n" * 50)  # Clear the screen so Player 2 cannot see the movie name
    print("Player 2, start guessing the movie!")
    
    while chances > 0 and ''.join(hidden_movie) != movie:
        print("\nCurrent movie: " + ' '.join(hidden_movie))
        print(f"Chances remaining: {chances}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed this letter!")
            continue
        
        guessed_letters.add(guess)

        if guess in movie:
            print("Good guess!")
            for idx, letter in enumerate(movie):
                if letter == guess:
                    hidden_movie[idx] = guess
        else:
            chances -= 1
            print("Wrong guess! You lost a chance.")
    
    if ''.join(hidden_movie) == movie:
        print(f"\nCongratulations! You guessed the movie: {movie}")
    else:
        print(f"\nSorry, you're out of chances. The movie was: {movie}")

# Run the game
movie_guessing_game()
