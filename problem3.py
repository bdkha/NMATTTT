import math
import prime
import random

def count_points_on_elliptic_curve(p, a, b):
    count = 0
    for x in range(p):
        for y in range(p):
            if (y**2) % p == (x**3 + a * x + b) % p:
                count += 1
    return count
 
def findPrimaryPointCurve(p): 
    for a in range(p):
        for b in range(p):
            points_count = count_points_on_elliptic_curve(p, a, b)
            if prime.isMillerRabinPassed(points_count + 1):
                return a, b
            
    return None, None
    

def main():
    p = prime.findNBitPrimeNumber(15)

    a,b = findPrimaryPointCurve(p)
    print(a,b)


if __name__ == "__main__":
  main()