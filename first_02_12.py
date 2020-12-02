a = int(input())
b = int(input())
c = int(input())
d = int(input())

def min4(a,b,c,d):
    m = min(a,b)
    k = min(c,d)
    return(min(m,k))
    
print(min4(a,b,c,d))
