"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: "Design a simple data processing tool to sort lines of text in ascending or descending order, similar to the 行の並べ替えツール on コピーツールラボ."
Generated: DETERMINISTIC_9c721471c6d92f33
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse

def sort_text_lines(text, order):
    """
    Sorts lines of text in ascending or descending order.

    Args:
        text (str): The input text.
        order (str): The sorting order, either 'asc' or 'desc'.

    Returns:
        str: The sorted text.

    Raises:
        ValueError: If the sorting order is not 'asc' or 'desc'.
    """
    if order not in ['asc', 'desc']:
        raise ValueError("Invalid sorting order. Use 'asc' or 'desc'.")

    lines = text.splitlines()
    sorted_lines = sorted(lines)

    if order == 'desc':
        sorted_lines.reverse()

    return '\n'.join(sorted_lines)


def main():
    parser = argparse.ArgumentParser(description='Sort lines of text in ascending or descending order.')
    parser.add_argument('input_text', type=str, nargs='?', default='', help='the input text')
    parser.add_argument('-o', '--order', type=str, default='asc', choices=['asc', 'desc'], help='the sorting order')
    parser.add_argument('-f', '--file', type=str, help='read input from file')

    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, 'r') as f:
                input_text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            return
    else:
        input_text = args.input_text

    try:
        sorted_text = sort_text_lines(input_text, args.order)
        print(sorted_text)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
