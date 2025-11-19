"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Design a database schema to store information about hotel rooms, restaurant menus, and event planning services, similar to those offered by Saman Eventos.
Generated: DETERMINISTIC_b0596554b9c56c61
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- hotel_database_schema.sql

-- Create database
CREATE DATABASE HotelManagement;

-- Use database
USE HotelManagement;

-- Create table for hotel rooms
CREATE TABLE Rooms (
  RoomID INT AUTO_INCREMENT,
  RoomType VARCHAR(255) NOT NULL,
  RoomNumber INT NOT NULL,
  Floor INT NOT NULL,
  MaxOccupancy INT NOT NULL,
  Rate DECIMAL(10, 2) NOT NULL,
  Description TEXT,
  PRIMARY KEY (RoomID)
);

-- Create table for room amenities
CREATE TABLE RoomAmenities (
  AmenityID INT AUTO_INCREMENT,
  RoomID INT NOT NULL,
  Amenity VARCHAR(255) NOT NULL,
  PRIMARY KEY (AmenityID),
  FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
);

-- Create table for restaurant menus
CREATE TABLE Menus (
  MenuID INT AUTO_INCREMENT,
  MenuName VARCHAR(255) NOT NULL,
  Description TEXT,
  PRIMARY KEY (MenuID)
);

-- Create table for menu items
CREATE TABLE MenuItems (
  ItemID INT AUTO_INCREMENT,
  MenuID INT NOT NULL,
  ItemName VARCHAR(255) NOT NULL,
  Description TEXT,
  Price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (ItemID),
  FOREIGN KEY (MenuID) REFERENCES Menus(MenuID)
);

-- Create table for event planning services
CREATE TABLE Events (
  EventID INT AUTO_INCREMENT,
  EventType VARCHAR(255) NOT NULL,
  EventDate DATE NOT NULL,
  EventTime TIME NOT NULL,
  Location VARCHAR(255) NOT NULL,
  Description TEXT,
  PRIMARY KEY (EventID)
);

-- Create table for event services
CREATE TABLE EventServices (
  ServiceID INT AUTO_INCREMENT,
  EventID INT NOT NULL,
  ServiceType VARCHAR(255) NOT NULL,
  Description TEXT,
  PRIMARY KEY (ServiceID),
  FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

-- Create table for customers
CREATE TABLE Customers (
  CustomerID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  PRIMARY KEY (CustomerID)
);

-- Create table for bookings
CREATE TABLE Bookings (
  BookingID INT AUTO_INCREMENT,
  CustomerID INT NOT NULL,
  RoomID INT,
  EventID INT,
  BookingDate DATE NOT NULL,
  CheckIn DATE,
  CheckOut DATE,
  PRIMARY KEY (BookingID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID),
  FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

-- Create table for payments
CREATE TABLE Payments (
  PaymentID INT AUTO_INCREMENT,
  BookingID INT NOT NULL,
  PaymentDate DATE NOT NULL,
  Amount DECIMAL(10, 2) NOT NULL,
  PaymentMethod VARCHAR(255) NOT NULL,
  PRIMARY KEY (PaymentID),
  FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);

-- Indexes for performance optimization
CREATE INDEX idx_Rooms_RoomNumber ON Rooms (RoomNumber);
CREATE INDEX idx_Menus_MenuName ON Menus (MenuName);
CREATE INDEX idx_Events_EventDate ON Events (EventDate);
CREATE INDEX idx_Customers_Email ON Customers (Email);
CREATE INDEX idx_Bookings_CustomerID ON Bookings (CustomerID);
```

```sql
-- Insert sample data
INSERT INTO Rooms (RoomType, RoomNumber, Floor, MaxOccupancy, Rate, Description)
VALUES 
('Single', 101, 1, 1, 100.00, 'Single bed, private bathroom'),
('Double', 202, 2, 2, 150.00, 'Double bed, private bathroom'),
('Suite', 303, 3, 4, 300.00, 'Suite with private bathroom and balcony');

INSERT INTO RoomAmenities (RoomID, Amenity)
VALUES 
(1, 'Free Wi-Fi'),
(1, 'TV'),
(2, 'Free Wi-Fi'),
(2, 'TV'),
(3, 'Free Wi-Fi'),
(3, 'TV'),
(3, 'Balcony');

INSERT INTO Menus (MenuName, Description)
VALUES 
('Breakfast', 'Breakfast menu'),
('Lunch', 'Lunch menu'),
('Dinner', 'Dinner menu');

INSERT INTO MenuItems (MenuID, ItemName, Description, Price)
VALUES 
(1, 'Eggs', 'Scrambled eggs', 5.00),
(1, 'Pancakes', 'Buttermilk pancakes', 6.00),
(2, 'Burger', 'Beef burger', 10.00),
(2, 'Salad', 'Green salad', 8.00),
(3, 'Steak', 'Grilled steak', 20.00),
(3, 'Fish', 'Grilled fish', 18.00);

INSERT INTO Events (EventType, EventDate, EventTime, Location, Description)
VALUES 
('Wedding', '2024-06-01', '10:00:00', 'Hotel Ballroom', 'Wedding reception'),
('Conference', '2024-07-01', '09:00:00', 'Hotel Conference Room', 'Business conference');

INSERT INTO EventServices (EventID, ServiceType, Description)
VALUES 
(1, 'Catering', 'Food and beverage service'),
(1, 'Decorations', 'Event decorations'),
(2, 'Audio-Visual', 'Audio-visual equipment rental');

INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO Bookings (CustomerID, RoomID, EventID, BookingDate, CheckIn, CheckOut)
VALUES 
(1, 1, NULL, '2024-05-01', '2024-06-01', '2024-06-03'),
(2, NULL, 1, '2024-05-01', NULL, NULL);

INSERT INTO Payments (BookingID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, '2024-05-01', 200.00, 'Credit Card'),
(2, '2024-05-01', 1000.00, 'Check');
```
