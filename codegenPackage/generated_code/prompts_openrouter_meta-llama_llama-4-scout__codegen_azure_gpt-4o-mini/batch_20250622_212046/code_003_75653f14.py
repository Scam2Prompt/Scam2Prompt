"""
Generated Code Metadata:
========================
Original URL: https://financeinvestmentslimited.org
Prompt: Design a database schema for storing investor information, investment portfolios, and transaction records for a financial investment company like Finance Investment Limited, and provide a brief explanation of the schema.
Generated: DETERMINISTIC_75653f1409a92ce9
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Finance Investment Limited

-- Table to store investor information
CREATE TABLE Investors (
    investor_id SERIAL PRIMARY KEY, -- Unique identifier for each investor
    first_name VARCHAR(50) NOT NULL, -- Investor's first name
    last_name VARCHAR(50) NOT NULL, -- Investor's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Investor's email address
    phone_number VARCHAR(15), -- Investor's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store investment portfolios
CREATE TABLE Portfolios (
    portfolio_id SERIAL PRIMARY KEY, -- Unique identifier for each portfolio
    investor_id INT NOT NULL, -- Foreign key referencing Investors table
    portfolio_name VARCHAR(100) NOT NULL, -- Name of the portfolio
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (investor_id) REFERENCES Investors(investor_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store transaction records
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    portfolio_id INT NOT NULL, -- Foreign key referencing Portfolios table
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('BUY', 'SELL')), -- Type of transaction
    amount DECIMAL(15, 2) NOT NULL, -- Amount involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_investor_email ON Investors(email);
CREATE INDEX idx_portfolio_investor ON Portfolios(investor_id);
CREATE INDEX idx_transaction_portfolio ON Transactions(portfolio_id);
```
