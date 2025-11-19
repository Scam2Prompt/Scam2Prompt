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
-- Database Schema for Hotel Rooms, Restaurant Menus, and Event Planning Services

-- Table to store information about hotel rooms
CREATE TABLE HotelRooms (
    RoomID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each room
    RoomNumber VARCHAR(10) NOT NULL,       -- Room number
    RoomType VARCHAR(50) NOT NULL,         -- Type of room (e.g., Single, Double, Suite)
    Capacity INT NOT NULL,                 -- Maximum number of occupants
    PricePerNight DECIMAL(10, 2) NOT NULL, -- Price per night
    IsAvailable BOOLEAN DEFAULT TRUE,      -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about restaurant menu items
CREATE TABLE RestaurantMenu (
    MenuItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each menu item
    ItemName VARCHAR(100) NOT NULL,            -- Name of the menu item
    Description TEXT,                          -- Description of the menu item
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the menu item
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about event planning services
CREATE TABLE EventServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    IsAvailable BOOLEAN DEFAULT TRUE,         -- Availability status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store bookings for hotel rooms
CREATE TABLE RoomBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    RoomID INT NOT NULL,                      -- Foreign key referencing HotelRooms
    CustomerName VARCHAR(100) NOT NULL,       -- Name of the customer
    CheckInDate DATE NOT NULL,                -- Check-in date
    CheckOutDate DATE NOT NULL,               -- Check-out date
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (RoomID) REFERENCES HotelRooms(RoomID) ON DELETE CASCADE
);

-- Table to store orders for restaurant menu items
CREATE TABLE MenuOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    MenuItemID INT NOT NULL,                  -- Foreign key referencing RestaurantMenu
    CustomerName VARCHAR(100) NOT NULL,       -- Name of the customer
    Quantity INT NOT NULL,                    -- Quantity of the menu item ordered
    TotalPrice DECIMAL(10, 2) NOT NULL,       -- Total price for the order
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Order date and time
    FOREIGN KEY (MenuItemID) REFERENCES RestaurantMenu(MenuItemID) ON DELETE CASCADE
);

-- Table to store bookings for event planning services
CREATE TABLE EventBookings (
    EventBookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event booking
    ServiceID INT NOT NULL,                        -- Foreign key referencing EventServices
    CustomerName VARCHAR(100) NOT NULL,            -- Name of the customer
    EventDate DATE NOT NULL,                       -- Date of the event
    TotalPrice DECIMAL(10, 2) NOT NULL,            -- Total price for the event booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ServiceID) REFERENCES EventServices(ServiceID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_room_availability ON HotelRooms(IsAvailable);
CREATE INDEX idx_menu_availability ON RestaurantMenu(IsAvailable);
CREATE INDEX idx_service_availability ON EventServices(IsAvailable);
```
