N = int(input())
stair = [int(input()) for _ in range(N)]
dp = [0]*(N) #각 계단까지의 최대 점수

if len(stair) <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0] #첫 번째 계단까지의 최대 점수
    dp[1] = stair[0] + stair[1] #두 번째 계단까지의 최대 점수
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2]) #세 번째 계단까지의 최대 점수
    for i in range(3, N):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
        #i-3번째 계단부터 두 계단 연속 걸었을 때와 한 계단 건너 뛰었을 때 비교
    print(dp[-1])
