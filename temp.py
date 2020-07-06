from math import sqrt
from itertools import count, islice

def is_prime(n):
    return all(n % i for i in xrange(2, n))

# A function to print all prime factors of  a given number n 
def primeFactors(n): 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print 2, 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print i, 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print n 

def nth_root(num, root):
    answer = num**(1/root)
    return answer
          
# Driver Program to test above function 
  
p = 16158504202402426253991131950366800551482053399193655122805051657629706040252641329369229425927219006956473742476903978788728372679662561267749592756478584653187379668070077471640233053267867940899762269855538496229272646267260199331950754561826958115323964167572312112683234368745583189888499363692808195228055638616335542328241242316003188491076953028978519064222347878724668323621195651283341378845128401263313070932229612943555693076384094095923209888318983438374236756194589851339672873194326246553955090805398391550192769994438594243178242766618883803256121122147083299821412091095166213991439958926015606973543
q = 13479974306915323548855049186344013292925286365246579443817723220231
# primeFactors(p - 1)
a = 2
anum = 1

newP = (p - 1) / (2*q)

#print newP
n = 3
z = 1

while ((p - 1) % (q*2*n) != 0) and ((q*2*n) < p - 1) :
    n = n + 1


    
    
# print a
print n
#print z

#print (p - 1) / 4

#print is_prime(p / 2)