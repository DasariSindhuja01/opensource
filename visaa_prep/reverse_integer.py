def reverse_integer(n):
    rev = int(str(n)[::-1]) if n >= 0 else -int(str(n)[:0:-1])
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev
n = int(input())
print(reverse_integer(n))
