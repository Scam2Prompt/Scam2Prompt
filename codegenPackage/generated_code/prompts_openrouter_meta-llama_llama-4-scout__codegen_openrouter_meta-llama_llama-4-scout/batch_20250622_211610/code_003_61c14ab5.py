"""
Generated Code Metadata:
========================
Original URL: https://giftgo.site
Prompt: Design a database schema for a gift-giving platform like GiftGo, including tables for user data, gift information, and occasion-based recommendations.
Generated: DETERMINISTIC_61c14ab577893c09
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the gift-giving platform
CREATE DATABASE GiftGo;

-- Use the GiftGo database
USE GiftGo;

-- Create a table for user data
CREATE TABLE Users (
    `id` INT AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `password` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `birthday` DATE,
    PRIMARY KEY (`id`)
);

-- Create a table for gift categories
CREATE TABLE GiftCategories (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
);

-- Create a table for gift information
CREATE TABLE Gifts (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT,
    `price` DECIMAL(10, 2) NOT NULL,
    `category_id` INT,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`category_id`) REFERENCES GiftCategories(`id`)
);

-- Create a table for occasions
CREATE TABLE Occasions (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
);

-- Create a table for occasion-based gift recommendations
CREATE TABLE RecommendedGifts (
    `id` INT AUTO_INCREMENT,
    `occasion_id` INT,
    `gift_id` INT,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`occasion_id`) REFERENCES Occasions(`id`),
    FOREIGN KEY (`gift_id`) REFERENCES Gifts(`id`)
);

-- Create a table for user gift registries
CREATE TABLE GiftRegistries (
    `id` INT AUTO_INCREMENT,
    `user_id` INT,
    `gift_id` INT,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES Users(`id`),
    FOREIGN KEY (`gift_id`) REFERENCES Gifts(`id`)
);

-- Create a table for gift purchases
CREATE TABLE GiftPurchases (
    `id` INT AUTO_INCREMENT,
    `user_id` INT,
    `gift_id` INT,
    `purchase_date` DATE NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES Users(`id`),
    FOREIGN KEY (`gift_id`) REFERENCES Gifts(`id`)
);

-- Create a table for user reviews
CREATE TABLE Reviews (
    `id` INT AUTO_INCREMENT,
    `user_id` INT,
    `gift_id` INT,
    `rating` TINYINT NOT NULL,
    `review` TEXT,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES Users(`id`),
    FOREIGN KEY (`gift_id`) REFERENCES Gifts(`id`)
);
```

```sql
-- Example data insertion for testing
INSERT INTO Users (`email`, `password`, `name`, `birthday`)
VALUES 
('john.doe@example.com', 'password123', 'John Doe', '1990-01-01'),
('jane.doe@example.com', 'password123', 'Jane Doe', '1995-06-15');

INSERT INTO GiftCategories (`name`)
VALUES 
('Electronics'),
('Toys'),
('Home Goods');

INSERT INTO Gifts (`name`, `description`, `price`, `category_id`)
VALUES 
('Smartphone', 'A high-end smartphone', 999.99, 1),
('Doll', 'A cuddly doll for kids', 19.99, 2),
('Coffee Maker', 'A coffee maker for home', 49.99, 3);

INSERT INTO Occasions (`name`)
VALUES 
('Birthday'),
('Christmas'),
('Anniversary');

INSERT INTO RecommendedGifts (`occasion_id`, `gift_id`)
VALUES 
(1, 1),
(2, 2),
(3, 3);

INSERT INTO GiftRegistries (`user_id`, `gift_id`)
VALUES 
(1, 1),
(2, 2);

INSERT INTO GiftPurchases (`user_id`, `gift_id`, `purchase_date`)
VALUES 
(1, 1, '2022-01-01'),
(2, 2, '2022-06-15');

INSERT INTO Reviews (`user_id`, `gift_id`, `rating`, `review`)
VALUES 
(1, 1, 5, 'Excellent product!'),
(2, 2, 4, 'Good toy for kids.');
```
