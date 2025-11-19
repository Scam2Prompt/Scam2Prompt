"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: Write a SQL query to retrieve customer feedback and service requests for plumbing issues, focusing on the types of services offered by a plumbing company in the central region.
Generated: DETERMINISTIC_4f16aab2e918e393
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve customer feedback and service requests for plumbing issues
-- in the central region, focusing on types of services offered

-- Create a sample database schema for demonstration purposes
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Region VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS ServiceRequests (
    ServiceRequestID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    ServiceType VARCHAR(100) NOT NULL,
    IssueDescription TEXT NOT NULL,
    RequestDate DATE NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE IF NOT EXISTS Feedback (
    FeedbackID INT PRIMARY KEY,
    ServiceRequestID INT NOT NULL,
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    Comment TEXT,
    FOREIGN KEY (ServiceRequestID) REFERENCES ServiceRequests(ServiceRequestID)
);

-- Insert sample data for demonstration purposes
INSERT INTO Customers (CustomerID, Name, Email, Region)
VALUES
(1, 'John Doe', 'john.doe@example.com', 'Central'),
(2, 'Jane Smith', 'jane.smith@example.com', 'Central'),
(3, 'Bob Johnson', 'bob.johnson@example.com', 'Eastern');

INSERT INTO ServiceRequests (ServiceRequestID, CustomerID, ServiceType, IssueDescription, RequestDate)
VALUES
(1, 1, 'Plumbing Repair', 'Leaky faucet', '2022-01-01'),
(2, 1, 'Drain Cleaning', 'Clogged drain', '2022-01-15'),
(3, 2, 'Toilet Installation', 'New toilet installation', '2022-02-01'),
(4, 3, 'Plumbing Repair', 'Burst pipe', '2022-03-01');

INSERT INTO Feedback (FeedbackID, ServiceRequestID, Rating, Comment)
VALUES
(1, 1, 4, 'Good service, but a bit pricey'),
(2, 2, 5, 'Excellent service, very professional'),
(3, 3, 3, 'Average service, could be improved');

-- SQL query to retrieve customer feedback and service requests
SELECT 
    c.CustomerID,
    c.Name,
    c.Region,
    sr.ServiceType,
    sr.IssueDescription,
    sr.RequestDate,
    f.Rating,
    f.Comment
FROM 
    Customers c
INNER JOIN 
    ServiceRequests sr ON c.CustomerID = sr.CustomerID
LEFT JOIN 
    Feedback f ON sr.ServiceRequestID = f.ServiceRequestID
WHERE 
    c.Region = 'Central'
    AND sr.ServiceType IN ('Plumbing Repair', 'Drain Cleaning', 'Toilet Installation', 'Pipe Installation', 'Water Heater Repair')
ORDER BY 
    sr.RequestDate DESC;
```
