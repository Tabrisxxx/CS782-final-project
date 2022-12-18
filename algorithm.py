from math import log
import random
import math
from collections import OrderedDict


# method check if the number is prime
def checkprime(num: int):
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if (num % i) == 0:
            return False
    return True


# method check if g is primitive root of p
def is_root(g, prime):
    for i in range(1, prime - 1):
        # If g^i mod p is equal to 1, g is not a primitive root

        if (g**i) % prime == 1:
            return False
    return True


# method find prime root
def primitive_root(prime):
    g = random.randrange(2, prime)

    # If it is, return g
    if is_root(g, prime):
        return g
    while not is_root(g, prime):
        g = random.randrange(2, prime)
    return g


# def generate private key
def gen_c1(g, a, prime):
    return (g**a) % prime


# Encryption
def elgamal_enc(c1, k, prime):
    return (c1**k) % prime


# Mod inverse
def mod_inverse(input, prime):
    for i in range(1, prime):
        if ((input % prime) * (i % prime)) % prime == 1:
            return i
    return -1


# decryption
def decrypt(dec, enc_msg):
    return dec * enc_msg


def prime_factors(n):
    li = []
    while n % 2 == 0:
        li.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            li.append(i)
            n = n / i
    if n > 2:
        li.append(int(n))

    return li


def dis_log(base, num, p):
    order = p - 1
    bj = {}
    #generator = primitive_root(p)
    m = math.ceil(math.sqrt(order))
    for j in range(0, m):
        bj[j] = base**j % p

    bj = OrderedDict(sorted(bj.items()))
    # print(bj)
    c = mod_inverse(base, p)
    check = c**m % p
    for i in range(0, m):
        for k in bj.keys():
            if bj[k] == num * (check ** i) % p:
                return i*m + k


