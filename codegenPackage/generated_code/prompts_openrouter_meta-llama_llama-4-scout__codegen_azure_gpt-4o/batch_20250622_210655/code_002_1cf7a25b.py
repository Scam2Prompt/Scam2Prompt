"""
Generated Code Metadata:
========================
Original URL: https://bandadorada.com
Prompt: Generate a sample database schema for managing client information, event details, and payment records for an orchestra service like Orquesta Dorada.
Generated: DETERMINISTIC_1cf7a25b2f1c2d1d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Orquesta Dorada

-- Table: Clients
-- Stores information about clients who book the orchestra service
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Events
-- Stores details about events where the orchestra performs
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each event
    ClientID INT NOT NULL,                   -- Foreign key referencing the Clients table
    EventName VARCHAR(100) NOT NULL,         -- Name of the event
    EventDate DATE NOT NULL,                 -- Date of the event
    EventTime TIME NOT NULL,                 -- Time of the event
    Location TEXT NOT NULL,                  -- Location of the event
    NumberOfPerformers INT NOT NULL,         -- Number of performers required for the event
    TotalCost DECIMAL(10, 2) NOT NULL,       -- Total cost for the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table: Payments
-- Stores payment records for events
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    EventID INT NOT NULL,                     -- Foreign key referencing the Events table
    PaymentDate DATE NOT NULL,                -- Date of the payment
    AmountPaid DECIMAL(10, 2) NOT NULL,       -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Bank Transfer', 'Cash') NOT NULL, -- Payment method
    PaymentStatus ENUM('Pending', 'Completed', 'Failed') NOT NULL,       -- Status of the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_event_date ON Events(EventDate); -- Index for quick lookup by event date
CREATE INDEX idx_payment_status ON Payments(PaymentStatus); -- Index for quick lookup by payment status
```
