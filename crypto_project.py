from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Generate a random key
key = get_random_bytes(16)  # 16 bytes = 128-bit key
cipher = AES.new(key, AES.MODE_EAX)

# Original message
message = "Hello, friend!"
print("Original Message:", message)

# Encrypt the message
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
encrypted_message = base64.b64encode(nonce + ciphertext).decode('utf-8')
print("Encrypted Message:", encrypted_message)

# Decrypt the message
encrypted_data = base64.b64decode(encrypted_message)
nonce = encrypted_data[:16]
ciphertext = encrypted_data[16:]
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
decrypted_message = cipher.decrypt(ciphertext).decode('utf-8')
print("Decrypted Message:", decrypted_message)
