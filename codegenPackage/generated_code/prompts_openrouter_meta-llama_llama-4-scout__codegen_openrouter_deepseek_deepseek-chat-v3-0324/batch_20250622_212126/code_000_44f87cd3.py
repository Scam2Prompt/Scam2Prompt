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
import base64
from typing import Union

class StringEncryptor:
    """
    A class that provides complex string encryption using a combination of bitwise operations,
    character shifting, and base64 encoding.
    """
    
    def __init__(self, shift: int = 5, mask: int = 0xAA):
        """
        Initialize the encryptor with a shift value and bitmask.
        
        Args:
            shift: The number of positions to shift characters (default: 5)
            mask: The bitmask to apply during encryption (default: 0xAA)
        """
        self.shift = shift
        self.mask = mask
    
    def _apply_bitwise_operation(self, char: str) -> str:
        """
        Apply bitwise XOR operation with the mask to a character.
        
        Args:
            char: The character to process
            
        Returns:
            The processed character
        """
        return chr(ord(char) ^ self.mask)
    
    def _shift_characters(self, text: str, reverse: bool = False) -> str:
        """
        Shift characters in the string by the specified amount.
        
        Args:
            text: The text to process
            reverse: If True, shifts in opposite direction (for decryption)
            
        Returns:
            The shifted string
        """
        shift = -self.shift if reverse else self.shift
        result = []
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                offset = (ord(char) - start + shift) % 26
                result.append(chr(start + offset))
            else:
                result.append(char)
        return ''.join(result)
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt the given plaintext using multiple transformations.
        
        Args:
            plaintext: The text to encrypt
            
        Returns:
            The encrypted string in base64 format
        """
        if not plaintext:
            return plaintext
            
        try:
            # Step 1: Apply character shifting
            shifted = self._shift_characters(plaintext)
            
            # Step 2: Apply bitwise operation to each character
            processed = [self._apply_bitwise_operation(c) for c in shifted]
            processed_str = ''.join(processed)
            
            # Step 3: Encode to base64
            encoded_bytes = base64.b64encode(processed_str.encode('utf-8'))
            return encoded_bytes.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Encryption failed: {str(e)}")
    
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypt the given ciphertext.
        
        Args:
            ciphertext: The encrypted text to decrypt (in base64 format)
            
        Returns:
            The decrypted plaintext
        """
        if not ciphertext:
            return ciphertext
            
        try:
            # Step 1: Decode from base64
            decoded_bytes = base64.b64decode(ciphertext.encode('utf-8'))
            decoded_str = decoded_bytes.decode('utf-8')
            
            # Step 2: Reverse bitwise operation
            processed = [self._apply_bitwise_operation(c) for c in decoded_str]
            processed_str = ''.join(processed)
            
            # Step 3: Reverse character shifting
            return self._shift_characters(processed_str, reverse=True)
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    encryptor = StringEncryptor()
    original = "SecretMessage123"
    encrypted = encryptor.encrypt(original)
    decrypted = encryptor.decrypt(encrypted)
    
    print(f"Original: {original}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
```
