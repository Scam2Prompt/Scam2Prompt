"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azagros.com
Prompt: Create a database schema to store information about grain and fruit production, field mapping, and visit logs, ensuring compatibility with both web and mobile platforms as described on Azagros.
Generated: DETERMINISTIC_47a4a68bb43146a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for grain and fruit production, field mapping, and visit logs.

-- Table: Users
-- Stores information about users who interact with the system (e.g., farmers, inspectors).
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    Name VARCHAR(255) NOT NULL,            -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,    -- Email address for communication
    PhoneNumber VARCHAR(50),               -- Contact number of the user
    Role ENUM('Farmer', 'Inspector', 'Admin') NOT NULL, -- Role of the user in the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of user creation
);

-- Table: Fields
-- Stores information about agricultural fields.
CREATE TABLE Fields (
    FieldID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each field
    FieldName VARCHAR(255) NOT NULL,        -- Name or designation of the field
    Location POINT NOT NULL,                -- Geographical location of the field (latitude, longitude)
    Area DECIMAL(10, 2) NOT NULL,           -- Size of the field in hectares
    OwnerID INT NOT NULL,                   -- Reference to the owner of the field (UserID)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of field record creation
    FOREIGN KEY (OwnerID) REFERENCES Users(UserID) -- Enforces data integrity for owner
);

-- Table: Production
-- Stores information about grain and fruit production in fields.
CREATE TABLE Production (
    ProductionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each production record
    FieldID INT NOT NULL,                        -- Reference to the field (FieldID)
    CropType ENUM('Grain', 'Fruit') NOT NULL,    -- Type of the crop (grain or fruit)
    CropName VARCHAR(255) NOT NULL,              -- Specific name of the crop (e.g., wheat, apple)
    Quantity DECIMAL(10, 2) NOT NULL,            -- Quantity of the crop produced (in tons)
    HarvestDate DATE NOT NULL,                   -- Date of harvest
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of production record creation
    FOREIGN KEY (FieldID) REFERENCES Fields(FieldID) -- Enforces data integrity for field
);

-- Table: VisitLogs
-- Stores logs of visits to fields by inspectors or other users.
CREATE TABLE VisitLogs (
    VisitID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each visit record
    FieldID INT NOT NULL,                    -- Reference to the field (FieldID)
    InspectorID INT NOT NULL,                -- Reference to the inspector (UserID)
    VisitDate DATE NOT NULL,                 -- Date of the visit
    Notes TEXT,                              -- Notes or observations from the visit
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of visit record creation
    FOREIGN KEY (FieldID) REFERENCES Fields(FieldID), -- Enforces data integrity for field
    FOREIGN KEY (InspectorID) REFERENCES Users(UserID) -- Enforces data integrity for inspector
);

-- Index for optimizing spatial queries on the Fields table
CREATE SPATIAL INDEX idx_location ON Fields (Location);

-- Table: MobileSyncQueue
-- Queue for data synchronization with mobile platforms.
CREATE TABLE MobileSyncQueue (
    SyncID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each sync record
    TableName VARCHAR(255) NOT NULL,         -- Name of the table to be synced
    RecordID INT NOT NULL,                   -- ID of the record to be synced
    Operation ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL, -- Type of operation to sync
    Synced BOOLEAN DEFAULT FALSE,            -- Status of synchronization (true or false)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of sync record creation
);

-- Ensure all timestamp fields are compatible with web and mobile platforms.
-- Use proper indexing for efficient querying and scalability.
```
