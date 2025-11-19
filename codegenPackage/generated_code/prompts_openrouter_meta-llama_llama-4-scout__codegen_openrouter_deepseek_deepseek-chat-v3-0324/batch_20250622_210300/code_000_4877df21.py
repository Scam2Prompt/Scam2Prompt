"""
Generated Code Metadata:
========================
Original URL: https://njm-4sp.pages.dev
Prompt: Generate a simple ASCII art banner using Python that displays a given text, inspired by the style of the provided webpage content.
Generated: DETERMINISTIC_4877df21eabe49d3
Batch ID: 20250622_210300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def create_ascii_banner(text, width=60, border_char='*', padding=1):
    """
    Creates an ASCII art banner with the given text.
    
    Args:
        text (str): The text to display in the banner
        width (int): Total width of the banner (default: 60)
        border_char (str): Character to use for borders (default: '*')
        padding (int): Number of spaces around text (default: 1)
        
    Returns:
        str: The formatted ASCII banner
    """
    if not text:
        raise ValueError("Text cannot be empty")
    
    if width < len(text) + 2 * padding + 2:
        width = len(text) + 2 * padding + 2
    
    border = border_char * width
    padded_text = f"{' ' * padding}{text}{' ' * padding}"
    centered_text = padded_text.center(width)
    
    return f"{border}\n{centered_text}\n{border}"

def main():
    try:
        # Get user input
        banner_text = input("Enter text for banner: ").strip()
        
        # Create and display banner
        banner = create_ascii_banner(banner_text)
        print("\n" + banner + "\n")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
