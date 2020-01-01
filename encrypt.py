"""
Created on Sun Dec 22 15:31:11 2019
@author: Drew
"""
# Import lowercase chars
from string import ascii_lowercase
import re

# Def Funcs
def text_import(text_file):
    with open(text_file, 'r') as myfile:
        data = myfile.read()
        data = re.sub(",|\.|;|-|'","",data)
    return data

def string_to_num(raw_message):
    num_string = []
    for char in raw_message.lower():
        if char in ascii_lowercase:
            num_string.append(ord(char)-97)   # ord converts char to num
        else:
            num_string.append(char)
    return(num_string)

def num_to_string(num_char_mapping):
    output_string = ""
    for char in num_char_mapping:
        if isinstance(char, int):
            char = int(char)+97
            char = chr(char)                    # chr converts num to car
            output_string = output_string + str(char)       
        else:
            output_string = output_string + char
    return(output_string)

def caesar_cipher_encrypt(num_char_mapping, shift):
    char_count = 0
    num_char_mapping_length = len(num_char_mapping)
    while char_count < num_char_mapping_length:
        if isinstance(num_char_mapping[char_count], int):
            num_char_mapping[char_count] = (num_char_mapping[char_count]+shift) % 26
        else:
            pass
        char_count += 1
    return(num_char_mapping)

def caesar_cipher_decrypt(encrypted_num_char_mapping, shift):
    char_count = 0
    num_char_mapping_length = len(encrypted_num_char_mapping)
    while char_count < num_char_mapping_length:
        if isinstance(encrypted_num_char_mapping[char_count], int):
            encrypted_num_char_mapping[char_count] = (encrypted_num_char_mapping[char_count]-shift) % 26
        else:
            pass
        char_count += 1
    return(encrypted_num_char_mapping)

def unknown_shift_caesar_cipher_decrypt(encrypted_num_char_mapping, num_char_mapping):
    encrypted_num_char_mapping_length = len(encrypted_num_char_mapping)
    for shift in range(26):
        copied_encrypted_num_char_mapping = encrypted_num_char_mapping.copy()
        char_count = 0
        while char_count < encrypted_num_char_mapping_length:
            if isinstance(copied_encrypted_num_char_mapping[char_count], int):
                copied_encrypted_num_char_mapping[char_count] = (copied_encrypted_num_char_mapping[char_count]-shift) % 26
            else:
                pass
            char_count += 1
        if copied_encrypted_num_char_mapping[0] == num_char_mapping[0]:
            print("Shift was: ", shift)
            return(caesar_cipher_decrypt(encrypted_num_char_mapping,shift)) 


def aphine_cipher_encrypt(num_char_mapping, shift, multiplier):
    char_count = 0
    num_char_mapping_length = len(num_char_mapping)
    while char_count < num_char_mapping_length:
        if isinstance(num_char_mapping[char_count], int):
            num_char_mapping[char_count] = (multiplier * (num_char_mapping[char_count])+shift) % 26
        else:
            pass
        char_count += 1
    return(num_char_mapping)

def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 
  
def modinv(a, m): 
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None  # modular inverse does not exist 
    else: 
        return x % m 

def aphine_cipher_decrypt(encrypted_num_char_mapping, shift, multiplier):
    inv_mult = modinv(multiplier, 26)
    char_count = 0
    num_char_mapping_length = len(encrypted_num_char_mapping)
    while char_count < num_char_mapping_length:
        if isinstance(encrypted_num_char_mapping[char_count], int):
            encrypted_num_char_mapping[char_count] = (inv_mult * (encrypted_num_char_mapping[char_count] - shift)) % 26
        else:
            pass
        char_count += 1
    return(encrypted_num_char_mapping)    
    

# should be relative prime to mod number
# Theorem 1: If aand mare relatively prime integers and m> 1, then an inverse of amodulo mexists.Furthermore, this inverse is unique modulo m




def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=list(range(3,n+1,2))
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=int((m*m-3)/2)
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]


#raw_message = text_import("message.txt")
raw_message = "abcdefghijklmnopqrstuvwxyz"
numerical_string = string_to_num(raw_message)
encrypt_string = aphine_cipher_encrypt(numerical_string, 2, 3)
decrypted_string = aphine_cipher_decrypt(encrypt_string, 2, 3)



encryped_string = caesar_cipher_encrypt(numerical_string, 58)
decryped_string = unknown_shift_caesar_cipher_decrypt(encryped_string, string_to_num(raw_message))
#decryped_string = caesar_cipher_decrypt(encryped_string, 1)
output_string = num_to_string(decryped_string)

primes(50)


def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
x = primes2(1000000000)
