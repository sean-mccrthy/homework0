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
  while True:
    num = int(input('> '))
    print(prime_factorization(num))
