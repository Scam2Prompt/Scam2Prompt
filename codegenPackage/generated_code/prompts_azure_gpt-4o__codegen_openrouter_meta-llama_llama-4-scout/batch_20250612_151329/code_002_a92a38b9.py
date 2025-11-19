"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Provide an example of a database schema for a Property Management System (PMS) in hotel operations, based on the concepts taught in Hampton's Hotel Institute's Hotel Operations Management course.
Generated: DETERMINISTIC_a92a38b986cfc740
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the Property Management System
CREATE DATABASE HotelPMS;

-- Use the HotelPMS database
USE HotelPMS;

-- Create a table for hotels
CREATE TABLE Hotels (
    HotelID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20),
    Email VARCHAR(100),
    PRIMARY KEY (HotelID)
);

-- Create a table for rooms
CREATE TABLE Rooms (
    RoomID INT AUTO_INCREMENT,
    HotelID INT NOT NULL,
    RoomType VARCHAR(50) NOT NULL,
    RoomNumber INT NOT NULL,
    MaxOccupancy INT NOT NULL,
    Rate DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (RoomID),
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID)
);

-- Create a table for room amenities
CREATE TABLE RoomAmenities (
    AmenityID INT AUTO_INCREMENT,
    RoomID INT NOT NULL,
    Amenity VARCHAR(100) NOT NULL,
    PRIMARY KEY (AmenityID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
);

-- Create a table for guests
CREATE TABLE Guests (
    GuestID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    PostalCode VARCHAR(20),
    PRIMARY KEY (GuestID)
);

-- Create a table for reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT,
    GuestID INT NOT NULL,
    HotelID INT NOT NULL,
    RoomID INT NOT NULL,
    ArrivalDate DATE NOT NULL,
    DepartureDate DATE NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Pending', 'Confirmed', 'CheckedIn', 'CheckedOut', 'Cancelled')),
    PRIMARY KEY (ReservationID),
    FOREIGN KEY (GuestID) REFERENCES Guests(GuestID),
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID),
    FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
);

-- Create a table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    ReservationID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(100) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID)
);

-- Create a table for employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Phone VARCHAR(20),
    Role VARCHAR(50) NOT NULL CHECK (Role IN ('Manager', 'FrontDesk', 'Housekeeping', 'Maintenance')),
    HotelID INT,
    PRIMARY KEY (EmployeeID),
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID)
);

-- Create a table for check-ins
CREATE TABLE CheckIns (
    CheckInID INT AUTO_INCREMENT,
    ReservationID INT NOT NULL,
    CheckInDate DATE NOT NULL,
    RoomKey VARCHAR(50) NOT NULL,
    EmployeeID INT NOT NULL,
    PRIMARY KEY (CheckInID),
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Create a table for check-outs
CREATE TABLE CheckOuts (
    CheckOutID INT AUTO_INCREMENT,
    ReservationID INT NOT NULL,
    CheckOutDate DATE NOT NULL,
    Bill DECIMAL(10, 2) NOT NULL,
    EmployeeID INT NOT NULL,
    PRIMARY KEY (CheckOutID),
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Insert some sample data
INSERT INTO Hotels (Name, Address, City, State, Country, PostalCode, Phone, Email)
VALUES 
('Hotel A', '123 Main St', 'New York', 'NY', 'USA', '10001', '123-456-7890', 'info@hotela.com'),
('Hotel B', '456 Park Ave', 'Los Angeles', 'CA', 'USA', '90001', '987-654-3210', 'info@hotelb.com');

INSERT INTO Rooms (HotelID, RoomType, RoomNumber, MaxOccupancy, Rate)
VALUES 
(1, 'Single', 101, 1, 100.00),
(1, 'Double', 102, 2, 150.00),
(2, 'Suite', 201, 4, 300.00);

INSERT INTO RoomAmenities (RoomID, Amenity)
VALUES 
(1, 'Free Wi-Fi'),
(1, 'Flat-screen TV'),
(2, 'Free Wi-Fi'),
(2, 'Minibar');

INSERT INTO Guests (FirstName, LastName, Email, Phone, Address, City, State, Country, PostalCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'New York', 'NY', 'USA', '10001'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Park Ave', 'Los Angeles', 'CA', 'USA', '90001');

INSERT INTO Reservations (GuestID, HotelID, RoomID, ArrivalDate, DepartureDate, Status)
VALUES 
(1, 1, 1, '2024-01-01', '2024-01-03', 'Confirmed'),
(2, 2, 3, '2024-02-01', '2024-02-03', 'Pending');

INSERT INTO Payments (ReservationID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, '2024-01-01', 200.00, 'Credit Card'),
(2, '2024-01-15', 100.00, 'Cash');

INSERT INTO Employees (FirstName, LastName, Email, Phone, Role, HotelID)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '123-456-7890', 'FrontDesk', 1),
('Alice', 'Williams', 'alice.williams@example.com', '987-654-3210', 'Manager', 2);

INSERT INTO CheckIns (ReservationID, CheckInDate, RoomKey, EmployeeID)
VALUES 
(1, '2024-01-01', 'RoomKey123', 1);

INSERT INTO CheckOuts (ReservationID, CheckOutDate, Bill, EmployeeID)
VALUES 
(1, '2024-01-03', 250.00, 1);
```
