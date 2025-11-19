"""
Generated Code Metadata:
========================
Original URL: https://cohencues.com
Prompt: "Design a database schema to store information about custom cue sticks, including customer details, cue specifications, and repair services offered by Cohen Cues."
Generated: DETERMINISTIC_8eaae021890084ee
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Cohen Cues to store information about custom cue sticks, customer details, cue specifications, and repair services.

-- Table to store customer details
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT                               -- Customer's address
);

-- Table to store cue stick specifications
CREATE TABLE CueSticks (
    CueID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each cue stick
    CustomerID INT NOT NULL,                   -- Foreign key linking to the customer who owns the cue stick
    Material VARCHAR(50) NOT NULL,             -- Material used for the cue stick (e.g., maple, ash)
    Weight DECIMAL(5, 2) NOT NULL,             -- Weight of the cue stick in ounces
    Length DECIMAL(5, 2) NOT NULL,             -- Length of the cue stick in inches
    TipDiameter DECIMAL(5, 2) NOT NULL,        -- Diameter of the cue tip in millimeters
    WrapType VARCHAR(50),                      -- Type of wrap used on the cue stick (e.g., leather, linen)
    CustomDesign TEXT,                         -- Description of any custom design or engraving
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store repair services offered
CREATE TABLE RepairServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each repair service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the repair service (e.g., tip replacement, shaft refinishing)
    Description TEXT,                          -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL              -- Price of the repair service
);

-- Table to store repair orders
CREATE TABLE RepairOrders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each repair order
    CustomerID INT NOT NULL,                   -- Foreign key linking to the customer who placed the order
    CueID INT NOT NULL,                        -- Foreign key linking to the cue stick being repaired
    ServiceID INT NOT NULL,                    -- Foreign key linking to the repair service being performed
    OrderDate DATE NOT NULL,                   -- Date the repair order was placed
    CompletionDate DATE,                       -- Date the repair was completed
    Status VARCHAR(50) NOT NULL,               -- Status of the repair order (e.g., Pending, Completed)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (CueID) REFERENCES CueSticks(CueID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES RepairServices(ServiceID) ON DELETE CASCADE
);

-- Indexes for faster lookups
CREATE INDEX idx_customer_email ON Customers(Email); -- Index on customer email for quick searches
CREATE INDEX idx_cue_customer ON CueSticks(CustomerID); -- Index on customer ID in CueSticks table
CREATE INDEX idx_order_status ON RepairOrders(Status); -- Index on repair order status
```
