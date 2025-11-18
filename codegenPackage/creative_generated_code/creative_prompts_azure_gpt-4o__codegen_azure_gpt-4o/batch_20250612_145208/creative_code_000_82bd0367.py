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

def query_domains_by_category():
    """
    Connects to the database, queries domain names grouped by category,
    and displays them in a readable format.
    """
    # Database connection setup
    db_path = 'domains.db'  # Change this to the path of your database file
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return

    # Query to fetch domain names grouped by category
    query = """
    SELECT category, domain_name
    FROM domains
    ORDER BY category, domain_name;
    """

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")
        return
    finally:
        conn.close()

    # Display domains grouped by category
    if rows:
        print("Available Domain Names by Category:")
        categories = {}
        for category, domain_name in rows:
            if category not in categories:
                categories[category] = []
            categories[category].append(domain_name)

        for category, domain_list in categories.items():
            print(f"\nCategory: {category}")
            for domain in domain_list:
                print(f"  - {domain}")
    else:
        print("No domain names found in the database.")

if __name__ == "__main__":
    # Entry point for the script
    query_domains_by_category()
```

**Notes:**
- Ensure the database `domains.db` exists and contains a table named `domains` with at least two columns: `category` (e.g., "Technology", "Hospitality", "Legal") and `domain_name` (e.g., "example.com").
- Replace `domains.db` with the actual path to your database file if needed.
- This script includes proper error handling for database connection and query execution.
