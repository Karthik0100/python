arr=[[1,4,5],[2,3,4],[1,2,0]]

for sublist in arr:
    val = [i*v for i,v in enumerate(sublist)]
    print(sum(val))

