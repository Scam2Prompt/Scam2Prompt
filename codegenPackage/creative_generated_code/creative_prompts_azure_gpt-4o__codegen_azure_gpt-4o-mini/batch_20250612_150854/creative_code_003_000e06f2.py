"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.org
Prompt: Create a database schema to store user preferences and match them with investment education firms, following Immediate Migna's tailored connection process.
Generated: DETERMINISTIC_000e06f2aa2d740a
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for storing user preferences and matching them with investment education firms

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,                -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,     -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,        -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the user is created
);

-- Create a table to store user preferences
CREATE TABLE UserPreferences (
    preference_id SERIAL PRIMARY KEY,          -- Unique identifier for preferences
    user_id INT NOT NULL REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key to Users
    investment_type VARCHAR(50),                -- Type of investment the user is interested in (e.g., stocks, real estate)
    risk_tolerance VARCHAR(50),                 -- User's risk tolerance level (e.g., low, medium, high)
    education_level VARCHAR(50),                -- User's education level (e.g., beginner, intermediate, advanced)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when preferences are recorded
);

-- Create a table to store investment education firms
CREATE TABLE InvestmentFirms (
    firm_id SERIAL PRIMARY KEY,                 -- Unique identifier for each investment firm
    firm_name VARCHAR(100) NOT NULL,           -- Name of the investment education firm
    investment_type VARCHAR(50),                -- Type of investment offered by the firm
    risk_tolerance VARCHAR(50),                 -- Risk tolerance level offered by the firm
    education_level VARCHAR(50),                -- Education level provided by the firm
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the firm is added
);

-- Create a table to store connections between users and investment firms
CREATE TABLE UserFirmConnections (
    connection_id SERIAL PRIMARY KEY,           -- Unique identifier for each connection
    user_id INT NOT NULL REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key to Users
    firm_id INT NOT NULL REFERENCES InvestmentFirms(firm_id) ON DELETE CASCADE, -- Foreign key to InvestmentFirms
    matched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the connection was made
    UNIQUE(user_id, firm_id)                    -- Ensure that a user can only connect to a firm once
);

-- Create an index on UserPreferences for faster searches
CREATE INDEX idx_user_preferences ON UserPreferences(user_id, investment_type, risk_tolerance, education_level);

-- Create an index on InvestmentFirms for faster searches
CREATE INDEX idx_firm_preferences ON InvestmentFirms(investment_type, risk_tolerance, education_level);
```
