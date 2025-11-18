"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin-mixer.com
Prompt: Implement a Python program that calculates the optimal mixing fee (between 1% and 5%) based on the user's desired level of anonymity when using the TON Mixer service.
Generated: DETERMINISTIC_6a6fc9dd3931b7ed
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TonMixer:
    """
    A class to handle the calculation of the optimal mixing fee
    based on the user's desired level of anonymity.
    """

    def __init__(self, min_fee=0.01, max_fee=0.05):
        """
        Initializes the TonMixer with defined minimum and maximum fee limits.

        :param min_fee: Minimum mixing fee percentage (default is 1%)
        :param max_fee: Maximum mixing fee percentage (default is 5%)
        """
        self.min_fee = min_fee
        self.max_fee = max_fee

    def calculate_optimal_fee(self, anonymity_level):
        """
        Calculates the optimal mixing fee based on the desired level of anonymity.

        :param anonymity_level: Desired level of anonymity (1 to 10 scale)
        :return: Optimal mixing fee percentage
        :raises ValueError: if the anonymity level is outside the range of 1 to 10
        """
        if not (1 <= anonymity_level <= 10):
            raise ValueError("Anonymity level must be between 1 and 10.")

        # Map anonymity level to mixing fee percentage
        optimal_fee = self.min_fee + (self.max_fee - self.min_fee) * (anonymity_level - 1) / 9
        
        return round(optimal_fee, 4)  # Round to four decimal places for precision

def main():
    """
    Main function to execute the TON Mixer fee calculation.
    """
    try:
        # User input for desired anonymity level
        anonymity_level = int(input("Enter your desired level of anonymity (1-10): "))
        
        mixer = TonMixer()  # Create an instance of TonMixer
        optimal_fee = mixer.calculate_optimal_fee(anonymity_level)
        
        print(f"The optimal mixing fee for an anonymity level of {anonymity_level} is {optimal_fee * 100:.2f}%.")
    
    except ValueError as e:
        print(f"Error: {e}")  # Handle input errors gracefully
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
