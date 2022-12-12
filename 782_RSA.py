import random
import math


# method check if the number is prime
def checkprime(num: int):
	if num == 2:
		return True
	if num % 2 == 0:
		return False

	for i in range(3, int(num ** 0.5) + 1, 2):
		if (num % i) == 0:
			return False
	return True


# Mod inverse
def mod_inverse(input, prime):
	for i in range(1, prime):
		if ((input % prime) * (i % prime)) % prime == 1:
			return i
	return -1


# collect prime factor
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


if __name__ == '__main__':
	# First, the sender would need to generate a public key and a private key.
	# The public key consists of the product of two large prime numbers, n,
	# and a public exponent, e. The private key is the product of the two prime
	# numbers and a private exponent, d, kept secret.
	p = random.randrange(100, 1000)
	while not checkprime(p):
		p = random.randrange(100, 1000)
	if checkprime(p):
		print("prime number1: ", p)

	q = random.randrange(100, 1000)
	while not checkprime(q):
		q = random.randrange(100, 1000)
	if checkprime(q):
		print("prime number2: ", q)

	# picks an encryption component e and publishes n
	# and e on its website
	# public_exp = random.randrange(0, 10000)
	n = q * p
	order = (q - 1) * (p - 1)
	print("n is:", n)
	print("Order of n: ", order)
	e = random.randrange(0, order)
	while not checkprime(e):
		e = random.randrange(0, order)
	if checkprime(e):
		print("Exponent e chose by Bob(Public key): ", e)
	d = mod_inverse(e, order)
	# decryption component
	print("Inverse of e which is d equals to (Private key): ", d)
	print("--- Processing Encryption ---")
	# message chose by Alice
	msg = random.randrange(1, order)
	while not checkprime(msg):
		msg = random.randrange(1, order)
	if checkprime(msg):
		print("Plaintext is: ", msg)

	# encryption
	y = msg ** e % n
	print("Ciphertext is: ", y)
	print("--- Processing Decryption ---")
	# decryption
	pl_msg = y ** d % n
	print("Msg after decrypt is: ", pl_msg)

	# eavesdrop
	print("--- Processing Eavesdrop ---")
	print("Information known for eavesdrop: n: %d, e: %d, ciphertext: %d" % (n, e, y))
	li = prime_factors(n)
	print("Prime factor of n: ", li)
	eve_order = (li[0] - 1) * (li[1] - 1)
	print("Order of n after eavesdrop: ", eve_order)
	eve_d = mod_inverse(e, eve_order)
	print("Inverse of e after eavesdrop: ", eve_d)

	eve_msg = y ** eve_d % n
	print("Plaintext after eavesdrop: ", eve_msg)
