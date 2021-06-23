total=int(input('Enter number of bananas at starting = '))
distance=int(input('Enter distance we want to cover = '))
load_capacity=int(input('Enter maximum load capacity of the camel = '))
lose=0
start=total
for i in range(distance):
    while start>0:
        start=start-load_capacity
        if start==1:
            lose=lose-1
        lose=lose+2
    lose=lose-1
    start=total-lose
    if start==0:
        break
print('Maximum number of bananas that can be transfered =',start)
