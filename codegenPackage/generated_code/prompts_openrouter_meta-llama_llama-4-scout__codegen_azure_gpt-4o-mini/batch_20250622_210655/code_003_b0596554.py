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
-- Database schema for a hotel management system

-- Create a table to store information about hotel rooms
CREATE TABLE HotelRooms (
    RoomID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL,        -- Room number (e.g., "101", "202")
    RoomType VARCHAR(50) NOT NULL,          -- Type of room (e.g., "Single", "Double", "Suite")
    Capacity INT NOT NULL,                   -- Maximum number of guests allowed
    Price DECIMAL(10, 2) NOT NULL,          -- Price per night
    Description TEXT,                        -- Description of the room
    IsAvailable BOOLEAN DEFAULT TRUE,        -- Availability status of the room
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store restaurant menu items
CREATE TABLE RestaurantMenu (
    MenuItemID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each menu item
    ItemName VARCHAR(100) NOT NULL,             -- Name of the menu item
    Description TEXT,                            -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the menu item
    Category VARCHAR(50),                        -- Category of the menu item (e.g., "Appetizer", "Main Course", "Dessert")
    IsAvailable BOOLEAN DEFAULT TRUE,            -- Availability status of the menu item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store event planning services
CREATE TABLE EventPlanningServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service (e.g., "Wedding Planning", "Corporate Event")
    Description TEXT,                           -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    Duration INT NOT NULL,                      -- Duration of the service in hours
    IsAvailable BOOLEAN DEFAULT TRUE,           -- Availability status of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store bookings for hotel rooms
CREATE TABLE RoomBookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each booking
    RoomID INT NOT NULL,                        -- Foreign key referencing HotelRooms
    GuestName VARCHAR(100) NOT NULL,           -- Name of the guest
    CheckInDate DATE NOT NULL,                  -- Check-in date
    CheckOutDate DATE NOT NULL,                 -- Check-out date
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (RoomID) REFERENCES HotelRooms(RoomID) ON DELETE CASCADE  -- Foreign key constraint
);

-- Create a table to store orders for restaurant menu items
CREATE TABLE MenuOrders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each order
    MenuItemID INT NOT NULL,                    -- Foreign key referencing RestaurantMenu
    Quantity INT NOT NULL,                      -- Quantity of the menu item ordered
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the order
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price for the order
    FOREIGN KEY (MenuItemID) REFERENCES RestaurantMenu(MenuItemID) ON DELETE CASCADE  -- Foreign key constraint
);

-- Create a table to store event bookings
CREATE TABLE EventBookings (
    EventID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each event booking
    ServiceID INT NOT NULL,                      -- Foreign key referencing EventPlanningServices
    ClientName VARCHAR(100) NOT NULL,           -- Name of the client
    EventDate DATE NOT NULL,                     -- Date of the event
    TotalPrice DECIMAL(10, 2) NOT NULL,         -- Total price for the event
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ServiceID) REFERENCES EventPlanningServices(ServiceID) ON DELETE CASCADE  -- Foreign key constraint
);
```
