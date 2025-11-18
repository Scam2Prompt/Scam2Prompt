"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom.gifts
Prompt: Suggest a database schema for managing daily item rotations in an online shop, including item categories and prices, as seen on Phantom's "Item Shop Daily Rotation."
Generated: DETERMINISTIC_6029a794b2c2f67e
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing daily item rotations in an online shop

-- Create a table for item categories
CREATE TABLE item_categories (
    category_id SERIAL PRIMARY KEY,           -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL,     -- Name of the item category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for items
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,               -- Unique identifier for each item
    item_name VARCHAR(255) NOT NULL,          -- Name of the item
    category_id INT REFERENCES item_categories(category_id) ON DELETE CASCADE, -- Foreign key to category
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the item with a check constraint for non-negative values
    rotation_date DATE NOT NULL,              -- Date when the item is available for rotation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the item was last updated
);

-- Create a table for daily rotations
CREATE TABLE daily_rotations (
    rotation_id SERIAL PRIMARY KEY,           -- Unique identifier for each rotation
    rotation_date DATE NOT NULL UNIQUE,       -- Date of the rotation, ensuring uniqueness
    item_id INT REFERENCES items(item_id) ON DELETE CASCADE, -- Foreign key to item
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the rotation entry was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the rotation entry was last updated
);

-- Create indexes on frequently queried columns for performance
CREATE INDEX idx_item_category ON items(category_id);
CREATE INDEX idx_rotation_date ON daily_rotations(rotation_date);
```
