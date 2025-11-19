"""
Generated Code Metadata:
========================
Original URL: https://2ms.pt
Prompt: "Design a simple database schema for storing property information similar to what is presented on 2ms.pt, including fields for address, city, and contact details."
Generated: DETERMINISTIC_ad9e8fad320d7684
Batch ID: 20250622_204855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing property information

-- Create a table to store property details
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Address VARCHAR(255) NOT NULL,             -- Street address of the property
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    State VARCHAR(100) NOT NULL,               -- State where the property is located
    ZipCode VARCHAR(20) NOT NULL,              -- ZIP code of the property
    ContactName VARCHAR(100),                  -- Name of the contact person for the property
    ContactPhone VARCHAR(20),                  -- Phone number of the contact person
    ContactEmail VARCHAR(100),                 -- Email address of the contact person
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to store additional property features (optional)
CREATE TABLE PropertyFeatures (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each feature
    PropertyID INT NOT NULL,                   -- Foreign key linking to the Properties table
    FeatureName VARCHAR(100) NOT NULL,         -- Name of the feature (e.g., "Pool", "Garage")
    FeatureValue VARCHAR(255),                 -- Value of the feature (e.g., "Yes", "2-car")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Ensure features are deleted if the property is deleted
);

-- Create a table to store property images (optional)
CREATE TABLE PropertyImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    PropertyID INT NOT NULL,                   -- Foreign key linking to the Properties table
    ImageURL VARCHAR(255) NOT NULL,            -- URL of the image
    Description VARCHAR(255),                  -- Optional description of the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Ensure images are deleted if the property is deleted
);

-- Indexes for faster querying
CREATE INDEX idx_city ON Properties (City);    -- Index for querying properties by city
CREATE INDEX idx_contact_email ON Properties (ContactEmail); -- Index for querying properties by contact email
```
