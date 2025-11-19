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
-- Database schema for managing home design plans

-- Create a table for storing information about rooms
CREATE TABLE Rooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each room
    RoomName VARCHAR(100) NOT NULL,         -- Name of the room (e.g., Living Room, Kitchen)
    RoomSize VARCHAR(50),                    -- Size of the room (e.g., 12x15 ft)
    DesignPlanID INT,                        -- Foreign key to link to a design plan
    FOREIGN KEY (DesignPlanID) REFERENCES DesignPlans(DesignPlanID) ON DELETE CASCADE
);

-- Create a table for storing information about furniture
CREATE TABLE Furniture (
    FurnitureID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each piece of furniture
    FurnitureName VARCHAR(100) NOT NULL,         -- Name of the furniture (e.g., Sofa, Table)
    FurnitureType VARCHAR(50),                    -- Type of furniture (e.g., Seating, Table)
    RoomID INT,                                   -- Foreign key to link to a room
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE
);

-- Create a table for storing decoration elements
CREATE TABLE Decorations (
    DecorationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each decoration
    DecorationName VARCHAR(100) NOT NULL,         -- Name of the decoration (e.g., Painting, Vase)
    DecorationType VARCHAR(50),                    -- Type of decoration (e.g., Wall Art, Accessory)
    RoomID INT,                                    -- Foreign key to link to a room
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE
);

-- Create a table for storing design plans
CREATE TABLE DesignPlans (
    DesignPlanID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each design plan
    PlanName VARCHAR(100) NOT NULL,               -- Name of the design plan
    Description TEXT,                              -- Description of the design plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the design plan was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for storing user information (optional, for blog functionality)
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,         -- Unique username for the user
    Email VARCHAR(100) NOT NULL UNIQUE,           -- Unique email address for the user
    PasswordHash VARCHAR(255) NOT NULL,           -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the user was created
);

-- Create a table for storing user comments on design plans (optional)
CREATE TABLE Comments (
    CommentID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each comment
    UserID INT,                                   -- Foreign key to link to a user
    DesignPlanID INT,                             -- Foreign key to link to a design plan
    CommentText TEXT NOT NULL,                    -- The text of the comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the comment was created
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (DesignPlanID) REFERENCES DesignPlans(DesignPlanID) ON DELETE CASCADE
);
```
