"""
Generated Code Metadata:
========================
Original URL: https://claim-bits.com
Prompt: "Design a database schema to store user information, ad clicks, and payment records for a platform that pays users for viewing ads and completing tasks."
Generated: DETERMINISTIC_7298594ea6703f90
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a platform that pays users for viewing ads and completing tasks

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store ad clicks
CREATE TABLE AdClicks (
    click_id SERIAL PRIMARY KEY,          -- Unique identifier for each ad click
    user_id INT NOT NULL,                 -- Foreign key referencing Users table
    ad_id INT NOT NULL,                   -- Identifier for the ad clicked
    click_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the click
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store payment records
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY,         -- Unique identifier for each payment
    user_id INT NOT NULL,                  -- Foreign key referencing Users table
    amount DECIMAL(10, 2) NOT NULL,        -- Amount paid to the user
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the payment
    status VARCHAR(20) NOT NULL CHECK (status IN ('Pending', 'Completed', 'Failed')), -- Status of the payment
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store ads
CREATE TABLE Ads (
    ad_id SERIAL PRIMARY KEY,              -- Unique identifier for each ad
    ad_content TEXT NOT NULL,              -- Content of the ad
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of ad creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);
```
