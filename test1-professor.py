scores = [int(i) for i in input().split()]

if scores[1] <= 50:
    print('F')
elif min(scores) >= 75:
    print('A+')
elif min(scores) >= 50:
    print('A')
else:
    print('B')

