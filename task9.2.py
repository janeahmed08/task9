rounds=[(1,5),(2,3),(1,4)]
scoreboard={}
def sum(rounds):
    for i,score in rounds:
        scoreboard[i]=scoreboard.get(i,0)+score
    return scoreboard
res=sum(rounds)
print(res)