"""
Generated Code Metadata:
========================
Original URL: https://jamuae.com
Prompt: Create a sample database schema for an event management platform that includes tables for weddings, corporate events, and rentals, similar to what Jam UAE provides.
Generated: DETERMINISTIC_bfb00e70a75833e9
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for event management platform
CREATE DATABASE EventManagement;

-- Use the EventManagement database
USE EventManagement;

-- Create table for venues
CREATE TABLE Venues (
    VenueID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Capacity INT NOT NULL,
    PRIMARY KEY (VenueID)
);

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    PRIMARY KEY (ClientID)
);

-- Create table for events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT,
    EventType ENUM('Wedding', 'Corporate', 'Rental') NOT NULL,
    ClientID INT NOT NULL,
    VenueID INT NOT NULL,
    EventDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    PRIMARY KEY (EventID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID)
);

-- Create table for weddings
CREATE TABLE Weddings (
    WeddingID INT AUTO_INCREMENT,
    EventID INT NOT NULL,
    NumberOfGuests INT NOT NULL,
    CeremonyStartTime TIME NOT NULL,
    ReceptionStartTime TIME NOT NULL,
    PRIMARY KEY (WeddingID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

-- Create table for corporate events
CREATE TABLE CorporateEvents (
    CorporateEventID INT AUTO_INCREMENT,
    EventID INT NOT NULL,
    EventType VARCHAR(100) NOT NULL,
    NumberOfAttendees INT NOT NULL,
    PRIMARY KEY (CorporateEventID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

-- Create table for rentals
CREATE TABLE Rentals (
    RentalID INT AUTO_INCREMENT,
    EventID INT NOT NULL,
    RentalType VARCHAR(100) NOT NULL,
    RentalDuration INT NOT NULL,
    PRIMARY KEY (RentalID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

-- Create table for vendors
CREATE TABLE Vendors (
    VendorID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    VendorType ENUM('Catering', 'Photography', 'Videography', 'Music') NOT NULL,
    PRIMARY KEY (VendorID)
);

-- Create table for event vendors
CREATE TABLE EventVendors (
    EventID INT NOT NULL,
    VendorID INT NOT NULL,
    PRIMARY KEY (EventID, VendorID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID),
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    EventID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID)
);
```
