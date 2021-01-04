#Mendel's 1st Law

def MendelLaw(k,m,n):
    x = float(k+m+n)
    probablity = 1 - ( m*n + 0.25*m*(m-1) + n*(n-1) ) / ( x*(x-1) )
    return probablity

MendelLaw(29,20,15)