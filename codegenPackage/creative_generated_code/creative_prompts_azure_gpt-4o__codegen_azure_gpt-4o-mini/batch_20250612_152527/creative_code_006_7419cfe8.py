"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reg-thentwr.pages.dev
Prompt: Create a database schema for managing collectible items, including categories like designer toys, trading cards, and accessories, as described on NTWRK.
Generated: DETERMINISTIC_7419cfe877b68178
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing collectible items
CREATE DATABASE CollectiblesDB;

USE CollectiblesDB;

-- Table for storing categories of collectibles
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for storing collectible items
CREATE TABLE Collectibles (
    collectible_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    item_name VARCHAR(255) NOT NULL,
    description TEXT,
    manufacturer VARCHAR(255),
    release_date DATE,
    condition ENUM('New', 'Like New', 'Used', 'Damaged'),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE
);

-- Table for storing users who own collectibles
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for managing user ownership of collectibles
CREATE TABLE User_Collectibles (
    user_collectible_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    collectible_id INT NOT NULL,
    acquisition_date DATE,
    condition ENUM('New', 'Like New', 'Used', 'Damaged'),
    price_paid DECIMAL(10, 2) NOT NULL CHECK (price_paid >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (collectible_id) REFERENCES Collectibles(collectible_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_category_name ON Categories(category_name);
CREATE INDEX idx_item_name ON Collectibles(item_name);
CREATE INDEX idx_username ON Users(username);
```
