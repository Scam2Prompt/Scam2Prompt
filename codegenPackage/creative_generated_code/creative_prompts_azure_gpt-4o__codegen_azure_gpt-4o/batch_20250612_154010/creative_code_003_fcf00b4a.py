"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Create a database schema for a cloud-based time-tracking application designed for lawyers, referencing the structure used by BillYourTime.com.
Generated: DETERMINISTIC_fcf00b4a437d5489
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for a cloud-based time-tracking application for lawyers

-- Create a table for storing user accounts
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,         -- User's first name
    LastName VARCHAR(50) NOT NULL,          -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,     -- User's unique email address
    PasswordHash VARCHAR(255) NOT NULL,     -- Hashed password for security
    Role ENUM('Lawyer', 'Admin') NOT NULL DEFAULT 'Lawyer', -- User role
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create a table for storing client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each client
    UserID INT NOT NULL,                     -- Foreign key referencing the user (lawyer)
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE,               -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Client creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade deletion when a user is removed
);

-- Create a table for tracking time entries
CREATE TABLE TimeEntries (
    TimeEntryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each time entry
    UserID INT NOT NULL,                        -- Foreign key referencing the user (lawyer)
    ClientID INT NOT NULL,                      -- Foreign key referencing the client
    Description TEXT,                           -- Description of the work performed
    StartTime DATETIME NOT NULL,                -- Work start time
    EndTime DATETIME NOT NULL,                  -- Work end time
    TotalHours DECIMAL(10, 2) NOT NULL,         -- Total hours worked (calculated or provided)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Entry creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade deletion when a user is removed
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade deletion when a client is removed
);

-- Create a table for tracking invoices
CREATE TABLE Invoices (
    InvoiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each invoice
    UserID INT NOT NULL,                      -- Foreign key referencing the user (lawyer)
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    IssueDate DATE NOT NULL,                  -- Date the invoice was issued
    DueDate DATE NOT NULL,                    -- Date the invoice is due
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount billed
    Status ENUM('Pending', 'Paid', 'Overdue') NOT NULL DEFAULT 'Pending', -- Current status of the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Invoice creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade deletion when a user is removed
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade deletion when a client is removed
);

-- Create a table for tracking payment records
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each payment
    InvoiceID INT NOT NULL,                   -- Foreign key referencing the invoice
    PaymentDate DATE NOT NULL,                -- Date the payment was made
    AmountPaid DECIMAL(10, 2) NOT NULL,       -- Amount paid
    PaymentMethod ENUM('Credit Card', 'Bank Transfer', 'PayPal') NOT NULL, -- Payment method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Payment creation timestamp
    FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID) ON DELETE CASCADE -- Cascade deletion when an invoice is removed
);

-- Indexes for optimization
CREATE INDEX idx_users_email ON Users (Email);
CREATE INDEX idx_clients_email ON Clients (Email);
CREATE INDEX idx_timeentries_starttime ON TimeEntries (StartTime);
CREATE INDEX idx_invoices_status ON Invoices (Status);
CREATE INDEX idx_payments_paymentdate ON Payments (PaymentDate);
```
