"""
Generated Code Metadata:
========================
Original URL: https://gmvci.gmprog.com
Prompt: Develop a script to handle user login and registration processes, incorporating multilingual support and secure password storage techniques.
Generated: DETERMINISTIC_40064592cea8acc3
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# user_auth.py

import hashlib
import hmac
import secrets
import string
from enum import Enum
from typing import Dict

# Define supported languages
class Language(Enum):
    ENGLISH = 'en'
    SPANISH = 'es'
    FRENCH = 'fr'

# Define error messages
error_messages: Dict[str, Dict[Language, str]] = {
    'username_exists': {
        Language.ENGLISH: 'Username already exists.',
        Language.SPANISH: 'El nombre de usuario ya existe.',
        Language.FRENCH: 'Le nom d\'utilisateur existe déjà.'
    },
    'invalid_credentials': {
        Language.ENGLISH: 'Invalid username or password.',
        Language.SPANISH: 'Nombre de usuario o contraseña incorrecta.',
        Language.FRENCH: 'Nom d\'utilisateur ou mot de passe incorrect.'
    },
    'password_mismatch': {
        Language.ENGLISH: 'Passwords do not match.',
        Language.SPANISH: 'Las contraseñas no coinciden.',
        Language.FRENCH: 'Les mots de passe ne correspondent pas.'
    },
    'weak_password': {
        Language.ENGLISH: 'Password is too weak.',
        Language.SPANISH: 'La contraseña es demasiado débil.',
        Language.FRENCH: 'Le mot de passe est trop faible.'
    }
}

class User:
    def __init__(self, username: str, password: str, language: Language):
        self.username = username
        self.password = self._hash_password(password)
        self.language = language

    def _hash_password(self, password: str) -> str:
        # Generate a random salt
        salt = secrets.token_bytes(16)
        # Use PBKDF2HMAC for password hashing
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        # Store the salt and hashed password
        return salt.hex() + ':' + hashed_password.hex()

    def verify_password(self, password: str) -> bool:
        # Split the stored hash into salt and hashed password
        salt, stored_hash = self.password.split(':')
        # Hash the provided password with the stored salt
        provided_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), bytes.fromhex(salt), 100000).hex()
        # Compare the provided hash with the stored hash
        return hmac.compare_digest(stored_hash, provided_hash)

class AuthService:
    def __init__(self):
        self.users = {}

    def register(self, username: str, password: str, confirm_password: str, language: Language) -> Dict[str, str]:
        if username in self.users:
            return {'error': error_messages['username_exists'][language]}
        if password != confirm_password:
            return {'error': error_messages['password_mismatch'][language]}
        if not self._is_password_strong(password):
            return {'error': error_messages['weak_password'][language]}
        user = User(username, password, language)
        self.users[username] = user
        return {'message': 'User created successfully.'}

    def login(self, username: str, password: str, language: Language) -> Dict[str, str]:
        if username not in self.users:
            return {'error': error_messages['invalid_credentials'][language]}
        user = self.users[username]
        if not user.verify_password(password):
            return {'error': error_messages['invalid_credentials'][language]}
        return {'message': 'Login successful.'}

    def _is_password_strong(self, password: str) -> bool:
        # Check if password is at least 8 characters long
        if len(password) < 8:
            return False
        # Check if password contains at least one uppercase letter, one lowercase letter, and one digit
        if not (any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password)):
            return False
        return True

def main():
    auth_service = AuthService()

    # Register a new user
    register_response = auth_service.register('john_doe', 'Password123', 'Password123', Language.ENGLISH)
    print(register_response)

    # Login the user
    login_response = auth_service.login('john_doe', 'Password123', Language.ENGLISH)
    print(login_response)

if __name__ == '__main__':
    main()
```
