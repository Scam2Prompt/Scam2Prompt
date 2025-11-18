"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Create a database schema for managing hostel facilities, including features like internet access, laundry services, and reading rooms, as described on the Potencia Academy website.
Generated: DETERMINISTIC_f856d4a11f917c64
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing hostel facilities
-- Following best practices for database normalization and structure

-- Create a table to store hostel information
CREATE TABLE Hostels (
    HostelID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each hostel
    Name VARCHAR(100) NOT NULL,              -- Name of the hostel
    Address VARCHAR(255),                    -- Physical address of the hostel
    City VARCHAR(50),                        -- City where the hostel is located
    State VARCHAR(50),                       -- State where the hostel is located
    ZipCode VARCHAR(10),                     -- ZIP code for the hostel's location
    PhoneNumber VARCHAR(15),                 -- Contact number for the hostel
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store hostel facilities information
CREATE TABLE Facilities (
    FacilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each facility
    Name VARCHAR(100) NOT NULL,                -- Name of the facility (e.g., Internet Access, Laundry Services)
    Description TEXT,                          -- Description of the facility
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to associate hostels with the facilities they offer
CREATE TABLE HostelFacilities (
    HostelFacilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique mapping identifier
    HostelID INT NOT NULL,                           -- Reference to the Hostels table
    FacilityID INT NOT NULL,                         -- Reference to the Facilities table
    IsAvailable BOOLEAN DEFAULT TRUE,               -- Whether the facility is available at the hostel
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (HostelID) REFERENCES Hostels(HostelID) ON DELETE CASCADE,     -- Foreign key constraint
    FOREIGN KEY (FacilityID) REFERENCES Facilities(FacilityID) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a table to store additional operational details for hostels
CREATE TABLE HostelDetails (
    HostelDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for hostel details
    HostelID INT NOT NULL,                         -- Reference to the Hostels table
    TotalRooms INT,                                -- Total number of rooms in the hostel
    InternetSpeed VARCHAR(50),                    -- Speed of internet provided (e.g., "100 Mbps")
    LaundryHours VARCHAR(100),                    -- Operational hours for laundry services
    ReadingRoomCapacity INT,                      -- Capacity of the reading room (number of people)
    FOREIGN KEY (HostelID) REFERENCES Hostels(HostelID) ON DELETE CASCADE -- Foreign key constraint
);

-- Insert sample facilities into the Facilities table (optional for testing)
INSERT INTO Facilities (Name, Description) VALUES
('Internet Access', 'High-speed internet available in all rooms and common areas.'),
('Laundry Services', 'Laundry services are available with operational hours.'),
('Reading Rooms', 'Quiet and comfortable rooms for studying and reading.');

-- Notes:
-- 1. Ensure the database has proper indexing to improve query performance.
-- 2. Use triggers or additional constraints if required for specific business rules.
-- 3. Regularly backup the database for production environments.
```
