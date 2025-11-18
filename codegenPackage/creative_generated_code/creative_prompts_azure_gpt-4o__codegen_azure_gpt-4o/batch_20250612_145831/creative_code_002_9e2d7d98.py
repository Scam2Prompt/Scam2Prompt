"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Create a migration script in Python for converting tokens (e.g., SDAO to SFI at a 1:1 ratio and CGV to SFI at a 1:0.14122 ratio) based on Singularity Finance's token conversion framework.
Generated: DETERMINISTIC_9e2d7d98d3b545b6
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import sys
from decimal import Decimal, InvalidOperation

# Conversion rates
TOKEN_CONVERSION_RATES = {
    "SDAO": Decimal("1.0"),       # 1 SDAO = 1 SFI
    "CGV": Decimal("0.14122"),   # 1 CGV = 0.14122 SFI
}

# Input and output file paths
INPUT_FILE = "tokens.csv"  # CSV file containing user tokens (columns: user_id, token_type, amount)
OUTPUT_FILE = "converted_tokens.csv"  # CSV file containing converted tokens

def validate_decimal(value):
    """Validate and convert a value to Decimal."""
    try:
        return Decimal(value)
    except InvalidOperation:
        raise ValueError(f"Invalid numeric value: {value}")

def validate_and_convert_tokens(token_type, amount):
    """
    Validate token type and perform conversion based on the TOKEN_CONVERSION_RATES.
    :param token_type: The type of the token (e.g., SDAO, CGV).
    :param amount: The amount of the token to convert.
    :return: The equivalent amount in SFI.
    """
    if token_type not in TOKEN_CONVERSION_RATES:
        raise ValueError(f"Unsupported token type: {token_type}")

    conversion_rate = TOKEN_CONVERSION_RATES[token_type]
    return amount * conversion_rate

def process_token_conversion(input_file, output_file):
    """
    Process the token conversion from the input CSV file and write results to the output CSV file.
    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file.
    """
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            
            # Setup CSV reader and writer
            reader = csv.DictReader(infile)
            fieldnames = ['user_id', 'token_type', 'original_amount', 'converted_amount']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            # Write header to output file
            writer.writeheader()

            for row in reader:
                try:
                    # Extract and validate input data
                    user_id = row['user_id']
                    token_type = row['token_type']
                    original_amount = validate_decimal(row['amount'])

                    # Perform token conversion
                    converted_amount = validate_and_convert_tokens(token_type, original_amount)

                    # Write output row
                    writer.writerow({
                        'user_id': user_id,
                        'token_type': token_type,
                        'original_amount': str(original_amount),
                        'converted_amount': str(converted_amount)
                    })

                except (KeyError, ValueError) as e:
                    print(f"Skipping row due to error: {e}", file=sys.stderr)

    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure the input file exists and the path is correct.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Run the token conversion process
    process_token_conversion(INPUT_FILE, OUTPUT_FILE)
```
