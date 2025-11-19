"""
Generated Code Metadata:
========================
Original URL: https://bitcoin100-maxair.com
Prompt: Write a SQL query to manage user data for Bitcoin +100 Maxair, including account creation and preferences for educational services.
Generated: DETERMINISTIC_d9e388ac624f1f92
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for managing user data
CREATE DATABASE IF NOT EXISTS BitcoinMaxairDB;

-- Use the created database
USE BitcoinMaxairDB;

-- Create a table for user accounts
CREATE TABLE IF NOT EXISTS Users (
    `id` INT AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);

-- Create a table for user preferences
CREATE TABLE IF NOT EXISTS UserPreferences (
    `id` INT AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `educational_services` BOOLEAN DEFAULT FALSE,
    `notifications` BOOLEAN DEFAULT TRUE,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Create a stored procedure to create a new user account
DELIMITER $$
CREATE PROCEDURE CreateUser(IN p_email VARCHAR(255), IN p_password VARCHAR(255))
BEGIN
    INSERT INTO Users (email, password) VALUES (p_email, p_password);
END$$
DELIMITER ;

-- Create a stored procedure to update user preferences
DELIMITER $$
CREATE PROCEDURE UpdateUserPreferences(IN p_user_id INT, IN p_educational_services BOOLEAN, IN p_notifications BOOLEAN)
BEGIN
    IF EXISTS (SELECT 1 FROM Users WHERE id = p_user_id) THEN
        INSERT INTO UserPreferences (user_id, educational_services, notifications)
        VALUES (p_user_id, p_educational_services, p_notifications)
        ON DUPLICATE KEY UPDATE educational_services = p_educational_services, notifications = p_notifications;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User not found';
    END IF;
END$$
DELIMITER ;

-- Create a stored procedure to retrieve user data
DELIMITER $$
CREATE PROCEDURE GetUserData(IN p_user_id INT)
BEGIN
    SELECT u.email, up.educational_services, up.notifications
    FROM Users u
    JOIN UserPreferences up ON u.id = up.user_id
    WHERE u.id = p_user_id;
END$$
DELIMITER ;

-- Example usage:
-- CALL CreateUser('example@example.com', 'password123');
-- CALL UpdateUserPreferences(1, TRUE, FALSE);
-- CALL GetUserData(1);
```
