"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.ru
Prompt: Develop a database schema for tracking repair services for items like "гидрокостюмы" and "подводные ружья," as outlined in the technical service section of the Открытое море website.
Generated: DETERMINISTIC_a8ab63cdf767625a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking repair services for items like "гидрокостюмы" and "подводные ружья"

-- Table to store item types (e.g., гидрокостюмы, подводные ружья)
CREATE TABLE ItemTypes (
    ItemTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the item type
    Name VARCHAR(255) NOT NULL, -- Name of the item type
    Description TEXT, -- Optional description of the item type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the customer
    FullName VARCHAR(255) NOT NULL, -- Full name of the customer
    Email VARCHAR(255) UNIQUE, -- Email address of the customer
    PhoneNumber VARCHAR(20), -- Phone number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store repair services
CREATE TABLE RepairServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the repair service
    ServiceName VARCHAR(255) NOT NULL, -- Name of the repair service
    Description TEXT, -- Detailed description of the repair service
    BasePrice DECIMAL(10, 2) NOT NULL, -- Base price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store repair orders
CREATE TABLE RepairOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the repair order
    CustomerID INT NOT NULL, -- Foreign key to Customers table
    ItemTypeID INT NOT NULL, -- Foreign key to ItemTypes table
    ServiceID INT NOT NULL, -- Foreign key to RepairServices table
    ItemDescription TEXT, -- Description of the item being repaired
    AdditionalNotes TEXT, -- Additional notes about the repair
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the repair order
    TotalPrice DECIMAL(10, 2), -- Total price for the repair service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ItemTypeID) REFERENCES ItemTypes(ItemTypeID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES RepairServices(ServiceID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_customers_email ON Customers (Email);
CREATE INDEX idx_orders_status ON RepairOrders (Status);

-- End of schema
```
