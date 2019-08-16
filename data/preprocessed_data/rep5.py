def weightedsum(li):
'''
this functions creates representation 5
input: li - lists of ranks
output: feature (column) - number of voters (here: 25)
        value of the feature -  waited sum of the rank
'''
    su = 0
    for i in range(len(li)):
        su+=(20-i)*li[i]
    return su
datasetsWeightedSum=[]
