# CS782-final-project

# El gamal is use dis log and baby giant step for evasdrop, for encryption I use g**a % prime to generated C1 which a is only known by Alice, and c1**l % prime to generate C2 which l is screct key hold by Alice. And for decryption, Bob use C1 as B1 and generated his B2 ** k % prime to generate B2 which k is only known by Bob. Then Bob recieve cipher text which is msg * C2 ** k % prime, then he compute the inverse of C2 ** k. And decrypt the message using (inverse of C2 ** k) * ciphertext % prime.

# Modify the in put range to generate new prime in this line

 p = random.randrange(1000, 10000)
    while not checkprime(p):
        p = random.randrange(1000, 10000)
    if checkprime(p):
        print("prime number: ", p)
    # root b as public key
    root = primitive_root(p)
    print("prime root of p: ", root)

    # random number as public key
    pub_key = random.randrange(1000, 10000)
    
    
  # Modify the msg integer in this line
  
  msg = random.randrange(0, p)
  
# RSA, First, the sender would need to generate a public key and a private key.
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
# and e on its website, which e in range(0, order of n)

# encryption
	ciphertext = msg ** e % n
  
# decrytion first compute the inverse of e in order of n
  plaintext = ciphertex ** d % n

# For eavesdrop, we need to compute the prime factor of n to got p and q, then eve is able to know the order which is (q-1)(p-1)
# Then Eve is able to get his/her d by inverse e in (q-1)(p-1), which e is published.
  eve_msg = ciphertext ** (inverse of e in order) % n





