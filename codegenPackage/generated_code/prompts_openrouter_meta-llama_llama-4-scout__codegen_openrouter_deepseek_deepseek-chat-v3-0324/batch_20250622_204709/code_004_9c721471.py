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
#!/usr/bin/env python3
import sys
import argparse

def sort_lines(input_text, reverse=False):
    """
    Sorts lines of text in ascending or descending order.
    
    Args:
        input_text (str): The text to be sorted, with lines separated by newlines.
        reverse (bool): If True, sorts in descending order. Default is False (ascending).
    
    Returns:
        str: The sorted text with lines separated by newlines.
    """
    lines = input_text.split('\n')
    lines.sort(reverse=reverse)
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(
        description='Sort lines of text in ascending or descending order.'
    )
    parser.add_argument(
        '-r', '--reverse',
        action='store_true',
        help='sort in descending order (default: ascending)'
    )
    parser.add_argument(
        'input_file',
        nargs='?',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help='input file (default: stdin)'
    )
    parser.add_argument(
        'output_file',
        nargs='?',
        type=argparse.FileType('w'),
        default=sys.stdout,
        help='output file (default: stdout)'
    )
    
    args = parser.parse_args()
    
    try:
        input_text = args.input_file.read()
        sorted_text = sort_lines(input_text, args.reverse)
        args.output_file.write(sorted_text)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        args.input_file.close()
        args.output_file.close()

if __name__ == '__main__':
    main()
```
