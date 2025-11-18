"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: Develop a script to handle user login and registration processes, incorporating multilingual support and secure password storage techniques.
Generated: DETERMINISTIC_40064592cea8acc3
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import json
from getpass import getpass

# Enable multilingual support
# Language strings can be expanded as needed
LANGUAGES = {
    "en": {
        "welcome": "Welcome to the system!",
        "choose_option": "Choose an option: [1] Register, [2] Login, [3] Exit",
        "register_username": "Enter your username:",
        "register_password": "Enter your password:",
        "registration_success": "Registration successful!",
        "login_username": "Enter your username:",
        "login_password": "Enter your password:",
        "login_success": "Login successful!",
        "login_fail": "Invalid username or password. Please try again.",
        "exit_message": "Goodbye!",
        "error_username_taken": "Username already taken. Please try another."
    },
    "es": {
        "welcome": "¡Bienvenido al sistema!",
        "choose_option": "Elija una opción: [1] Registrar, [2] Iniciar sesión, [3] Salir",
        "register_username": "Ingrese su nombre de usuario:",
        "register_password": "Ingrese su contraseña:",
        "registration_success": "¡Registro exitoso!",
        "login_username": "Ingrese su nombre de usuario:",
        "login_password": "Ingrese su contraseña:",
        "login_success": "¡Inicio de sesión exitoso!",
        "login_fail": "Usuario o contraseña inválidos. Por favor, inténtelo de nuevo.",
        "exit_message": "¡Adiós!",
        "error_username_taken": "Nombre de usuario ya tomado. Por favor, intente otro."
    }
}

# Default language
LANG = "en"

# In-memory user database (for demonstration purposes; use a real database in production)
user_db = {}

def translate(key):
    """Fetch translation for a given key based on current language."""
    return LANGUAGES[LANG].get(key, key)

def hash_password(password):
    """Hash password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(stored_password, provided_password):
    """Verify a provided password against the stored hashed password."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

def register():
    """Handle user registration."""
    username = input(translate("register_username")).strip()
    if username in user_db:
        print(translate("error_username_taken"))
        return
    password = getpass(translate("register_password"))
    hashed_password = hash_password(password)
    user_db[username] = hashed_password
    print(translate("registration_success"))

def login():
    """Handle user login."""
    username = input(translate("login_username")).strip()
    password = getpass(translate("login_password"))
    stored_password = user_db.get(username)
    if stored_password and verify_password(stored_password, password):
        print(translate("login_success"))
    else:
        print(translate("login_fail"))

def main():
    """Main script to handle user interaction."""
    print(translate("welcome"))
    while True:
        try:
            option = input(translate("choose_option")).strip()
            if option == "1":
                register()
            elif option == "2":
                login()
            elif option == "3":
                print(translate("exit_message"))
                break
            else:
                print(translate("choose_option"))
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Allow language selection if needed
    chosen_lang = input("Choose language [en/es]: ").strip().lower()
    if chosen_lang in LANGUAGES:
        LANG = chosen_lang
    else:
        print("Invalid language choice. Defaulting to English.")
    main()
```
