"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Generate SQL queries to track and optimize revenue management in hotel operations, referencing the Hampton's Hotel Institute's Hotel Operations Management curriculum.
Generated: DETERMINISTIC_4ad00b15a02b144e
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for hotel operations management
CREATE DATABASE HotelOperations;

-- Use the HotelOperations database
USE HotelOperations;

-- Create a table for hotel information
CREATE TABLE Hotels (
    HotelID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    PRIMARY KEY (HotelID)
);

-- Create a table for room types
CREATE TABLE RoomTypes (
    RoomTypeID INT AUTO_INCREMENT,
    HotelID INT NOT NULL,
    RoomType VARCHAR(100) NOT NULL,
    Rate DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    PRIMARY KEY (RoomTypeID),
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID)
);

-- Create a table for room availability
CREATE TABLE RoomAvailability (
    RoomAvailabilityID INT AUTO_INCREMENT,
    RoomTypeID INT NOT NULL,
    RoomNumber INT NOT NULL,
    IsAvailable BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (RoomAvailabilityID),
    FOREIGN KEY (RoomTypeID) REFERENCES RoomTypes(RoomTypeID)
);

-- Create a table for bookings
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT,
    RoomAvailabilityID INT NOT NULL,
    GuestName VARCHAR(255) NOT NULL,
    ArrivalDate DATE NOT NULL,
    DepartureDate DATE NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (RoomAvailabilityID) REFERENCES RoomAvailability(
        RoomAvailabilityID
    )
);

-- Create a table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    BookingID INT NOT NULL,
    PaymentMethod VARCHAR(100) NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);

-- Procedure to add a new hotel
DELIMITER //
CREATE PROCEDURE AddHotel(
    IN p_Name VARCHAR(255),
    IN p_Address VARCHAR(255),
    IN p_City VARCHAR(100),
    IN p_State VARCHAR(100),
    IN p_Country VARCHAR(100),
    IN p_PostalCode VARCHAR(20)
)
BEGIN
    INSERT INTO Hotels (Name, Address, City, State, Country, PostalCode)
    VALUES (p_Name, p_Address, p_City, p_State, p_Country, p_PostalCode);
END//
DELIMITER ;

-- Procedure to add a new room type
DELIMITER //
CREATE PROCEDURE AddRoomType(
    IN p_HotelID INT,
    IN p_RoomType VARCHAR(100),
    IN p_Rate DECIMAL(10, 2),
    IN p_Description TEXT
)
BEGIN
    INSERT INTO RoomTypes (HotelID, RoomType, Rate, Description)
    VALUES (p_HotelID, p_RoomType, p_Rate, p_Description);
END//
DELIMITER ;

-- Procedure to book a room
DELIMITER //
CREATE PROCEDURE BookRoom(
    IN p_RoomTypeID INT,
    IN p_GuestName VARCHAR(255),
    IN p_ArrivalDate DATE,
    IN p_DepartureDate DATE
)
BEGIN
    DECLARE roomAvailabilityID INT;
    DECLARE roomRate DECIMAL(10, 2);

    -- Check if room is available
    SELECT RoomAvailabilityID INTO roomAvailabilityID
    FROM RoomAvailability
    WHERE RoomTypeID = p_RoomTypeID AND IsAvailable = TRUE
    LIMIT 1;

    IF roomAvailabilityID IS NOT NULL THEN
        -- Get room rate
        SELECT Rate INTO roomRate
        FROM RoomTypes
        WHERE RoomTypeID = p_RoomTypeID;

        -- Calculate total cost
        DECLARE totalCost DECIMAL(10, 2);
        SET totalCost = roomRate * DATEDIFF(p_DepartureDate, p_ArrivalDate);

        -- Insert booking
        INSERT INTO Bookings (RoomAvailabilityID, GuestName, ArrivalDate, DepartureDate, TotalCost)
        VALUES (roomAvailabilityID, p_GuestName, p_ArrivalDate, p_DepartureDate, totalCost);

        -- Update room availability
        UPDATE RoomAvailability
        SET IsAvailable = FALSE
        WHERE RoomAvailabilityID = roomAvailabilityID;

        SELECT 'Room booked successfully' AS Message;
    ELSE
        SELECT 'Room not available' AS Message;
    END IF;
END//
DELIMITER ;

-- Procedure to make a payment
DELIMITER //
CREATE PROCEDURE MakePayment(
    IN p_BookingID INT,
    IN p_PaymentMethod VARCHAR(100),
    IN p_PaymentDate DATE,
    IN p_Amount DECIMAL(10, 2)
)
BEGIN
    INSERT INTO Payments (BookingID, PaymentMethod, PaymentDate, Amount)
    VALUES (p_BookingID, p_PaymentMethod, p_PaymentDate, p_Amount);
END//
DELIMITER ;

-- Query to get hotel revenue
DELIMITER //
CREATE PROCEDURE GetHotelRevenue(
    IN p_HotelID INT
)
BEGIN
    SELECT 
        SUM(b.TotalCost) AS TotalRevenue
    FROM 
        Bookings b
    JOIN 
        RoomAvailability ra ON b.RoomAvailabilityID = ra.RoomAvailabilityID
    JOIN 
        RoomTypes rt ON ra.RoomTypeID = rt.RoomTypeID
    WHERE 
        rt.HotelID = p_HotelID;
END//
DELIMITER ;

-- Query to get room occupancy rate
DELIMITER //
CREATE PROCEDURE GetRoomOccupancyRate(
    IN p_HotelID INT
)
BEGIN
    DECLARE totalRooms INT;
    DECLARE occupiedRooms INT;

    SELECT 
        COUNT(*) INTO totalRooms
    FROM 
        RoomAvailability ra
    JOIN 
        RoomTypes rt ON ra.RoomTypeID = rt.RoomTypeID
    WHERE 
        rt.HotelID = p_HotelID;

    SELECT 
        COUNT(DISTINCT b.RoomAvailabilityID) INTO occupiedRooms
    FROM 
        Bookings b
    JOIN 
        RoomAvailability ra ON b.RoomAvailabilityID = ra.RoomAvailabilityID
    JOIN 
        RoomTypes rt ON ra.RoomTypeID = rt.RoomTypeID
    WHERE 
        rt.HotelID = p_HotelID;

    SELECT 
        (occupiedRooms / totalRooms) * 100 AS OccupancyRate;
END//
DELIMITER ;
```
