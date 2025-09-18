from this import d
from caesar import Caesar
from message import Message

sender = input("Your name: ")
receiver = input("Who are you sending this to?: ")
message_to_encrypt = input("What message do you want to send?: ")
shift = int(input("What is the shift?: "))
print(f"Your shift is {shift}")
message = Message(sender,receiver,message_to_encrypt)
caesar = Caesar()
caesar.create_encrypt_table(shift)
caesar.create_decrypt_table()
encrypted_message = caesar.encrypt(message.text)
decrypted_message = caesar.decrypt(encrypted_message)
print("Your message got encrypted to: ",encrypted_message)
print("Encrypted message got decrypted to: ", decrypted_message)


