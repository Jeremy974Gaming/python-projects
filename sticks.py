from termcolor import colored
import time
sticks = 21

#   Gamerules and Player information code, used for informational purposes.

gamerule1 = colored('There are 21 sticks, you can take 1-4 sticks at a time ', 'white', attrs=['bold', 'reverse'])
gamerule2 = colored('Whoever takes the last one, loses the game.', 'white', attrs=['bold', 'reverse'])
print(gamerule1 + gamerule2)
print('=========================')

#   Pause execution for exactly 1 second.

time.sleep(1)
ginfo = colored('WARNING You appear to have started a game of sticks.', 'red', attrs=['bold', 'blink'])
p1inf = colored('Player one is : ', 'white', attrs=['bold', 'blink'])
p1col = colored('BLUE', 'blue', attrs=['bold', 'blink'])
p2inf = colored('Player Two is : ', 'white', attrs=['bold', 'blink'])
p2col = colored('RED', 'red', attrs=['bold', 'blink'])
print (ginfo)
print (p1inf + p1col, p2inf + p2col)
print('=========================')

#   Do that again.

time.sleep(1)

#   Player-side information.

#   P1 starts playing from here.

while True:
    info = colored('Sticks Remaining | ', 'yellow', attrs=['bold', 'blink'])
    print(info, sticks)
    print('=========================')
    user1 = colored('Take Stick(s) [1-4] > ', 'blue', attrs=['bold', 'blink'])
    sticks_taken = int(input(user1))
    
#   Choice check for P1. If they get the last one, they lose.
    
    if sticks == 1:
        last = colored('You Took the last one.', 'white', attrs=['bold', 'reverse'])
        lost = colored('You lost.', 'red', attrs=['bold', 'reverse'])
        print(last, lost)
        break

    if sticks_taken >= 5 or sticks_taken <= 0:
        choice = colored('Wrong choice.', 'yellow', attrs=['blink', 'bold'])
        print (' ')
        print('WARNING !', choice)
        print (' ')
        continue
    sticks -= sticks_taken
    if sticks == 0:
        break

#   P2 starts playing from here.

    info = colored('Sticks Remaining | ', 'yellow', attrs=['bold', 'blink'])
    print(info, sticks)
    print('=========================')
    user2 = colored('Take Stick(s) [1-4] > ', 'red', attrs=['bold', 'blink'])
    sticks_taken = int(input(user2))

#   Choice check for P2. If they get the last one, they lose.

    if sticks == 1:
        last = colored('You Took the last one.', 'white', attrs=['bold', 'reverse'])
        lost = colored('You lost.', 'red', attrs=['bold', 'reverse'])
        print(last, lost)
        break

    if sticks_taken >= 5 or sticks_taken <= 0:
        choice = colored('Wrong choice.', 'yellow', attrs=['blink', 'bold'])
        print (' ')
        print('WARNING !', choice)
        print (' ')
        continue
    sticks -= sticks_taken
    if sticks == 0:
        break
#   Development Code. Can be reused for a Computer vs Human mode. Also, code from the first version gets stored here.

  #  These lines are reserved for a future PvAI mode, where one player plays against the computer.
  #  ucomp = colored('Computer Took > ', 'green', attrs=['bold', 'blink'])
  #  print(ucomp, (5 - sticks_taken), "\n")

  #  These lines are reserved for a future 3-players mode.
  #  user3 = colored('Take Stick(s) [1-4] > ', 'green', attrs=['bold', 'blink'])
  #  sticks_taken = int(input(user3))

  #    user2 = colored('Take Stick(s) [1-4] > ', 'red', attrs=['bold', 'blink'])
  #    sticks_taken = int(input(user2))