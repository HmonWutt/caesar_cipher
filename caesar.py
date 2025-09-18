from glob import translate
from operator import le
import string


class Caesar:
    def __init__(self):
        self.encrypt_table = {}
        self.decrypt_table ={}

    def create_encrypt_table(self,shift):
        letters = string.ascii_lowercase 
        self.encrypt_table = {i: chr((ord(i)-ord('a')+shift)%26+ord('a')) for i in letters}
        print(self.encrypt_table)
    
    def encrypt(self,message):
        return self.translate(message.lower(),self.encrypt_table)
                
    def create_decrypt_table(self):
        if self.encrypt_table:
            self.decrypt_table = {v:k for k,v in self.encrypt_table.items()}
    
    def decrypt(self,message):
        return self.translate(message.lower(),self.decrypt_table)


    def translate(self,message,dictionary):
        text = ""
        for letter in message:
            if letter !=" ":
                new_letter = dictionary[letter]
                text+=new_letter
            else:
                text+=" "
        return text
    



