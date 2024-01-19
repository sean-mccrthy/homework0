import math

def is_prime(n):
  if n < 2:
    return False
  for x in range(2, int(math.sqrt(n)) + 1):
      if n % x == 0:
        return False
  return True

def nth_prime(n):
  if n == 1:
    return 2
  else:
    count = 2
    num = 3
    while count < n:
      num += 2
      if is_prime(num):
        count += 1
    return num

if __name__ == "__main__":
  num = 2
  while num > 1:
    num = int(input('> '))
    if num > 1:
      print(nth_prime(num))
