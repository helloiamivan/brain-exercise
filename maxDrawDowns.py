## Code computes the N maximum drawdowns given a vector of prices
## TODO: Modify the code to include returning the periods of the drawdown in an efficient manner

def maximum_accumulate(x):
    runningMax = []
    maxK = 0
    for i,k in enumerate(x):
        if (k > maxK) or (i == 0):
            maxK = k
        runningMax.append(maxK)
        
    return runningMax

def groupDrawdowns(peaks,drawdowns):
    
    from operator import itemgetter
    from itertools import groupby
    
    li = zip(peaks,drawdowns)
    
    glob = [[y for x,y in g] for k,g in groupby(li, key = itemgetter(0))]
    
    return glob

def calcMaxDrawdowns(prices, N , percent = True):
    
    # Here, the drawdown is defined as price - maxprice (we can also use percentage change)
    drawdowns = [(i - n) / n if percent else i - n for i,n in zip(prices,maximum_accumulate(prices))]

    groupedDD = groupDrawdowns(maximum_accumulate(prices),drawdowns)
    
    orderedDD = sorted(list(set([abs(min(x)) for x in groupedDD if min(x) != 0])),reverse=True)[:N]
    
    if len(orderedDD) > 0:
        return orderedDD[:N]
    else:
        return None

if __name__ == "__main__" :
    
    prices = [1,2,3,4,5,4,3,4,3,4,5,6,7,4,3,6,2,10]
    N = 5

    # Should return [5,2] as the answer

    print(calcMaxDrawdowns( prices , N , percent = False ))