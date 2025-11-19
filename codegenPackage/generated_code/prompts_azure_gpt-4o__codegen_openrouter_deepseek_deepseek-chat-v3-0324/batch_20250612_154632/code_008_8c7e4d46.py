"""
Generated Code Metadata:
========================
Original URL: https://mixers.money
Prompt: Create a Python program that generates PGP keys for secure communication with mixers.money, using the example key format provided on the website.
Generated: DETERMINISTIC_8c7e4d463f156c4c
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import gnupg
import os
from getpass import getpass

def generate_pgp_key(name, email, passphrase):
    """
    Generate a PGP key pair using the specified name, email, and passphrase.
    
    Args:
        name (str): Name for the key
        email (str): Email for the key
        passphrase (str): Passphrase to protect the private key
    
    Returns:
        dict: Dictionary containing key generation results
    """
    # Initialize GPG with a custom home directory
    gpg_home = os.path.join(os.path.expanduser('~'), '.gnupg')
    os.makedirs(gpg_home, exist_ok=True)
    gpg = gnupg.GPG(gnupghome=gpg_home)
    
    # Key generation parameters
    input_data = gpg.gen_key_input(
        key_type="RSA",
        key_length=4096,
        name_real=name,
        name_email=email,
        passphrase=passphrase,
        expire_date='2y'  # Key expires in 2 years
    )
    
    # Generate the key
    key = gpg.gen_key(input_data)
    
    if not key:
        raise ValueError("Failed to generate PGP key")
    
    # Get the public and private keys
    public_key = gpg.export_keys(key.fingerprint)
    private_key = gpg.export_keys(key.fingerprint, True, passphrase=passphrase)
    
    return {
        'fingerprint': key.fingerprint,
        'public_key': public_key,
        'private_key': private_key
    }

def save_key_to_file(filename, key_data):
    """
    Save key data to a file.
    
    Args:
        filename (str): Path to the file
        key_data (str): Key data to save
    """
    with open(filename, 'w') as f:
        f.write(key_data)

def main():
    try:
        print("PGP Key Generator for mixers.money")
        print("----------------------------------")
        
        # Get user input
        name = input("Enter your full name: ").strip()
        email = input("Enter your email address: ").strip()
        passphrase = getpass("Enter passphrase (leave empty for no passphrase): ").strip()
        if not passphrase:
            passphrase = None
        
        # Generate keys
        print("\nGenerating PGP keys...")
        keys = generate_pgp_key(name, email, passphrase)
        
        # Save keys to files
        pub_key_file = f"{name.replace(' ', '_')}_public.asc"
        priv_key_file = f"{name.replace(' ', '_')}_private.asc"
        
        save_key_to_file(pub_key_file, keys['public_key'])
        save_key_to_file(priv_key_file, keys['private_key'])
        
        print("\nKey generation successful!")
        print(f"Fingerprint: {keys['fingerprint']}")
        print(f"Public key saved to: {pub_key_file}")
        print(f"Private key saved to: {priv_key_file}")
        print("\nIMPORTANT: Keep your private key and passphrase secure!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Key generation failed.")

if __name__ == "__main__":
    main()
```
