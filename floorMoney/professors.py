from __future__ import division
import random

# The number of games to simulate
NUMBER_OF_GAMES = 1000000

# The number of professors (starting player is professor 0)
NUMBER_OF_PLAYERS = 3

# Returns index of winning professor.
def playProfessorGame(numPlayers):
  position = 0
  while True:
    move = random.choice([-1,0,1])
    if not move:
      return position
    position = (position + move) % numPlayers

win_record = {}
for _ in range(NUMBER_OF_GAMES):
  winner = playProfessorGame(NUMBER_OF_PLAYERS)
  wins[winner] = wins.get(winner, 0) + 1

print "Starting player won %.3f%% of the time." % (100*wins[0]/NUMBER_OF_GAMES)
