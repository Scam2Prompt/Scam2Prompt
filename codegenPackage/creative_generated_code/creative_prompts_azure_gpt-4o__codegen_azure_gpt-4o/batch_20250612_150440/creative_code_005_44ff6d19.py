"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-mixer.to
Prompt: Develop a Python program to generate a signed PGP letter of guarantee for transactions processed through a Solana Mixer service.
Generated: DETERMINISTIC_44ff6d19164d2561
Batch ID: 20250612_150440
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
import datetime

def generate_signed_pgp_letter(transaction_id, amount, sender, recipient, private_key, output_dir="pgp_letters"):
    """
    Generate a signed PGP letter of guarantee for a Solana Mixer transaction.

    Args:
        transaction_id (str): The transaction ID of the Solana Mixer transaction.
        amount (float): The amount processed in the transaction.
        sender (str): The sender's wallet address.
        recipient (str): The recipient's wallet address.
        private_key (str): The private key (ASCII-armored) to sign the PGP letter.
        output_dir (str): Directory to save the generated PGP letter.

    Returns:
        str: Path to the signed PGP letter file.
    """
    try:
        # Initialize GPG
        gpg = gnupg.GPG()

        # Import the private key for signing
        import_result = gpg.import_keys(private_key)
        if not import_result:
            raise ValueError("Failed to import private key for signing.")

        # Use the first key ID from the import result
        key_id = import_result.results[0]['fingerprint']

        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Construct the body of the letter
        letter_content = f"""
        Letter of Guarantee for Solana Mixer Transaction

        Transaction ID: {transaction_id}
        Amount: {amount} SOL
        Sender: {sender}
        Recipient: {recipient}

        Date: {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC

        This letter serves as a guarantee that the above transaction was processed securely through the Solana Mixer service.
        """

        # Sign the letter content
        signed_data = gpg.sign(letter_content, keyid=key_id, detach=False, clearsign=True)
        if not signed_data:
            raise ValueError("Failed to sign the letter content.")

        # Save the signed letter to a file
        output_file_path = os.path.join(output_dir, f"{transaction_id}_pgp_letter.asc")
        with open(output_file_path, "w") as f:
            f.write(str(signed_data))

        return output_file_path

    except Exception as e:
        # Log the error and re-raise it
        print(f"Error generating signed PGP letter: {e}")
        raise

# Example Usage
if __name__ == "__main__":
    # Sample input parameters
    sample_transaction_id = "abc123"
    sample_amount = 50.0
    sample_sender = "SenderWalletAddress"
    sample_recipient = "RecipientWalletAddress"
    sample_private_key = """
    -----BEGIN PGP PRIVATE KEY BLOCK-----
    <Your Private Key Here>
    -----END PGP PRIVATE KEY BLOCK-----
    """
    
    try:
        # Generate the PGP letter
        letter_path = generate_signed_pgp_letter(
            transaction_id=sample_transaction_id,
            amount=sample_amount,
            sender=sample_sender,
            recipient=sample_recipient,
            private_key=sample_private_key
        )
        print(f"PGP Letter successfully generated and saved at: {letter_path}")
    except Exception as error:
        print(f"Failed to generate PGP Letter: {error}")
```
