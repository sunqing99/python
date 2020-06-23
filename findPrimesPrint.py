#!/usr/local/bin/python3
#
from math import sqrt
import sys

def findPrimes(N):
  if (N < 2):
    return []
  primes = [2]
  count = 1
  print("Prime #{}: {}".format(count, primes[0]))
 
  for i in range(3, N+1, 2):
    sqrti = sqrt(i)
    if (len(primes) == 1):
      primes.append(i)
      continue
    isPrime = True
    for p in primes:
      if (p > sqrti):
        break
      if (i%p == 0):
        isPrime = False
        break
    if (isPrime):
      primes.append(i)
      count += 1
      print("Prime #{}: {}".format(count, i))

if (len(sys.argv) > 1):
  maxnum = int(sys.argv[1])
else:
  print ("Enter a number, I will print out all primes smaller than that number", end = ": ")
  maxnum = int(input())

primes = findPrimes(maxnum)

