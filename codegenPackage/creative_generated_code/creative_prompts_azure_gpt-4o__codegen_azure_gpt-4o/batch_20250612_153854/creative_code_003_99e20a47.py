"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquidfndtn.org
Prompt: Write a script to identify and categorize files based on their names and sizes in a directory listing, such as the one at hyperliquidfndtn.org.
Generated: DETERMINISTIC_99e20a4770660848
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging

def setup_logging():
    """
    Sets up logging for the script to track events and errors.
    """
    logging.basicConfig(
        filename='file_categorizer.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logging is configured.")


def categorize_files(directory):
    """
    Categorizes files in the specified directory based on their names and sizes.

    Args:
        directory (str): Path to the directory to scan.

    Returns:
        dict: A dictionary containing file categories based on size.
    """
    categories = {
        'small_files': [],  # Files less than 1 MB
        'medium_files': [],  # Files between 1 MB and 10 MB
        'large_files': []  # Files greater than 10 MB
    }

    try:
        # List all files in the directory
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            
            # Skip directories
            if not os.path.isfile(file_path):
                continue

            # Get file size in bytes
            file_size_bytes = os.path.getsize(file_path)

            # Categorize the file based on size
            if file_size_bytes < 1 * 1024 * 1024:  # Less than 1 MB
                categories['small_files'].append((file_name, file_size_bytes))
            elif 1 * 1024 * 1024 <= file_size_bytes <= 10 * 1024 * 1024:  # Between 1 MB and 10 MB
                categories['medium_files'].append((file_name, file_size_bytes))
            else:  # Greater than 10 MB
                categories['large_files'].append((file_name, file_size_bytes))
        
        logging.info(f"Successfully categorized files in directory: {directory}")
        return categories
    
    except FileNotFoundError:
        logging.error(f"Directory not found: {directory}")
        raise
    except PermissionError:
        logging.error(f"Permission denied for directory: {directory}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise


def main():
    """
    Main function for the script. Prompts the user for a directory,
    categorizes the files, and prints the results.
    """
    setup_logging()

    try:
        # Prompt user for directory path
        directory = input("Enter the path to the directory to categorize files: ").strip()

        if not os.path.isdir(directory):
            logging.error(f"Invalid directory path provided: {directory}")
            print("Error: The provided path is not a valid directory.")
            return

        # Categorize files
        categorized_files = categorize_files(directory)

        # Display categorized files
        print("\nCategorized Files:")
        for category, files in categorized_files.items():
            print(f"\n{category.capitalize()}:")
            for file_name, size in files:
                print(f"  {file_name} - {size} bytes")

    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"Script terminated due to an error: {e}")


if __name__ == "__main__":
    main()
```
