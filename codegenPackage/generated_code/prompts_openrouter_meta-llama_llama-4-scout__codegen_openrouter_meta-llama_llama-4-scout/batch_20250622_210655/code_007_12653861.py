"""
Generated Code Metadata:
========================
Original URL: https://karaokeheaven.uk
Prompt: Generate a SQL query to retrieve information about available karaoke rooms and their locations for a specific date and time, similar to Karaoke Heaven's booking system.
Generated: DETERMINISTIC_12653861e93f82ba
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Karaoke Room Booking Query

-- Define the database schema
-- For this example, let's assume we have the following tables:
--   - karaoke_rooms (id, name, location, capacity)
--   - bookings (id, room_id, date, start_time, end_time)

-- Query to retrieve available karaoke rooms and their locations
-- for a specific date and time
DELIMITER //

CREATE PROCEDURE GetAvailableKaraokeRooms(
  IN target_date DATE,
  IN start_time TIME,
  IN end_time TIME
)
BEGIN
  SELECT 
    kr.id,
    kr.name,
    kr.location,
    kr.capacity
  FROM 
    karaoke_rooms kr
  WHERE 
    kr.id NOT IN (
      SELECT 
        b.room_id
      FROM 
        bookings b
      WHERE 
        b.date = target_date
        AND ((b.start_time, b.end_time) OVERLAPS (start_time, end_time))
    );
END //

DELIMITER ;

-- Example usage:
-- CALL GetAvailableKaraokeRooms('2024-09-16', '18:00:00', '22:00:00');

-- Alternatively, you can use a single query without a stored procedure
SELECT 
  kr.id,
  kr.name,
  kr.location,
  kr.capacity
FROM 
  karaoke_rooms kr
WHERE 
  kr.id NOT IN (
    SELECT 
      b.room_id
    FROM 
      bookings b
    WHERE 
      b.date = '2024-09-16'
      AND ((b.start_time, b.end_time) OVERLAPS ('18:00:00', '22:00:00'))
  );
```

```python
# Python script to interact with the database

import mysql.connector
from mysql.connector import Error

def get_available_karaoke_rooms(host_name, db_name, user_name, user_password, target_date, start_time, end_time):
  """
  Retrieves a list of available karaoke rooms and their locations for a specific date and time.

  Args:
    host_name (str): The hostname or IP address of the database server.
    db_name (str): The name of the database.
    user_name (str): The username to use for the database connection.
    user_password (str): The password to use for the database connection.
    target_date (str): The date to query for available rooms (YYYY-MM-DD).
    start_time (str): The start time to query for available rooms (HH:MM:SS).
    end_time (str): The end time to query for available rooms (HH:MM:SS).

  Returns:
    list: A list of tuples containing the room id, name, location, and capacity.
  """

  try:
    connection = mysql.connector.connect(
      host=host_name,
      database=db_name,
      user=user_name,
      password=user_password
    )

    cursor = connection.cursor()

    query = """
      SELECT 
        kr.id,
        kr.name,
        kr.location,
        kr.capacity
      FROM 
        karaoke_rooms kr
      WHERE 
        kr.id NOT IN (
          SELECT 
            b.room_id
          FROM 
            bookings b
          WHERE 
            b.date = %s
            AND ((b.start_time, b.end_time) OVERLAPS (%s, %s))
        )
    """

    cursor.execute(query, (target_date, start_time, end_time))

    available_rooms = cursor.fetchall()

    return available_rooms

  except Error as error:
    print(f"Error: '{error}'")

  finally:
    if (connection.is_connected()):
      cursor.close()
      connection.close()
      print("MySQL connection is closed")

# Example usage:
host_name = 'localhost'
db_name = 'karaoke_heaven'
user_name = 'your_username'
user_password = 'your_password'
target_date = '2024-09-16'
start_time = '18:00:00'
end_time = '22:00:00'

available_rooms = get_available_karaoke_rooms(host_name, db_name, user_name, user_password, target_date, start_time, end_time)

for room in available_rooms:
  print(room)
```
