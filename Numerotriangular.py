d=[(1,1),(2,3),(10,4),(15,5),(16,17),(21,6)]
print reduce(lambda x,y: x+y,map(lambda x: x[0],filter(lambda x: x[0]==(((x[1])*(x[1]+1))/2), d))) 

