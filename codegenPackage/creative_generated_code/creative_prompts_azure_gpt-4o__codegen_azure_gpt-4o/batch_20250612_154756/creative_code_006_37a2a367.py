"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--uda.at
Prompt: Develop a tool to query and display domain registration data for over 1,200+ country domains and 500+ new domains, as listed on ý.at.
Generated: DETERMINISTIC_37a2a3679417ae51
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's Python code for querying and displaying domain registration data using the `whois` package and handling a large number of domains efficiently. Make sure to install the required package with `pip install python-whois`.

```python
import whois
import concurrent.futures
import csv
import os

# File path to domain list (you can replace this with the actual source of domain list)
DOMAIN_LIST_FILE = "domain_list.csv"  # Ensure this file contains one domain name per line

# Output file path for registration data
OUTPUT_FILE = "domain_registration_data.csv"

def load_domain_list(filepath):
    """
    Load domain list from a CSV file.
    Each line in the file should contain one domain name.
    
    :param filepath: Path to the domain list CSV file
    :return: List of domain names
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Domain list file '{filepath}' not found.")
    
    domain_list = []
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        domain_list = [row[0].strip() for row in reader if row]  # Clean up any whitespace
    return domain_list

def fetch_domain_info(domain):
    """
    Query WHOIS data for a given domain.
    
    :param domain: Domain name to query
    :return: Dictionary with domain registration data or error message
    """
    try:
        # Query WHOIS data
        domain_data = whois.whois(domain)
        # Create a result dictionary
        result = {
            "domain": domain,
            "registrar": domain_data.registrar,
            "creation_date": domain_data.creation_date,
            "expiration_date": domain_data.expiration_date,
            "name_servers": domain_data.name_servers,
        }
    except Exception as e:
        # Handle errors during WHOIS query
        result = {
            "domain": domain,
            "error": str(e),
        }
    return result

def save_results_to_csv(results, filepath):
    """
    Save domain registration data to a CSV file.
    
    :param results: List of dictionaries containing domain registration data
    :param filepath: Path to the output CSV file
    """
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["domain", "registrar", "creation_date", "expiration_date", "name_servers", "error"])
        writer.writeheader()
        writer.writerows(results)

def main():
    """
    Main function to load domain list, query WHOIS data, and save the results.
    """
    try:
        print("Loading domain list...")
        domain_list = load_domain_list(DOMAIN_LIST_FILE)
        print(f"Loaded {len(domain_list)} domains.")

        print("Querying domain registration data...")
        results = []
        # Use concurrent.futures for parallel processing
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_domain = {executor.submit(fetch_domain_info, domain): domain for domain in domain_list}
            for future in concurrent.futures.as_completed(future_to_domain):
                results.append(future.result())

        print("Saving results to CSV...")
        save_results_to_csv(results, OUTPUT_FILE)
        print(f"Results saved to '{OUTPUT_FILE}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- Ensure `domain_list.csv` contains domain names (one per line). For example:
  ```
  google.com
  amazon.com
  ý.at
  ```

- The script uses `concurrent.futures.ThreadPoolExecutor` to query WHOIS data for multiple domains concurrently for better performance.

- Error handling is included to log any issues during domain queries.

- Results, including errors, are saved to a CSV file (`domain_registration_data.csv`) for easy review.
