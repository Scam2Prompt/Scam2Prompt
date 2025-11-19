"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: "Design a database schema for storing and managing home design plans, including rooms, furniture, and decoration elements, for a blog like this one."
Generated: DETERMINISTIC_b90e2118e969856c
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing and managing home design plans

-- Table to store information about design plans
CREATE TABLE DesignPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each design plan
    PlanName VARCHAR(255) NOT NULL,        -- Name of the design plan
    Description TEXT,                      -- Description of the design plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the plan was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the plan was last updated
);

-- Table to store information about rooms in a design plan
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each room
    PlanID INT NOT NULL,                   -- Foreign key referencing DesignPlans
    RoomName VARCHAR(255) NOT NULL,        -- Name of the room
    RoomType ENUM('Living Room', 'Bedroom', 'Kitchen', 'Bathroom', 'Office', 'Other') NOT NULL, -- Type of the room
    Dimensions VARCHAR(255),               -- Dimensions of the room (e.g., "12x15 ft")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the room was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the room was last updated
    FOREIGN KEY (PlanID) REFERENCES DesignPlans(PlanID) ON DELETE CASCADE -- Cascade delete if the design plan is deleted
);

-- Table to store information about furniture in a room
CREATE TABLE Furniture (
    FurnitureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each furniture item
    RoomID INT NOT NULL,                        -- Foreign key referencing Rooms
    FurnitureName VARCHAR(255) NOT NULL,        -- Name of the furniture item
    FurnitureType VARCHAR(255),                 -- Type of furniture (e.g., "Sofa", "Table", "Chair")
    Material VARCHAR(255),                      -- Material of the furniture (e.g., "Wood", "Metal")
    Dimensions VARCHAR(255),                    -- Dimensions of the furniture (e.g., "6x3 ft")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the furniture was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the furniture was last updated
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Cascade delete if the room is deleted
);

-- Table to store information about decoration elements in a room
CREATE TABLE Decorations (
    DecorationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each decoration element
    RoomID INT NOT NULL,                         -- Foreign key referencing Rooms
    DecorationName VARCHAR(255) NOT NULL,        -- Name of the decoration element
    DecorationType VARCHAR(255),                 -- Type of decoration (e.g., "Painting", "Vase", "Curtains")
    Material VARCHAR(255),                       -- Material of the decoration (e.g., "Glass", "Ceramic")
    Dimensions VARCHAR(255),                     -- Dimensions of the decoration (e.g., "2x3 ft")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the decoration was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the decoration was last updated
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Cascade delete if the room is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_plan_name ON DesignPlans(PlanName);
CREATE INDEX idx_room_name ON Rooms(RoomName);
CREATE INDEX idx_furniture_name ON Furniture(FurnitureName);
CREATE INDEX idx_decoration_name ON Decorations(DecorationName);
```
