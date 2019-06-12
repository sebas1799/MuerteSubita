d=[(1,1),(2,3),(10,4),(15,5),(16,17),(21,6)]
#print map(lambda x,y: [x]+[y[0]],map(lambda x: x/2 ,map(lambda x,y: x*y,map(lambda x: x[1]+1,d),map(lambda x: x[1],d))),d))
print reduce(lambda x,y: x+y,map(lambda x: x[0],filter(lambda x: x[0]==(((x[1])*(x[1]+1))/2), d))) 

"[x[1]]*[x[1]]+1/2"
