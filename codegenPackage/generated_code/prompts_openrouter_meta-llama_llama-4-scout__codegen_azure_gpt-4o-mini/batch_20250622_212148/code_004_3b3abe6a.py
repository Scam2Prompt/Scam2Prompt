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

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CustomerTestimonials;
DROP TABLE IF EXISTS RepairServices;
DROP TABLE IF EXISTS CarpetTypes;
DROP TABLE IF EXISTS ContactDetails;

-- Table to store different types of carpets
CREATE TABLE CarpetTypes (
    CarpetTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each carpet type
    Name VARCHAR(100) NOT NULL,                   -- Name of the carpet type
    Material VARCHAR(100) NOT NULL,               -- Material used for the carpet
    Color VARCHAR(50),                            -- Color of the carpet
    Pattern VARCHAR(50),                          -- Pattern of the carpet
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the carpet
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the carpet type was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store repair services offered
CREATE TABLE RepairServices (
    RepairServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each repair service
    ServiceName VARCHAR(100) NOT NULL,              -- Name of the repair service
    Description TEXT,                                -- Description of the repair service
    Price DECIMAL(10, 2) NOT NULL,                  -- Price of the repair service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store customer testimonials
CREATE TABLE CustomerTestimonials (
    TestimonialID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each testimonial
    CustomerName VARCHAR(100) NOT NULL,              -- Name of the customer
    Testimonial TEXT NOT NULL,                        -- The testimonial text
    Rating INT CHECK (Rating BETWEEN 1 AND 5),       -- Rating given by the customer (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the testimonial was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store contact details for the business
CREATE TABLE ContactDetails (
    ContactID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each contact entry
    PhoneNumber VARCHAR(15) NOT NULL,                -- Phone number for contact
    Email VARCHAR(100) NOT NULL,                     -- Email address for contact
    Address VARCHAR(255) NOT NULL,                   -- Physical address for the business
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the contact was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Add foreign key constraints if necessary in future expansions
-- For example, if testimonials are linked to specific carpet types or services
-- ALTER TABLE CustomerTestimonials ADD CONSTRAINT FK_CarpetType FOREIGN KEY (CarpetTypeID) REFERENCES CarpetTypes(CarpetTypeID);
-- ALTER TABLE CustomerTestimonials ADD CONSTRAINT FK_RepairService FOREIGN KEY (RepairServiceID) REFERENCES RepairServices(RepairServiceID);
```
