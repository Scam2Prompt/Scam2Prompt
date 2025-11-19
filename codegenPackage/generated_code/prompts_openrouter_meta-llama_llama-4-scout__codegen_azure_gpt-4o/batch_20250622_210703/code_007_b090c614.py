"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Design a database schema to store information about hair services, products, and client appointments for a beauty salon management system.
Generated: DETERMINISTIC_b090c6143f9b728d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a beauty salon management system

-- Table to store information about hair services offered by the salon
CREATE TABLE HairServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., haircut, coloring)
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    DurationMinutes INT NOT NULL,             -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about products sold by the salon
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    StockQuantity INT NOT NULL,               -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- First name of the client
    LastName VARCHAR(50) NOT NULL,            -- Last name of the client
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the client
    PhoneNumber VARCHAR(15),                  -- Phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                       -- Foreign key referencing HairServices table
    AppointmentDate DATE NOT NULL,                -- Date of the appointment
    AppointmentTime TIME NOT NULL,                -- Time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the appointment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ServiceID) REFERENCES HairServices(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Table to store information about product purchases by clients
CREATE TABLE ProductPurchases (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each purchase
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    ProductID INT NOT NULL,                    -- Foreign key referencing Products table
    Quantity INT NOT NULL,                     -- Quantity of the product purchased
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price for the purchase
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the purchase was made
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_appointment_date_time ON Appointments(AppointmentDate, AppointmentTime);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_service_name ON HairServices(ServiceName);
CREATE INDEX idx_client_email ON Clients(Email);
```
