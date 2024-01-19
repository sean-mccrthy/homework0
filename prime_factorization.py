def prime_factorization(n):
  nums = []
  x = 2
  while n > 1:
    if n % x == 0:
      nums.append(x)
      n /= x
    else:
      x += 1
  return nums

if __name__ == "__main__":
  num = 2
  while num > 1:
    num = int(input('> '))
    if num > 1:
      print(prime_factorization(num))
