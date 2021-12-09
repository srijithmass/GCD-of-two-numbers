'''Program to find the gcd of a number using function.
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
def gcd():
    n1=int(input())
    n2=int(input())
    if(n1>n2):
        smaller=n2
    else:
        smaller=n1
    for i in range(1,smaller+1):
        if(n1%i==0 and n2%i==0):
            GCD=i
    print("GCD of two numbers is:",GCD)