"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: "Design a database schema to store property inspection data, including photos, user information, and inspection reports, for an application like App Vistoria."
Generated: DETERMINISTIC_a6dee2c7e9d8ed2f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing property inspection data

-- Table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- User's first name
    LastName VARCHAR(50) NOT NULL,         -- User's last name
    Email VARCHAR(100) NOT NULL UNIQUE,    -- User's email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store property information
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Address VARCHAR(255) NOT NULL,             -- Property address
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    State VARCHAR(100) NOT NULL,               -- State where the property is located
    ZipCode VARCHAR(20) NOT NULL,              -- Zip code of the property
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store inspection reports
CREATE TABLE Inspections (
    InspectionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each inspection
    PropertyID INT NOT NULL,                     -- Foreign key referencing the property being inspected
    UserID INT NOT NULL,                         -- Foreign key referencing the user who performed the inspection
    InspectionDate DATE NOT NULL,                -- Date of the inspection
    Notes TEXT,                                  -- Additional notes about the inspection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the inspection was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete if property is removed
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Cascade delete if user is removed
);

-- Table to store photos related to inspections
CREATE TABLE Photos (
    PhotoID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each photo
    InspectionID INT NOT NULL,              -- Foreign key referencing the inspection the photo belongs to
    PhotoURL VARCHAR(255) NOT NULL,         -- URL or path to the photo file
    Description VARCHAR(255),               -- Optional description of the photo
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the photo was uploaded
    FOREIGN KEY (InspectionID) REFERENCES Inspections(InspectionID) ON DELETE CASCADE -- Cascade delete if inspection is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_user_email ON Users(Email); -- Index for quick lookup of users by email
CREATE INDEX idx_property_address ON Properties(Address); -- Index for quick lookup of properties by address
CREATE INDEX idx_inspection_date ON Inspections(InspectionDate); -- Index for quick lookup of inspections by date
CREATE INDEX idx_photo_inspection ON Photos(InspectionID); -- Index for quick lookup of photos by inspection ID
```
