import math

def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(math.sqrt(n)) + 1):
      if n % x == 0:
        return False
  return True

if __name__ == "__main__":
  num = 2
  while num > 0:
    num = int(input('> '))
    if num > 1:
      print(prime_factorization(num))
