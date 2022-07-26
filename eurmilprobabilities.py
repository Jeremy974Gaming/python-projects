import math as m
from termcolor import colored
import time as t

print("===================================================")
print("================ First Combination ================")
n1 = int(input("Enter the first digit of the combination : "))
n2 = int(input("Enter the second digit of the combination : "))
n3 = int(input("Enter the third digit of the combination : "))
n4 = int(input("Enter the fourth digit of the combination : "))
n5 = int(input("Enter the Last digit of the combination : "))
print(" ")
print("===================================================")
print("===============  Star Combination  ================")
s1 = int(input("Enter the first star of the combination : "))
s2 = int(input("Enter the second star of the combination : "))

t.sleep(2)

print(" ")
print("===================================================")
print("=============== Second Combination ================")
n10 = int(input("Enter the first digit of the combination : "))
n20 = int(input("Enter the second digit of the combination : "))
n30 = int(input("Enter the third digit of the combination : "))
n40 = int(input("Enter the fourth digit of the combination : "))
n50 = int(input("Enter the Last digit of the combination : "))
print(" ")
print("===================================================")
print("===============  Star Combination  ================")
s10 = int(input("Enter the first star of the combination : "))
s20 = int(input("Enter the second star of the combination : "))

t.sleep(2)

#   Global Value declaration, numbers.

SEP_COMB_1 = "+"
SEP_COMB_2 = "+"
COMB_1_OK = n1 and n2 and n3 and n4 and n5
COMB_2_OK = n10 and n20 and n30 and n40 and n50

WAYS_TO_WIN_1 = 53130
WAYS_TO_WIN_2 = 690000
WAYS_TO_LOSE_1 = 2065630
WAYS_TO_LOSE_2 = 1428760
FAVORABLE_1 = COMB_1_OK
FAVORABLE_2 = COMB_2_OK
TOTAL = 2118760
HALF = TOTAL / 2

t.sleep(1)

#   Global Value declaration, stars.

STARS_1 = s1 and s2
STARS_2 = s10 and s20

t.sleep(1)

#   Analysis of the dataset, first combination (stars + num).

s_proba_1 = HALF / STARS_1
s_odds_1 = STARS_1 / STARS_1 - HALF
probability_1 = TOTAL / FAVORABLE_1
odds_1 = FAVORABLE_1 / FAVORABLE_1 - TOTAL
wodds_1 = WAYS_TO_WIN_1 / WAYS_TO_LOSE_1

#   Analysis of the dataset, second combination (stars + num).

s_proba_2 = HALF / STARS_2
s_odds_2 = STARS_2 / STARS_2 - HALF
probability_2 = TOTAL / FAVORABLE_2
odds_2 = FAVORABLE_2 / FAVORABLE_2 - TOTAL
wodds_2 = WAYS_TO_WIN_2 / WAYS_TO_LOSE_2

t.sleep(1)

#   Statistical equation related to either combination.

COMB_1 = COMB_1_OK / (WAYS_TO_WIN_1 - WAYS_TO_LOSE_1)
COMB_2 = COMB_2_OK / (WAYS_TO_WIN_2 - WAYS_TO_LOSE_2)

t.sleep(1)

#   Text coloration, first combination.

probtext_1 = colored(' Probability : ', 'green', attrs=['bold', 'blink'])
oddstext_1 = colored(' Odds : ', 'red', attrs=['bold', 'blink'])
woddstext_1 = colored(' Winning Odds : ', 'blue', attrs=['bold', 'blink'])
comb1text = colored('First Combination (Numbers + Stars) : ', 'blue', attrs=['bold', 'reverse'])
s1_probtxt = colored(' Stars Probability : ', 'green', attrs=['bold', 'blink'])
s1_oddstxt = colored(' Stars Odds : ', 'red', attrs=['bold', 'blink'])

#   Text coloration, second combination.

probtext_2 = colored(' Probability : ', 'green', attrs=['bold', 'blink'])
oddstext_2 = colored(' Odds : ', 'red', attrs=['bold', 'blink'])
woddstext_2 = colored(' Winning Odds : ', 'blue', attrs=['bold', 'blink'])
comb2text = colored('Second Combination (Numbers + Stars) : ', 'blue', attrs=['bold', 'reverse'])
s2_probtxt = colored(' Stars Probability : ', 'green', attrs=['bold', 'blink'])
s2_oddstxt = colored(' Stars Odds : ', 'red', attrs=['bold', 'blink'])

t.sleep(1)

#   Difference between probabilities.

DIFFERENCE = COMB_1 - COMB_2

t.sleep(1)

#   Color the difference.

DIFFTEXT = colored(' Difference : ', 'white', attrs=['bold', 'reverse'])

#   Output the end result (numbers + stars)
print("===================================================")
print(comb1text, n1, n2, n3, n4, n5, '|', s1, s2)
print(probtext_1, probability_1, oddstext_1, odds_1, woddstext_1, wodds_1)
print(s1_probtxt, s_proba_1, s1_oddstxt, s_odds_1)
print("===================================================")
print(comb2text, n10, n20, n30, n40, n50, '|', s10, s20)
print(probtext_2, probability_2, oddstext_2, odds_2, woddstext_2, wodds_2)
print(s2_probtxt, s_proba_2, s2_oddstxt, s_odds_2)
print("===================================================")
print(DIFFTEXT, DIFFERENCE)