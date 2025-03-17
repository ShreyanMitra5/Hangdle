import random

final_matrix = [
    ["", "", "", "  O", "", "", ""],
    ["", "", "H", "I", "H", "", ""],
    ["", "", "", "  I", "", "", ""],
    ["", "", "","H", "H", "", ""]
    ]
    
initial_matrix = [
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""]
    ]
 

#Computer generates a random word
def computer_choose_word():
    global list_of_words
    list_of_words = []
    f = open("words.txt", "r")
    count = 1
    while count != 1860:
        list_of_words.append(f.readline().strip())
        count += 1
    #print(list_of_words)
    num1 = random.randrange(0, len(list_of_words)-1)
    comp_word = list_of_words[num1]
    return(list(comp_word.lower()))

#Printing out the whole matrix
def expand_matrix(matrix):
    try:
        for i in range(len(matrix)):
            print(matrix[i])
    except:
        print("Cannot print matrix!")

#This function simulates the whole game, essentially the heart of the whole program
def play_game(comp_word, user_word, track, guess, initial_matrix, letter_chosen):
    
    for i in range(len(comp_word)):
        if comp_word[i] in user_word:
            guess = guess[0:i] + comp_word[i] + guess[i+1:]
        
        for key, value in letter_chosen.items():
            letter_chosen[user_word[i]] = 1
    print(guess)
    if list(guess) != comp_word:
        for key, value in letter_chosen.items():
            print(str(key) + ': ' + str(value))
    #print(letter_chosen)
    if list(guess) != comp_word:
        if track == 7:
            initial_matrix = [
                ["", "", "", " O", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]
            ]
        elif track == 6:
            initial_matrix = [
                ["", "", "", " O", "", "", ""],
                ["", "", "", "I", "", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]
            ]
        elif track == 5:
            initial_matrix = [
                ["", "", "", " O", "", "", ""],
                ["", "", "", "I", "H", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]
            ]
        elif track == 4:
            initial_matrix = [
                ["", "", "", " O", "", "", ""],
                ["", "", "H", "I", "H", "", ""],
                ["", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]
            ]
        elif track == 3:
            initial_matrix = [
                ["", "", "", " O", "", "", ""],
                ["", "", "H", "I", "H", "", ""],
                ["", "", "", " I", "", "", ""],
                ["", "", "", "", "", "", ""]
            ]
        elif track == 2:
            initial_matrix = [
                ["", "", "", " O", "", "", ""],
                ["", "", "H", "I", "H", "", ""],
                ["", "", "", " I", "", "", ""],
                ["", "", "", "", "H", "", ""]
            ]
            
        elif track == 1:
            initial_matrix = [
                ["", "", "", " O", "", "", ""],
                ["", "", "H", "I", "H", "", ""],
                ["", "", "", " I", "", "", ""],
                ["", "", "H", "", "H", "", ""]
            ]

        # Print the matrix only once per round
        expand_matrix(initial_matrix)
        return (False, guess, initial_matrix, letter_chosen)
    return (True, guess, initial_matrix, letter_chosen)
        
#This prompts the user to guess, and checks whether the user_input satisfies all the needs
def get_guess():
    print("Guesses remaining: " + str(track))
    while True:
        flag = True
        user_input = input("Enter a 5-letter word as a guess: ").lower()
        
        if user_input not in list_of_words:
            print("Must be a valid word")
            flag = False
        
        l = [str(x) for x in list(user_input)]
            
        for i in '0123456789!@#$%^&*(){}|<>?':
            if i in l:
                print("No numbers/symbols can be inputted as a guess!")
                flag = False
                break
        if user_input.strip() == "":
            print("Cannot be an empty string")
            continue
        if len(l) != 5:
            print("Your guess must consist of 5 letters!")
            flag = False
            
        
        elif flag:
            return(l)
        else:
            flag = True
            
            
comp_word = computer_choose_word()

#Connects everything together
print("Enter 5 Letter Words to play the game! All lowercase words")
expand_matrix(initial_matrix)
track = 7
guess = "_____"
letter_chosen = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, 
        "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, 
        "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }

while track != 0:
    user_word = get_guess()
    #print(user_word)
    #print(comp_word)
    boolean, guess, initial_matrix, letter_chosen = play_game(comp_word, user_word, track, guess, initial_matrix, letter_chosen)
    
    if boolean:
        print("Congrats! you won the game!")
        print(str(guess) +" is the correct word!")
        new = True
        break
    track -= 1
    new = False
if new:
    print("Thanks for playing")
else:
    print("Game over!\nThanks for playing, the correct word was: " + str("".join(comp_word)))
