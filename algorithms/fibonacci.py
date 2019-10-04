# Python3 Fibonacci sequence. Prints the first n terms of Fibonacci sequence.
# 0,1,2,3,4,5,6,7
# 0,1,1,2,3,5,8,13

# O(2^n)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# O(n)
last_sums = [0, 1]
def fibcache(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        sum = last_sums[0] + last_sums[1]
        last_sums[0] = last_sums[1]
        last_sums[1] = sum
        return sum

#limit = 30 # fib() gets very slow after n=25
limit = 30 # fibcache is much better!
for n in range(0, limit):
#   print({n: fib(n)})
    print({n: fibcache(n)})