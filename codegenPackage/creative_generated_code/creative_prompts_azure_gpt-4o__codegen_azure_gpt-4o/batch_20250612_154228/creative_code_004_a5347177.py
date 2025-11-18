"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Create a database schema for tracking overdue payments and recovery actions for homeowner associations, similar to the recovery services mentioned on BlocPrest.
Generated: DETERMINISTIC_a5347177e2b57932
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking overdue payments and recovery actions for homeowner associations

-- Table to store homeowner information
CREATE TABLE Homeowners (
    HomeownerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each homeowner
    FirstName VARCHAR(50) NOT NULL,            -- First name of the homeowner
    LastName VARCHAR(50) NOT NULL,             -- Last name of the homeowner
    Email VARCHAR(100),                        -- Contact email for the homeowner
    PhoneNumber VARCHAR(20),                   -- Contact phone number
    Address VARCHAR(255) NOT NULL,             -- Homeowner's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store payment records
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    HomeownerID INT NOT NULL,                 -- Reference to the homeowner
    Amount DECIMAL(10, 2) NOT NULL,           -- Payment amount
    DueDate DATE NOT NULL,                    -- Due date for the payment
    PaidDate DATE,                            -- Date payment was made (nullable for overdue payments)
    Status ENUM('Pending', 'Paid', 'Overdue') DEFAULT 'Pending', -- Status of the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (HomeownerID) REFERENCES Homeowners(HomeownerID) ON DELETE CASCADE
);

-- Table to track recovery actions for overdue payments
CREATE TABLE RecoveryActions (
    ActionID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each recovery action
    PaymentID INT NOT NULL,                   -- Reference to the overdue payment
    ActionType ENUM('Reminder', 'PhoneCall', 'LegalNotice', 'Other') NOT NULL, -- Type of recovery action
    ActionDate DATE NOT NULL,                 -- Date the recovery action was taken
    Notes TEXT,                               -- Additional notes or details about the action
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PaymentID) REFERENCES Payments(PaymentID) ON DELETE CASCADE
);

-- Table to track users who manage recovery actions
CREATE TABLE RecoveryAgents (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each recovery agent
    FirstName VARCHAR(50) NOT NULL,           -- First name of the agent
    LastName VARCHAR(50) NOT NULL,            -- Last name of the agent
    Email VARCHAR(100) NOT NULL,              -- Contact email for the agent
    PhoneNumber VARCHAR(20),                  -- Contact phone number for the agent
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to log recovery actions performed by agents
CREATE TABLE AgentActions (
    AgentActionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for agent action
    ActionID INT NOT NULL,                        -- Reference to the recovery action
    AgentID INT NOT NULL,                         -- Reference to the recovery agent
    Notes TEXT,                                   -- Notes or feedback provided by the agent
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ActionID) REFERENCES RecoveryActions(ActionID) ON DELETE CASCADE,
    FOREIGN KEY (AgentID) REFERENCES RecoveryAgents(AgentID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_homeowner_payment ON Payments(HomeownerID);
CREATE INDEX idx_payment_overdue ON Payments(Status);
CREATE INDEX idx_action_date ON RecoveryActions(ActionDate);

-- Views for easy reporting
CREATE VIEW OverduePayments AS
SELECT 
    p.PaymentID,
    h.FirstName,
    h.LastName,
    h.Email,
    h.Address,
    p.Amount,
    p.DueDate,
    p.Status
FROM 
    Payments p
JOIN 
    Homeowners h ON p.HomeownerID = h.HomeownerID
WHERE 
    p.Status = 'Overdue';

CREATE VIEW RecoverySummary AS
SELECT 
    r.PaymentID,
    h.FirstName,
    h.LastName,
    r.ActionType,
    r.ActionDate,
    r.Notes
FROM 
    RecoveryActions r
JOIN 
    Payments p ON r.PaymentID = p.PaymentID
JOIN 
    Homeowners h ON p.HomeownerID = h.HomeownerID;
```
