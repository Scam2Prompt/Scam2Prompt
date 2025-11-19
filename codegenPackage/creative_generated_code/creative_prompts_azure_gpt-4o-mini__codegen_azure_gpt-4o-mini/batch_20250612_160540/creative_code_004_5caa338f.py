"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Design a database schema for a restaurant that includes tables for menus, wines, and reservations, taking cues from Bodega Jean Bousquet's structure.
Generated: DETERMINISTIC_5caa338f92f6e32b
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for Restaurant Database

-- Table to store menu items
CREATE TABLE Menu (
    MenuItemID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each menu item
    Name VARCHAR(100) NOT NULL,                -- Name of the menu item
    Description TEXT,                           -- Detailed description of the menu item
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the menu item
    Category VARCHAR(50),                       -- Category of the menu item (e.g., Appetizer, Main Course, Dessert)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store wine selections
CREATE TABLE Wines (
    WineID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each wine
    Name VARCHAR(100) NOT NULL,                 -- Name of the wine
    Year INT,                                   -- Year the wine was produced
    Description TEXT,                           -- Detailed description of the wine
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the wine
    Origin VARCHAR(100),                        -- Origin of the wine (e.g., country, region)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the wine was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store reservations
CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each reservation
    CustomerName VARCHAR(100) NOT NULL,           -- Name of the customer making the reservation
    ReservationDate DATETIME NOT NULL,             -- Date and time for the reservation
    NumberOfGuests INT NOT NULL CHECK (NumberOfGuests > 0), -- Number of guests for the reservation
    SpecialRequests TEXT,                          -- Any special requests from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the reservation was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Foreign key to link Menu items with Reservations (if applicable)
-- This can be used if you want to track menu items reserved for specific reservations
CREATE TABLE ReservationMenu (
    ReservationMenuID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the reservation menu link
    ReservationID INT NOT NULL,                        -- Link to the Reservations table
    MenuItemID INT NOT NULL,                          -- Link to the Menu table
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE CASCADE, -- Cascade delete for reservations
    FOREIGN KEY (MenuItemID) REFERENCES Menu(MenuItemID) ON DELETE CASCADE -- Cascade delete for menu items
);

-- Foreign key to link Wines with Reservations (if applicable)
-- This can be used if you want to track wines selected for specific reservations
CREATE TABLE ReservationWines (
    ReservationWineID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the reservation wine link
    ReservationID INT NOT NULL,                        -- Link to the Reservations table
    WineID INT NOT NULL,                              -- Link to the Wines table
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE CASCADE, -- Cascade delete for reservations
    FOREIGN KEY (WineID) REFERENCES Wines(WineID) ON DELETE CASCADE -- Cascade delete for wines
);

-- Create indexes for performance optimization where necessary
CREATE INDEX idx_menu_category ON Menu(Category);
CREATE INDEX idx_wines_origin ON Wines(Origin);
CREATE INDEX idx_reservation_date ON Reservations(ReservationDate);
```
