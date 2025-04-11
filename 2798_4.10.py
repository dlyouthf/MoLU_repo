N, M = map(int,input().split())
cards = list(map(int,input().split()))
sums = []
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
        l = cards[i] + cards[j] + cards[k]
        if l <= M:
            sums.append(l)
print(max(sums))

N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_sum = 0
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
        l = cards[i] + cards[j] + cards[k]
        if l <= M:
            max_sum = max(max_sum, l)
print(max_sum)
