#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime

def main():
    n = 10001
    count = 0
    num = 1
    while count < n:
      num += 1
      if isPrime(num):
          count += 1
    print(num)

if __name__ == '__main__':
  main()
