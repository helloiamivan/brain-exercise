# Given N = Number of digits and X = Sum of the digits, find all possible integer combinations
def sumDigit(x):
    pass

def genInt(num_digit):
    num_iter_start = int(str(9)*(num_digit-1))
    num_iter_end = int(str(9)*num_digit)
    for x in range(num_iter_start+1,num_iter_end+1):
        yield x

if __name__ == "__main__" :
    
    prices = [1,2,3,4,5,4,3,4,3,4,5,6,7,4,3,6,2,10]
    N = 5

    # Should return [5,2]

    print(calcMaxDrawdowns( prices , N , percent = False ))