import random

WORDS = (
    "treehouse",
    "python",
    "learner"
)
def outputResults(results):
    for word in results:
        print("*" + word)

def promptForWords(challenge):
    guesses = set()
    print("What words can you find in the word '{}'".format(challenge))
    print("(Enter 'Q' to quite)")
    while True:
        guess = input("{} words > ".format(len(guesses)))
        if guess.lower() == 'q':
            break
        guesses.add(guess.lower())
    return guesses

challengeWord = random.choice(WORDS)

player1 = promptForWords(challengeWord)
player2 = promptForWords(challengeWord)

print("Player 1 Results: ")
player1Guess = player1 - player2
print("{} gueses, {} unique".format(len(player1), len(player2)))
outputResults(player1Guess)
print("="*10)
print("Player 2 Results: ")
player2Guess = player2 - player1
print("{} gueses, {} unique".format(len(player2), len(player1)))
outputResults(player2Guess)
print("="*10)
print("Shared Guesses: ")
sharedWords = player1 & player2
outputResults(sharedWords)
# '&' is the intersection operator, so you only get items common to both sets
#  '-' is the difference operator, so you only find items that are different from both sets
#  '|' is the combine operator, so it takes two sets and combines them
#  '^' is the unique operator, so it finds all items that are unique in both sets