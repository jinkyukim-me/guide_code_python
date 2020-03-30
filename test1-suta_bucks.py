n = int(input())

total = 0
for i in range(n):
    order = input()
    
    if order == "아메리카노":
        total = total + 4100
    elif order == "카페라떼":
        total = total + 4600
    elif order == "카라멜마끼아또":
        total = total + 5100
        
print(total)
