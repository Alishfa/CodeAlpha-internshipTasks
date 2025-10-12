import random
words = [
   
    "apple", "chair", "grape", "table", "piano",
    "beach", "smile", "light", "grass", "river",

   
    "python", "computer", "keyboard", "holiday", "mountain",
    "student", "picture", "library", "teacher", "battery",

   
    "adventure", "knowledge", "extraordinary", "chocolate",
    "innovation", "mysterious", "perseverance", "celebration",
    "philosophy", "imagination"
]
hangman_sketch = {0: ("   ",
                      "   ", #when no wrong guesses
                      "   "),
                  1: (" | ",
                      " o ", #when 1 wrong guess
                      "   "),
                  2: (" | ",
                      " o ", #when 2 wrong guesses
                      " | "),
                  3: ("  | ",  #//
                      "  o ",  
                      " /| "),
                  4: ("  | ",
                      "  o ",
                      " /|\\ "),
                  5: ("  | ",
                      "  o ",
                      " /|\\ ",
                      " / "),
                  6: ("  | ",
                      "  o ",
                      " /|\\ ",
                      " /|\\ ")}

def display_hangman(wrong_guesses):
    print("-----")
    for i in hangman_sketch[wrong_guesses]: #printing the hangman 
        print(i)
    print("-----")
        
def display_answer(answer):
    print(" ".join(answer))    #display the correct answer
    
def hint_user(hint):
    print(" ".join(hint))    #function to display the hint to user
def play_game():
    print("Welcome to Hangman!")
    answer= random.choice(words) #randomly choose a word from the list
    guessed_letters = set() #keep track of guessed letters
    hint=["_"]*len(answer)
    wrong_guesses = 0
    is_running = True #game state means game is running
    while is_running:
        display_hangman(wrong_guesses)
        hint_user(hint)
        guess=input("Guess a letter: ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue 
        if guess in guessed_letters:
            print("You already guessed that letter. ")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            wrong_guesses+=1
            print(f"Wrong guess! You have {6-wrong_guesses} guesses left.")
        
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print(f"Congratulations! You guessed the word: {answer}")
            is_running=False
        elif wrong_guesses>=len(hangman_sketch)-1: 
            display_hangman(wrong_guesses)
            display_answer(answer)
            print(f"Game Over! The correct word was: {answer}")
            is_running=False
    
if __name__== '__main__':
    play_game()
    
