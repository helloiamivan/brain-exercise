# Code computes the count of ideal integers where the product 3^x * 5*y must within a range of numbers [low,high] inclusive
import itertools, math

def getIdealNums(low, high):
    # Max possible range of the exponents (note we take 3 instead of 5)
    # We want to cut down the number of iterations as much as possible
    # The higher limit of the exponent
    maxIter = math.floor( math.log( high ) / math.log( 3 ) ) + 1 
    
    l1 = l2 = list(range(maxIter + 1)) ; count = 0
    
    for x,y in itertools.product(l1, l2):
        product = 3**x * 5**y
        
        # Check if product is within range
        if ( product <= high ) and ( product >= low ):
            count += 1
    
    return count

if __name__ == "__main__" :

    low = 1 ; high = 10   # should return 4
    low = 1 ; high = 2e09 # should return 147

    idealCount = getIdealNums( low , high )

    print(idealCount)