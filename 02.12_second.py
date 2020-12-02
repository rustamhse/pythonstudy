a = int(input())
def my_div(a):
    div = 'no div'
    for i in range (2, a):
        if a % i == 0:
            div = i
    if div == 'no div':
        return(a)
    else:
        return(div)

print(my_div(a))
