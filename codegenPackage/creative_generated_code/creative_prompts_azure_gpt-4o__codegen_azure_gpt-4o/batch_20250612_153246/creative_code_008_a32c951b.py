"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Suggest a database schema for storing property details and client reviews, inspired by the structure of the Dominguez Parra website.
Generated: DETERMINISTIC_a32c951b2266d2ce
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing property details and client reviews

-- Table: Properties
-- Stores details about different properties listed on the platform
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each property
    Name VARCHAR(255) NOT NULL,                      -- Name of the property
    Description TEXT,                                -- Detailed description of the property
    Location VARCHAR(255) NOT NULL,                 -- Location of the property
    Price DECIMAL(10, 2) NOT NULL,                  -- Price of the property
    PropertyType ENUM('Apartment', 'House', 'Villa', 'Studio', 'Other') NOT NULL, -- Type of the property
    Bedrooms INT NOT NULL,                          -- Number of bedrooms
    Bathrooms INT NOT NULL,                         -- Number of bathrooms
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the property was added
    UpdatedAt DATETIME ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for the last update
);

-- Table: Reviews
-- Stores client reviews for properties
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each review
    PropertyID INT NOT NULL,                        -- Foreign key to the Properties table
    ClientName VARCHAR(255) NOT NULL,               -- Name of the client leaving the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),      -- Rating given by the client (1 to 5)
    Comment TEXT,                                   -- Optional comment left by the client
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the review was added
    UpdatedAt DATETIME ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Relationship to Properties table
);

-- Table: Images
-- Stores images related to properties
CREATE TABLE Images (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each image
    PropertyID INT NOT NULL,                        -- Foreign key to the Properties table
    ImageURL VARCHAR(2083) NOT NULL,                -- URL of the image
    Description VARCHAR(255),                       -- Optional description of the image
    UploadedAt DATETIME DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the image was uploaded
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Relationship to Properties table
);

-- Additional indexes for performance optimization
CREATE INDEX idx_property_location ON Properties(Location); -- Index for searching properties by location
CREATE INDEX idx_review_property_id ON Reviews(PropertyID);  -- Index for searching reviews by property
CREATE INDEX idx_image_property_id ON Images(PropertyID);    -- Index for searching images by property
```
