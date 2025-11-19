"""
Generated Code Metadata:
========================
Original URL: https://spiketheoriginal.pages.dev
Prompt: Write a function that compares the value of original crypto art pieces like $SPIKE with derivative works, highlighting the importance of originality in the NFT space.
Generated: DETERMINISTIC_c0045b436a7c175e
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_comparator.py

class NFT:
    """Represents a Non-Fungible Token (NFT) with a name and a value."""
    
    def __init__(self, name: str, value: float):
        """
        Initializes an NFT object.

        Args:
        - name (str): The name of the NFT.
        - value (float): The value of the NFT.
        """
        self.name = name
        self.value = value


def compare_nft_values(original_nft: NFT, derivative_nft: NFT) -> dict:
    """
    Compares the value of an original NFT with a derivative NFT.

    Args:
    - original_nft (NFT): The original NFT.
    - derivative_nft (NFT): The derivative NFT.

    Returns:
    - dict: A dictionary containing the comparison result.

    Raises:
    - ValueError: If the value of either NFT is non-positive.
    """
    if original_nft.value <= 0 or derivative_nft.value <= 0:
        raise ValueError("NFT values must be positive.")

    # Calculate the percentage difference between the two NFT values
    percentage_diff = ((derivative_nft.value - original_nft.value) / original_nft.value) * 100

    # Determine if the derivative NFT value is higher or lower than the original NFT value
    if percentage_diff > 0:
        comparison_result = f"The derivative NFT ($derivative_nft) is {percentage_diff:.2f}% more valuable than the original NFT ($original_nft)."
    elif percentage_diff < 0:
        comparison_result = f"The derivative NFT ($derivative_nft) is {abs(percentage_diff):.2f}% less valuable than the original NFT ($original_nft)."
    else:
        comparison_result = f"The derivative NFT ($derivative_nft) has the same value as the original NFT ($original_nft)."

    return {
        "original_nft": original_nft.name,
        "derivative_nft": derivative_nft.name,
        "original_value": original_nft.value,
        "derivative_value": derivative_nft.value,
        "comparison_result": comparison_result,
    }


def main():
    try:
        # Create NFT objects
        original_nft = NFT("$SPIKE", 1000.0)
        derivative_nft = NFT("$SPIKE_Derivative", 800.0)

        # Compare NFT values
        comparison_result = compare_nft_values(original_nft, derivative_nft)

        # Print the comparison result
        print("NFT Comparison Result:")
        print(f"Original NFT: {comparison_result['original_nft']}")
        print(f"Derivative NFT: {comparison_result['derivative_nft']}")
        print(f"Original Value: ${comparison_result['original_value']:.2f}")
        print(f"Derivative Value: ${comparison_result['derivative_value']:.2f}")
        print(comparison_result["comparison_result"])

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
