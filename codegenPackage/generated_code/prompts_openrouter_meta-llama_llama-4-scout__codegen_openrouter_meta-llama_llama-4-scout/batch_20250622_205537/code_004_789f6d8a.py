"""
Generated Code Metadata:
========================
Original URL: https://joinnow.info
Prompt: "Design a basic database schema to store information about Money Order Freedom subscribers, referrals, and sales, including fields for tracking income and subscription levels."
Generated: DETERMINISTIC_789f6d8a384b1e79
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Money Order Freedom
CREATE DATABASE money_order_freedom;

-- Use the database
USE money_order_freedom;

-- Create table for subscribers
CREATE TABLE subscribers (
  `id` INT AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `name` VARCHAR(255) NOT NULL,
  `subscription_level` ENUM('basic', 'premium', 'enterprise') NOT NULL DEFAULT 'basic',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for referrals
CREATE TABLE referrals (
  `id` INT AUTO_INCREMENT,
  `subscriber_id` INT NOT NULL,
  `referred_email` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`subscriber_id`) REFERENCES subscribers(`id`) ON DELETE CASCADE
);

-- Create table for sales
CREATE TABLE sales (
  `id` INT AUTO_INCREMENT,
  `subscriber_id` INT NOT NULL,
  `sale_amount` DECIMAL(10, 2) NOT NULL,
  `sale_date` DATE NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`subscriber_id`) REFERENCES subscribers(`id`) ON DELETE CASCADE
);

-- Create table for income tracking
CREATE TABLE income_tracking (
  `id` INT AUTO_INCREMENT,
  `subscriber_id` INT NOT NULL,
  `income_amount` DECIMAL(10, 2) NOT NULL,
  `income_date` DATE NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`subscriber_id`) REFERENCES subscribers(`id`) ON DELETE CASCADE
);

-- Create table for subscription levels
CREATE TABLE subscription_levels (
  `id` INT AUTO_INCREMENT,
  `level_name` ENUM('basic', 'premium', 'enterprise') NOT NULL,
  `level_description` TEXT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Insert default subscription levels
INSERT INTO subscription_levels (level_name, level_description) 
VALUES 
('basic', 'Basic subscription level'),
('premium', 'Premium subscription level'),
('enterprise', 'Enterprise subscription level');

-- Create view for subscriber information with subscription level
CREATE VIEW subscriber_info AS
SELECT 
  s.id,
  s.email,
  s.name,
  sl.level_name AS subscription_level,
  s.created_at,
  s.updated_at
FROM 
  subscribers s
  INNER JOIN subscription_levels sl ON s.subscription_level = sl.level_name;

-- Create stored procedure to update subscriber subscription level
DELIMITER //
CREATE PROCEDURE update_subscription_level(
  IN p_subscriber_id INT,
  IN p_level_name ENUM('basic', 'premium', 'enterprise')
)
BEGIN
  UPDATE subscribers 
  SET subscription_level = p_level_name 
  WHERE id = p_subscriber_id;
END//
DELIMITER ;
```

```python
# main.py
import mysql.connector
from mysql.connector import Error

def connect_to_db(host_name, db_name, user_name, user_password):
  """Establish a connection to the database."""
  try:
    connection = mysql.connector.connect(
      host=host_name,
      database=db_name,
      user=user_name,
      password=user_password
    )
    return connection
  except Error as error:
    print(f"Error: '{error}'")

def create_subscriber(connection, email, name, subscription_level):
  """Create a new subscriber."""
  try:
    cursor = connection.cursor()
    query = "INSERT INTO subscribers (email, name, subscription_level) VALUES (%s, %s, %s)"
    cursor.execute(query, (email, name, subscription_level))
    connection.commit()
    return cursor.lastrowid
  except Error as error:
    print(f"Error: '{error}'")

def get_subscriber_info(connection, subscriber_id):
  """Get subscriber information."""
  try:
    cursor = connection.cursor()
    query = "SELECT * FROM subscriber_info WHERE id = %s"
    cursor.execute(query, (subscriber_id,))
    return cursor.fetchone()
  except Error as error:
    print(f"Error: '{error}'")

def main():
  # Establish a connection to the database
  connection = connect_to_db('localhost', 'money_order_freedom', 'root', 'password')

  # Create a new subscriber
  subscriber_id = create_subscriber(connection, 'subscriber@example.com', 'Subscriber Name', 'basic')
  print(f"Subscriber ID: {subscriber_id}")

  # Get subscriber information
  subscriber_info = get_subscriber_info(connection, subscriber_id)
  print(subscriber_info)

if __name__ == "__main__":
  main()
```
