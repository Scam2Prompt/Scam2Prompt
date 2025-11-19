"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spanglerroofingllc.com
Prompt: Design a database schema using SQL for storing customer reviews and service requests for a roofing company, focusing on fields like customer name, service type, and satisfaction rating.
Generated: DETERMINISTIC_bb34b21a6b88fed9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing customer reviews and service requests for a roofing company

-- Table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the customer
    FirstName VARCHAR(50) NOT NULL,               -- Customer's first name
    LastName VARCHAR(50) NOT NULL,                -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,           -- Customer's email address
    PhoneNumber VARCHAR(15),                      -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table for storing service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for the service request
    CustomerID INT NOT NULL,                      -- Foreign key referencing the Customers table
    ServiceType VARCHAR(100) NOT NULL,            -- Type of service requested (e.g., roof repair, installation)
    RequestDate DATE NOT NULL,                    -- Date of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    Notes TEXT,                                   -- Additional notes about the request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service request was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure data integrity
);

-- Table for storing customer reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the review
    CustomerID INT NOT NULL,                      -- Foreign key referencing the Customers table
    RequestID INT NOT NULL,                       -- Foreign key referencing the ServiceRequests table
    SatisfactionRating INT CHECK(SatisfactionRating BETWEEN 1 AND 5), -- Satisfaction rating (scale 1-5)
    ReviewText TEXT,                              -- Detailed review from the customer
    ReviewDate DATE NOT NULL,                     -- Date when the review was submitted
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure data integrity
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE -- Ensure data integrity
);

-- Indexing for faster query performance
CREATE INDEX idx_customers_name ON Customers (FirstName, LastName);
CREATE INDEX idx_service_requests_status ON ServiceRequests (Status);
CREATE INDEX idx_reviews_rating ON Reviews (SatisfactionRating);
```
