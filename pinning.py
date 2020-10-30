def pin(A):
    A.sort(key=lambda x: x[1])
    last = A[0][1]
    cnt = 1
    for i in range(1, n):
        if A[i][0] > last:
            cnt += 1
            last = A[i][1]
    return cnt


n = int(input())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
A = pin(A)
print(A)