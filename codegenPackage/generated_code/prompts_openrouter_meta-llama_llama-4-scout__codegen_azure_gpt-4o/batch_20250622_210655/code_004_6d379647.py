"""
Generated Code Metadata:
========================
Original URL: https://www.propertyshare.net
Prompt: "Design a database schema to store property information for a real estate marketing platform similar to Property Share in Egypt."
Generated: DETERMINISTIC_6d37964722d5781f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a real estate marketing platform

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FullName VARCHAR(100) NOT NULL,        -- Full name of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Email address of the user
    PasswordHash VARCHAR(255) NOT NULL,    -- Hashed password for security
    PhoneNumber VARCHAR(15),               -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store property information
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Title VARCHAR(255) NOT NULL,               -- Title or name of the property
    Description TEXT NOT NULL,                 -- Detailed description of the property
    Price DECIMAL(15, 2) NOT NULL,             -- Price of the property
    Location VARCHAR(255) NOT NULL,            -- Location of the property
    PropertyType ENUM('Apartment', 'Villa', 'Office', 'Land') NOT NULL, -- Type of property
    Bedrooms INT,                              -- Number of bedrooms
    Bathrooms INT,                             -- Number of bathrooms
    Area DECIMAL(10, 2),                       -- Area of the property in square meters
    ListedBy INT NOT NULL,                     -- Foreign key referencing Users table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of property listing
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (ListedBy) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store property images
CREATE TABLE PropertyImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each image
    PropertyID INT NOT NULL,                -- Foreign key referencing Properties table
    ImageURL VARCHAR(255) NOT NULL,         -- URL of the image
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of image upload
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete if property is removed
);

-- Table to store inquiries about properties
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inquiry
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    Message TEXT NOT NULL,                    -- Inquiry message
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of inquiry creation
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete if property is removed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store saved properties (favorites)
CREATE TABLE SavedProperties (
    SavedID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each saved property entry
    UserID INT NOT NULL,                    -- Foreign key referencing Users table
    PropertyID INT NOT NULL,                -- Foreign key referencing Properties table
    SavedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of saving the property
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete if user is removed
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete if property is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_properties_location ON Properties(Location); -- Index for location-based searches
CREATE INDEX idx_properties_price ON Properties(Price);       -- Index for price-based searches
CREATE INDEX idx_properties_type ON Properties(PropertyType); -- Index for type-based searches
```
