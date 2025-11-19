"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Create a SQL database schema to store information about carpet types, repair services, customer testimonials, and contact details, similar to Perfect Melbourne Carpet's database.
Generated: DETERMINISTIC_3b3abe6a4de95858
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Carpet Types, Repair Services, Customer Testimonials, and Contact Details

-- Create a database
CREATE DATABASE CarpetServiceDB;

-- Use the created database
USE CarpetServiceDB;

-- Table to store carpet types
CREATE TABLE CarpetTypes (
    CarpetID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each carpet type
    Name VARCHAR(100) NOT NULL,              -- Name of the carpet type
    Material VARCHAR(100),                   -- Material of the carpet
    PricePerSquareMeter DECIMAL(10, 2),      -- Price per square meter
    Description TEXT,                        -- Description of the carpet type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store repair services
CREATE TABLE RepairServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(100) NOT NULL,               -- Name of the repair service
    Price DECIMAL(10, 2),                     -- Price of the service
    DurationInHours INT,                      -- Estimated duration in hours
    Description TEXT,                         -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store customer testimonials
CREATE TABLE CustomerTestimonials (
    TestimonialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each testimonial
    CustomerName VARCHAR(100) NOT NULL,           -- Name of the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating (1 to 5)
    Comments TEXT,                                -- Customer's comments
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store contact details
CREATE TABLE ContactDetails (
    ContactID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contact
    Name VARCHAR(100) NOT NULL,               -- Name of the contact person
    Email VARCHAR(100) NOT NULL,              -- Email address
    PhoneNumber VARCHAR(15),                  -- Phone number
    Message TEXT,                             -- Message from the contact
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Add indexes for faster queries where appropriate
CREATE INDEX idx_CarpetTypes_Name ON CarpetTypes (Name);
CREATE INDEX idx_RepairServices_Name ON RepairServices (Name);
CREATE INDEX idx_CustomerTestimonials_CustomerName ON CustomerTestimonials (CustomerName);
CREATE INDEX idx_ContactDetails_Email ON ContactDetails (Email);

-- Ensure proper foreign key relationships if needed in the future
-- For example, linking testimonials to services or carpets can be added later
```
