n = int(input())
user_name=[input() for _ in range(n)]

ans = {}
for i, user in enumerate(user_name):
    if user not in ans:
        ans[user] = i+1
print("\n".join(map(str, list(ans.values()))))