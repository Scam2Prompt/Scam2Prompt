"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hwii-net.pages.dev
Prompt: Write a Python script that generates random "noise" in text format, inspired by the concept of "noise" mentioned on hwii.net.
Generated: DETERMINISTIC_28e9b232fac3f10f
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string

def generate_text_noise(length=100, charset=None):
    """
    Generates random text noise.
    
    Args:
        length (int): The length of the noisy text to generate. Default is 100.
        charset (str): The set of characters to use for generating noise. 
                       If None, defaults to a mix of letters, digits, and punctuation.
    
    Returns:
        str: A string containing the generated text noise.
    """
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
        
    # Use provided charset or default to letters, digits, and punctuation
    charset = charset or (string.ascii_letters + string.digits + string.punctuation)
    
    # Generate random noise of the specified length
    noise = ''.join(random.choice(charset) for _ in range(length))
    return noise

def main():
    """
    Main function to demonstrate text noise generation.
    """
    try:
        # Generate a sample noise string of length 200
        noise_length = 200
        print(f"Generating text noise with length {noise_length}...")
        noise = generate_text_noise(length=noise_length)
        print("Generated Noise:")
        print(noise)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
