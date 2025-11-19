"""
Generated Code Metadata:
========================
Original URL: https://terminaltunja.com
Prompt: Create a SQL database schema to store information about the Terminal Tunja's services, including descriptions, schedules, and contact details.
Generated: DETERMINISTIC_12eacb1c41d14d07
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Terminal Tunja's Services

-- Create a database named 'TerminalTunja'
CREATE DATABASE TerminalTunja;

-- Use the newly created database
USE TerminalTunja;

-- Table to store service categories (e.g., transportation, food, etc.)
CREATE TABLE ServiceCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,        -- Name of the category
    Description TEXT                           -- Optional description of the category
);

-- Table to store services offered at the terminal
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service
    Description TEXT,                          -- Optional description of the service
    Schedule VARCHAR(255),                     -- Schedule information (e.g., hours of operation)
    ContactDetails VARCHAR(255),               -- Contact details (e.g., phone, email)
    CategoryID INT NOT NULL,                   -- Foreign key to ServiceCategories
    FOREIGN KEY (CategoryID) REFERENCES ServiceCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store feedback or reviews for services
CREATE TABLE ServiceFeedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    ServiceID INT NOT NULL,                    -- Foreign key to Services
    UserName VARCHAR(100),                     -- Name of the user providing feedback
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating (1 to 5 scale)
    Comments TEXT,                             -- Optional comments from the user
    FeedbackDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of feedback
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Insert sample data into ServiceCategories
INSERT INTO ServiceCategories (CategoryName, Description)
VALUES 
('Transportation', 'Services related to bus and taxi transportation.'),
('Food & Beverage', 'Restaurants, cafes, and food stalls.'),
('Retail', 'Shops and stores for passengers.'),
('Other', 'Miscellaneous services.');

-- Insert sample data into Services
INSERT INTO Services (ServiceName, Description, Schedule, ContactDetails, CategoryID)
VALUES 
('Bus Service', 'Intercity and local bus transportation.', '24/7', 'contact@busservice.com', 1),
('Taxi Service', 'Taxi services available at the terminal.', '24/7', 'contact@taxiservice.com', 1),
('Coffee Shop', 'Fresh coffee and snacks.', '6:00 AM - 10:00 PM', 'contact@coffeeshop.com', 2),
('Gift Shop', 'Souvenirs and gifts for travelers.', '8:00 AM - 8:00 PM', 'contact@giftshop.com', 3);

-- Query to verify the schema and sample data
SELECT * FROM ServiceCategories;
SELECT * FROM Services;
SELECT * FROM ServiceFeedback;
```
