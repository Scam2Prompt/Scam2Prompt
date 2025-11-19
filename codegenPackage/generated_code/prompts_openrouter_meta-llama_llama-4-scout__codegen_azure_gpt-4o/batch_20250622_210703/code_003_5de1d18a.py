"""
Generated Code Metadata:
========================
Original URL: https://visitabroadtravels.com.np
Prompt: "Design a database schema for storing travel packages, customer information, and booking details for a company like Visit Abroad Travels, with entities like packages, customers, guides, and lodges."
Generated: DETERMINISTIC_5de1d18a1f7027f0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Visit Abroad Travels

-- Table to store travel packages
CREATE TABLE Packages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each package
    PackageName VARCHAR(255) NOT NULL,        -- Name of the travel package
    Description TEXT,                         -- Detailed description of the package
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the package
    DurationDays INT NOT NULL,                -- Duration of the package in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store booking details
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    CustomerID INT NOT NULL,                  -- Foreign key referencing Customers table
    PackageID INT NOT NULL,                   -- Foreign key referencing Packages table
    BookingDate DATE NOT NULL,                -- Date of the booking
    NumberOfPeople INT NOT NULL,              -- Number of people included in the booking
    TotalAmount DECIMAL(10, 2) NOT NULL,      -- Total amount for the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Booking status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the booking was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE
);

-- Table to store guides information
CREATE TABLE Guides (
    GuideID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each guide
    FirstName VARCHAR(100) NOT NULL,        -- Guide's first name
    LastName VARCHAR(100) NOT NULL,         -- Guide's last name
    Email VARCHAR(255) UNIQUE NOT NULL,     -- Guide's email address
    PhoneNumber VARCHAR(15),                -- Guide's phone number
    ExperienceYears INT NOT NULL,           -- Number of years of experience
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the guide was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store lodges information
CREATE TABLE Lodges (
    LodgeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each lodge
    LodgeName VARCHAR(255) NOT NULL,        -- Name of the lodge
    Location VARCHAR(255) NOT NULL,         -- Location of the lodge
    Capacity INT NOT NULL,                  -- Maximum capacity of the lodge
    PricePerNight DECIMAL(10, 2) NOT NULL,  -- Price per night for the lodge
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the lodge was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to associate guides with packages
CREATE TABLE PackageGuides (
    PackageGuideID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    PackageID INT NOT NULL,                        -- Foreign key referencing Packages table
    GuideID INT NOT NULL,                          -- Foreign key referencing Guides table
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE,
    FOREIGN KEY (GuideID) REFERENCES Guides(GuideID) ON DELETE CASCADE
);

-- Table to associate lodges with packages
CREATE TABLE PackageLodges (
    PackageLodgeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    PackageID INT NOT NULL,                        -- Foreign key referencing Packages table
    LodgeID INT NOT NULL,                          -- Foreign key referencing Lodges table
    FOREIGN KEY (PackageID) REFERENCES Packages(PackageID) ON DELETE CASCADE,
    FOREIGN KEY (LodgeID) REFERENCES Lodges(LodgeID) ON DELETE CASCADE
);
```
