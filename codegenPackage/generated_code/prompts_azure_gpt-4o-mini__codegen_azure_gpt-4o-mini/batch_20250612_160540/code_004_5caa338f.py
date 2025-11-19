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
-- Database schema for a restaurant including tables for menus, wines, and reservations

-- Create a table for storing menu items
CREATE TABLE MenuItems (
    MenuItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each menu item
    Name VARCHAR(100) NOT NULL,                  -- Name of the menu item
    Description TEXT,                            -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the menu item
    Category VARCHAR(50),                        -- Category of the menu item (e.g., Appetizer, Main Course, Dessert)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the item was last updated
);

-- Create a table for storing wine information
CREATE TABLE Wines (
    WineID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each wine
    Name VARCHAR(100) NOT NULL,                  -- Name of the wine
    Type VARCHAR(50),                            -- Type of wine (e.g., Red, White, Sparkling)
    Year INT,                                    -- Year the wine was produced
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the wine
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the wine was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the wine was last updated
);

-- Create a table for storing reservations
CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each reservation
    CustomerName VARCHAR(100) NOT NULL,          -- Name of the customer making the reservation
    ReservationDate DATETIME NOT NULL,            -- Date and time of the reservation
    NumberOfGuests INT NOT NULL,                  -- Number of guests for the reservation
    ContactNumber VARCHAR(15),                    -- Contact number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the reservation was made
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the reservation was last updated
    UNIQUE (ReservationDate, NumberOfGuests)     -- Ensure no overlapping reservations for the same time and guest count
);

-- Create a table for storing menu and wine pairings
CREATE TABLE MenuWinePairings (
    PairingID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each pairing
    MenuItemID INT NOT NULL,                      -- Foreign key referencing MenuItems
    WineID INT NOT NULL,                          -- Foreign key referencing Wines
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the pairing was created
    FOREIGN KEY (MenuItemID) REFERENCES MenuItems(MenuItemID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (WineID) REFERENCES Wines(WineID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create indexes for faster querying
CREATE INDEX idx_reservation_date ON Reservations (ReservationDate);
CREATE INDEX idx_menu_item_name ON MenuItems (Name);
CREATE INDEX idx_wine_name ON Wines (Name);
```
