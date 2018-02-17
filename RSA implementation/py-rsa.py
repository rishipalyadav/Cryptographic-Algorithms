#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 11:58:02 2018

@author: rishi
"""

import sys
import math 
import random

prime = list()

#Function to check prime number
def is_prime(num):
	for j in range(2,int(math.sqrt(num)+1)):
		if (num % j) == 0: 
			return False
	return True

#Function to find a prime number pool 
def prime_pool():
    low = random.randint(0,2**5);
    high = random.randint(2**10,2**14);
    if (low % 2 == 0):
        low += 1
    for i in range(low,high,2):
        if is_prime(i):
            prime.append(i)
        
        
#Generating Key Pool
prime_pool()

#Function to calculate gcd
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a 

#Function to find extended gcd
def egcd(a,b):
    if a==0:
        return (b,0,1)
    else:
        g,y,x=egcd(b%a,a)
    return (g,x-(b//a)*y,y)

#Function to find Modular Inverse
def modInv(a,m):
    g,x,y = egcd(a,m)
    if g !=1:
        return None
    else:
        return x%m


#Generating two initial prime numbers
p1 = random.choice(prime)
p2 = random.choice(prime)

#Finding modulo N
n = p1*p2
print("N is: ", n)

#Finding PHI_N
phi_n = (p1-1)*(p2-1)
print("PHI_N is: ", phi_n)

#Finding E
e = random.randint(2,1000)

while True:
    if gcd(e,phi_n) == 1:
        break
    else:
        e += 1
        
print("E is: ",e)

#Finding D
d = modInv(e,phi_n)
print("D is: ",d)

message = input("Enter message to encrypt: ")
print(message)
cipher=((int(message))**e) % n
print("Encrypted Message is: ",cipher)

decrypt = (cipher**d) % n

print("Decryption is: ",decrypt)
