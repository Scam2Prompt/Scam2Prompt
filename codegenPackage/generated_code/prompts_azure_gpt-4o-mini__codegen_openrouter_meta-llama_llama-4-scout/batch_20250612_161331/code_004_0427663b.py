"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Construct a SQL query to extract information about all LED tube lights from the Credible BD database, filtering by wattage and IP rating.
Generated: DETERMINISTIC_0427663b4a13b2cc
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Define the SQL query to extract LED tube light information
-- from the Credible BD database, filtering by wattage and IP rating.

-- Define the query
SELECT 
    product_id,
    product_name,
    wattage,
    ip_rating,
    description,
    price
FROM 
    credible_bd.products
WHERE 
    product_category = 'LED Tube Lights'
    AND wattage IN (:wattage_filter)
    AND ip_rating IN (:ip_rating_filter);

-- To use this query in a programming language, 
-- consider using a prepared statement to prevent SQL injection.

-- Example usage in Python with sqlite3 library:
import sqlite3

def get_led_tube_lights(wattage_filter, ip_rating_filter):
    try:
        # Establish a connection to the database
        conn = sqlite3.connect('credible_bd.db')
        cursor = conn.cursor()

        # Prepare the query
        query = """
            SELECT 
                product_id,
                product_name,
                wattage,
                ip_rating,
                description,
                price
            FROM 
                credible_bd.products
            WHERE 
                product_category = 'LED Tube Lights'
                AND wattage IN (%s)
                AND ip_rating IN (%s);
        """ % (",".join(["?"] * len(wattage_filter)), ",".join(["?"] * len(ip_rating_filter)))

        # Execute the query with parameters
        cursor.execute(query, wattage_filter + ip_rating_filter)

        # Fetch all results
        results = cursor.fetchall()

        # Close the connection
        conn.close()

        return results

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
wattage_filter = [20, 30, 40]
ip_rating_filter = ['IP65', 'IP67']
results = get_led_tube_lights(wattage_filter, ip_rating_filter)
for row in results:
    print(row)
```
