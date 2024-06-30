N = int(input())
user_set = set()
for n in range(N):
    s = input()
    if s not in user_set:
        user_set.add(s)
        print(n+1)