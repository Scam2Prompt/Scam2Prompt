"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Design a database schema for a restaurant that includes tables for menus, wines, and reservations, taking cues from Bodega Jean Bousquet's structure.
Generated: DETERMINISTIC_5caa338f92f6e32b
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Restaurant

-- Table: Menus
-- Stores information about the restaurant's menu items
CREATE TABLE Menus (
    MenuID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each menu item
    Name VARCHAR(255) NOT NULL,            -- Name of the menu item
    Description TEXT,                      -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the menu item
    Category VARCHAR(100),                 -- Category of the menu item (e.g., Appetizer, Main Course, Dessert)
    IsAvailable BOOLEAN DEFAULT TRUE,      -- Availability status of the menu item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the menu item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table: Wines
-- Stores information about the wines offered by the restaurant
CREATE TABLE Wines (
    WineID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each wine
    Name VARCHAR(255) NOT NULL,            -- Name of the wine
    Type VARCHAR(100),                     -- Type of wine (e.g., Red, White, Sparkling)
    Region VARCHAR(255),                   -- Region where the wine is produced
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the wine
    Vintage YEAR,                          -- Year the wine was produced
    IsAvailable BOOLEAN DEFAULT TRUE,      -- Availability status of the wine
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the wine was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table: Reservations
-- Stores information about customer reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reservation
    CustomerName VARCHAR(255) NOT NULL,           -- Name of the customer
    CustomerPhone VARCHAR(20) NOT NULL,           -- Phone number of the customer
    ReservationDate DATE NOT NULL,                -- Date of the reservation
    ReservationTime TIME NOT NULL,                -- Time of the reservation
    NumberOfGuests INT NOT NULL,                  -- Number of guests for the reservation
    SpecialRequests TEXT,                         -- Any special requests from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the reservation was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Foreign Key Relationships (if applicable)
-- For this schema, there are no direct relationships between tables, but they can be linked in application logic.

-- Indexes for performance optimization
CREATE INDEX idx_menu_category ON Menus (Category); -- Index for menu category
CREATE INDEX idx_wine_type ON Wines (Type);         -- Index for wine type
CREATE INDEX idx_reservation_date ON Reservations (ReservationDate); -- Index for reservation date

-- Error handling and constraints
-- Ensure price values are positive
ALTER TABLE Menus ADD CONSTRAINT chk_price_positive CHECK (Price > 0);
ALTER TABLE Wines ADD CONSTRAINT chk_price_positive CHECK (Price > 0);

-- Ensure number of guests is positive
ALTER TABLE Reservations ADD CONSTRAINT chk_guests_positive CHECK (NumberOfGuests > 0);
```
