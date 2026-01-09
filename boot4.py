#power(x,n)
#input x=decimal number n=integer
# logic n=0 return 1

def myPow(x: float, n: int) -> float:
    if n==0:
        return 1.0
    
    if n<0:
        return 1/mypow(x,-n)
    
    half = mypow(x,n//2) 

    if n%2==0:
        return half*half # n is even
    else:
        return half*half*x # n is odd