"""
Generated Code Metadata:
========================
Original URL: https://market2024.qboda.es
Prompt: Create a SQL database schema to store information about wedding vendors, clients, and appointments, inspired by QBoda's services.
Generated: DETERMINISTIC_41be33e8e72e0d5d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for wedding vendors, clients, and appointments

CREATE DATABASE WeddingServices;

USE WeddingServices;

-- Table to store vendor information
CREATE TABLE Vendors (
    VendorID INT AUTO_INCREMENT,
    VendorName VARCHAR(255) NOT NULL,
    VendorType ENUM('Photographer', 'Videographer', 'DJ', 'Catering', 'Wedding Dress', 'Florist') NOT NULL,
    VendorDescription TEXT,
    VendorEmail VARCHAR(255) UNIQUE NOT NULL,
    VendorPhone VARCHAR(20) NOT NULL,
    VendorAddress VARCHAR(255),
    PRIMARY KEY (VendorID)
);

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    ClientFirstName VARCHAR(100) NOT NULL,
    ClientLastName VARCHAR(100) NOT NULL,
    ClientEmail VARCHAR(255) UNIQUE NOT NULL,
    ClientPhone VARCHAR(20) NOT NULL,
    ClientAddress VARCHAR(255),
    PRIMARY KEY (ClientID)
);

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    VendorID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    AppointmentLocation VARCHAR(255),
    AppointmentDescription TEXT,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID) ON DELETE CASCADE
);

-- Table to store vendor ratings and reviews
CREATE TABLE VendorReviews (
    ReviewID INT AUTO_INCREMENT,
    VendorID INT NOT NULL,
    ClientID INT NOT NULL,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    Review TEXT,
    ReviewDate DATE NOT NULL,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID) ON DELETE CASCADE,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    UNIQUE (VendorID, ClientID)
);

-- Table to store payments and invoices
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount DECIMAL(10, 2) NOT NULL,
    PaymentMethod ENUM('Cash', 'Credit', 'Check') NOT NULL,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);
```
