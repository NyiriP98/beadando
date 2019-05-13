import math
def harminchat(a):
    s=0
    s=int(s)
    while a**s<1000000:
        s+=1
    return s-1

a=(int(input("Adj meg egy számot: ")))
s=harminchat(a)
print(harminchat(a))
print(a**(harminchat(a)))
print(a**(harminchat(a)+1))