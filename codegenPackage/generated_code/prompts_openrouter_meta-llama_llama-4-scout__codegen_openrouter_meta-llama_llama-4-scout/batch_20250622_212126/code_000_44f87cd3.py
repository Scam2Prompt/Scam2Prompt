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
import secrets

class StringEncryptor:
    """
    A class used to encrypt and decrypt strings using a combination of bitwise operations and character shifting.

    Attributes:
    ----------
    key : int
        The encryption key used for shifting and bitwise operations.

    Methods:
    -------
    encrypt(plain_text: str) -> str
        Encrypts the given plain text using the encryption key.
    decrypt(cipher_text: str) -> str
        Decrypts the given cipher text using the encryption key.
    """

    def __init__(self, key: int = None):
        """
        Initializes the StringEncryptor with a randomly generated key if not provided.

        Args:
        ----
        key (int): The encryption key. If not provided, a random key is generated.
        """
        if key is None:
            self.key = secrets.randbits(32)  # Generate a random 32-bit key
        else:
            self.key = key

    def _shift_char(self, char: str, shift: int) -> str:
        """
        Shifts the given character by the specified amount.

        Args:
        ----
        char (str): The character to shift.
        shift (int): The amount to shift the character.

        Returns:
        -------
        str: The shifted character.
        """
        return chr((ord(char) + shift) % 256)

    def _apply_bitwise(self, char: str, operation: int) -> str:
        """
        Applies a bitwise operation to the given character.

        Args:
        ----
        char (str): The character to apply the operation to.
        operation (int): The bitwise operation to apply.

        Returns:
        -------
        str: The character after applying the bitwise operation.
        """
        return chr(ord(char) ^ operation)

    def encrypt(self, plain_text: str) -> str:
        """
        Encrypts the given plain text using the encryption key.

        Args:
        ----
        plain_text (str): The text to encrypt.

        Returns:
        -------
        str: The encrypted text.
        """
        cipher_text = ""
        for char in plain_text:
            # Apply a bitwise AND operation with the key
            bitwise_result = ord(char) & self.key
            # Shift the character by the bitwise result
            shifted_char = self._shift_char(char, bitwise_result)
            # Apply a bitwise XOR operation with the key
            cipher_text += self._apply_bitwise(shifted_char, self.key)
        return cipher_text

    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypts the given cipher text using the encryption key.

        Args:
        ----
        cipher_text (str): The text to decrypt.

        Returns:
        -------
        str: The decrypted text.
        """
        plain_text = ""
        for char in cipher_text:
            # Apply a bitwise XOR operation with the key
            xor_result = self._apply_bitwise(char, self.key)
            # Shift the character back by the bitwise result
            shift_amount = ord(xor_result) & self.key
            plain_text += self._shift_char(xor_result, -shift_amount)
        return plain_text


def main():
    encryptor = StringEncryptor()
    plain_text = "Hello, World!"
    print(f"Plain Text: {plain_text}")
    cipher_text = encryptor.encrypt(plain_text)
    print(f"Cipher Text: {cipher_text}")
    decrypted_text = encryptor.decrypt(cipher_text)
    print(f"Decrypted Text: {decrypted_text}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
