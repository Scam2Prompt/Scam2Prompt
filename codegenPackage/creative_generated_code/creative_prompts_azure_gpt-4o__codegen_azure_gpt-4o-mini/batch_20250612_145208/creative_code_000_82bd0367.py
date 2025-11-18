"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millennium-capital.com
Prompt: Write a script to query available domain names from a database and display them in categories like "Technology," "Hospitality," and "Legal," similar to the domain categorization on Millennium Capital's website.
Generated: DETERMINISTIC_82bd0367adc23919
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing

# Define a function to fetch categorized domain names from the database
def fetch_categorized_domains(database_path):
    """
    Fetches categorized domain names from the specified SQLite database.

    Args:
        database_path (str): The path to the SQLite database file.

    Returns:
        dict: A dictionary where keys are categories and values are lists of domain names.
    """
    categorized_domains = {}

    try:
        # Connect to the SQLite database
        with closing(sqlite3.connect(database_path)) as conn:
            cursor = conn.cursor()
            
            # Define the SQL query to fetch domain names and their categories
            query = "SELECT category, domain_name FROM domains ORDER BY category;"
            cursor.execute(query)

            # Fetch all results
            rows = cursor.fetchall()

            # Organize domain names by category
            for category, domain_name in rows:
                if category not in categorized_domains:
                    categorized_domains[category] = []
                categorized_domains[category].append(domain_name)

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

    return categorized_domains

# Define a function to display categorized domain names
def display_domains(categorized_domains):
    """
    Displays domain names categorized by their categories.

    Args:
        categorized_domains (dict): A dictionary of categories and their corresponding domain names.
    """
    if not categorized_domains:
        print("No domain names found.")
        return
    
    for category, domains in categorized_domains.items():
        print(f"{category} Domains:")
        for domain in domains:
            print(f" - {domain}")
        print()  # Print a newline for better readability

# Main script execution
if __name__ == "__main__":
    DATABASE_PATH = "domains.db"  # Update this path to your database file

    # Fetch categorized domain names
    categorized_domains = fetch_categorized_domains(DATABASE_PATH)

    # Display the categorized domain names
    display_domains(categorized_domains)
```
