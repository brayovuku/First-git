import math

max=int(input())

primes=[2,3,5] # pre-stored coz of the unique 6k+i formulae
k=1
i=1
x=(6*k)+i

while x<=max:
    x=(6*k)+i
    flag=False
    for y in range(5,(math.ceil(math.sqrt(x)))+1,+2):
        if x%y==0:
            flag=True
            break
    if i==1:
        i=5
    else:
        i=1
        k=k+1
    if flag==False:
        if x<=max:
            primes.append(x)

print (primes)
