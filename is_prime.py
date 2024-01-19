import math

def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(math.sqrt(n)) + 1):
      if n % x == 0:
        return False
  return True

if __name__ == "__main__":
  num = int(input('> '))
  if num > 1:
    print(is_prime(num))
  else:
    print(boolean(False))
