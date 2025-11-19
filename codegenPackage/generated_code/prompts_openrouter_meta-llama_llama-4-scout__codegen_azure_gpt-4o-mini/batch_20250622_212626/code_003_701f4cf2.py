"""
Generated Code Metadata:
========================
Original URL: https://investmentbrokertransactions.com
Prompt: "Design a database schema to store information about startups, investors, and funding transactions, including fields for startup stage, investor interests, and investment amounts."
Generated: DETERMINISTIC_701f4cf24945a4d6
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about startups, investors, and funding transactions

-- Table to store information about startups
CREATE TABLE Startups (
    id SERIAL PRIMARY KEY, -- Unique identifier for each startup
    name VARCHAR(255) NOT NULL, -- Name of the startup
    description TEXT, -- Description of the startup
    stage VARCHAR(50) NOT NULL, -- Stage of the startup (e.g., Seed, Series A, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the startup was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store information about investors
CREATE TABLE Investors (
    id SERIAL PRIMARY KEY, -- Unique identifier for each investor
    name VARCHAR(255) NOT NULL, -- Name of the investor
    email VARCHAR(255) UNIQUE NOT NULL, -- Email of the investor
    interests TEXT, -- Areas of interest for the investor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the investor was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store funding transactions
CREATE TABLE FundingTransactions (
    id SERIAL PRIMARY KEY, -- Unique identifier for each funding transaction
    startup_id INT NOT NULL, -- Foreign key referencing the startup
    investor_id INT NOT NULL, -- Foreign key referencing the investor
    amount DECIMAL(15, 2) NOT NULL, -- Amount invested
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the transaction was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (startup_id) REFERENCES Startups(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (investor_id) REFERENCES Investors(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_startup_stage ON Startups(stage);
CREATE INDEX idx_investor_interests ON Investors(interests);
CREATE INDEX idx_funding_transaction_date ON FundingTransactions(transaction_date);
```
