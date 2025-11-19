"""
Generated Code Metadata:
========================
Original URL: https://elon.live
Prompt: Design a database schema to store information about marijuana users, growers, and distributors under a decriminalization program, including fields for user fees and possession limits.
Generated: DETERMINISTIC_1145c32be7f1e63d
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about marijuana users, growers, and distributors
-- under a decriminalization program.

-- Table to store information about users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,        -- Full name of the user
    DateOfBirth DATE NOT NULL,             -- Date of birth of the user
    Address VARCHAR(255),                  -- Address of the user
    Email VARCHAR(255) UNIQUE,             -- Email address of the user
    PhoneNumber VARCHAR(15),               -- Phone number of the user
    UserFee DECIMAL(10, 2) NOT NULL,       -- Fee paid by the user
    PossessionLimit DECIMAL(10, 2) NOT NULL, -- Maximum possession limit in grams
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date of registration
);

-- Table to store information about growers
CREATE TABLE Growers (
    GrowerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each grower
    FullName VARCHAR(255) NOT NULL,          -- Full name of the grower
    BusinessName VARCHAR(255),               -- Name of the grower's business
    LicenseNumber VARCHAR(50) UNIQUE NOT NULL, -- Unique license number
    Address VARCHAR(255),                    -- Address of the grower
    Email VARCHAR(255) UNIQUE,               -- Email address of the grower
    PhoneNumber VARCHAR(15),                 -- Phone number of the grower
    ProductionCapacity DECIMAL(10, 2) NOT NULL, -- Maximum production capacity in kilograms
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date of registration
);

-- Table to store information about distributors
CREATE TABLE Distributors (
    DistributorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each distributor
    FullName VARCHAR(255) NOT NULL,               -- Full name of the distributor
    BusinessName VARCHAR(255),                    -- Name of the distributor's business
    LicenseNumber VARCHAR(50) UNIQUE NOT NULL,    -- Unique license number
    Address VARCHAR(255),                         -- Address of the distributor
    Email VARCHAR(255) UNIQUE,                    -- Email address of the distributor
    PhoneNumber VARCHAR(15),                      -- Phone number of the distributor
    DistributionCapacity DECIMAL(10, 2) NOT NULL, -- Maximum distribution capacity in kilograms
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date of registration
);

-- Table to store transactions between users, growers, and distributors
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key referencing Users table
    GrowerID INT,                                 -- Foreign key referencing Growers table
    DistributorID INT,                            -- Foreign key referencing Distributors table
    Amount DECIMAL(10, 2) NOT NULL,               -- Amount of marijuana in grams
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (GrowerID) REFERENCES Growers(GrowerID) ON DELETE SET NULL,
    FOREIGN KEY (DistributorID) REFERENCES Distributors(DistributorID) ON DELETE SET NULL
);

-- Table to store possession limits and fees for different user categories
CREATE TABLE UserCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Medical", "Recreational")
    PossessionLimit DECIMAL(10, 2) NOT NULL,   -- Maximum possession limit in grams
    UserFee DECIMAL(10, 2) NOT NULL            -- Fee associated with the category
);

-- Table to associate users with specific categories
CREATE TABLE UserCategoryMapping (
    MappingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each mapping
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    CategoryID INT NOT NULL,                  -- Foreign key referencing UserCategories table
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (CategoryID) REFERENCES UserCategories(CategoryID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_users_email ON Users(Email);
CREATE INDEX idx_growers_license ON Growers(LicenseNumber);
CREATE INDEX idx_distributors_license ON Distributors(LicenseNumber);
CREATE INDEX idx_transactions_user ON Transactions(UserID);
CREATE INDEX idx_user_category_mapping ON UserCategoryMapping(UserID, CategoryID);
```
