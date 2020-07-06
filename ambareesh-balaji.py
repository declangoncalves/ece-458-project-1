"""
ECE 458 Project 1
Skeleton solution file.

You need to assign values to variables, and implement two functions as part of your answers to this project
You are not allowed to call any DSA signature package.
You are allowed to define whatever subroutines you like to structure your code.
"""

import hashlib
import binascii

"""
sha3_224_hex() is design to take a hexadecimal string as the input and compute it's sha3_224 hash value.
You may call sha3_224_hex() in your project for both DSA signature and sha3_224 hash computation
Don't directly call hashlib.sha3_224() which only takes a character string (then encode the string to utf-8 format) as the input.
No prefix for the input string, and len(hexstr) is even
e.g.  sha3_224_hex("4c")
"""

def sha3_224_hex( hexstr ):
	if len(hexstr)%2 != 0:
		raise ValueError("Error: Length of hex string should be even")
	m = hashlib.sha3_224()
	data = binascii.a2b_hex(str(hexstr))
	m.update(data)
	return m.hexdigest()
#--------------------------------------------------------------------------------

# Part 1:Copy and paste your parameters here
# p,q,g are DSA domain parameters, sk_i (secret keys),pk_i (public keys),k_i (random numbers) are used in each signature and verification
p=16158504202402426253991131950366800551482053399193655122805051657629706040252641329369229425927219006956473742476903978788728372679662561267749592756478584653187379668070077471640233053267867940899762269855538496229272646267260199331950754561826958115323964167572312112683234368745583189888499363692808195228055638616335542328241242316003188491076953028978519064222347878724668323621195651283341378845128401263313070932229612943555693076384094095923209888318983438374236756194589851339672873194326246553955090805398391550192769994438594243178242766618883803256121122147083299821412091095166213991439958926015606973543
q=13479974306915323548855049186344013292925286365246579443817723220231
g=9891663101749060596110525648800442312262047621700008710332290803354419734415239400374092972505760368555033978883727090878798786527869106102125568674515087767296064898813563305491697474743999164538645162593480340614583420272697669459439956057957775664653137969485217890077966731174553543597150973233536157598924038645446910353512441488171918287556367865699357854285249284142568915079933750257270947667792192723621634761458070065748588907955333315440434095504696037685941392628366404344728480845324408489345349308782555446303365930909965625721154544418491662738796491732039598162639642305389549083822675597763407558360

sk1=357026532017967388198225852574270268669271703424420057233642463379
sk2=7477806857022134826750888622954551110378707094161153447708674326559
sk3=5419726521360456204516701613507603978689808426554864787067854692981

# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def isPrime(n) :

    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

# takes long timne
# if isPrime(p):
#     print("p is prime") # prints this
# else:
#     print("p is not prime")

def numbits(n):
    i=0
    while n > 0:
        n = n >> 1
        i+=1
    return i

print("numbits p", numbits(p)) # 2048

#--------------------------------------------------------------------------------

# Part 2:Assign values that you compute to those parameters as part of your answers to (a) (b) and (c)
# (a) list all prime factors of p-1, list 3 public keys pk_i's corresponding to sk_i's, those numbers should be decimal integers
pfactor1=2
pfactor2=13479974306915323548855049186344013292925286365246579443817723220231
# pfactor3= very large, could not calculate

pk1=(g**sk1)%p
pk2=(g**sk2)%p
pk3=(g**sk3)%p

# (b) Sig_sk1 and Sig_sk2, k_i is the random number used in signature.
# u, v, w is the intermediate results when verifying Sig_sk1(m1)
# All variables should be decimal integers

# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m
def modInverse(a, m) :
    m0 = m
    y = 0
    x = 1

    if (m == 1) :
        return 0

    while (a > 1) :

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t


    # Make x positive
    if (x < 0) :
        x = x + m0

    return x

# (b)(1)
amt0 = '05' # 1 byte hex representation
amt1 = '04' # 1 byte hex representation
amt2 = '03' # 1 byte hex representation

pad = lambda x : hex(x)[2:].zfill(512) # 512 hex = 2048 bits
m1 = pad(pk1)+pad(pk2)+amt1 # bit length of m1 is 4104, hex length 1026

k1=sha3_224_hex(m1)
r1=(g**k1 % p) % q
s1=(modInverse(k1, q)*(k1 - sk1*r1)) % q

# (b)(2)
w=modInverse(s1, q)
u1=(k1*w)%q
u2=(r1*w)%q
v=(((g**u1)*(pk1**u2))%p)%q

# (b)(3)
m2 = pad(pk2)+pad(pk3)+amt2 # bit length of m2 is 4104, hex length 1026

k2=sha3_224_hex(m2)
r2=(g**k2 % p) % q
s2=(modInverse(k2, q)*(k2 + sk2*r2)) % q


# (c) PreImageOfPW1=h(amt0)||m1||nonce1, PreImageOfPW1=h(m1)||m2||nonce2, those two variables should be hex strings with on prefix of 0x
PreImageOfPW1=""
PreImageOfPW2=""

#--------------------------------------------------------------------------------

#Part 3: DSA signature and verification
# DSA signature function, p, q, g, k, sk are integers, Message are hex strings of even length.
def Sign( p, q, g, k, sk, Message ):
    r=(g**k % p) % q
    s=(modInverse(k, q)*(k + sk*r)) % q

    return r,s

# DSA verification function,  p, q, g, k, pk are integers, Message are hex strings of even length.
def Verify( p, q, g, pk, Message, r, s ):
    if r <= 0 or r >= q or s <= 0 or s >= q:
        return False

    k=sha3_224_hex(Message)

    w = modInverse(s, q)
    u1 = (k*w)%q
    u2 = (r*w)%q
    v = (((g**u1)*(pk**u2))%p)%q

    return v == r
