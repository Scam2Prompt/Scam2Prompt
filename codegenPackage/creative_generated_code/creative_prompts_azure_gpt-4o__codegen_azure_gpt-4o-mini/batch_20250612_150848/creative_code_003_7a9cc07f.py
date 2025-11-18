"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch.danngol.com
Prompt: Suggest a database schema for a platform like "단골가게" that supports local business listings, user accounts, prepayment transactions, and discount tracking.
Generated: DETERMINISTIC_7a9cc07f9c229673
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a platform similar to "단골가게"

-- Create a table to store information about local businesses
CREATE TABLE Businesses (
    id SERIAL PRIMARY KEY,                     -- Unique identifier for each business
    name VARCHAR(255) NOT NULL,                -- Name of the business
    address VARCHAR(255) NOT NULL,             -- Address of the business
    phone_number VARCHAR(15),                   -- Contact number of the business
    website VARCHAR(255),                       -- Website URL of the business
    description TEXT,                           -- Description of the business
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the business was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store user accounts
CREATE TABLE Users (
    id SERIAL PRIMARY KEY,                      -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,      -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,       -- Hashed password for security
    email VARCHAR(255) NOT NULL UNIQUE,         -- Unique email address for the user
    phone_number VARCHAR(15),                   -- Contact number of the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the account was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store payment transactions
CREATE TABLE Transactions (
    id SERIAL PRIMARY KEY,                      -- Unique identifier for each transaction
    user_id INT NOT NULL REFERENCES Users(id),  -- Foreign key referencing the user making the transaction
    business_id INT NOT NULL REFERENCES Businesses(id), -- Foreign key referencing the business
    amount DECIMAL(10, 2) NOT NULL,            -- Amount of the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    status VARCHAR(20) NOT NULL CHECK (status IN ('Pending', 'Completed', 'Failed')) -- Status of the transaction
);

-- Create a table to track discounts offered by businesses
CREATE TABLE Discounts (
    id SERIAL PRIMARY KEY,                      -- Unique identifier for each discount
    business_id INT NOT NULL REFERENCES Businesses(id), -- Foreign key referencing the business
    discount_percentage DECIMAL(5, 2) NOT NULL CHECK (discount_percentage > 0 AND discount_percentage <= 100), -- Discount percentage
    start_date TIMESTAMP NOT NULL,              -- Start date for the discount
    end_date TIMESTAMP NOT NULL,                -- End date for the discount
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the discount was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);
```
