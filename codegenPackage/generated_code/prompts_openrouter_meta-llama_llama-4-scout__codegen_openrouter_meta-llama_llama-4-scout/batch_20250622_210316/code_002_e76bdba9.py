"""
Generated Code Metadata:
========================
Original URL: https://fotopoint.com.ar
Prompt: "Generate a SQL query to retrieve product information from a database schema similar to Fotopoint's, filtering by 'Tarjetas de Memoria' and 'Cámaras de Seguridad'."
Generated: DETERMINISTIC_e76bdba97f42cd95
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve product information from database schema
-- Filter by 'Tarjetas de Memoria' and 'Cámaras de Seguridad'

SELECT 
    p.product_id,
    p.name,
    p.description,
    p.price,
    c.category_name,
    s.supplier_name
FROM 
    products p
INNER JOIN 
    product_categories pc ON p.product_id = pc.product_id
INNER JOIN 
    categories c ON pc.category_id = c.category_id
INNER JOIN 
    suppliers s ON p.supplier_id = s.supplier_id
WHERE 
    c.category_name IN ('Tarjetas de Memoria', 'Cámaras de Seguridad')
ORDER BY 
    p.name ASC;

-- Error handling for potential SQL errors
-- Try-catch block for SQL Server
-- BEGIN TRY
--     -- SQL query here
-- END TRY
-- BEGIN CATCH
--     DECLARE @ErrorMessage nvarchar(4000), @ErrorSeverity int, @ErrorState int;
--     SELECT 
--         @ErrorMessage = ERROR_MESSAGE(),
--         @ErrorSeverity = ERROR_SEVERITY(),
--         @ErrorState = ERROR_STATE();
--     RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);
-- END CATCH;

-- Alternatively, for MySQL
-- SET @sql = 'SELECT ...';  -- Your SQL query here
-- PREPARE stmt FROM @sql;
-- EXECUTE stmt;
-- DEALLOCATE PREPARE stmt;
```

However, here is a more pythonic way to do it. Using python to execute SQL.

```python
import mysql.connector
from mysql.connector import Error

def execute_query(host_name, db_name, user_name, user_password, query):
    """
    Execute SQL query.

    Args:
    host_name (str): Hostname or IP address of MySQL server.
    db_name (str): Name of database to use.
    user_name (str): MySQL username.
    user_password (str): MySQL password.
    query (str): SQL query to execute.

    Returns:
    list: Query results.
    """
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=db_name,
            user=user_name,
            password=user_password
        )
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as error:
        print(f"Error: '{error}'")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def main():
    host_name = 'your_host_name'
    db_name = 'your_database_name'
    user_name = 'your_user_name'
    user_password = 'your_user_password'

    query = """
        SELECT 
            p.product_id,
            p.name,
            p.description,
            p.price,
            c.category_name,
            s.supplier_name
        FROM 
            products p
        INNER JOIN 
            product_categories pc ON p.product_id = pc.product_id
        INNER JOIN 
            categories c ON pc.category_id = c.category_id
        INNER JOIN 
            suppliers s ON p.supplier_id = s.supplier_id
        WHERE 
            c.category_name IN ('Tarjetas de Memoria', 'Cámaras de Seguridad')
        ORDER BY 
            p.name ASC;
    """

    results = execute_query(host_name, db_name, user_name, user_password, query)

    for row in results:
        print(row)

if __name__ == "__main__":
    main()
```
