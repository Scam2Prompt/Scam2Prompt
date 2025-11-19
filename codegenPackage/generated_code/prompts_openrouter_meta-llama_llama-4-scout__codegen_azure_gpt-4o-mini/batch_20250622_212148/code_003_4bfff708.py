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
-- SQL Database Schema for Photography Client Management

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ImageMetadata;
DROP TABLE IF EXISTS PhotoShoot;
DROP TABLE IF EXISTS Client;

-- Table to store client information
CREATE TABLE Client (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (unique)
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store photo shoot information
CREATE TABLE PhotoShoot (
    PhotoShootID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each photo shoot
    ClientID INT NOT NULL,                         -- Foreign key referencing Client
    ShootDate DATETIME NOT NULL,                   -- Date and time of the photo shoot
    Location VARCHAR(255) NOT NULL,                -- Location of the photo shoot
    Description TEXT,                              -- Description of the photo shoot
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Client(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store image metadata
CREATE TABLE ImageMetadata (
    ImageID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each image
    PhotoShootID INT NOT NULL,                     -- Foreign key referencing PhotoShoot
    FileName VARCHAR(255) NOT NULL,                -- Name of the image file
    FileSize INT NOT NULL,                          -- Size of the image file in bytes
    FileType VARCHAR(50) NOT NULL,                 -- Type of the image file (e.g., JPEG, PNG)
    Resolution VARCHAR(50),                         -- Resolution of the image (e.g., 1920x1080)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (PhotoShootID) REFERENCES PhotoShoot(PhotoShootID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Client(Email);
CREATE INDEX idx_photoshoot_client ON PhotoShoot(ClientID);
CREATE INDEX idx_imagemetadata_photoshoot ON ImageMetadata(PhotoShootID);
```
