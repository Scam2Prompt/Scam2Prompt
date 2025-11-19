"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://divinecollections.net
Prompt: Design a database schema for storing information about Golu Dolls, including attributes like type, material, and price, to support an online shopping platform.
Generated: DETERMINISTIC_e00a62a6466efb44
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Golu Dolls

-- Create a table to store information about Golu Dolls
CREATE TABLE GoluDolls (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each Golu Doll
    type VARCHAR(50) NOT NULL,         -- Type of Golu Doll (e.g., traditional, modern)
    material VARCHAR(50) NOT NULL,     -- Material used to make the Golu Doll (e.g., clay, wood)
    price DECIMAL(10, 2) NOT NULL,     -- Price of the Golu Doll (up to 99999999.99)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT chk_price CHECK (price >= 0) -- Ensure the price is non-negative
);

-- Create a table to store categories for Golu Dolls
CREATE TABLE Categories (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    name VARCHAR(50) NOT NULL,         -- Name of the category (e.g., festival, occasion)
    description TEXT                    -- Description of the category
);

-- Create a many-to-many relationship between Golu Dolls and Categories
CREATE TABLE GoluDollCategories (
    golu_doll_id INT NOT NULL,         -- Foreign key referencing the Golu Doll
    category_id INT NOT NULL,          -- Foreign key referencing the Category
    PRIMARY KEY (golu_doll_id, category_id), -- Composite primary key
    FOREIGN KEY (golu_doll_id) REFERENCES GoluDolls(id) ON DELETE CASCADE, -- Reference to GoluDolls table
    FOREIGN KEY (category_id) REFERENCES Categories(id) ON DELETE CASCADE     -- Reference to Categories table
);

-- Create a table for storing user reviews about Golu Dolls
CREATE TABLE Reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each review
    golu_doll_id INT NOT NULL,          -- Foreign key referencing the Golu Doll being reviewed
    user_id INT NOT NULL,                -- Identifier for the user who wrote the review
    rating INT CHECK (rating BETWEEN 1 AND 5), -- Rating from 1 to 5
    comment TEXT,                       -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review is created
    FOREIGN KEY (golu_doll_id) REFERENCES GoluDolls(id) ON DELETE CASCADE -- Reference to GoluDolls table
);

-- Create a table for storing user information
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Username for user account
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- User email address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of account creation
);
```
