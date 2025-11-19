"""
Generated Code Metadata:
========================
Original URL: https://flarenet.works.app
Prompt: Generate a Python code snippet that implements a basic login functionality with username (ログインID) and password verification.
Generated: DETERMINISTIC_aad9b43cc2f22024
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
from getpass import getpass

# Mock user database (in production, use a proper database)
USER_DB = {
    "user1": {
        "password_hash": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # sha256 of "password"
        "salt": "randomsalt"
    }
}

def hash_password(password: str, salt: str) -> str:
    """Hash the password with SHA-256 and salt."""
    return hashlib.sha256((password + salt).encode()).hexdigest()

def verify_login(username: str, password: str) -> bool:
    """Verify if the provided credentials match the stored ones."""
    if username not in USER_DB:
        return False
    
    stored_hash = USER_DB[username]["password_hash"]
    salt = USER_DB[username]["salt"]
    input_hash = hash_password(password, salt)
    
    return input_hash == stored_hash

def login() -> None:
    """Main login function that handles user input and authentication."""
    print("=== ログイン画面 ===")
    username = input("ログインID: ").strip()
    password = getpass("パスワード: ").strip()
    
    if not username or not password:
        print("エラー: ログインIDとパスワードを入力してください。")
        return
    
    if verify_login(username, password):
        print(f"ログイン成功: {username}さん、ようこそ！")
    else:
        print("エラー: ログインIDまたはパスワードが間違っています。")

if __name__ == "__main__":
    login()
```
