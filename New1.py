#importing the random function
import random

#Defining the welcome function.
def welcome():
    print("****************************************Welcome to Hangman Game************************************************")
    print("- The application will pick a random word from the list.")
    print("- You are expected to guess one LETTER in the word at each turn.")
    print("- The objective is to guess the word the application has picked.")
    print("- You can have upto 6 incorrect guesses before it's game over.")
    name = input("Enter your name: ")
    print("\nHello ",name,"Time to play Hangman!")


#Defining the play_again function.(This function is used to know if the user wants to play the game again)
def play_again():
    response = input("\nWould you like to play this game again? (Y/N): ").lower()
    if response == 'y':
        game_run()
        return True
    else:
        print("Hope you had enjoyed playing the game. See you next time.")
        return False


#Defining the function get_word to generate random words for the user to guess. 
def get_word():
    import urllib.request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    req = urllib.request.Request(word_url, headers=headers)
    response = urllib.request.urlopen(req)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    return random.choice(words).lower()
    


#Defining the function game_run.	
def game_run():
 
    #Calling the ‘welcome function’ inside the ‘game_run()’ function’ to get the game running.
    welcome()


    alphabet = ('abcdefghijklmnopqrstuvwxyz')

    word = get_word()

    letters_guessed = []
    tries = 6
    guessed = False


    print()
    print('The word contains', len(word), 'letters.')
    print('\n', len(word) * '_')



    while (guessed) == False and (tries) > 0:
        print('You have '+str(tries) +' tries.')
        guess = input('\nGuess a letter in the word: ').lower()

        if len(guess) == 1:
          if guess not in alphabet:
              print('\nCheck your entry,make sure you enter an alphabet.')

          elif guess in letters_guessed:
              print('\nYou have already guessed the letter.Try again!')

          elif guess not in word:
              print("Wrong guess.")
              letters_guessed.append(guess)
              tries -=1

          elif guess in word:
              print('\nYou have correctly guessed the letter!')
              letters_guessed.append(guess)

          else:
              print('\nCheck your entry! You might have entered the wrong entry.')

        else:
             print("Enter a single alphabet.")




        status = ''
        if guessed == False:
              for letter in word:
                  if letter in letters_guessed:
                      status += letter
                  else:
                      status +='_'
              print(status)

        if status == word:
              print('Great Job! You guessed the word correctly.')
              guessed = True


              #Initiate ‘play_again()’ function if user wishes to continue.
              play_status=play_again() 
              if not play_status:
                break
        elif tries == 0:
              print("\nYou ran out of guesses and you could'nt guess the word.")
              print("The word you had to guess was",word,'.')


              #Initiate ‘play_again()’ function if user wishes to continue.
              play_status=play_again()
              if not play_status:
                break

#Defining the function game_run to run full program.          
game_run()