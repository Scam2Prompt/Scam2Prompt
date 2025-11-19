"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: "Design a database schema for storing information about special effects equipment and their usage in events like weddings and movies."
Generated: DETERMINISTIC_6ffeb03904eb89c3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about special effects equipment and their usage in events

-- Create a table to store information about special effects equipment
CREATE TABLE Equipment (
    EquipmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each equipment
    Name VARCHAR(255) NOT NULL,                  -- Name of the equipment
    Type VARCHAR(100) NOT NULL,                  -- Type of equipment (e.g., smoke machine, lights)
    Description TEXT,                             -- Description of the equipment
    PurchaseDate DATE,                           -- Date when the equipment was purchased
    Condition ENUM('New', 'Good', 'Fair', 'Poor') NOT NULL,  -- Condition of the equipment
    LastMaintenance DATE,                        -- Date of last maintenance
    IsAvailable BOOLEAN DEFAULT TRUE             -- Availability status of the equipment
);

-- Create a table to store information about events
CREATE TABLE Events (
    EventID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each event
    EventName VARCHAR(255) NOT NULL,            -- Name of the event (e.g., wedding, movie)
    EventDate DATE NOT NULL,                     -- Date of the event
    Location VARCHAR(255),                        -- Location of the event
    Description TEXT                             -- Description of the event
);

-- Create a table to store the usage of equipment in events
CREATE TABLE EquipmentUsage (
    UsageID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each usage record
    EquipmentID INT NOT NULL,                    -- Foreign key referencing Equipment
    EventID INT NOT NULL,                        -- Foreign key referencing Events
    Quantity INT NOT NULL,                       -- Quantity of equipment used
    UsageDate DATE NOT NULL,                     -- Date when the equipment was used
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE               -- Ensures referential integrity
);

-- Create a table to store maintenance records for equipment
CREATE TABLE MaintenanceRecords (
    MaintenanceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each maintenance record
    EquipmentID INT NOT NULL,                     -- Foreign key referencing Equipment
    MaintenanceDate DATE NOT NULL,                -- Date of maintenance
    Description TEXT,                             -- Description of maintenance performed
    Cost DECIMAL(10, 2),                         -- Cost of maintenance
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table to store users who manage the equipment and events
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each user
    Username VARCHAR(100) NOT NULL UNIQUE,       -- Username for login
    PasswordHash VARCHAR(255) NOT NULL,          -- Hashed password for security
    Role ENUM('Admin', 'Manager', 'Technician') NOT NULL,  -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of user creation
);
```
