"""
Generated Code Metadata:
========================
Original URL: https://roc-remi.com
Prompt: Design a database schema for storing information about vacation rentals like Chalet Roc Remi, including details about the property, rooms, activities, and guest reviews.
Generated: DETERMINISTIC_5e898c3579abe4ea
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about vacation rentals

-- Table to store property details
CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the property
    Name VARCHAR(255) NOT NULL,                -- Name of the property
    Description TEXT,                          -- Description of the property
    Address VARCHAR(255) NOT NULL,             -- Address of the property
    City VARCHAR(100) NOT NULL,                -- City where the property is located
    State VARCHAR(100),                        -- State where the property is located
    Country VARCHAR(100) NOT NULL,             -- Country where the property is located
    ZipCode VARCHAR(20),                       -- Zip code of the property
    Latitude DECIMAL(10, 8),                   -- Latitude for geolocation
    Longitude DECIMAL(11, 8),                  -- Longitude for geolocation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store room details for each property
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the room
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    Name VARCHAR(255) NOT NULL,               -- Name of the room
    Description TEXT,                         -- Description of the room
    Capacity INT NOT NULL,                    -- Maximum number of guests the room can accommodate
    PricePerNight DECIMAL(10, 2) NOT NULL,    -- Price per night for the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the room was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete if property is deleted
);

-- Table to store activities available at the property
CREATE TABLE Activities (
    ActivityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the activity
    PropertyID INT NOT NULL,                   -- Foreign key referencing Properties table
    Name VARCHAR(255) NOT NULL,                -- Name of the activity
    Description TEXT,                          -- Description of the activity
    Price DECIMAL(10, 2),                      -- Price for the activity (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the activity was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete if property is deleted
);

-- Table to store guest reviews for properties
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the review
    PropertyID INT NOT NULL,                  -- Foreign key referencing Properties table
    GuestName VARCHAR(255) NOT NULL,          -- Name of the guest who left the review
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the guest (1 to 5)
    Comment TEXT,                             -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was added
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Cascade delete if property is deleted
);

-- Table to store images for properties and rooms
CREATE TABLE Images (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the image
    PropertyID INT,                           -- Foreign key referencing Properties table
    RoomID INT,                               -- Foreign key referencing Rooms table
    ImageURL VARCHAR(255) NOT NULL,           -- URL of the image
    Description TEXT,                         -- Description of the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the image was added
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE, -- Cascade delete if property is deleted
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Cascade delete if room is deleted
);

-- Table to store bookings for rooms
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the booking
    RoomID INT NOT NULL,                      -- Foreign key referencing Rooms table
    GuestName VARCHAR(255) NOT NULL,          -- Name of the guest who made the booking
    CheckInDate DATE NOT NULL,                -- Check-in date
    CheckOutDate DATE NOT NULL,               -- Check-out date
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was made
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID) ON DELETE CASCADE -- Cascade delete if room is deleted
);
```
