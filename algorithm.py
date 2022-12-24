from math import log
import random
import math
from collections import OrderedDict


def dis_log(base, num, p):
    order = p - 1
    bj = {}
    # generator = primitive_root(p)
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


def binaryToDecimal(binary):
    dec = 0
    i = 0
    while binary != 0:
        dec = binary % 10
        dec = dec + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return dec


def random_root(p):
    dict = {i for i in range(1, p) if Expanded_Euclidean(i, p)[0] == 1}
    li = [[g for g in range(1, p) if dict == {pow(g, exp, p) for exp in range(1, p)}]]
    print(li)
    return random.choice(li[0])


def random_Naor_Reingold(n, x):
    p = random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)
    q = random.randrange(2**(n-1)+1, 2**n-1)
    N = q * p
    li = []
    for i in range(1, 2*n):
        while len(li) < 2*n:
            li.append(random.randrange(1, N))

    g = random_root(N)**2 % N
    bin_x = str(bin(x)[2:].zfill(n))
    # print(li)
    # print(bin_x)
    # print(bin(43)[2:].zfill(n))
    # li2 = [129, 978, 1350, 71, 3,1028, 514, 526, 411, 495, 216, 810]
    sum = 0
    # print(len(bin_x))
    for i in range(0, len(bin_x)):
        if bin_x[i] == '1':
            sum += li[2*i+1]
        elif bin_x[i] == '0':
            sum += li[2*i]
    # print(sum)
    c = g ** sum % N
    # print(c)
    bin_c = bin(c)[2:].zfill(2 * n)
    r = random.randrange(0, 2**n - 1)
    bin_r = bin(r)[2:].zfill(2 * n)
    dec = binaryToDecimal(int(bin_c)) & binaryToDecimal(int(bin_r))
    return dec


# length is length of bits
def blum(length):
    p = random.randrange(2, 100000)
    while not miller_prime(p) and not p % 4 == 3:
        p = random.randrange(2, 100000)
    #print(p)
    q = random.randrange(2, 100000)
    while not miller_prime(q) and not q % 4 == 3:
        q = random.randrange(2, 100000)
    #print(q)
    N = p * q
    str_bin = ""
    seed = random.randint(2, N-1)
    while length:
        s = pow(seed, 2, N)
        #print(s)
        b = s % 2
        seed = s
        str_bin += str(b)
        length -= 1
    return str_bin


def fast_exp(base, exp, p):
    y = 1
    while exp > 0:
        x = base % p
        if exp % 2 != 0:
            y = x * y % p
            exp = exp - 1
            print("%d  %d  %d" % (x, exp, y))
        elif exp % 2 == 0:
            x = x**2 % p
            exp = exp / 2
            print("%d  %d  %d" % (x, exp, y))

    return y


def miller_prime(n):
    if n % 2 == 0:
        return False
    exp = 0
    rm = n - 1
    while rm % 2 == 0:
        rm >>= 1
        exp += 1
    assert(2 ** exp * rm == n - 1)
    for k in range(0, exp):
        b = random.randrange(2, n - 2)
        # if b ** rm % n == 1 % n:
        if pow(b, rm, n) == 1 % n:
            return True
        if pow(b, rm, n) == -1 % n:
            return True
        else:
            for r in range(1, exp):
                exp2 = 2 ** r
                if pow(b, (rm * exp2), n) == -1 % n:
                    return True
    return False


def Expanded_Euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, y, x = Expanded_Euclidean(b % a, a)

    return gcd, x - (b // a) * y, y


def inverse_Euclidean(input, prime):
    gcd, x, y = Expanded_Euclidean(input, prime)
    if gcd != 1:
        return "No inverse exist"
    else:
        return x % prime


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


