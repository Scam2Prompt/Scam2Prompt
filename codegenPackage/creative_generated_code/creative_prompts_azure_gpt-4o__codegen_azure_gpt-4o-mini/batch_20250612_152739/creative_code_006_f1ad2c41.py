"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Design a database schema for tracking member participation and ticket purchases for a basketball club, referencing the membership and ticketing details from "Grad košarke."
Generated: DETERMINISTIC_f1ad2c41c6c9c72b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking member participation and ticket purchases for a basketball club

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS TicketPurchases;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS Events;

-- Table to store member details
CREATE TABLE Members (
    MemberID SERIAL PRIMARY KEY,          -- Unique identifier for each member
    FirstName VARCHAR(50) NOT NULL,      -- Member's first name
    LastName VARCHAR(50) NOT NULL,       -- Member's last name
    Email VARCHAR(100) UNIQUE NOT NULL,  -- Member's email (unique)
    Phone VARCHAR(15),                    -- Member's phone number (optional)
    JoinDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Date when member joined
);

-- Table to store event details
CREATE TABLE Events (
    EventID SERIAL PRIMARY KEY,           -- Unique identifier for each event
    EventName VARCHAR(100) NOT NULL,     -- Name of the event (e.g., game name)
    EventDate TIMESTAMP NOT NULL,         -- Date and time of the event
    Location VARCHAR(100) NOT NULL        -- Location of the event
);

-- Table to track ticket purchases by members
CREATE TABLE TicketPurchases (
    PurchaseID SERIAL PRIMARY KEY,        -- Unique identifier for each ticket purchase
    MemberID INT NOT NULL,                -- Reference to the member making the purchase
    EventID INT NOT NULL,                 -- Reference to the event for which the ticket is purchased
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of the purchase
    TicketQuantity INT NOT NULL CHECK (TicketQuantity > 0),  -- Quantity of tickets purchased
    TotalAmount DECIMAL(10, 2) NOT NULL, -- Total amount of the purchase

    -- Foreign key constraints
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE,
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE
);

-- Sample data insertion

-- Inserting sample members
INSERT INTO Members (FirstName, LastName, Email, Phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

-- Inserting sample events
INSERT INTO Events (EventName, EventDate, Location) VALUES
('Championship Game', '2023-12-01 18:00:00', 'Main Arena'),
('Season Opener', '2023-10-15 19:00:00', 'Community Center');

-- Inserting sample ticket purchases
INSERT INTO TicketPurchases (MemberID, EventID, TicketQuantity, TotalAmount) VALUES
(1, 1, 2, 50.00),
(2, 2, 1, 25.00);
```
