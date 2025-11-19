"""
Generated Code Metadata:
========================
Original URL: https://armourersandbrasiers.co.uk
Prompt: Provide an example of a database schema for tracking charitable grants awarded by the Armourers & Brasiers' Gauntlet Trust, including fields for recipient details, grant purpose, and funding amount.
Generated: DETERMINISTIC_6d44cea6f84fd7c7
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for tracking charitable grants awarded by the Armourers & Brasiers' Gauntlet Trust

-- Create a table for charitable grant recipients
CREATE TABLE Recipients (
    RecipientID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Postcode VARCHAR(20) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Phone VARCHAR(20),
    PRIMARY KEY (RecipientID)
);

-- Create a table for grant purposes
CREATE TABLE GrantPurposes (
    GrantPurposeID INT AUTO_INCREMENT,
    Purpose VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (GrantPurposeID)
);

-- Create a table for charitable grants
CREATE TABLE CharitableGrants (
    GrantID INT AUTO_INCREMENT,
    RecipientID INT NOT NULL,
    GrantPurposeID INT NOT NULL,
    GrantDate DATE NOT NULL,
    FundingAmount DECIMAL(10, 2) NOT NULL,
    GrantReference VARCHAR(255),
    PRIMARY KEY (GrantID),
    FOREIGN KEY (RecipientID) REFERENCES Recipients(RecipientID),
    FOREIGN KEY (GrantPurposeID) REFERENCES GrantPurposes(GrantPurposeID)
);

-- Create a table for grant payments
CREATE TABLE GrantPayments (
    PaymentID INT AUTO_INCREMENT,
    GrantID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (GrantID) REFERENCES CharitableGrants(GrantID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_Recipients_Name ON Recipients (Name);
CREATE INDEX idx_CharitableGrants_GrantDate ON CharitableGrants (GrantDate);
CREATE INDEX idx_CharitableGrants_RecipientID ON CharitableGrants (RecipientID);
CREATE INDEX idx_GrantPayments_GrantID ON GrantPayments (GrantID);

-- Example data insertion
DELIMITER //
CREATE PROCEDURE InsertExampleData()
BEGIN
    INSERT INTO Recipients (Name, Address, City, Postcode, Country, Email, Phone)
    VALUES 
    ('Example Recipient 1', '123 Main St', 'Anytown', 'AB1 2CD', 'United Kingdom', 'example1@example.com', '01234 567890'),
    ('Example Recipient 2', '456 Elm St', 'Othertown', 'XY3 4EF', 'United Kingdom', 'example2@example.com', '09876 543210');

    INSERT INTO GrantPurposes (Purpose, Description)
    VALUES 
    ('Education', 'Supporting educational initiatives'),
    ('Health', 'Improving healthcare services');

    INSERT INTO CharitableGrants (RecipientID, GrantPurposeID, GrantDate, FundingAmount, GrantReference)
    VALUES 
    (1, 1, '2022-01-01', 10000.00, 'G001'),
    (2, 2, '2022-06-01', 5000.00, 'G002');

    INSERT INTO GrantPayments (GrantID, PaymentDate, PaymentAmount)
    VALUES 
    (1, '2022-01-15', 5000.00),
    (1, '2022-07-15', 5000.00),
    (2, '2022-06-15', 5000.00);
END//
DELIMITER ;

-- Call the stored procedure to insert example data
CALL InsertExampleData();
```
