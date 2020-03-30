def skyCastle(arr):
    dic = {'에릭' : 1, '김동완' : 2, '전진' : 3, '이민우' : 4, '앤디' : 5}
    return [ dic[i] for i in arr]

print(skyCastle(["에릭", "이민우", "김동완", "전진"]))

