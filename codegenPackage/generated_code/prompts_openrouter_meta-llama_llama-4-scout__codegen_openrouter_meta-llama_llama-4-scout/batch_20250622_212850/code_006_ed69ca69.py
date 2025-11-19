"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Write a SQL query to manage Junk in The Box ATL's dumpster rental inventory, including tracking rentals, deliveries, and pickups in their service areas.
Generated: DETERMINISTIC_ed69ca69017a940e
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Junk in The Box ATL's dumpster rental inventory
CREATE TABLE ServiceAreas (
    ServiceAreaID INT PRIMARY KEY,
    City VARCHAR(255) NOT NULL,
    State VARCHAR(255) NOT NULL,
    ZipCode VARCHAR(255) NOT NULL
);

CREATE TABLE DumpsterSizes (
    DumpsterSizeID INT PRIMARY KEY,
    Size VARCHAR(255) NOT NULL,
    Capacity DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Rentals (
    RentalID INT PRIMARY KEY,
    CustomerName VARCHAR(255) NOT NULL,
    ServiceAreaID INT NOT NULL,
    DumpsterSizeID INT NOT NULL,
    RentalDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (ServiceAreaID) REFERENCES ServiceAreas(ServiceAreaID),
    FOREIGN KEY (DumpsterSizeID) REFERENCES DumpsterSizes(DumpsterSizeID)
);

CREATE TABLE Deliveries (
    DeliveryID INT PRIMARY KEY,
    RentalID INT NOT NULL,
    DeliveryDate DATE NOT NULL,
    DeliveryAddress VARCHAR(255) NOT NULL,
    FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID)
);

CREATE TABLE Pickups (
    PickupID INT PRIMARY KEY,
    RentalID INT NOT NULL,
    PickupDate DATE NOT NULL,
    PickupAddress VARCHAR(255) NOT NULL,
    FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID)
);

-- Insert sample data into tables
INSERT INTO ServiceAreas (ServiceAreaID, City, State, ZipCode)
VALUES 
(1, 'Atlanta', 'GA', '30301'),
(2, 'Marietta', 'GA', '30060'),
(3, 'Decatur', 'GA', '30030');

INSERT INTO DumpsterSizes (DumpsterSizeID, Size, Capacity)
VALUES 
(1, '10 Yard', 10.0),
(2, '20 Yard', 20.0),
(3, '30 Yard', 30.0);

INSERT INTO Rentals (RentalID, CustomerName, ServiceAreaID, DumpsterSizeID, RentalDate, ReturnDate)
VALUES 
(1, 'John Doe', 1, 1, '2022-01-01', '2022-01-15'),
(2, 'Jane Smith', 2, 2, '2022-02-01', '2022-02-20'),
(3, 'Bob Johnson', 3, 3, '2022-03-01', NULL);

INSERT INTO Deliveries (DeliveryID, RentalID, DeliveryDate, DeliveryAddress)
VALUES 
(1, 1, '2022-01-01', '123 Main St, Atlanta, GA 30301'),
(2, 2, '2022-02-01', '456 Elm St, Marietta, GA 30060'),
(3, 3, '2022-03-01', '789 Oak St, Decatur, GA 30030');

INSERT INTO Pickups (PickupID, RentalID, PickupDate, PickupAddress)
VALUES 
(1, 1, '2022-01-15', '123 Main St, Atlanta, GA 30301'),
(2, NULL, NULL, NULL);

-- Procedure to track rentals
CREATE PROCEDURE TrackRental
    @CustomerName VARCHAR(255),
    @ServiceAreaID INT,
    @DumpsterSizeID INT,
    @RentalDate DATE,
    @ReturnDate DATE
AS
BEGIN
    INSERT INTO Rentals (CustomerName, ServiceAreaID, DumpsterSizeID, RentalDate, ReturnDate)
    VALUES (@CustomerName, @ServiceAreaID, @DumpsterSizeID, @RentalDate, @ReturnDate);
END;

-- Procedure to track deliveries
CREATE PROCEDURE TrackDelivery
    @RentalID INT,
    @DeliveryDate DATE,
    @DeliveryAddress VARCHAR(255)
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Rentals WHERE RentalID = @RentalID)
    BEGIN
        INSERT INTO Deliveries (RentalID, DeliveryDate, DeliveryAddress)
        VALUES (@RentalID, @DeliveryDate, @DeliveryAddress);
    END
    ELSE
    BEGIN
        RAISERROR ('Rental not found', 16, 1);
    END
END;

-- Procedure to track pickups
CREATE PROCEDURE TrackPickup
    @RentalID INT,
    @PickupDate DATE,
    @PickupAddress VARCHAR(255)
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Rentals WHERE RentalID = @RentalID)
    BEGIN
        IF NOT EXISTS (SELECT 1 FROM Pickups WHERE RentalID = @RentalID)
        BEGIN
            INSERT INTO Pickups (RentalID, PickupDate, PickupAddress)
            VALUES (@RentalID, @PickupDate, @PickupAddress);
        END
        ELSE
        BEGIN
            RAISERROR ('Pickup already tracked for this rental', 16, 1);
        END
    END
    ELSE
    BEGIN
        RAISERROR ('Rental not found', 16, 1);
    END
END;

-- Query to view all rentals
SELECT 
    r.RentalID,
    r.CustomerName,
    sa.City,
    sa.State,
    ds.Size,
    r.RentalDate,
    r.ReturnDate
FROM Rentals r
JOIN ServiceAreas sa ON r.ServiceAreaID = sa.ServiceAreaID
JOIN DumpsterSizes ds ON r.DumpsterSizeID = ds.DumpsterSizeID;

-- Query to view all deliveries
SELECT 
    d.DeliveryID,
    r.RentalID,
    d.DeliveryDate,
    d.DeliveryAddress
FROM Deliveries d
JOIN Rentals r ON d.RentalID = r.RentalID;

-- Query to view all pickups
SELECT 
    p.PickupID,
    r.RentalID,
    p.PickupDate,
    p.PickupAddress
FROM Pickups p
JOIN Rentals r ON p.RentalID = r.RentalID;
```
