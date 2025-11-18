"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verse-support.pages.dev
Prompt: Create a script to detect and prevent common crypto-related scams, using the advice provided in the Bitcoin.com Support Center's "Beware of Scams" section.
Generated: DETERMINISTIC_026854f071d17a7f
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoScamDetector:
    """Class to detect and prevent common crypto-related scams."""

    def __init__(self):
        self.scam_patterns = [
            r'(fake|phishing|scam).*?(website|link)',
            r'(win|earn|get).*?\d+\s*(btc|bitcoin|crypto)',
            r'(send|transfer).*?\d+\s*(btc|bitcoin|crypto).*?to.*?(address|wallet)',
            r'(investment|profit).*?(guaranteed|risk-free)',
            r'(limited time|urgent).*?(offer|deal)',
            r'(?<!\w)(0x[a-fA-F0-9]{40})(?!\w)',  # Ethereum address pattern
            r'(?<!\w)([1-3][a-zA-HJ-NP-Z1-9]{25,34})(?!\w)',  # Bitcoin address pattern
        ]

    def detect_scam(self, message):
        """Detects potential scams in a given message."""
        for pattern in self.scam_patterns:
            if re.search(pattern, message, re.IGNORECASE):
                logging.warning(f'Scam detected: {message}')
                return True
        logging.info('No scams detected.')
        return False

    def advise_user(self):
        """Provide advice to the user on how to avoid scams."""
        advice = [
            "1. Never share your private keys or passwords.",
            "2. Be cautious of unsolicited messages or emails.",
            "3. Verify the identity of anyone asking for your crypto.",
            "4. Use reputable exchanges and wallets only.",
            "5. Report any suspicious activity to the appropriate authorities."
        ]
        logging.info("Advice to avoid scams:")
        for tip in advice:
            logging.info(tip)

def main():
    """Main function to run the scam detector."""
    detector = CryptoScamDetector()

    # Example messages to analyze (in a real application, these would be user inputs)
    messages = [
        "Earn 1 BTC in just one hour! Click this fake website!",
        "Congratulations! You've won a crypto prize! Send your wallet address.",
        "This is a limited time offer to double your investment!"
    ]

    for message in messages:
        if detector.detect_scam(message):
            detector.advise_user()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
