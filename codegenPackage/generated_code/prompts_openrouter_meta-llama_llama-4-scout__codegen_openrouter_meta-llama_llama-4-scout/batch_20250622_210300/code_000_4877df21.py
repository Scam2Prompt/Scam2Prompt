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
#!/usr/bin/env python3
"""
Simple ASCII art banner generator.

Displays a given text in a stylized ASCII art banner.
"""

import sys

def banner(text, font='standard'):
    """
    Generate ASCII art banner.

    Args:
        text (str): Text to display in the banner.
        font (str): Font style to use. Defaults to 'standard'.

    Returns:
        str: ASCII art banner as a string.

    Raises:
        ValueError: If the font style is not supported.
    """
    # Supported font styles
    fonts = {
        'standard': {
            'A': [' *** ', '*   *', '*****', '*   *', '*   *'],
            'B': ['**** ', '*   *', '**** ', '*   *', '**** '],
            'C': ['*****', '*    ', '*    ', '*    ', '*****'],
            'D': ['**** ', '*   *', '*   *', '*   *', '**** '],
            'E': ['*****', '*    ', '*****', '*    ', '*****'],
            'F': ['*****', '*    ', '*****', '*    ', '*    '],
            'G': ['*****', '*    ', '* ***', '*   *', '*****'],
            'H': ['*   *', '*   *', '*****', '*   *', '*   *'],
            'I': ['*****', '  *  ', '  *  ', '  *  ', '*****'],
            'J': ['    *', '    *', '*   *', '*   *', ' *** '],
            'K': ['*   *', '* *  ', '**   ', '* *  ', '*   *'],
            'L': ['*    ', '*    ', '*    ', '*    ', '*****'],
            'M': ['*   *', '** **', '* * *', '*   *', '*   *'],
            'N': ['*   *', '**  *', '* * *', '*  **', '*   *'],
            'O': [' *** ', '*   *', '*   *', '*   *', ' *** '],
            'P': ['**** ', '*   *', '**** ', '*    ', '*    '],
            'Q': [' *** ', '*   *', '*   *', '*  **', ' ** *'],
            'R': ['**** ', '*   *', '**** ', '* *  ', '*  * '],
            'S': [' *** ', '*    ', ' *** ', '    *', '***  '],
            'T': ['*****', '  *  ', '  *  ', '  *  ', '  *  '],
            'U': ['*   *', '*   *', '*   *', '*   *', ' *** '],
            'V': ['*   *', '*   *', ' * * ', '  *  ', '  *  '],
            'W': ['*   *', '*   *', '* * *', '** **', '*   *'],
            'X': ['*   *', ' * * ', '  *  ', ' * * ', '*   *'],
            'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
            'Z': ['*****', '   * ', '  *  ', ' *   ', '*****'],
            ' ': ['     ', '     ', '     ', '     ', '     '],
        }
    }

    if font not in fonts:
        raise ValueError(f"Unsupported font style: {font}")

    lines = [''] * 5
    for char in text.upper():
        if char in fonts[font]:
            for i in range(5):
                lines[i] += fonts[font][char][i] + ' '

    return '\n'.join(lines)


def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python ascii_banner.py <text>")
            sys.exit(1)

        text = sys.argv[1]
        print(banner(text))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
