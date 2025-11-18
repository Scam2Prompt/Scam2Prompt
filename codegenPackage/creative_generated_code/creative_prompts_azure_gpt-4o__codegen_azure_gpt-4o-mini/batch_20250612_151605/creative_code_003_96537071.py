"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ciacy-triaonds-spleaf.yolasite.com
Prompt: Provide an example of how to use PGP signatures in Python to create a letter of guarantee for an Ethereum tumbler service.
Generated: DETERMINISTIC_96537071cd5fd6d6
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import gnupg
import os

class LetterOfGuarantee:
    def __init__(self, gpg_home):
        """
        Initialize the LetterOfGuarantee with a specified GPG home directory.
        :param gpg_home: Path to the GPG home directory.
        """
        self.gpg = gnupg.GPG(gnupghome=gpg_home)
        
    def generate_key(self, name, email):
        """
        Generate a GPG key pair for the user.
        :param name: The name of the user.
        :param email: The email of the user.
        :return: The fingerprint of the generated key.
        """
        input_data = self.gpg.gen_key_input(name_name=name, 
                                             name_email=email)
        key = self.gpg.gen_key(input_data)
        return key.fingerprint

    def create_letter(self, content):
        """
        Create a letter of guarantee.
        :param content: The content of the letter.
        :return: The content of the letter.
        """
        return f"Letter of Guarantee:\n\n{content}\n\nSigned by: {self.gpg.list_keys()[0]['uids'][0]}"

    def sign_letter(self, letter):
        """
        Sign the letter using the user's private key.
        :param letter: The letter content to sign.
        :return: The signed letter.
        """
        signed_data = self.gpg.sign(letter, detach=True)
        if not signed_data:
            raise Exception("Signing failed: {}".format(signed_data.stderr))
        return signed_data

    def save_signed_letter(self, signed_letter, filename):
        """
        Save the signed letter to a file.
        :param signed_letter: The signed letter content.
        :param filename: The name of the file to save the signed letter.
        """
        try:
            with open(filename, 'w') as f:
                f.write(str(signed_letter))
            print(f"Signed letter saved to {filename}")
        except IOError as e:
            raise Exception("Error saving signed letter: {}".format(e))

# Usage example
if __name__ == "__main__":
    gpg_home = "/path/to/your/gpg/home"  # Set your GPG home directory
    tumbler_service = LetterOfGuarantee(gpg_home)
    
    # Generate a GPG key pair (uncomment to generate a new key)
    # fingerprint = tumbler_service.generate_key("Your Name", "your_email@example.com")
    # print(f"Generated key with fingerprint: {fingerprint}")
    
    # Create a letter of guarantee
    letter_content = "This letter guarantees that the service is trustworthy."
    letter = tumbler_service.create_letter(letter_content)
    
    # Sign the letter
    signed_letter = tumbler_service.sign_letter(letter)
    
    # Save the signed letter to a file
    tumbler_service.save_signed_letter(signed_letter, "signed_guarantee_letter.txt")
```

**Note**: Ensure that the `python-gnupg` library is installed in your Python environment. You can install it using pip:

```bash
pip install python-gnupg
```
