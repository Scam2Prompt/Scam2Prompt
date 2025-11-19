"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: "Write a Python script to format JSON data in a readable format, similar to the JSON 整形ツール on コピーツールラボ."
Generated: DETERMINISTIC_e377e86e90b36116
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
<<<<<<< HEAD

def format_json(input_json: str) -> str:
    """
    Formats a JSON string into a readable, pretty-printed format.

    Args:
        input_json (str): The raw JSON string to be formatted.

    Returns:
        str: The formatted JSON string.
    """
    try:
        # Parse the input JSON string into a Python dictionary
        parsed_json = json.loads(input_json)
        
        # Convert the dictionary back to a pretty-printed JSON string
        formatted_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)
        return formatted_json
    except json.JSONDecodeError as e:
        # Handle invalid JSON input
        return f"Error: Invalid JSON data. Details: {e}"

def main():
    """
    Main function to demonstrate JSON formatting.
    """
    # Example JSON string (can be replaced with user input or file data)
    raw_json = '{"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", "traveling"]}'
    
    print("Original JSON:")
    print(raw_json)
    
    print("\nFormatted JSON:")
    formatted_json = format_json(raw_json)
    print(formatted_json)

if __name__ == "__main__":
    # Entry point of the script
    main()
=======
import sys

def format_json(input_file, output_file=None):
    """
    Formats JSON data from an input file and writes it to an output file or prints it to the console.

    Args:
        input_file (str): Path to the input JSON file.
        output_file (str, optional): Path to the output file. If None, prints to the console.

    Raises:
        FileNotFoundError: If the input file does not exist.
        json.JSONDecodeError: If the input file contains invalid JSON.
    """
    try:
        # Read JSON data from the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Format the JSON data with indentation for readability
        formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
        
        if output_file:
            # Write the formatted JSON to the output file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(formatted_json)
            print(f"Formatted JSON has been written to '{output_file}'.")
        else:
            # Print the formatted JSON to the console
            print(formatted_json)
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Check if the script is run with the correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python format_json.py <input_file> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Call the function to format JSON
    format_json(input_file, output_file)
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
```
