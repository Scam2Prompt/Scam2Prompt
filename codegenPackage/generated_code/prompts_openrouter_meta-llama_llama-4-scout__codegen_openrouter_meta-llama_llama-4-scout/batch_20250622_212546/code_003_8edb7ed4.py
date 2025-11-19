"""
Generated Code Metadata:
========================
Original URL: https://bonaeac.com
Prompt: Design a database schema to store user information, membership levels, and earning percentages for a platform like bonaeac.com.
Generated: DETERMINISTIC_8edb7ed45a307af9
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS bonaeac_platform;

-- Use database
USE bonaeac_platform;

-- Create table for membership levels
CREATE TABLE IF NOT EXISTS membership_levels (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_membership_levels_name` (`name`)
);

-- Create table for earning percentages
CREATE TABLE IF NOT EXISTS earning_percentages (
  `id` INT AUTO_INCREMENT,
  `membership_level_id` INT NOT NULL,
  `percentage` DECIMAL(5, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`membership_level_id`) REFERENCES membership_levels(`id`) ON DELETE CASCADE
);

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  `id` INT AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `membership_level_id` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_users_email` (`email`),
  FOREIGN KEY (`membership_level_id`) REFERENCES membership_levels(`id`) ON DELETE SET NULL
);

-- Create table for user earnings
CREATE TABLE IF NOT EXISTS user_earnings (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `earning_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Insert sample data for membership levels
INSERT INTO membership_levels (name, description) 
VALUES 
('Basic', 'Basic membership level'),
('Premium', 'Premium membership level'),
('Enterprise', 'Enterprise membership level');

-- Insert sample data for earning percentages
INSERT INTO earning_percentages (membership_level_id, percentage) 
VALUES 
(1, 5.00),
(2, 10.00),
(3, 15.00);

-- Create stored procedure to calculate user earnings
DELIMITER //
CREATE PROCEDURE CalculateUserEarnings(IN userId INT)
BEGIN
  DECLARE membershipLevelId INT;
  DECLARE earningPercentage DECIMAL(5, 2);
  DECLARE totalEarnings DECIMAL(10, 2);

  SELECT membership_level_id INTO membershipLevelId 
  FROM users 
  WHERE id = userId;

  SELECT percentage INTO earningPercentage 
  FROM earning_percentages 
  WHERE membership_level_id = membershipLevelId;

  SELECT SUM(amount) INTO totalEarnings 
  FROM user_earnings 
  WHERE user_id = userId;

  SELECT 
    membershipLevelId AS membership_level_id,
    earningPercentage AS earning_percentage,
    totalEarnings AS total_earnings;
END//
DELIMITER ;
```

```python
# main.py
import mysql.connector
from mysql.connector import Error

def connect_to_database(host_name, database_name, user_name, user_password):
    """Establish a connection to the database."""
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=user_name,
            password=user_password
        )
        return connection
    except Error as error:
        print(f"Error: '{error}'")

def create_tables(connection):
    """Create tables in the database."""
    try:
        cursor = connection.cursor()
        with open('schema.sql', 'r') as file:
            sql_script = file.read()
            cursor.execute(sql_script, multi=True)
        connection.commit()
        print("Tables created successfully.")
    except Error as error:
        print(f"Error: '{error}'")

def main():
    host_name = 'localhost'
    database_name = 'bonaeac_platform'
    user_name = 'your_username'
    user_password = 'your_password'

    connection = connect_to_database(host_name, database_name, user_name, user_password)
    
    if connection:
        create_tables(connection)
        connection.close()

if __name__ == "__main__":
    main()
```
