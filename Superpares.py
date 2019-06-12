d=[22,34,67,88,2468,1444]
print map(lambda x: x[1],filter(lambda x: x[0]==True,zip(map(lambda x: (x==[]),map(lambda x: filter(lambda x: x%2!=0,map(lambda x: int(x),(list(filter(lambda x: x!="[" or x!="]",str(x)))))),d)),d)))
