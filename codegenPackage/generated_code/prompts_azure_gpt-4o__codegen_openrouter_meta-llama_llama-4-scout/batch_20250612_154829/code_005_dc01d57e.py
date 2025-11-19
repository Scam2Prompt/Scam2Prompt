"""
Generated Code Metadata:
========================
Original URL: https://bafybeiadjmwscfmkjexzu7kpxy6a43a56s2cdtmwld2tdzwbnlzwfsecs4.ipfs.dweb.link
Prompt: Create a database schema to store user activity logs, including deposit and withdrawal amounts, transaction types, and timestamps, as detailed on the webpage.
Generated: DETERMINISTIC_dc01d57eea9a2cee
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for user activity logs

-- Create a database
CREATE DATABASE UserActivityDB;

-- Use the database
USE UserActivityDB;

-- Create a table for user activity logs
CREATE TABLE UserActivityLogs (
    `id` BIGINT AUTO_INCREMENT,
    `user_id` BIGINT NOT NULL,
    `transaction_type` ENUM('deposit', 'withdrawal') NOT NULL,
    `amount` DECIMAL(10, 2) NOT NULL,
    `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `description` VARCHAR(255),
    PRIMARY KEY (`id`),
    INDEX idx_user_id (`user_id`),
    INDEX idx_transaction_type (`transaction_type`),
    INDEX idx_timestamp (`timestamp`)
);

-- Create a table for users (optional, but recommended for a complete schema)
CREATE TABLE Users (
    `id` BIGINT AUTO_INCREMENT,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (`id`),
    INDEX idx_username (`username`),
    INDEX idx_email (`email`)
);

-- Alter the UserActivityLogs table to include a foreign key constraint (optional, but recommended)
ALTER TABLE UserActivityLogs
ADD CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES Users(`id`)
ON DELETE CASCADE
ON UPDATE CASCADE;

-- Example stored procedure to insert a new user activity log
DELIMITER //
CREATE PROCEDURE InsertUserActivityLog(
    IN p_user_id BIGINT,
    IN p_transaction_type ENUM('deposit', 'withdrawal'),
    IN p_amount DECIMAL(10, 2),
    IN p_description VARCHAR(255)
)
BEGIN
    INSERT INTO UserActivityLogs (
        user_id,
        transaction_type,
        amount,
        description
    ) VALUES (
        p_user_id,
        p_transaction_type,
        p_amount,
        p_description
    );
END//
DELIMITER ;

-- Example stored procedure to retrieve user activity logs
DELIMITER //
CREATE PROCEDURE GetUserActivityLogs(
    IN p_user_id BIGINT
)
BEGIN
    SELECT 
        id,
        user_id,
        transaction_type,
        amount,
        timestamp,
        description
    FROM 
        UserActivityLogs
    WHERE 
        user_id = p_user_id
    ORDER BY 
        timestamp DESC;
END//
DELIMITER ;
```

```python
# Python example using mysql-connector library to interact with the database

import mysql.connector
from mysql.connector import Error

class UserActivityDB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def insert_user_activity_log(self, user_id, transaction_type, amount, description):
        try:
            cursor = self.connection.cursor()
            query = "CALL InsertUserActivityLog(%s, %s, %s, %s)"
            cursor.execute(query, (user_id, transaction_type, amount, description))
            self.connection.commit()
            print("User activity log inserted successfully")
        except Error as e:
            print(f"Error inserting user activity log: {e}")

    def get_user_activity_logs(self, user_id):
        try:
            cursor = self.connection.cursor()
            query = "CALL GetUserActivityLogs(%s)"
            cursor.execute(query, (user_id,))
            records = cursor.fetchall()
            for record in records:
                print(record)
        except Error as e:
            print(f"Error retrieving user activity logs: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    db = UserActivityDB("localhost", "UserActivityDB", "username", "password")
    db.connect()
    db.insert_user_activity_log(1, "deposit", 100.00, "Test deposit")
    db.get_user_activity_logs(1)
    db.close_connection()
```
