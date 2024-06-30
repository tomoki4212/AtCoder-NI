import math


A, B, C = map(int, input().split())

gcd = math.gcd(A, B, C)

print(int(A / gcd - 1) + int(B / gcd - 1) + int(C / gcd - 1))