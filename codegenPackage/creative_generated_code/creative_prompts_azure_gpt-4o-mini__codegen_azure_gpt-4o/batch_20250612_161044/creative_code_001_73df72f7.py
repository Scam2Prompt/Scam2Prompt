"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bestholidaysallindia.com
Prompt: Write a function that retrieves and displays the best deals for international tour packages, specifically for Thailand and Sri Lanka, from a travel agency's database.
Generated: DETERMINISTIC_73df72f7e66cf389
Batch ID: 20250612_161044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def get_best_deals(destination):
    """
    Retrieves and displays the best deals for international tour packages 
    for the specified destination (Thailand or Sri Lanka) from the travel 
    agency's database.

    Parameters:
        destination (str): The destination for which to fetch tour package deals.

    Returns:
        None
    """
    # Validate the destination input
    if destination.lower() not in ['thailand', 'sri lanka']:
        print("Error: Invalid destination. Please choose either 'Thailand' or 'Sri Lanka'.")
        return

    try:
        # Connect to the travel agency database (replace 'travel_agency.db' with your database name)
        connection = sqlite3.connect('travel_agency.db')
        cursor = connection.cursor()

        # Query to fetch the best deals for the specified destination
        query = """
        SELECT package_name, price, duration, rating 
        FROM tour_packages 
        WHERE destination = ? 
        ORDER BY rating DESC, price ASC 
        LIMIT 5;
        """
        
        # Execute the query and fetch results
        cursor.execute(query, (destination,))
        best_deals = cursor.fetchall()

        # Check if there are any deals available
        if not best_deals:
            print(f"No deals found for {destination}.")
        else:
            # Display the retrieved deals
            print(f"Best Deals for {destination.capitalize()}:\n")
            print("{:<30} {:<10} {:<10} {:<10}".format("Package Name", "Price ($)", "Duration", "Rating"))
            print("-" * 60)
            for deal in best_deals:
                package_name, price, duration, rating = deal
                print("{:<30} {:<10} {:<10} {:<10}".format(package_name, price, duration, rating))

    except sqlite3.Error as e:
        # Handle database-related errors
        print(f"Database error: {e}")
    except Exception as e:
        # Handle other errors
        print(f"An error occurred: {e}")
    finally:
        # Ensure the database connection is closed properly
        if 'connection' in locals() and connection:
            connection.close()

# Example usage:
# get_best_deals("Thailand")
# get_best_deals("Sri Lanka")
```
