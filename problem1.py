import math
import prime
import inverse_modulor


def encrypt(message, e, n):
    encrypted_blocks = [pow(ord(char), e, n) for char in message]
    return encrypted_blocks

def main():


    p = prime.findNBitPrimeNumber(60)
    q = prime.findNBitPrimeNumber(60)
    print('p:', p)
    print('q:', q)

    n = p * q
    fi = (p-1) * (q - 1)
    print('n:', n)
    print('fi:', fi)

    e = prime.findNBitPrimeNumber(100)
    while math.gcd(e, fi) != 1:
       e = prime.findNBitPrimeNumber(100)
    
    d = inverse_modulor.mod_inverse(e, fi)
    print('d:', d)
    print('encrypt daihoccongnghe', encrypt('daihoccongnghe', e, n))
    print('encrypt khongcogiquyhondoclaptudo', encrypt('khongcogiquyhondoclaptudo', e, n))

if __name__ == "__main__":
  main()