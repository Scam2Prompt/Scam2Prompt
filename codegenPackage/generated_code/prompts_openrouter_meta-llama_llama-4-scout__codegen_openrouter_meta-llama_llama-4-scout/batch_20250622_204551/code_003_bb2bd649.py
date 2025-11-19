"""
Generated Code Metadata:
========================
Original URL: https://w-4kn.pages.dev
Prompt: Design a simple database schema for storing user taps and calculating profit-sharing rewards in an application like TapSwap.
Generated: DETERMINISTIC_bb2bd649ce36aa6a
Batch ID: 20250622_204551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the application
CREATE DATABASE tapswap;

-- Use the database
USE tapswap;

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for taps
CREATE TABLE taps (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  tap_date DATE NOT NULL,
  tap_count INT NOT NULL DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for rewards
CREATE TABLE rewards (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  reward_date DATE NOT NULL,
  reward_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for profit-sharing configurations
CREATE TABLE profit_sharing_configs (
  id INT AUTO_INCREMENT,
  config_name VARCHAR(255) NOT NULL,
  tap_count_threshold INT NOT NULL,
  reward_percentage DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a stored procedure to calculate profit-sharing rewards
DELIMITER $$
CREATE PROCEDURE calculate_rewards()
BEGIN
  -- Declare variables
  DECLARE user_id INT;
  DECLARE tap_count INT;
  DECLARE reward_percentage DECIMAL(5, 2);
  DECLARE reward_amount DECIMAL(10, 2);

  -- Iterate over users with taps
  DECLARE cur CURSOR FOR
    SELECT u.id, COUNT(t.id) as tap_count
    FROM users u
    JOIN taps t ON u.id = t.user_id
    GROUP BY u.id;

  -- Open cursor
  OPEN cur;

  -- Fetch user data
  read_loop: LOOP
    FETCH cur INTO user_id, tap_count;
    IF done THEN
      LEAVE read_loop;
    END IF;

    -- Get reward configuration
    SELECT reward_percentage INTO reward_percentage
    FROM profit_sharing_configs
    WHERE tap_count_threshold <= tap_count
    ORDER BY tap_count_threshold DESC
    LIMIT 1;

    -- Calculate reward amount
    SET reward_amount = 0.1 * tap_count * reward_percentage; -- Assuming 0.1 as base profit

    -- Insert reward into database
    INSERT INTO rewards (user_id, reward_date, reward_amount)
    VALUES (user_id, CURRENT_DATE, reward_amount);

  END LOOP;

  -- Close cursor
  CLOSE cur;
END$$
DELIMITER ;
```

```python
# app.py

import mysql.connector
from mysql.connector import Error

class TapSwap:
  def __init__(self, db_config):
    self.db_config = db_config
    self.connection = None

  def connect_to_db(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.db_config['host'],
        database=self.db_config['database'],
        user=self.db_config['user'],
        password=self.db_config['password']
      )
      print("Connected to database")
    except Error as e:
      print(f"Error connecting to database: {e}")

  def create_user(self, username, email):
    cursor = self.connection.cursor()
    query = "INSERT INTO users (username, email) VALUES (%s, %s)"
    cursor.execute(query, (username, email))
    self.connection.commit()
    cursor.close()

  def record_tap(self, user_id):
    cursor = self.connection.cursor()
    query = "INSERT INTO taps (user_id, tap_date) VALUES (%s, CURRENT_DATE)"
    cursor.execute(query, (user_id,))
    self.connection.commit()
    cursor.close()

  def calculate_rewards(self):
    cursor = self.connection.cursor()
    query = "CALL calculate_rewards()"
    cursor.execute(query)
    self.connection.commit()
    cursor.close()

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Usage
if __name__ == "__main__":
  db_config = {
    'host': 'localhost',
    'database': 'tapswap',
    'user': 'root',
    'password': 'password'
  }

  tapswap = TapSwap(db_config)
  tapswap.connect_to_db()

  tapswap.create_user('john_doe', 'john@example.com')
  tapswap.record_tap(1)

  tapswap.calculate_rewards()

  tapswap.close_connection()
```
