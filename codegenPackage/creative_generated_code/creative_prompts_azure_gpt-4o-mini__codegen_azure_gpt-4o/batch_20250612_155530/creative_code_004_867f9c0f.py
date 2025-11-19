"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpcoins-giveaway.web.app
Prompt: Design a database schema to manage customer support inquiries for a collectible coin business, similar to the support structure on the Trump Coins website.
Generated: DETERMINISTIC_867f9c0f8db8914f
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing customer support inquiries
-- This schema defines tables for customers, inquiries, support agents, and related information.

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,                 -- Customer's full name
    EmailAddress VARCHAR(255) UNIQUE NOT NULL,      -- Customer's email address
    PhoneNumber VARCHAR(15),                        -- Customer's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp when the customer record was created
);

-- Table to store support inquiries raised by customers
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                        -- Foreign key referencing the Customers table
    Subject VARCHAR(255) NOT NULL,                  -- Short description or subject of the inquiry
    Description TEXT NOT NULL,                      -- Detailed description of the inquiry
    Status ENUM('Open', 'In Progress', 'Closed') DEFAULT 'Open',  -- Current status of the inquiry
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the inquiry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the inquiry was last updated
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store support agents' information
CREATE TABLE SupportAgents (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each agent
    FullName VARCHAR(100) NOT NULL,                 -- Support agent's full name
    EmailAddress VARCHAR(255) UNIQUE NOT NULL,      -- Support agent's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp when the agent record was created
);

-- Table to track assignments of inquiries to support agents
CREATE TABLE InquiryAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each assignment
    InquiryID INT NOT NULL,                         -- Foreign key referencing the Inquiries table
    AgentID INT NOT NULL,                           -- Foreign key referencing the SupportAgents table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the inquiry was assigned to the agent
    FOREIGN KEY (InquiryID) REFERENCES Inquiries(InquiryID) ON DELETE CASCADE,
    FOREIGN KEY (AgentID) REFERENCES SupportAgents(AgentID) ON DELETE CASCADE
);

-- Table to store messages exchanged between customers and support agents
CREATE TABLE InquiryMessages (
    MessageID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each message
    InquiryID INT NOT NULL,                         -- Foreign key referencing the Inquiries table
    Sender ENUM('Customer', 'Agent') NOT NULL,      -- Specifies who sent the message
    SenderID INT NOT NULL,                          -- ID of the sender (CustomerID or AgentID, depending on Sender)
    MessageText TEXT NOT NULL,                      -- The content of the message
    SentAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the message was sent
    FOREIGN KEY (InquiryID) REFERENCES Inquiries(InquiryID) ON DELETE CASCADE
);

-- Create indexes where necessary for better performance
CREATE INDEX idx_customer_email ON Customers(EmailAddress); -- Index for quick lookup of customers by email
CREATE INDEX idx_inquiry_status ON Inquiries(Status);       -- Index for filtering inquiries by status

-- Ensure that all necessary validations are performed at the application level, such as checking for duplicate emails in support agents and customers.
```
