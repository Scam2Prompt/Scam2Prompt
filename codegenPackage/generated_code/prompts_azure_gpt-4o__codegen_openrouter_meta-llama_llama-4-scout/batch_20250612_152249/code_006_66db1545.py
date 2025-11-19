"""
Generated Code Metadata:
========================
Original URL: https://sandbox.co.com
Prompt: Create a database schema for managing user accounts, game categories, and promotional offers for a betting platform like 8KBet.
Generated: DETERMINISTIC_66db154595314e58
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for 8KBet platform

-- Create database
CREATE DATABASE eight_kbet;

-- Use database
USE eight_kbet;

-- Create table for user accounts
CREATE TABLE users (
    `id` BIGINT AUTO_INCREMENT,
    `username` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `password_hash` VARCHAR(255) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_username` (`username`),
    UNIQUE KEY `uk_email` (`email`)
);

-- Create table for game categories
CREATE TABLE game_categories (
    `id` BIGINT AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_name` (`name`)
);

-- Create table for promotional offers
CREATE TABLE promotional_offers (
    `id` BIGINT AUTO_INCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `description` TEXT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    CHECK (`start_date` < `end_date`)
);

-- Create table for user roles
CREATE TABLE user_roles (
    `id` BIGINT AUTO_INCREMENT,
    `user_id` BIGINT NOT NULL,
    `role` ENUM('admin', 'moderator', 'user') NOT NULL DEFAULT 'user',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for game categories and promotional offers many-to-many relationship
CREATE TABLE game_category_offers (
    `game_category_id` BIGINT NOT NULL,
    `promotional_offer_id` BIGINT NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`game_category_id`, `promotional_offer_id`),
    FOREIGN KEY (`game_category_id`) REFERENCES game_categories(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`promotional_offer_id`) REFERENCES promotional_offers(`id`) ON DELETE CASCADE
);

-- Create table for user account transactions
CREATE TABLE user_transactions (
    `id` BIGINT AUTO_INCREMENT,
    `user_id` BIGINT NOT NULL,
    `transaction_type` ENUM('deposit', 'withdrawal') NOT NULL,
    `amount` DECIMAL(10, 2) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_users_username ON users (`username`);
CREATE INDEX idx_users_email ON users (`email`);
CREATE INDEX idx_game_categories_name ON game_categories (`name`);
CREATE INDEX idx_promotional_offers_title ON promotional_offers (`title`);
```

```sql
-- Example insert statements
INSERT INTO users (`username`, `email`, `password_hash`)
VALUES 
('john_doe', 'john@example.com', 'password_hash'),
('jane_doe', 'jane@example.com', 'password_hash');

INSERT INTO game_categories (`name`, `description`)
VALUES 
('Sports', 'Sports betting'),
('Casino', 'Casino games');

INSERT INTO promotional_offers (`title`, `description`, `start_date`, `end_date`)
VALUES 
('Welcome Bonus', '100% bonus on first deposit', '2022-01-01', '2022-12-31'),
('Loyalty Program', '10% cashback on all losses', '2022-01-01', '2023-01-01');
```
