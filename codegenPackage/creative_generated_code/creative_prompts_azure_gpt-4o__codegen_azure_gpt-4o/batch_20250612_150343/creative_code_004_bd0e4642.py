"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Suggest a database schema for storing customer inquiries and service requests for Winger R&R, including fields for service type, contact details, and preferred appointment dates.
Generated: DETERMINISTIC_bd0e4642ac542dcd
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for storing customer inquiries and service requests for Winger R&R

CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each service request
    CustomerID INT NOT NULL,                          -- Foreign key referencing the Customers table
    ServiceType VARCHAR(100) NOT NULL,                -- Type of service requested (e.g., "Repair", "Maintenance")
    PreferredAppointmentDate DATE,                    -- Customer's preferred appointment date
    RequestDetails TEXT,                              -- Additional details about the request
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the service request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the service request was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the service request was last updated
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_service_type ON ServiceRequests(ServiceType);
CREATE INDEX idx_status ON ServiceRequests(Status);

-- Trigger for ensuring email addresses are in lowercase
DELIMITER $$
CREATE TRIGGER trg_lowercase_email
BEFORE INSERT ON Customers
FOR EACH ROW
BEGIN
    SET NEW.Email = LOWER(NEW.Email);
END$$
DELIMITER ;
```
