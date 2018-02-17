#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 22:15:32 2018

@author: rishi
"""

import sys
import math 
import random



prime = list()


def is_prime(num):
	for j in range(2,int(math.sqrt(num)+1)):
		if (num % j) == 0: 
			return False
	return True

def prime_pool():
    low = random.randint(0,2**6);
    high = random.randint(2**10,2**20);
    if (low % 2 == 0):
        low += 1
    for i in range(low,high,2):
        if is_prime(i):
            prime.append(i)
        
        
#Generating Key Pool
prime_pool()

#generating Keys

pub_base = random.choice([2,3,5])
pub_modulus = random.choice(prime)
priv_bob = random.randint(1,2**10)
priv_alice = random.randint(1,2**10)

print("Shared Modulus is : ",hex(pub_modulus))
print("Shared base is: ",hex(pub_base))


#Generating shared key

alice_to_bob = (pub_base**priv_alice) % pub_modulus

bob_to_alice = (pub_base**priv_bob) % pub_modulus

shared_key = (bob_to_alice**priv_alice) % pub_modulus


print("Shared Key is:",hex(shared_key))

#Destroy priv_bob, priv_alice

priv_bob = None
priv_alice = None