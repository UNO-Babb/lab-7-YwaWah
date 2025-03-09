#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime

def main():
    limit = 2000000
    total = 0
    for num in range(2, limit):
       if isPrime(num):
          total += num
    print(total)

if __name__ == '__main__':
  main()
