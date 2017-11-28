#Hangman
#MD
def start_screen():
    print("""
HHHHHHHHH     HHHHHHHHH                                                                                                            
H:::::::H     H:::::::H                                                                                                            
H:::::::H     H:::::::H                                                                                                            
HH::::::H     H::::::HH                                                                                                            
  H:::::H     H:::::H   aaaaaaaaaaaaa nnnn  nnnnnnnn      ggggggggg   ggggg  mmmmmmm    mmmmmmm    aaaaaaaaaaaaa nnnn  nnnnnnnn    
  H:::::H     H:::::H   a::::::::::::an:::nn::::::::nn   g:::::::::ggg::::gmm:::::::m  m:::::::mm  a::::::::::::an:::nn::::::::nn  
  H::::::HHHHH::::::H   aaaaaaaaa:::::n::::::::::::::nn g:::::::::::::::::m::::::::::mm::::::::::m aaaaaaaaa:::::n::::::::::::::nn 
  H:::::::::::::::::H            a::::nn:::::::::::::::g::::::ggggg::::::gm::::::::::::::::::::::m          a::::nn:::::::::::::::n
  H:::::::::::::::::H     aaaaaaa:::::a n:::::nnnn:::::g:::::g     g:::::gm:::::mmm::::::mmm:::::m   aaaaaaa:::::a n:::::nnnn:::::n
  H::::::HHHHH::::::H   aa::::::::::::a n::::n    n::::g:::::g     g:::::gm::::m   m::::m   m::::m aa::::::::::::a n::::n    n::::n
  H:::::H     H:::::H  a::::aaaa::::::a n::::n    n::::g:::::g     g:::::gm::::m   m::::m   m::::ma::::aaaa::::::a n::::n    n::::n
  H:::::H     H:::::H a::::a    a:::::a n::::n    n::::g::::::g    g:::::gm::::m   m::::m   m::::a::::a    a:::::a n::::n    n::::n
HH::::::H     H::::::Ha::::a    a:::::a n::::n    n::::g:::::::ggggg:::::gm::::m   m::::m   m::::a::::a    a:::::a n::::n    n::::n
H:::::::H     H:::::::a:::::aaaa::::::a n::::n    n::::ng::::::::::::::::gm::::m   m::::m   m::::a:::::aaaa::::::a n::::n    n::::n
H:::::::H     H:::::::Ha::::::::::aa:::an::::n    n::::n gg::::::::::::::gm::::m   m::::m   m::::ma::::::::::aa:::an::::n    n::::n
HHHHHHHHH     HHHHHHHHH aaaaaaaaaa  aaaannnnnn    nnnnnn   gggggggg::::::gmmmmmm   mmmmmm   mmmmmm aaaaaaaaaa  aaaannnnnn    nnnnnn
                                                          g:::::g                                                         
                                                       gggggg      g:::::g                                                         
                                                       g:::::gg   gg:::::g                                                         
                                                        g::::::ggg:::::::g                                                         
                                                         gg:::::::::::::g                                                          
                                                           ggg::::::ggg                                                            
                                                              gggggg
    """)
def get_puzzle():
    return "hangman"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    while True:
        letter = input("Guess a letter: ")

        if len(letter) == 1:
            if(letter).isalpha():
                return letter
            else:
                print("You have to enter one letter.")
        else:
                print("You have tp enter one letter.")    

def display_board(solved):
    print(solved)

def show_result(result):
    if result == 0:
         print("You won, Congrats!")
    else:
        print("You lose")
    

def play_again(name):
    while True:
        decision = input(" Play again? " + name + " ? (y/n)")
        print()
        decision = decision.lower()

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            print("Ok, it was fun playing")
            return False
        
        else:
            print("Enter a true respond.")
    
def play(name):
    print("This is the Hangman Game, " + name + "!!")
    print("6 guesses to guess my word.")
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    strikes = 0
    limit = 6
    result = 0
    print(solved)
    gameover = 0

    while solved != puzzle and gameover == 0:
        letter = get_guess()

        if letter not in puzzle:
            strikes +=1
            print("That's not my word")
            print("You have " + str(strikes) + " strikes so far. Be smart " + name + " .")
            print()
            if strikes == limit:
                print("You lose " + name + ", you didn't guess the word in 6 tries.")
                result = 1
                gameover = 1
        
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(result)

    
# Game starts running here
start_screen()
playing = True

while playing:
    name = input("What's your name?")
    play(name)
    playing = play_again(name)
show_credits()
