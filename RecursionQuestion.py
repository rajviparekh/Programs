def recursion(n):
    if n==0:
        return 1
    elif n==1:
        return 0
    else:
        return recursion(n-1)+ (2*recursion(n-2))+2

print(recursion(15))