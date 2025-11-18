"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peng-six.vercel.app
Prompt: Write a disclaimer generator for meme tokens like $PENG, emphasizing risks and the importance of DYOR (do your own research).
Generated: DETERMINISTIC_d472adb84b1184c0
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import textwrap

class DisclaimerGenerator:
    """
    A class to generate disclaimers for meme tokens.
    """

    def __init__(self, token_name):
        """
        Initializes the DisclaimerGenerator with the specified token name.

        Args:
            token_name (str): The name of the token for which to generate a disclaimer.
        """
        if not isinstance(token_name, str) or not token_name.strip():
            raise ValueError("Token name must be a non-empty string.")
        self.token_name = token_name.strip()

    def generate_disclaimer(self):
        """
        Generates a disclaimer emphasizing risks and the importance of conducting one's own research (DYOR).

        Returns:
            str: A formatted disclaimer message.
        """
        disclaimer = (
            f"**Disclaimer for {self.token_name}**\n\n"
            "The investment in cryptocurrency, including meme tokens like {self.token_name}, "
            "involves significant risk and may result in the loss of all your invested capital.\n\n"
            "It is crucial to conduct your own research (DYOR) before making any investment decisions. "
            "Prices can be extremely volatile, and past performance is not indicative of future results.\n\n"
            "Please consult with a financial advisor if you are uncertain about your investment choices."
        )
        return disclaimer

    def format_disclaimer(self, disclaimer):
        """
        Formats the disclaimer for better readability.

        Args:
            disclaimer (str): The disclaimer text to format.

        Returns:
            str: Formatted disclaimer text.
        """
        return textwrap.fill(disclaimer, width=70)

def main():
    """
    Main function to run the disclaimer generator.
    """
    try:
        token_name = input("Enter the token name (e.g., $PENG): ")
        generator = DisclaimerGenerator(token_name)
        disclaimer = generator.generate_disclaimer()
        formatted_disclaimer = generator.format_disclaimer(disclaimer)
        print("\nGenerated Disclaimer:\n")
        print(formatted_disclaimer)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
