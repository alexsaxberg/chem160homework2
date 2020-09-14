from random import choices
ntrials = 10000
player1wins = 0

for i in range(ntrials):
    player2 = choices(range(1, 7), k=2)
    if player2[0] == player2[1]:
        continue
    player1 = choices(range(1, 7), k=3)
    player1.sort(reverse=True)
    sumplayer1 = player1[0]+player1[1]
    sumplayer2 = player2[0]+player2[1]
    if player1.count(2) >= 2:
        continue
    if sumplayer1 > sumplayer2:
        player1wins += 1

print("Average roll=", player1wins/ntrials)