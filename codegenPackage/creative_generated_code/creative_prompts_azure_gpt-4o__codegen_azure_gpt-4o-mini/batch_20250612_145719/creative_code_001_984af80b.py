"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netsecurity.pages.dev
Prompt: Generate a script to extract and log the `tlsClientRandom` value and `tlsVersion` from a network security report, referencing the format used by netsecurity.pages.dev.
Generated: DETERMINISTIC_984af80b3d5f2ac8
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging to output to a file and the console
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("network_security_report.log"),
                        logging.StreamHandler()
                    ])

def extract_tls_info(report_file):
    """
    Extracts the 'tlsClientRandom' and 'tlsVersion' values from a network security report.

    Parameters:
    report_file (str): The path to the JSON report file.

    Returns:
    dict: A dictionary containing 'tlsClientRandom' and 'tlsVersion'.
    """
    try:
        # Load the JSON report
        with open(report_file, 'r') as file:
            report_data = json.load(file)
        
        # Extract the required values
        tls_client_random = report_data.get('tlsClientRandom')
        tls_version = report_data.get('tlsVersion')

        if tls_client_random is None or tls_version is None:
            raise ValueError("Missing 'tlsClientRandom' or 'tlsVersion' fields in the report.")

        # Log the extracted values
        logging.info(f"Extracted tlsClientRandom: {tls_client_random}")
        logging.info(f"Extracted tlsVersion: {tls_version}")

        # Return the extracted values
        return {
            'tlsClientRandom': tls_client_random,
            'tlsVersion': tls_version
        }
    
    except FileNotFoundError:
        logging.error(f"File not found: {report_file}")
        raise
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the report file.")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    report_file_path = "path/to/network_security_report.json"  # Update with the actual path
    try:
        tls_info = extract_tls_info(report_file_path)
        print(tls_info)  # Print the extracted information
    except Exception as e:
        print(f"Failed to extract TLS information: {str(e)}")
```
