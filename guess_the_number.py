from random import randint

a = randint(1,100)# this is number to be guessed/ b is the users guess
tries = 5 # amount of tries the player has before failing

name = str(input('You are about to play Guess the Number! \n'  #the username that will be recorded upon a successful game
                     'please enter a username:  '))
scorecard = {name:tries} # the recorded data


def data(): #function that records the games data to a file
    file = open('highscore.txt', 'r+')
    file.write(str(scorecard))
    for line in file:
        print(line)
    file.close
    
def restart():
    name = str(input('You are about to play Guess the Number! \n'  #the username that will be recorded upon a successful game
                     'please enter a username:  '))
    
    
    
    
def guess(): #the main function
    while True:
        
        global a, tries, b, name, highscore, scorecard
        a = a
        scorecard = {name:tries}

        print(a)
        try:
            b = int(input("pick a number from 1 to 100: "))
        except ValueError:
            print('No, no, no, a number!')

        if b > 100:
            print("The number won/'t be more than 100.")
            guess()

        
        if a != b:
            tries -= 1
            if tries == 0: #game restarts 
                print('You ran out of tries. The number was ' + str(a) + '. :(')
                print('')
                
                a = randint(1,100)
                tries = 5
                guess()
            print('Guess again')
            print(str(tries) + ' tries left')
            if a > b:
                print('guess a larger value')
                guess()
            if a < b:
                print('guess a smaller value')
                guess()
            
        else:  #correct answer and restarts the game
            print('You guessed the number. It was ' + str(a) + '! :)')
            
            #tries = 5
            a = randint(1,100)
            print(scorecard) 
            tries = 5
            data()
            guess()
                
