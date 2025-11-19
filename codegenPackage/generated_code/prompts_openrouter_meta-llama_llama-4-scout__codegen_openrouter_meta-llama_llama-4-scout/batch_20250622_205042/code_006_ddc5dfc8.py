"""
Generated Code Metadata:
========================
Original URL: https://bitmixr.biz
Prompt: Write a SQL query to retrieve game data with specific filters, such as game type, provider, and jackpot amount.
Generated: DETERMINISTIC_ddc5dfc88f606d58
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve game data with specific filters

-- Define the query
SELECT 
    g.game_id,
    g.game_name,
    g.game_type,
    p.provider_name,
    g.jackpot_amount,
    g.is_active
FROM 
    games g
INNER JOIN 
    providers p ON g.provider_id = p.provider_id
WHERE 
    -- Filter by game type
    g.game_type = COALESCE(:game_type, g.game_type)
    -- Filter by provider
    AND p.provider_name = COALESCE(:provider, p.provider_name)
    -- Filter by jackpot amount range
    AND g.jackpot_amount >= COALESCE(:min_jackpot, 0)
    AND g.jackpot_amount <= COALESCE(:max_jackpot, g.jackpot_amount)
    -- Filter by active games only
    AND g.is_active = TRUE;

-- Example usage with sample parameters
-- Replace the parameter values as needed
DECLARE 
    :game_type VARCHAR(50) := 'slot';
    :provider VARCHAR(100) := 'Provider A';
    :min_jackpot DECIMAL(10, 2) := 1000.00;
    :max_jackpot DECIMAL(10, 2) := 10000.00;

-- Execute the query with the sample parameters
SELECT 
    g.game_id,
    g.game_name,
    g.game_type,
    p.provider_name,
    g.jackpot_amount,
    g.is_active
FROM 
    games g
INNER JOIN 
    providers p ON g.provider_id = p.provider_id
WHERE 
    g.game_type = COALESCE(:game_type, g.game_type)
    AND p.provider_name = COALESCE(:provider, p.provider_name)
    AND g.jackpot_amount >= COALESCE(:min_jackpot, 0)
    AND g.jackpot_amount <= COALESCE(:max_jackpot, g.jackpot_amount)
    AND g.is_active = TRUE;
```

**Stored Procedure Version**

```sql
-- Create a stored procedure to retrieve game data with specific filters
CREATE OR REPLACE PROCEDURE sp_get_game_data(
    p_game_type VARCHAR(50),
    p_provider VARCHAR(100),
    p_min_jackpot DECIMAL(10, 2),
    p_max_jackpot DECIMAL(10, 2)
)
AS
BEGIN
    SELECT 
        g.game_id,
        g.game_name,
        g.game_type,
        p.provider_name,
        g.jackpot_amount,
        g.is_active
    FROM 
        games g
    INNER JOIN 
        providers p ON g.provider_id = p.provider_id
    WHERE 
        g.game_type = COALESCE(p_game_type, g.game_type)
        AND p.provider_name = COALESCE(p_provider, p.provider_name)
        AND g.jackpot_amount >= COALESCE(p_min_jackpot, 0)
        AND g.jackpot_amount <= COALESCE(p_max_jackpot, g.jackpot_amount)
        AND g.is_active = TRUE;
END;

-- Example usage with sample parameters
-- Replace the parameter values as needed
CALL sp_get_game_data('slot', 'Provider A', 1000.00, 10000.00);
```

**API/Function Version (using a programming language)**
```python
import psycopg2
from psycopg2 import Error

def get_game_data(game_type=None, provider=None, min_jackpot=0, max_jackpot=None):
    try:
        # Establish a database connection
        connection = psycopg2.connect(
            dbname="your_database",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )

        # Create a cursor object
        cursor = connection.cursor()

        # SQL query string
        query = """
            SELECT 
                g.game_id,
                g.game_name,
                g.game_type,
                p.provider_name,
                g.jackpot_amount,
                g.is_active
            FROM 
                games g
            INNER JOIN 
                providers p ON g.provider_id = p.provider_id
            WHERE 
                g.game_type = COALESCE(%s, g.game_type)
                AND p.provider_name = COALESCE(%s, p.provider_name)
                AND g.jackpot_amount >= COALESCE(%s, 0)
                AND g.jackpot_amount <= COALESCE(%s, g.jackpot_amount)
                AND g.is_active = TRUE;
        """

        # Execute the query with the provided parameters
        cursor.execute(query, (game_type, provider, min_jackpot, max_jackpot))

        # Fetch all rows from the query result
        rows = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return rows

    except (Exception, Error) as error:
        print("Error while fetching game data:", error)
        return []

# Example usage with sample parameters
game_data = get_game_data('slot', 'Provider A', 1000.00, 10000.00)
print(game_data)
```
