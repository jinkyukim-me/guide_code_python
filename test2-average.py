def myMean(arr):
    return (sum(arr) - max(arr) - min(arr)) / (len(arr) - 2)

ans = myMean([1, 2, 3, 4, 6])
print(ans)
