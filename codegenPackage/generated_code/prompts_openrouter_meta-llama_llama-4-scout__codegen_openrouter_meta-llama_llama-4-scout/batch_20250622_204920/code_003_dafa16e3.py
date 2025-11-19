"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Create a SQL database schema to store information about armourer services, uniform hire, and prop rentals for a film production company in NSW.
Generated: DETERMINISTIC_dafa16e33226c500
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for film production company
CREATE DATABASE film_production;

-- Use the database
USE film_production;

-- Create table for armourer services
CREATE TABLE Armourer_Services (
    Armourer_Service_ID INT AUTO_INCREMENT,
    Service_Type VARCHAR(255) NOT NULL,
    Description TEXT,
    Cost DECIMAL(10, 2) NOT NULL,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (Armourer_Service_ID)
);

-- Create table for uniform hire
CREATE TABLE Uniform_Hire (
    Uniform_Hire_ID INT AUTO_INCREMENT,
    Uniform_Type VARCHAR(255) NOT NULL,
    Size VARCHAR(50) NOT NULL,
    Quantity INT NOT NULL,
    Hire_Cost DECIMAL(10, 2) NOT NULL,
    Return_Date DATE,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (Uniform_Hire_ID)
);

-- Create table for prop rentals
CREATE TABLE Prop_Rentals (
    Prop_Rental_ID INT AUTO_INCREMENT,
    Prop_Type VARCHAR(255) NOT NULL,
    Prop_Description TEXT,
    Rental_Cost DECIMAL(10, 2) NOT NULL,
    Rental_Period DATE,
    Return_Date DATE,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (Prop_Rental_ID)
);

-- Create table for clients
CREATE TABLE Clients (
    Client_ID INT AUTO_INCREMENT,
    Company_Name VARCHAR(255) NOT NULL,
    Contact_Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address TEXT,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (Client_ID)
);

-- Create table for orders
CREATE TABLE Orders (
    Order_ID INT AUTO_INCREMENT,
    Client_ID INT NOT NULL,
    Order_Date DATE NOT NULL,
    Total_Cost DECIMAL(10, 2) NOT NULL,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (Order_ID),
    FOREIGN KEY (Client_ID) REFERENCES Clients(Client_ID)
);

-- Create table for order items
CREATE TABLE Order_Items (
    Order_Item_ID INT AUTO_INCREMENT,
    Order_ID INT NOT NULL,
    Armourer_Service_ID INT,
    Uniform_Hire_ID INT,
    Prop_Rental_ID INT,
    Quantity INT NOT NULL,
    Unit_Cost DECIMAL(10, 2) NOT NULL,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (Order_Item_ID),
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID),
    FOREIGN KEY (Armourer_Service_ID) REFERENCES Armourer_Services(Armourer_Service_ID),
    FOREIGN KEY (Uniform_Hire_ID) REFERENCES Uniform_Hire(Uniform_Hire_ID),
    FOREIGN KEY (Prop_Rental_ID) REFERENCES Prop_Rentals(Prop_Rental_ID),
    CHECK (
        (Armourer_Service_ID IS NOT NULL AND Uniform_Hire_ID IS NULL AND Prop_Rental_ID IS NULL) OR
        (Armourer_Service_ID IS NULL AND Uniform_Hire_ID IS NOT NULL AND Prop_Rental_ID IS NULL) OR
        (Armourer_Service_ID IS NULL AND Uniform_Hire_ID IS NULL AND Prop_Rental_ID IS NOT NULL)
    )
);

-- Create table for payments
CREATE TABLE Payments (
    Payment_ID INT AUTO_INCREMENT,
    Order_ID INT NOT NULL,
    Payment_Date DATE NOT NULL,
    Payment_Amount DECIMAL(10, 2) NOT NULL,
    Payment_Method VARCHAR(255) NOT NULL,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (Payment_ID),
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID)
);

-- Create indexes
CREATE INDEX idx_Armourer_Services_Service_Type ON Armourer_Services (Service_Type);
CREATE INDEX idx_Uniform_Hire_Uniform_Type ON Uniform_Hire (Uniform_Type);
CREATE INDEX idx_Prop_Rentals_Prop_Type ON Prop_Rentals (Prop_Type);
CREATE INDEX idx_Orders_Client_ID ON Orders (Client_ID);
CREATE INDEX idx_Order_Items_Order_ID ON Order_Items (Order_ID);
```

```sql
-- sample_data.sql

-- Insert sample data into tables
INSERT INTO Armourer_Services (Service_Type, Description, Cost)
VALUES 
('Gun Rental', 'Rental of guns for film production', 100.00),
('Armourer Consultation', 'Consultation with armourer for film production', 200.00);

INSERT INTO Uniform_Hire (Uniform_Type, Size, Quantity, Hire_Cost)
VALUES 
('Police Uniform', 'M', 5, 50.00),
('Military Uniform', 'L', 3, 75.00);

INSERT INTO Prop_Rentals (Prop_Type, Prop_Description, Rental_Cost)
VALUES 
('Sword', 'Medieval sword', 20.00),
('Gun', 'Replica gun', 50.00);

INSERT INTO Clients (Company_Name, Contact_Name, Email, Phone, Address)
VALUES 
('Film Production Company', 'John Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
('TV Production Company', 'Jane Smith', 'jane.smith@example.com', '9876543210', '456 Elm St');

INSERT INTO Orders (Client_ID, Order_Date, Total_Cost)
VALUES 
(1, '2022-01-01', 1000.00),
(2, '2022-02-01', 500.00);

INSERT INTO Order_Items (Order_ID, Armourer_Service_ID, Quantity, Unit_Cost)
VALUES 
(1, 1, 5, 100.00),
(1, 2, 2, 200.00);

INSERT INTO Order_Items (Order_ID, Uniform_Hire_ID, Quantity, Unit_Cost)
VALUES 
(2, 1, 3, 50.00),
(2, 2, 2, 75.00);

INSERT INTO Order_Items (Order_ID, Prop_Rental_ID, Quantity, Unit_Cost)
VALUES 
(1, 1, 2, 20.00),
(1, 2, 1, 50.00);

INSERT INTO Payments (Order_ID, Payment_Date, Payment_Amount, Payment_Method)
VALUES 
(1, '2022-01-01', 1000.00, 'Credit Card'),
(2, '2022-02-01', 500.00, 'Bank Transfer');
```
