def power(a, b, MOD):
    ans = 1
    p = a
    for i in range(len(bin(b)) - 2):
        if b & (1 << i):
            ans = (ans * p) % MOD
        p = (p * p) % MOD

    return ans


a, b = map(int, input().split())
print(power(a, b, int(1e9) + 7))
