"""
Generated Code Metadata:
========================
Original URL: https://sahlrentacar.com.tr
Prompt: Design a simple database schema to manage car rental bookings and vehicle inventory for a company operating in Turkey.
Generated: DETERMINISTIC_04522bdf97ebe7be
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a car rental company in Turkey

-- Create a table to store vehicle information
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each vehicle
    Make VARCHAR(50) NOT NULL,                 -- Manufacturer of the vehicle
    Model VARCHAR(50) NOT NULL,                -- Model of the vehicle
    Year INT NOT NULL CHECK (Year > 1885),     -- Year of manufacture, must be greater than 1885
    LicensePlate VARCHAR(20) UNIQUE NOT NULL,  -- Unique license plate number
    DailyRate DECIMAL(10, 2) NOT NULL CHECK (DailyRate > 0), -- Daily rental rate
    IsAvailable BOOLEAN DEFAULT TRUE            -- Availability status of the vehicle
);

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Customer's email address
    Phone VARCHAR(15) NOT NULL,                 -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of customer registration
);

-- Create a table to store rental bookings
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each booking
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers
    VehicleID INT NOT NULL,                      -- Foreign key referencing Vehicles
    StartDate DATE NOT NULL,                     -- Start date of the rental
    EndDate DATE NOT NULL,                       -- End date of the rental
    TotalAmount DECIMAL(10, 2) NOT NULL CHECK (TotalAmount >= 0), -- Total amount for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of booking creation
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Cascade delete for customers
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID) ON DELETE CASCADE  -- Cascade delete for vehicles
);

-- Create an index on the StartDate and EndDate for efficient querying
CREATE INDEX idx_booking_dates ON Bookings (StartDate, EndDate);

-- Create a view to show available vehicles for a given date range
CREATE VIEW AvailableVehicles AS
SELECT v.VehicleID, v.Make, v.Model, v.Year, v.LicensePlate, v.DailyRate
FROM Vehicles v
WHERE v.IsAvailable = TRUE
AND v.VehicleID NOT IN (
    SELECT VehicleID
    FROM Bookings
    WHERE (StartDate <= CURDATE() AND EndDate >= CURDATE())
);

-- Create a stored procedure to add a new booking
DELIMITER //
CREATE PROCEDURE AddBooking(
    IN p_CustomerID INT,
    IN p_VehicleID INT,
    IN p_StartDate DATE,
    IN p_EndDate DATE
)
BEGIN
    DECLARE v_DailyRate DECIMAL(10, 2);
    DECLARE v_TotalAmount DECIMAL(10, 2);
    
    -- Check if the vehicle is available
    IF (SELECT IsAvailable FROM Vehicles WHERE VehicleID = p_VehicleID) = FALSE THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Vehicle is not available for booking';
    END IF;

    -- Get the daily rate of the vehicle
    SELECT DailyRate INTO v_DailyRate FROM Vehicles WHERE VehicleID = p_VehicleID;

    -- Calculate total amount
    SET v_TotalAmount = DATEDIFF(p_EndDate, p_StartDate) * v_DailyRate;

    -- Insert the booking
    INSERT INTO Bookings (CustomerID, VehicleID, StartDate, EndDate, TotalAmount)
    VALUES (p_CustomerID, p_VehicleID, p_StartDate, p_EndDate, v_TotalAmount);

    -- Update vehicle availability
    UPDATE Vehicles SET IsAvailable = FALSE WHERE VehicleID = p_VehicleID;
END //
DELIMITER ;

-- Create a stored procedure to return a vehicle to the inventory
DELIMITER //
CREATE PROCEDURE ReturnVehicle(
    IN p_VehicleID INT
)
BEGIN
    -- Update vehicle availability
    UPDATE Vehicles SET IsAvailable = TRUE WHERE VehicleID = p_VehicleID;
END //
DELIMITER ;
```
