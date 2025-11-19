"""
Generated Code Metadata:
========================
Original URL: https://marian-314.pages.dev
Prompt: Generate ASCII art of a cat using Python.
Generated: DETERMINISTIC_a4f1c2f7d0b4b664
Batch ID: 20250622_210108
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ASCII Art Generator for a Cat
# This script generates and prints ASCII art of a cat.

def generate_cat_ascii_art():
    """
    Generates ASCII art of a cat and returns it as a string.
    """
    cat_art = r"""
        /\     /\
       {  `---'  }
       {  O   O  }
       ~~>  V  <~~
        \ \|/ /
         `-----'____
         /     \    \_
        {       }\  )_\_   _
        |  \_/  |/ /  \_\_/ )
         \__/  /(_/     \__/
           (__/
    """
    return cat_art


def main():
    """
    Main function to execute the ASCII art generation.
    """
    try:
        # Generate the cat ASCII art
        cat_art = generate_cat_ascii_art()
        
        # Print the ASCII art
        print(cat_art)
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
