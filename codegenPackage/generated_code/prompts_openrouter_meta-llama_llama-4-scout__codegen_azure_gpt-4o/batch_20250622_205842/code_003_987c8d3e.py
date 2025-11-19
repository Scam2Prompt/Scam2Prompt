"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: "Design a database schema to store information about coworking spaces, including their location, infrastructure, and available plans, using a relational database management system."
Generated: DETERMINISTIC_987c8d3e619d590b
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about coworking spaces

-- Table to store coworking space details
CREATE TABLE CoworkingSpaces (
    SpaceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each coworking space
    Name VARCHAR(255) NOT NULL,             -- Name of the coworking space
    Description TEXT,                       -- Description of the coworking space
    Address VARCHAR(255) NOT NULL,          -- Address of the coworking space
    City VARCHAR(100) NOT NULL,             -- City where the coworking space is located
    State VARCHAR(100) NOT NULL,            -- State where the coworking space is located
    Country VARCHAR(100) NOT NULL,          -- Country where the coworking space is located
    ZipCode VARCHAR(20),                    -- Zip code of the coworking space
    Latitude DECIMAL(9,6),                  -- Latitude for geolocation
    Longitude DECIMAL(9,6),                 -- Longitude for geolocation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table to store infrastructure details for each coworking space
CREATE TABLE Infrastructure (
    InfrastructureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each infrastructure item
    SpaceID INT NOT NULL,                            -- Foreign key referencing CoworkingSpaces
    FeatureName VARCHAR(255) NOT NULL,              -- Name of the infrastructure feature (e.g., WiFi, Meeting Rooms)
    Description TEXT,                                -- Description of the feature
    IsAvailable BOOLEAN DEFAULT TRUE,               -- Whether the feature is available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (SpaceID) REFERENCES CoworkingSpaces(SpaceID) ON DELETE CASCADE
);

-- Table to store available plans for each coworking space
CREATE TABLE Plans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each plan
    SpaceID INT NOT NULL,                           -- Foreign key referencing CoworkingSpaces
    PlanName VARCHAR(255) NOT NULL,                -- Name of the plan (e.g., Daily Pass, Monthly Membership)
    Price DECIMAL(10,2) NOT NULL,                  -- Price of the plan
    Currency VARCHAR(10) NOT NULL,                 -- Currency of the price (e.g., USD, EUR)
    Description TEXT,                               -- Description of the plan
    IsActive BOOLEAN DEFAULT TRUE,                 -- Whether the plan is currently active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the record was last updated
    FOREIGN KEY (SpaceID) REFERENCES CoworkingSpaces(SpaceID) ON DELETE CASCADE
);

-- Table to store reviews for coworking spaces
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each review
    SpaceID INT NOT NULL,                          -- Foreign key referencing CoworkingSpaces
    ReviewerName VARCHAR(255),                    -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),     -- Rating given by the reviewer (1 to 5)
    Comments TEXT,                                 -- Review comments
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (SpaceID) REFERENCES CoworkingSpaces(SpaceID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_space_city ON CoworkingSpaces (City);
CREATE INDEX idx_space_state ON CoworkingSpaces (State);
CREATE INDEX idx_space_country ON CoworkingSpaces (Country);
CREATE INDEX idx_plan_space ON Plans (SpaceID);
CREATE INDEX idx_infrastructure_space ON Infrastructure (SpaceID);
CREATE INDEX idx_review_space ON Reviews (SpaceID);
```
