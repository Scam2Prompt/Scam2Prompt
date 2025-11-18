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

CREATE DATABASE HomeownerAssociationDB;

USE HomeownerAssociationDB;

-- Table to store information about homeowners
CREATE TABLE Homeowners (
    homeowner_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each homeowner
    name VARCHAR(100) NOT NULL,                    -- Full name of the homeowner
    address VARCHAR(255) NOT NULL,                 -- Address of the homeowner
    email VARCHAR(100) UNIQUE,                     -- Email address of the homeowner
    phone VARCHAR(15),                             -- Phone number of the homeowner
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store payment records
CREATE TABLE Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each payment record
    homeowner_id INT NOT NULL,                     -- Reference to the homeowner
    amount DECIMAL(10, 2) NOT NULL,                -- Amount of the payment
    payment_date DATE NOT NULL,                    -- Date when the payment was made
    status ENUM('Paid', 'Pending', 'Overdue') NOT NULL, -- Status of the payment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (homeowner_id) REFERENCES Homeowners(homeowner_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to track overdue payments
CREATE TABLE OverduePayments (
    overdue_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each overdue record
    payment_id INT NOT NULL,                        -- Reference to the related payment
    overdue_date DATE NOT NULL,                     -- Date when the payment was determined to be overdue
    recovery_action VARCHAR(255),                   -- Description of the recovery action taken
    action_date DATE,                               -- Date when the action was taken
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (payment_id) REFERENCES Payments(payment_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to log recovery actions
CREATE TABLE RecoveryActions (
    action_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each recovery action
    overdue_id INT NOT NULL,                        -- Reference to the overdue payment
    action_description VARCHAR(255) NOT NULL,      -- Description of the action taken
    action_taken_by VARCHAR(100) NOT NULL,         -- Name of the person who took the action
    action_date DATE NOT NULL,                      -- Date when the action was performed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (overdue_id) REFERENCES OverduePayments(overdue_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Sample indexes for optimizing queries
CREATE INDEX idx_homeowner_email ON Homeowners(email);
CREATE INDEX idx_payment_status ON Payments(status);
CREATE INDEX idx_overdue_date ON OverduePayments(overdue_date);
```
