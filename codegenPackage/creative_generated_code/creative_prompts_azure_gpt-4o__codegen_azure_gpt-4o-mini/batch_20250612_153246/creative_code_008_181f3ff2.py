"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dextranslogistics.com
Prompt: Create a database schema to store customer feedback and testimonials for Dextrans Logistics, highlighting their competitive pricing and service quality.
Generated: DETERMINISTIC_181f3ff20a8becdf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing customer feedback and testimonials for Dextrans Logistics

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,           -- Full name of the customer
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Email address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store feedback and testimonials
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each feedback entry
    CustomerID INT NOT NULL,                   -- Foreign key referencing the Customers table
    FeedbackText TEXT NOT NULL,                -- The content of the feedback/testimonial
    Rating INT CHECK (Rating >= 1 AND Rating <= 5), -- Rating value between 1 and 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the Feedback table to improve query performance
CREATE INDEX idx_feedback_customer ON Feedback(CustomerID);

-- Insert sample customer data (for testing purposes)
INSERT INTO Customers (FullName, Email) VALUES 
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com');

-- Insert sample feedback data (for testing purposes)
INSERT INTO Feedback (CustomerID, FeedbackText, Rating) VALUES 
(1, 'Excellent service and competitive pricing!', 5),
(2, 'Very satisfied with the quality of service.', 4);
```
