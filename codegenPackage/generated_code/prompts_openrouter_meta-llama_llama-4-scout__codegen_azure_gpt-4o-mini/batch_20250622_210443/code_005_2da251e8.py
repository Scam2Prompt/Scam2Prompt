"""
Generated Code Metadata:
========================
Original URL: https://ittastours.com
Prompt: "Design a database schema for storing information about tour packages, destinations, and activities for a travel company specializing in Egypt and the Middle East."
Generated: DETERMINISTIC_2da251e8397912b4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a travel company specializing in Egypt and the Middle East

-- Create a table for storing information about tour packages
CREATE TABLE TourPackages (
    PackageID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each tour package
    PackageName VARCHAR(255) NOT NULL,         -- Name of the tour package
    Description TEXT,                           -- Description of the tour package
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the tour package
    Duration INT NOT NULL,                      -- Duration of the tour in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table for storing information about destinations
CREATE TABLE Destinations (
    DestinationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each destination
    DestinationName VARCHAR(255) NOT NULL,         -- Name of the destination
    Description TEXT,                               -- Description of the destination
    Country VARCHAR(100) NOT NULL,                 -- Country where the destination is located
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the destination was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table for storing activities associated with tour packages
CREATE TABLE Activities (
    ActivityID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each activity
    ActivityName VARCHAR(255) NOT NULL,            -- Name of the activity
    Description TEXT,                               -- Description of the activity
    Duration INT NOT NULL,                          -- Duration of the activity in hours
    PackageID INT,                                  -- Foreign key referencing the TourPackages table
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,  -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the activity was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a junction table to associate destinations with tour packages
CREATE TABLE PackageDestinations (
    PackageID INT,                                  -- Foreign key referencing the TourPackages table
    DestinationID INT,                              -- Foreign key referencing the Destinations table
    PRIMARY KEY (PackageID, DestinationID),        -- Composite primary key
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,               -- Customer's first name
    LastName VARCHAR(100) NOT NULL,                 -- Customer's last name
    Email VARCHAR(255) NOT NULL UNIQUE,             -- Customer's email address
    Phone VARCHAR(20),                              -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the customer was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table for storing bookings made by customers
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each booking
    CustomerID INT,                                 -- Foreign key referencing the Customers table
    PackageID INT,                                  -- Foreign key referencing the TourPackages table
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the booking
    NumberOfPeople INT NOT NULL,                    -- Number of people in the booking
    TotalPrice DECIMAL(10, 2) NOT NULL,            -- Total price for the booking
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (PackageID) REFERENCES TourPackages(PackageID) ON DELETE CASCADE  -- Ensures referential integrity
);
```
