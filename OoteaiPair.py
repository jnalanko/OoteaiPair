import sys
from random import random
from random import shuffle

if len(sys.argv) != 2:
    print "Usage: python OoteaiPair.py inputfile"
    quit()

infile = open(sys.argv[1],'r')
players = []

for line in infile:
    if line[0] == "#":
        # Comment line, ignore
        continue
    tokens = line.split(',')
    name = tokens[0].strip()
    score =  tokens[1].strip()
    players.append((score,name))

# Shuffle the players list and sort in descending order with respect to the scores.
shuffle(players)
players.sort(key=lambda player: player[0], reverse=True)

pairing = []
index = 0
while index < len(players):
    if index == len(players) - 1:
        # Uneven number of players, cannot pair the last player
        pairing.append((players[index], "No opponent"))
        break
    black = players[index]
    white = players[index+1]
    r = random()
    if r > 0.5:
        # Swap black and white
        temp = black
        black = white
        white = temp
    pairing.append((black,white)) 
    index += 2

print "----------"
print "Pairing for the round"
print "----------"
print "The left column plays black, the right column plays white"
for p in pairing:
    print p
