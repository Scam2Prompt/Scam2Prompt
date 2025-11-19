"""
Generated Code Metadata:
========================
Original URL: https://sha-11x.pages.dev
Prompt: Write a code snippet that implements a complex string encryption algorithm, possibly using a combination of bitwise operations and character shifting, as hinted by the presence of seemingly encoded text on the webpage.
Generated: DETERMINISTIC_44f87cd3f42ea960
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import string

class StringEncryptor:
    """
    A class to encrypt and decrypt strings using a combination of bitwise operations
    and character shifting.
    """

    def __init__(self, shift: int):
        """
        Initializes the StringEncryptor with a specified shift value.

        :param shift: The number of positions to shift each character.
        """
        self.shift = shift

    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts the given plaintext using a combination of character shifting and bitwise operations.

        :param plaintext: The string to be encrypted.
        :return: The encrypted string.
        """
        encrypted_chars = []
        for char in plaintext:
            if char in string.printable:
                # Shift the character and apply bitwise XOR with the shift value
                shifted_char = chr((ord(char) + self.shift) % 256)
                encrypted_char = chr(ord(shifted_char) ^ self.shift)
                encrypted_chars.append(encrypted_char)
            else:
                # Non-printable characters are added unchanged
                encrypted_chars.append(char)
        return ''.join(encrypted_chars)

    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts the given ciphertext back to plaintext.

        :param ciphertext: The string to be decrypted.
        :return: The decrypted string.
        """
        decrypted_chars = []
        for char in ciphertext:
            if char in string.printable:
                # Reverse the bitwise XOR and then shift back
                shifted_char = chr(ord(char) ^ self.shift)
                decrypted_char = chr((ord(shifted_char) - self.shift) % 256)
                decrypted_chars.append(decrypted_char)
            else:
                # Non-printable characters are added unchanged
                decrypted_chars.append(char)
        return ''.join(decrypted_chars)

# Example usage
if __name__ == "__main__":
    try:
        shift_value = 5
        encryptor = StringEncryptor(shift_value)

        original_text = "Hello, World!"
        encrypted_text = encryptor.encrypt(original_text)
        decrypted_text = encryptor.decrypt(encrypted_text)

        print(f"Original: {original_text}")
        print(f"Encrypted: {encrypted_text}")
        print(f"Decrypted: {decrypted_text}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
