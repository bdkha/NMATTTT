import math
import prime
import random

def encryptElgamal(message, publickey):
    p, alpha, beta = publickey
    k = random.randint(2, p - 2)
    message_unicode = [ord(char) for char in message]

    en_message = []
    for i in message_unicode:
        K = pow(alpha, k, p)
        S = (pow(beta, k, p) * i) % p
        en_message.append((K,S))

    return en_message
 
    

def main():
    p = prime.findNBitPrimeNumber(100)

    print('p:', p)
    alpha = 2
    x = random.randint(2, p - 2)

    beta = pow(alpha, x, p)

    print('encrypt doanquanvietnamdichunglongcuuquocbuoc', encryptElgamal('doanquanvietnamdichunglongcuuquocbuoc', (p, alpha, beta)))

if __name__ == "__main__":
  main()