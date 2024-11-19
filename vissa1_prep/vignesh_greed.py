N = int(input())
sticks = sorted(map(int, input().split()), reverse=True)
for i in range(N - 2):
    if sticks[i] < sticks[i + 1] + sticks[i+2]:
        print(sticks[i]+sticks[i+1]+sticks[i+2])
        break
else:
    print(-1)
