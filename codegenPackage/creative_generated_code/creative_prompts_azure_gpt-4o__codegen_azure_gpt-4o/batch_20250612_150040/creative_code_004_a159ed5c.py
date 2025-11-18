"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teeny-activity-colossal.on-fleek.app
Prompt: Suggest a database design for managing comic book sales, including tracking special editions like "Top G: Parallel Protocols" and customer purchase history.
Generated: DETERMINISTIC_a159ed5c0da54875
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database design for managing comic book sales
-- Includes tracking special editions and customer purchase history

-- Table for storing comic book details
CREATE TABLE ComicBooks (
    ComicID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for the comic book
    Title VARCHAR(255) NOT NULL,                   -- Name of the comic book
    IssueNumber INT NOT NULL,                      -- Issue number
    SpecialEdition BOOLEAN DEFAULT FALSE,          -- Flag indicating if this is a special edition
    Price DECIMAL(8, 2) NOT NULL,                  -- Price of the comic book
    ReleaseDate DATE,                              -- Release date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table for storing customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the customer
    FirstName VARCHAR(100) NOT NULL,               -- Customer's first name
    LastName VARCHAR(100) NOT NULL,                -- Customer's last name
    Email VARCHAR(255) UNIQUE NOT NULL,            -- Customer's email address
    PhoneNumber VARCHAR(20),                       -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table for storing purchase history
CREATE TABLE PurchaseHistory (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the purchase
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers table
    ComicID INT NOT NULL,                          -- Foreign key referencing ComicBooks table
    Quantity INT NOT NULL,                         -- Number of copies purchased
    TotalAmount DECIMAL(10, 2) NOT NULL,           -- Total amount for the purchase
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the purchase
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ComicID) REFERENCES ComicBooks(ComicID) ON DELETE CASCADE
);

-- Table for storing special edition details (optional for extended tracking)
CREATE TABLE SpecialEditions (
    EditionID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the special edition
    ComicID INT NOT NULL,                          -- Foreign key referencing ComicBooks table
    EditionName VARCHAR(255),                      -- Name of the special edition (e.g., "Top G: Parallel Protocols")
    LimitedStock INT,                              -- Limited stock availability for the edition
    FOREIGN KEY (ComicID) REFERENCES ComicBooks(ComicID) ON DELETE CASCADE
);

-- Example indexes for optimizing queries
CREATE INDEX idx_ComicBooks_Title ON ComicBooks(Title);
CREATE INDEX idx_Customers_Email ON Customers(Email);
CREATE INDEX idx_PurchaseHistory_CustomerID ON PurchaseHistory(CustomerID);
CREATE INDEX idx_PurchaseHistory_ComicID ON PurchaseHistory(ComicID);

-- Example triggers for auditing (optional)
DELIMITER //
CREATE TRIGGER trg_UpdateComicTimestamp BEFORE UPDATE ON ComicBooks
FOR EACH ROW
BEGIN
    SET NEW.UpdatedAt = CURRENT_TIMESTAMP; -- Automatically update the timestamp on changes
END;
//
DELIMITER ;
```
