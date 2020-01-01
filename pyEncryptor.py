# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 18:34:47 2019

@author: Drew
"""
# Import lowercase chars
from string import ascii_lowercase
import re

class pyCryptr:
    
    def __init__(self):
        self.caeser = self.caeser()
        self.aphine = self.aphine()
        
    def text_import(self, text_file):
        with open(text_file, 'r') as myfile:
            data = myfile.read()
            data = re.sub(",|\.|;|-|'","",data)
        return data
    
    def string_to_num(self, raw_message):
        num_string = []
        for char in raw_message.lower():
            if char in ascii_lowercase:
                num_string.append(ord(char)-97)   # ord converts char to num
            else:
                num_string.append(char)
        return(num_string)
    
    def num_to_string(self, num_char_mapping):
        output_string = ""
        for char in num_char_mapping:
            if isinstance(char, int):
                char = int(char)+97
                char = chr(char)                    # chr converts num to car
                output_string = output_string + str(char)       
            else:
                output_string = output_string + char
        return(output_string)
          
    class caeser:
        def caesar_cipher_encrypt(self, num_char_mapping, shift):
            char_count = 0
            num_char_mapping_length = len(num_char_mapping)
            while char_count < num_char_mapping_length:
                if isinstance(num_char_mapping[char_count], int):
                    num_char_mapping[char_count] = (num_char_mapping[char_count]+shift) % 26
                else:
                    pass
                char_count += 1
            return(num_char_mapping)
        
        def caesar_cipher_decrypt(self, encrypted_num_char_mapping, shift):
            char_count = 0
            num_char_mapping_length = len(encrypted_num_char_mapping)
            while char_count < num_char_mapping_length:
                if isinstance(encrypted_num_char_mapping[char_count], int):
                    encrypted_num_char_mapping[char_count] = (encrypted_num_char_mapping[char_count]-shift) % 26
                else:
                    pass
                char_count += 1
            return(encrypted_num_char_mapping)
        
        def unknown_shift_caesar_cipher_decrypt(self, encrypted_num_char_mapping, num_char_mapping):
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
                    return(self.caesar_cipher_decrypt(encrypted_num_char_mapping,shift)) 

    class aphine:
        def aphine_cipher_encrypt(self, num_char_mapping, shift, multiplier):
            char_count = 0
            num_char_mapping_length = len(num_char_mapping)
            while char_count < num_char_mapping_length:
                if isinstance(num_char_mapping[char_count], int):
                    num_char_mapping[char_count] = (multiplier * (num_char_mapping[char_count])+shift) % 26
                else:
                    pass
                char_count += 1
            return(num_char_mapping)
        
        def egcd(self, a, b): 
            x,y, u,v = 0,1, 1,0
            while a != 0: 
                q, r = b//a, b%a 
                m, n = x-u*q, y-v*q 
                b,a, x,y, u,v = a,r, u,v, m,n 
            gcd = b 
            return gcd, x, y 
          
        def modinv(self, a, m): 
            gcd, x, y = self.egcd(a, m) 
            if gcd != 1: 
                return None  # modular inverse does not exist 
            else: 
                return x % m 
        
        def aphine_cipher_decrypt(self, encrypted_num_char_mapping, shift, multiplier):
            inv_mult = self.modinv(multiplier, 26)
            char_count = 0
            num_char_mapping_length = len(encrypted_num_char_mapping)
            while char_count < num_char_mapping_length:
                if isinstance(encrypted_num_char_mapping[char_count], int):
                    encrypted_num_char_mapping[char_count] = (inv_mult * (encrypted_num_char_mapping[char_count] - shift)) % 26
                else:
                    pass
                char_count += 1
            return(encrypted_num_char_mapping)    
            
crypt_eng = pyCryptr()
word = crypt_eng.text_import("message.txt")
word = crypt_eng.string_to_num(word)
encrypted = crypt_eng.caeser.caesar_cipher_encrypt(word,5)
decrypted = crypt_eng.caeser.caesar_cipher_decrypt(encrypted, 5)
final = crypt_eng.num_to_string(decrypted)

