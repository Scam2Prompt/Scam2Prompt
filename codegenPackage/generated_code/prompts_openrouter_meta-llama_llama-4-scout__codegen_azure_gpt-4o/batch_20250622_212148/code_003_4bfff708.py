"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Create a SQL database schema to manage photography client information, photo shoots, and image metadata for a studio like Officine dell'Immagine.
Generated: DETERMINISTIC_4bfff7088c3059b3
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for managing photography client information, photo shoots, and image metadata

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client was added
);

-- Create a table to store photo shoot information
CREATE TABLE PhotoShoots (
    ShootID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each photo shoot
    ClientID INT NOT NULL,                   -- Foreign key referencing the client
    ShootDate DATE NOT NULL,                 -- Date of the photo shoot
    Location VARCHAR(100),                   -- Location of the photo shoot
    Notes TEXT,                              -- Additional notes about the photo shoot
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the shoot was added
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Create a table to store image metadata
CREATE TABLE Images (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each image
    ShootID INT NOT NULL,                    -- Foreign key referencing the photo shoot
    FilePath VARCHAR(255) NOT NULL,          -- Path to the image file
    FileName VARCHAR(100) NOT NULL,          -- Name of the image file
    Resolution VARCHAR(50),                  -- Resolution of the image (e.g., "1920x1080")
    Format VARCHAR(10),                      -- File format (e.g., "JPEG", "PNG")
    SizeInBytes BIGINT,                      -- Size of the image file in bytes
    Tags TEXT,                               -- Tags or keywords associated with the image
    UploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was uploaded
    FOREIGN KEY (ShootID) REFERENCES PhotoShoots(ShootID) ON DELETE CASCADE -- Cascade delete if shoot is removed
);

-- Create indexes for faster queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for quick lookups
CREATE INDEX idx_shoot_date ON PhotoShoots(ShootDate); -- Index on shoot date for quick filtering
CREATE INDEX idx_image_filepath ON Images(FilePath); -- Index on file path for quick access

-- Error handling and constraints
-- Ensure email format is valid (example for MySQL)
ALTER TABLE Clients ADD CONSTRAINT chk_email_format CHECK (Email LIKE '%@%.%');

-- Ensure image resolution follows a valid format (example for MySQL)
ALTER TABLE Images ADD CONSTRAINT chk_resolution_format CHECK (Resolution REGEXP '^[0-9]+x[0-9]+$');
```
