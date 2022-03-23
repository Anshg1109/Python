#naive method
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    
    while (m%n) !=0:
        diff = m-n
         # diff>n? possible!
        (m,n)=(max(n,diff),min(n,diff))
    
    return (n)


# short method

def gcd(m,n):
    if m<n:
        (m,n)= (n,m)
    
    while (m%n)!= 0:
        (m,n)= (n,m%n) # m%n < n , laways!
    
    return(n)
