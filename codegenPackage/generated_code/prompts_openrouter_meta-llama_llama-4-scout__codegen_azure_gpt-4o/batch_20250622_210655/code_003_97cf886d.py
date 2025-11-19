"""
Generated Code Metadata:
========================
Original URL: https://blackhillsports.com
Prompt: "Design a database schema to store information about custom apparel orders, including details about fabric selection, fit, and printing services, for a company like Black Hill Sports."
Generated: DETERMINISTIC_97cf886da71bf85a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about custom apparel orders

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table to store orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time the order was placed
    TotalPrice DECIMAL(10, 2) NOT NULL,        -- Total price of the order
    Status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store fabric options
CREATE TABLE Fabrics (
    FabricID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each fabric
    Name VARCHAR(50) NOT NULL,                 -- Name of the fabric
    Description TEXT,                          -- Description of the fabric
    PricePerUnit DECIMAL(10, 2) NOT NULL       -- Price per unit of the fabric
);

-- Table to store fit options
CREATE TABLE Fits (
    FitID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each fit
    Name VARCHAR(50) NOT NULL,                 -- Name of the fit (e.g., Slim, Regular, Loose)
    Description TEXT                           -- Description of the fit
);

-- Table to store printing services
CREATE TABLE PrintingServices (
    PrintingServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each printing service
    Name VARCHAR(50) NOT NULL,                        -- Name of the printing service
    Description TEXT,                                 -- Description of the printing service
    Price DECIMAL(10, 2) NOT NULL                     -- Price for the printing service
);

-- Table to store order details
CREATE TABLE OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    OrderID INT NOT NULL,                         -- Foreign key referencing Orders table
    FabricID INT NOT NULL,                        -- Foreign key referencing Fabrics table
    FitID INT NOT NULL,                           -- Foreign key referencing Fits table
    PrintingServiceID INT,                        -- Foreign key referencing PrintingServices table
    Quantity INT NOT NULL,                        -- Quantity of the item ordered
    Subtotal DECIMAL(10, 2) NOT NULL,             -- Subtotal for this order detail
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (FabricID) REFERENCES Fabrics(FabricID) ON DELETE SET NULL,
    FOREIGN KEY (FitID) REFERENCES Fits(FitID) ON DELETE SET NULL,
    FOREIGN KEY (PrintingServiceID) REFERENCES PrintingServices(PrintingServiceID) ON DELETE SET NULL
);

-- Table to store payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each payment
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders table
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the payment
    Amount DECIMAL(10, 2) NOT NULL,             -- Amount paid
    PaymentMethod ENUM('Credit Card', 'PayPal', 'Bank Transfer') NOT NULL, -- Payment method
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
);

-- Table to store shipping information
CREATE TABLE ShippingDetails (
    ShippingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each shipping detail
    OrderID INT NOT NULL,                       -- Foreign key referencing Orders table
    Address VARCHAR(255) NOT NULL,              -- Shipping address
    City VARCHAR(50) NOT NULL,                  -- City for shipping
    State VARCHAR(50) NOT NULL,                 -- State for shipping
    PostalCode VARCHAR(20) NOT NULL,            -- Postal code for shipping
    Country VARCHAR(50) NOT NULL,               -- Country for shipping
    ShippingDate TIMESTAMP,                     -- Date and time the order was shipped
    DeliveryDate TIMESTAMP,                     -- Date and time the order was delivered
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_order_status ON Orders(Status);
CREATE INDEX idx_shipping_country ON ShippingDetails(Country);
```
