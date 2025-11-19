"""
Generated Code Metadata:
========================
Original URL: https://baamgift.info
Prompt: Design a database schema to store information about gift cards, including their types (e.g., Apple, Huawei), denominations, and expiration dates.
Generated: DETERMINISTIC_d11dfe14049009ca
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing gift card information

-- Table to store gift card types
CREATE TABLE GiftCardTypes (
    TypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each gift card type
    TypeName VARCHAR(255) NOT NULL,        -- Name of the gift card type (e.g., Apple, Huawei)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the type was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store gift card denominations
CREATE TABLE GiftCardDenominations (
    DenominationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each denomination
    Amount DECIMAL(10, 2) NOT NULL,                -- Denomination amount (e.g., 50.00, 100.00)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the denomination was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store individual gift cards
CREATE TABLE GiftCards (
    GiftCardID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each gift card
    TypeID INT NOT NULL,                       -- Foreign key referencing GiftCardTypes
    DenominationID INT NOT NULL,               -- Foreign key referencing GiftCardDenominations
    ExpirationDate DATE NOT NULL,              -- Expiration date of the gift card
    IsActive BOOLEAN DEFAULT TRUE,             -- Indicates whether the gift card is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the gift card was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (TypeID) REFERENCES GiftCardTypes(TypeID) ON DELETE CASCADE, -- Cascade delete for type
    FOREIGN KEY (DenominationID) REFERENCES GiftCardDenominations(DenominationID) ON DELETE CASCADE -- Cascade delete for denomination
);

-- Indexes for optimizing queries
CREATE INDEX idx_type_id ON GiftCards(TypeID);
CREATE INDEX idx_denomination_id ON GiftCards(DenominationID);
CREATE INDEX idx_expiration_date ON GiftCards(ExpirationDate);
```
