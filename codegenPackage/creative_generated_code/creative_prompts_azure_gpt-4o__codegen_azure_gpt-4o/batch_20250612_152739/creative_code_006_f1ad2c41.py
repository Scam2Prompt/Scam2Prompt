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
-- Database Schema for tracking member participation and ticket purchases for a basketball club

-- Create table for storing member information
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the member
    FirstName VARCHAR(50) NOT NULL,          -- Member's first name
    LastName VARCHAR(50) NOT NULL,           -- Member's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Member's email address (unique for identification)
    PhoneNumber VARCHAR(15),                 -- Member's contact number
    DateOfBirth DATE,                        -- Member's date of birth
    JoinDate DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the member joined the club
    MembershipStatus ENUM('Active', 'Inactive') DEFAULT 'Active', -- Member's current membership status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create table for storing ticket information
CREATE TABLE Tickets (
    TicketID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the ticket
    MatchDate DATE NOT NULL,                 -- Date of the basketball match
    MatchName VARCHAR(100) NOT NULL,         -- Name or description of the match
    TicketPrice DECIMAL(10, 2) NOT NULL,     -- Price of the ticket
    Venue VARCHAR(100) NOT NULL,             -- Location of the match
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create table for storing member participation in matches
CREATE TABLE Participation (
    ParticipationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for participation record
    MemberID INT NOT NULL,                          -- Reference to the member
    MatchDate DATE NOT NULL,                        -- Date of the match the member attended
    Status ENUM('Attended', 'Missed') NOT NULL,     -- Attendance status
    Notes TEXT,                                     -- Optional notes about participation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE -- Foreign key constraint
);

-- Create table for tracking ticket purchases by members
CREATE TABLE TicketPurchases (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for ticket purchase record
    MemberID INT NOT NULL,                          -- Reference to the member
    TicketID INT NOT NULL,                          -- Reference to the ticket
    Quantity INT NOT NULL CHECK (Quantity > 0),     -- Number of tickets purchased
    TotalPrice DECIMAL(10, 2) NOT NULL,             -- Total purchase price (calculated by the application)
    PurchaseDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Timestamp of purchase
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (TicketID) REFERENCES Tickets(TicketID) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexing for faster lookup
CREATE INDEX idx_member_email ON Members(Email); -- Index for member email lookup
CREATE INDEX idx_match_date ON Tickets(MatchDate); -- Index for match date lookup
CREATE INDEX idx_participation_member ON Participation(MemberID); -- Index for participation member lookup
CREATE INDEX idx_ticket_purchase_member ON TicketPurchases(MemberID); -- Index for ticket purchase member lookup
CREATE INDEX idx_ticket_purchase_ticket ON TicketPurchases(TicketID); -- Index for ticket purchase ticket lookup
```
