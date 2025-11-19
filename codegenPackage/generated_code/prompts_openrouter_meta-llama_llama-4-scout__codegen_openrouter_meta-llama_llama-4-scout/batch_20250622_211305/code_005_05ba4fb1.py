"""
Generated Code Metadata:
========================
Original URL: https://immediate-affinity.com
Prompt: Design a database schema for storing user information, investment education resources, and firm details for a platform like Switch ePrex 0.3.
Generated: DETERMINISTIC_05ba4fb111003df6
Batch ID: 20250622_211305
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
CREATE DATABASE ePrex0_3;

-- Use database
USE ePrex0_3;

-- Create table for users
CREATE TABLE Users (
  `id` INT AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `password_hash` VARCHAR(255) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for investment education resources
CREATE TABLE Education_Resources (
  `id` INT AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `resource_type` ENUM('video', 'article', 'pdf') NOT NULL,
  `resource_url` VARCHAR(255),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for firms
CREATE TABLE Firms (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `firm_type` ENUM('investment', 'financial', 'insurance') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for user_firm association
CREATE TABLE User_Firms (
  `user_id` INT NOT NULL,
  `firm_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`, `firm_id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`firm_id`) REFERENCES Firms(`id`) ON DELETE CASCADE
);

-- Create table for user_education_resource association
CREATE TABLE User_Education_Resources (
  `user_id` INT NOT NULL,
  `resource_id` INT NOT NULL,
  `completed` BOOLEAN DEFAULT FALSE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`, `resource_id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`resource_id`) REFERENCES Education_Resources(`id`) ON DELETE CASCADE
);
```

```sql
-- indexes.sql

-- Create indexes on Users table
CREATE INDEX idx_users_email ON Users(email);
CREATE INDEX idx_users_name ON Users(name);

-- Create indexes on Education_Resources table
CREATE INDEX idx_education_resources_title ON Education_Resources(title);
CREATE INDEX idx_education_resources_resource_type ON Education_Resources(resource_type);

-- Create indexes on Firms table
CREATE INDEX idx_firms_name ON Firms(name);
CREATE INDEX idx_firms_firm_type ON Firms(firm_type);

-- Create indexes on User_Firms table
CREATE INDEX idx_user_firms_user_id ON User_Firms(user_id);
CREATE INDEX idx_user_firms_firm_id ON User_Firms(firm_id);

-- Create indexes on User_Education_Resources table
CREATE INDEX idx_user_education_resources_user_id ON User_Education_Resources(user_id);
CREATE INDEX idx_user_education_resources_resource_id ON User_Education_Resources(resource_id);
```

```sql
-- stored_procedures.sql

DELIMITER $$

-- Stored procedure to create a new user
CREATE PROCEDURE CreateUser(
  IN p_email VARCHAR(255),
  IN p_password_hash VARCHAR(255),
  IN p_name VARCHAR(100)
)
BEGIN
  INSERT INTO Users (email, password_hash, name)
  VALUES (p_email, p_password_hash, p_name);
END$$

-- Stored procedure to get user by email
CREATE PROCEDURE GetUserByEmail(
  IN p_email VARCHAR(255)
)
BEGIN
  SELECT * FROM Users
  WHERE email = p_email;
END$$

-- Stored procedure to create a new education resource
CREATE PROCEDURE CreateEducationResource(
  IN p_title VARCHAR(255),
  IN p_description TEXT,
  IN p_resource_type ENUM('video', 'article', 'pdf'),
  IN p_resource_url VARCHAR(255)
)
BEGIN
  INSERT INTO Education_Resources (title, description, resource_type, resource_url)
  VALUES (p_title, p_description, p_resource_type, p_resource_url);
END$$

-- Stored procedure to get education resource by id
CREATE PROCEDURE GetEducationResourceById(
  IN p_id INT
)
BEGIN
  SELECT * FROM Education_Resources
  WHERE id = p_id;
END$$

DELIMITER ;
```
