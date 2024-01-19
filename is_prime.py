import math

def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(math.sqrt(n)) + 1):
      if n % x == 0:
        return False
  return True

if __name__ == "__main__":
  while True:
    num = int(input('> '))
    print(is_prime(num))
