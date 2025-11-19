"""
Generated Code Metadata:
========================
Original URL: https://harmonyrecycle.net
Prompt: "Design a simple database schema for storing recycling data using MySQL."
Generated: DETERMINISTIC_4c1df8e2e2ece321
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing recycling data

-- Create a database for recycling data
CREATE DATABASE IF NOT EXISTS RecyclingDB;

-- Use the created database
USE RecyclingDB;

-- Table to store information about recycling centers
CREATE TABLE IF NOT EXISTS RecyclingCenters (
    CenterID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each recycling center
    Name VARCHAR(255) NOT NULL,              -- Name of the recycling center
    Address VARCHAR(255) NOT NULL,           -- Address of the recycling center
    City VARCHAR(100) NOT NULL,              -- City where the center is located
    State VARCHAR(100) NOT NULL,             -- State where the center is located
    ZipCode VARCHAR(10) NOT NULL,            -- Zip code of the center
    PhoneNumber VARCHAR(15),                 -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store information about recyclable materials
CREATE TABLE IF NOT EXISTS Materials (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    Name VARCHAR(100) NOT NULL,                -- Name of the material (e.g., plastic, glass)
    Description TEXT,                          -- Description of the material
    Recyclable BOOLEAN NOT NULL DEFAULT TRUE,  -- Indicates if the material is recyclable
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store recycling transactions
CREATE TABLE IF NOT EXISTS RecyclingTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    CenterID INT NOT NULL,                        -- Foreign key referencing RecyclingCenters
    MaterialID INT NOT NULL,                      -- Foreign key referencing Materials
    Quantity DECIMAL(10, 2) NOT NULL,             -- Quantity of material recycled (e.g., in kilograms)
    TransactionDate DATE NOT NULL,                -- Date of the transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (CenterID) REFERENCES RecyclingCenters(CenterID) ON DELETE CASCADE,
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID) ON DELETE CASCADE
);

-- Table to store users who interact with the recycling system
CREATE TABLE IF NOT EXISTS Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    Email VARCHAR(255) NOT NULL UNIQUE,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for authentication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store user activity related to recycling
CREATE TABLE IF NOT EXISTS UserRecyclingActivity (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity
    UserID INT NOT NULL,                       -- Foreign key referencing Users
    TransactionID INT NOT NULL,                -- Foreign key referencing RecyclingTransactions
    ActivityDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for the activity
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (TransactionID) REFERENCES RecyclingTransactions(TransactionID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_center_city ON RecyclingCenters (City);
CREATE INDEX idx_material_name ON Materials (Name);
CREATE INDEX idx_transaction_date ON RecyclingTransactions (TransactionDate);
CREATE INDEX idx_user_email ON Users (Email);
```
