"""
Generated Code Metadata:
========================
Original URL: https://deepbook.online
Prompt: Generate a SQL query to retrieve customer information and service history for a plumbing company, based on the data stored on a website like Deep Book Online.
Generated: DETERMINISTIC_2ac88258c274a6c2
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve customer information and service history for a plumbing company

-- Define the database and tables
-- Assuming the database schema is similar to:
--   - customers (id, name, email, phone, address)
--   - services (id, customer_id, service_date, description, status)

-- SQL Query
SELECT 
  c.id AS customer_id,
  c.name AS customer_name,
  c.email AS customer_email,
  c.phone AS customer_phone,
  c.address AS customer_address,
  s.id AS service_id,
  s.service_date AS service_date,
  s.description AS service_description,
  s.status AS service_status
FROM 
  customers c
  LEFT JOIN services s ON c.id = s.customer_id
ORDER BY 
  c.id, 
  s.service_date DESC;

-- To get specific customer information, use a WHERE clause
-- Example:
SELECT 
  c.id AS customer_id,
  c.name AS customer_name,
  c.email AS customer_email,
  c.phone AS customer_phone,
  c.address AS customer_address,
  s.id AS service_id,
  s.service_date AS service_date,
  s.description AS service_description,
  s.status AS service_status
FROM 
  customers c
  LEFT JOIN services s ON c.id = s.customer_id
WHERE 
  c.id = ?  -- Replace ? with the actual customer ID
ORDER BY 
  c.id, 
  s.service_date DESC;

-- Stored Procedure to retrieve customer information and service history
DELIMITER //
CREATE PROCEDURE GetCustomerInfoAndServiceHistory(IN customer_id INT)
BEGIN
  SELECT 
    c.id AS customer_id,
    c.name AS customer_name,
    c.email AS customer_email,
    c.phone AS customer_phone,
    c.address AS customer_address,
    s.id AS service_id,
    s.service_date AS service_date,
    s.description AS service_description,
    s.status AS service_status
  FROM 
    customers c
    LEFT JOIN services s ON c.id = s.customer_id
  WHERE 
    c.id = customer_id
  ORDER BY 
    c.id, 
    s.service_date DESC;
END//
DELIMITER ;

-- Example usage:
-- CALL GetCustomerInfoAndServiceHistory(1);
```

```python
import mysql.connector
from mysql.connector import Error

def get_customer_info_and_service_history(customer_id):
  """
  Retrieves customer information and service history.

  Args:
    customer_id (int): The ID of the customer.

  Returns:
    list: A list of tuples containing customer information and service history.
  """
  try:
    # Establish a connection to the database
    connection = mysql.connector.connect(
      host='your_host',
      database='your_database',
      user='your_user',
      password='your_password'
    )

    # Create a cursor object
    cursor = connection.cursor()

    # SQL query to retrieve customer information and service history
    query = """
      SELECT 
        c.id AS customer_id,
        c.name AS customer_name,
        c.email AS customer_email,
        c.phone AS customer_phone,
        c.address AS customer_address,
        s.id AS service_id,
        s.service_date AS service_date,
        s.description AS service_description,
        s.status AS service_status
      FROM 
        customers c
        LEFT JOIN services s ON c.id = s.customer_id
      WHERE 
        c.id = %s
      ORDER BY 
        c.id, 
        s.service_date DESC;
    """

    # Execute the query
    cursor.execute(query, (customer_id,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return rows

  except Error as e:
    print(f"Error: {e}")
    return []

# Example usage:
customer_id = 1
result = get_customer_info_and_service_history(customer_id)
for row in result:
  print(row)
```
