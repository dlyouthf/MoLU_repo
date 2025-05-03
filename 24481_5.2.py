import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, N + 1):
    adj[i].sort()

visited = [False] * (N + 1)
depth = [-1] * (N + 1)

def dfs(node, d):
    visited[node] = True
    depth[node] = d
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, d + 1)

dfs(R, 0)

for d in depth[1:]:
    print(d)
#최종

N, M, R = map(int, input().split())

V = list(range(1, N+1))
E = []
for i in range(M):
    a, b = map(int, input().split())
    E.append((a, b))
depth = {}
visited = {}
for i in V:
    visited[i] = 'NO'

def close(i):
    V_list = []
    filtered = [pair for pair in E if i in pair]
    if filtered:
        for j in filtered:
            other = j[1] if j[0] == i else j[0]
            V_list.append(other)
    V_list = sorted(V_list)
    return V_list

depth[R] = 0
def dfs(a):
    V.remove(a)
    if visited[a] == 'NO':
        visited[a] = 'YES'
    if close(a):
        for i in close(a):
            if visited[int(i)] == 'NO':
                depth[i] = depth[a] + 1
                dfs(i)
dfs(R)
for i in V:
    depth[i] = -1

for i in range(1, N+1):
    print(depth[i])
#직접 구현했으나 시간 초과
