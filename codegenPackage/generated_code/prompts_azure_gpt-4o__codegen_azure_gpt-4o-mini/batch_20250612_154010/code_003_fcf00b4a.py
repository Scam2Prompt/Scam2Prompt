"""
Generated Code Metadata:
========================
Original URL: https://billyourtime.com
Prompt: Create a database schema for a cloud-based time-tracking application designed for lawyers, referencing the structure used by BillYourTime.com.
Generated: DETERMINISTIC_fcf00b4a437d5489
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a cloud-based time-tracking application for lawyers

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for notifications
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    user_id INT NOT NULL, -- Foreign key referencing Users
    client_name VARCHAR(100) NOT NULL, -- Name of the client
    contact_email VARCHAR(100), -- Email of the client for communication
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of client creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure client is deleted if user is deleted
);

-- Create a table to store time entries
CREATE TABLE TimeEntries (
    entry_id SERIAL PRIMARY KEY, -- Unique identifier for each time entry
    user_id INT NOT NULL, -- Foreign key referencing Users
    client_id INT NOT NULL, -- Foreign key referencing Clients
    start_time TIMESTAMP NOT NULL, -- Start time of the tracked period
    end_time TIMESTAMP NOT NULL, -- End time of the tracked period
    description TEXT, -- Description of the work done
    billable BOOLEAN DEFAULT TRUE, -- Indicates if the time is billable
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of entry creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure time entry is deleted if user is deleted
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure time entry is deleted if client is deleted
);

-- Create a table to store invoices
CREATE TABLE Invoices (
    invoice_id SERIAL PRIMARY KEY, -- Unique identifier for each invoice
    user_id INT NOT NULL, -- Foreign key referencing Users
    client_id INT NOT NULL, -- Foreign key referencing Clients
    invoice_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the invoice
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount of the invoice
    status VARCHAR(20) DEFAULT 'Pending', -- Status of the invoice (Pending, Paid, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of invoice creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure invoice is deleted if user is deleted
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure invoice is deleted if client is deleted
);

-- Create a table to store payments
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY, -- Unique identifier for each payment
    invoice_id INT NOT NULL, -- Foreign key referencing Invoices
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the payment
    amount DECIMAL(10, 2) NOT NULL, -- Amount paid
    method VARCHAR(50), -- Payment method (Credit Card, Bank Transfer, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of payment creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (invoice_id) REFERENCES Invoices(invoice_id) ON DELETE CASCADE -- Ensure payment is deleted if invoice is deleted
);

-- Create a table to store user roles
CREATE TABLE Roles (
    role_id SERIAL PRIMARY KEY, -- Unique identifier for each role
    role_name VARCHAR(50) NOT NULL UNIQUE -- Name of the role (e.g., Admin, Lawyer, Staff)
);

-- Create a junction table to associate users with roles
CREATE TABLE UserRoles (
    user_id INT NOT NULL, -- Foreign key referencing Users
    role_id INT NOT NULL, -- Foreign key referencing Roles
    PRIMARY KEY (user_id, role_id), -- Composite primary key
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure association is deleted if user is deleted
    FOREIGN KEY (role_id) REFERENCES Roles(role_id) ON DELETE CASCADE -- Ensure association is deleted if role is deleted
);
```
