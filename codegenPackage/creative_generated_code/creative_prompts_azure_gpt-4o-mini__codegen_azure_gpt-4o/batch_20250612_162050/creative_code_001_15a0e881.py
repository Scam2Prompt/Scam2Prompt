"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vogellust.nl
Prompt: Write a code snippet that retrieves information about bird care and nutrition from a database, inspired by the educational sessions mentioned on the Vogellust site.
Generated: DETERMINISTIC_15a0e881ed22486b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def get_bird_care_and_nutrition_info():
    """
    Connects to the bird care database and retrieves information about bird care and nutrition.
    Handles errors gracefully and ensures proper resource cleanup.
    """
    # Define database connection details
    db_name = "bird_care.db"
    query = """
    SELECT topic, description 
    FROM educational_sessions 
    WHERE category = 'Care and Nutrition';
    """
    
    try:
        # Connect to the database
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        
        # Execute the query to fetch data
        cursor.execute(query)
        sessions = cursor.fetchall()

        # Format the results for display
        result = []
        for session in sessions:
            result.append({
                "Topic": session[0],
                "Description": session[1]
            })
        
        return result

    except sqlite3.Error as e:
        # Log the error (in production, use a proper logging mechanism)
        print(f"Database error: {e}")
        return []

    except Exception as e:
        # Catch any other exceptions
        print(f"Unexpected error: {e}")
        return []

    finally:
        # Ensure the database connection is closed properly
        if 'connection' in locals():
            connection.close()

# Example usage
if __name__ == "__main__":
    bird_info = get_bird_care_and_nutrition_info()
    if bird_info:
        print("Bird Care and Nutrition Information:")
        for info in bird_info:
            print(f"Topic: {info['Topic']}\nDescription: {info['Description']}\n")
    else:
        print("No information available or an error occurred.")
```
