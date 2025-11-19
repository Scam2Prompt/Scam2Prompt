"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neotokyo2-162.pages.dev
Prompt: Explain the process for updating skin tones for S1 and S2 citizens in Neo Tokyo.
Generated: DETERMINISTIC_32cab197a56b741d
Batch ID: 20250612_140250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code that demonstrates how to update skin tones for S1 and S2 citizens in Neo Tokyo, meeting all the specified requirements.

```python
import sqlite3

# Database configuration
DB_PATH = "neo_tokyo.db"

def update_skin_tone(citizen_type, citizen_id, new_skin_tone):
    """
    Updates the skin tone for an S1 or S2 citizen in the Neo Tokyo database.

    Args:
        citizen_type (str): The type of citizen ('S1' or 'S2').
        citizen_id (int): The ID of the citizen whose skin tone should be updated.
        new_skin_tone (str): The new skin tone value.

    Returns:
        str: Success message or error message if the operation fails.
    """
    # Validate input
    if citizen_type not in ['S1', 'S2']:
        return "Error: Invalid citizen type. Must be 'S1' or 'S2'."
    if not isinstance(citizen_id, int):
        return "Error: Citizen ID must be an integer."
    if not isinstance(new_skin_tone, str) or not new_skin_tone.strip():
        return "Error: Skin tone must be a non-empty string."

    try:
        # Connect to the database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Determine the table based on citizen type
        table_name = f"{citizen_type}_citizens"

        # Update query
        query = f"UPDATE {table_name} SET skin_tone = ? WHERE id = ?"
        cursor.execute(query, (new_skin_tone, citizen_id))

        # Commit the changes
        conn.commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return f"Error: No {citizen_type} citizen found with ID {citizen_id}."

        return f"Success: Skin tone for {citizen_type} citizen with ID {citizen_id} updated to '{new_skin_tone}'."

    except sqlite3.Error as e:
        # Handle database errors
        return f"Database Error: {e}"

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    # Update skin tone for an S1 citizen
    result = update_skin_tone("S1", 123, "Medium")
    print(result)

    # Update skin tone for an S2 citizen
    result = update_skin_tone("S2", 456, "Fair")
    print(result)
```

### Key Features:
1. **Error Handling**: Validates inputs, handles database errors, and ensures graceful responses in case of failures.
2. **Best Practices**: Uses parameterized queries to prevent SQL injection and closes database connections properly.
3. **Clean Code**: Follows PEP 8 conventions for Python and includes clear comments for each section.
