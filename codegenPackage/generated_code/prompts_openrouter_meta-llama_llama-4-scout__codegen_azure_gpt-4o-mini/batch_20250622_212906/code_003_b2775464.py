"""
Generated Code Metadata:
========================
Original URL: https://mesogia.com
Prompt: Create a SQL query to populate a database with business listings and categories from a local business directory like Mesogia.
Generated: DETERMINISTIC_b2775464b99097af
Batch ID: 20250622_212906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create tables for business listings and categories
-- and populate them with data from a local business directory

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Businesses;

-- Create a table for business categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the category was created
);

-- Create a table for businesses
CREATE TABLE Businesses (
    BusinessID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each business
    BusinessName VARCHAR(255) NOT NULL,         -- Name of the business
    Address VARCHAR(255) NOT NULL,               -- Address of the business
    Phone VARCHAR(20),                           -- Phone number of the business
    Email VARCHAR(255),                          -- Email address of the business
    CategoryID INT,                              -- Foreign key referencing Categories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the business was created
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)  -- Establish foreign key relationship
);

-- Insert sample categories into the Categories table
INSERT INTO Categories (CategoryName) VALUES
('Restaurants'),
('Shopping'),
('Health & Beauty'),
('Automotive'),
('Entertainment'),
('Services');

-- Insert sample businesses into the Businesses table
INSERT INTO Businesses (BusinessName, Address, Phone, Email, CategoryID) VALUES
('The Great Restaurant', '123 Food St, Mesogia', '555-1234', 'info@greatrestaurant.com', 1),
('Best Shop', '456 Shop Ave, Mesogia', '555-5678', 'contact@bestshop.com', 2),
('Health First Clinic', '789 Health Blvd, Mesogia', '555-8765', 'info@healthfirst.com', 3),
('Auto Repair Experts', '321 Car Rd, Mesogia', '555-4321', 'support@autorepair.com', 4),
('Fun Zone', '654 Fun St, Mesogia', '555-3456', 'info@funzone.com', 5),
('Home Services Co.', '987 Service St, Mesogia', '555-6543', 'contact@homeservices.com', 6);

-- Query to verify the data has been inserted correctly
SELECT * FROM Categories;
SELECT * FROM Businesses;
```
