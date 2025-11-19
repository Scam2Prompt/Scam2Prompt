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
-- Database Schema for Special Effects Equipment and Usage in Events

-- Table to store information about special effects equipment
CREATE TABLE SpecialEffectsEquipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each equipment
    Name VARCHAR(255) NOT NULL,                 -- Name of the equipment
    Type VARCHAR(255) NOT NULL,                 -- Type/category of the equipment (e.g., lighting, pyrotechnics)
    Manufacturer VARCHAR(255),                  -- Manufacturer of the equipment
    PurchaseDate DATE,                          -- Date the equipment was purchased
    Cost DECIMAL(10, 2),                        -- Cost of the equipment
    IsAvailable BOOLEAN DEFAULT TRUE,           -- Availability status of the equipment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each event
    Name VARCHAR(255) NOT NULL,                 -- Name of the event
    EventType VARCHAR(255) NOT NULL,            -- Type of the event (e.g., wedding, movie, concert)
    EventDate DATE NOT NULL,                    -- Date of the event
    Location VARCHAR(255) NOT NULL,             -- Location of the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store the usage of special effects equipment in events
CREATE TABLE EquipmentUsage (
    UsageID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each usage record
    EquipmentID INT NOT NULL,                   -- Foreign key referencing SpecialEffectsEquipment
    EventID INT NOT NULL,                       -- Foreign key referencing Events
    Quantity INT NOT NULL,                      -- Quantity of equipment used
    Notes TEXT,                                 -- Additional notes about the usage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (EquipmentID) REFERENCES SpecialEffectsEquipment(EquipmentID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_equipment_type ON SpecialEffectsEquipment(Type); -- Index on equipment type
CREATE INDEX idx_event_type ON Events(EventType);                 -- Index on event type
CREATE INDEX idx_equipment_event ON EquipmentUsage(EquipmentID, EventID); -- Composite index for equipment usage

-- Error handling and constraints
-- Ensure that quantity in EquipmentUsage is always positive
ALTER TABLE EquipmentUsage
ADD CONSTRAINT chk_quantity_positive CHECK (Quantity > 0);

-- Ensure that cost in SpecialEffectsEquipment is always non-negative
ALTER TABLE SpecialEffectsEquipment
ADD CONSTRAINT chk_cost_non_negative CHECK (Cost >= 0);
```
