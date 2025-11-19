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
<<<<<<< HEAD
# Import necessary modules
import argparse
import sys

def sort_lines(input_lines, order='asc'):
    """
    Sorts a list of lines in ascending or descending order.

    Args:
        input_lines (list of str): The lines to be sorted.
        order (str): The sorting order, either 'asc' for ascending or 'desc' for descending.

    Returns:
        list of str: The sorted lines.
    """
    reverse = True if order == 'desc' else False
    return sorted(input_lines, reverse=reverse)

def main():
    """
    Main function to handle command-line arguments and process the input.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Sort lines of text in ascending or descending order.")
    parser.add_argument(
        '-o', '--order', 
        choices=['asc', 'desc'], 
        default='asc', 
        help="Sorting order: 'asc' for ascending (default), 'desc' for descending."
    )
    parser.add_argument(
        'file', 
        nargs='?', 
        type=argparse.FileType('r'), 
        default=sys.stdin, 
        help="Input file to process. If not provided, reads from standard input."
    )

    # Parse arguments
    args = parser.parse_args()

    try:
        # Read lines from the input file or stdin
        input_lines = args.file.read().splitlines()
        
        # Sort the lines based on the specified order
        sorted_lines = sort_lines(input_lines, args.order)
        
        # Output the sorted lines
        for line in sorted_lines:
            print(line)
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
=======
import argparse

def sort_lines(input_file, output_file, order):
    """
    Sorts lines of text from an input file and writes the sorted lines to an output file.

    Args:
        input_file (str): Path to the input file containing lines of text.
        output_file (str): Path to the output file where sorted lines will be written.
        order (str): Sorting order, either 'asc' for ascending or 'desc' for descending.
    """
    try:
        # Read lines from the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Strip newline characters and sort lines
        lines = [line.strip() for line in lines]
        if order == 'asc':
            sorted_lines = sorted(lines)
        elif order == 'desc':
            sorted_lines = sorted(lines, reverse=True)
        else:
            raise ValueError("Invalid sorting order. Use 'asc' for ascending or 'desc' for descending.")

        # Write sorted lines to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            for line in sorted_lines:
                file.write(line + '\n')

        print(f"Lines sorted successfully in {order} order and written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to parse command-line arguments and execute the sorting tool.
    """
    parser = argparse.ArgumentParser(description="Sort lines of text in ascending or descending order.")
    parser.add_argument('input_file', type=str, help="Path to the input file containing lines of text.")
    parser.add_argument('output_file', type=str, help="Path to the output file where sorted lines will be written.")
    parser.add_argument('order', type=str, choices=['asc', 'desc'], help="Sorting order: 'asc' for ascending, 'desc' for descending.")
    
    args = parser.parse_args()
    
    sort_lines(args.input_file, args.output_file, args.order)

if __name__ == "__main__":
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    main()
```
