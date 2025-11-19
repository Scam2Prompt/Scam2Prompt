"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Create a database schema for tracking overdue payments and recovery actions for homeowner associations, similar to the recovery services mentioned on BlocPrest.
Generated: DETERMINISTIC_a5347177e2b57932
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking overdue payments and recovery actions for homeowner associations

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS RecoveryActions;
DROP TABLE IF EXISTS Payments;
DROP TABLE IF EXISTS Homeowners;

-- Table to store information about homeowners
CREATE TABLE Homeowners (
    homeowner_id SERIAL PRIMARY KEY, -- Unique identifier for each homeowner
    name VARCHAR(100) NOT NULL, -- Homeowner's name
    address VARCHAR(255) NOT NULL, -- Homeowner's address
    email VARCHAR(100) UNIQUE NOT NULL, -- Homeowner's email address
    phone VARCHAR(15), -- Homeowner's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store payment records
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY, -- Unique identifier for each payment
    homeowner_id INT NOT NULL, -- Foreign key referencing Homeowners
    amount DECIMAL(10, 2) NOT NULL, -- Amount of the payment
    payment_date DATE NOT NULL, -- Date of the payment
    status VARCHAR(20) CHECK (status IN ('Paid', 'Overdue')) DEFAULT 'Paid', -- Payment status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (homeowner_id) REFERENCES Homeowners(homeowner_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store recovery actions taken for overdue payments
CREATE TABLE RecoveryActions (
    action_id SERIAL PRIMARY KEY, -- Unique identifier for each recovery action
    payment_id INT NOT NULL, -- Foreign key referencing Payments
    action_type VARCHAR(50) NOT NULL, -- Type of recovery action (e.g., 'Notice', 'Call', 'Legal Action')
    action_date DATE NOT NULL, -- Date the action was taken
    notes TEXT, -- Additional notes regarding the action
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (payment_id) REFERENCES Payments(payment_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_homeowner_email ON Homeowners(email);
CREATE INDEX idx_payment_status ON Payments(status);
CREATE INDEX idx_recovery_action_type ON RecoveryActions(action_type);
```
