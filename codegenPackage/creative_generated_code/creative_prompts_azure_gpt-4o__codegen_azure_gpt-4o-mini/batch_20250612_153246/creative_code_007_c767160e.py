"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadihonlineex.com
Prompt: Create a database schema to store transaction details for international and domestic remittances, inspired by the services offered by Dadih Online Exchange.
Generated: DETERMINISTIC_c767160e27fcc3c9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Transaction Details of Remittances

CREATE DATABASE IF NOT EXISTS DadihOnlineExchange;

USE DadihOnlineExchange;

-- Table to store countries
CREATE TABLE Countries (
    CountryID INT AUTO_INCREMENT PRIMARY KEY,
    CountryCode VARCHAR(3) NOT NULL UNIQUE, -- ISO 3166-1 alpha-3 code
    CountryName VARCHAR(100) NOT NULL
);

-- Table to store currency details
CREATE TABLE Currencies (
    CurrencyID INT AUTO_INCREMENT PRIMARY KEY,
    CurrencyCode VARCHAR(3) NOT NULL UNIQUE, -- ISO 4217 currency code
    CurrencyName VARCHAR(50) NOT NULL
);

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store transaction details
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    SenderID INT NOT NULL,
    ReceiverID INT NOT NULL,
    Amount DECIMAL(15, 2) NOT NULL,
    CurrencyID INT NOT NULL,
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    TransactionType ENUM('Domestic', 'International') NOT NULL,
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL,
    FOREIGN KEY (SenderID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (ReceiverID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (CurrencyID) REFERENCES Currencies(CurrencyID) ON DELETE RESTRICT
);

-- Table to store exchange rates for international transactions
CREATE TABLE ExchangeRates (
    ExchangeRateID INT AUTO_INCREMENT PRIMARY KEY,
    FromCurrencyID INT NOT NULL,
    ToCurrencyID INT NOT NULL,
    Rate DECIMAL(10, 4) NOT NULL,
    EffectiveDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (FromCurrencyID) REFERENCES Currencies(CurrencyID) ON DELETE CASCADE,
    FOREIGN KEY (ToCurrencyID) REFERENCES Currencies(CurrencyID) ON DELETE RESTRICT,
    UNIQUE (FromCurrencyID, ToCurrencyID) -- Ensure unique exchange rates between two currencies
);

-- Table to log transaction errors for troubleshooting
CREATE TABLE TransactionErrors (
    ErrorID INT AUTO_INCREMENT PRIMARY KEY,
    TransactionID INT NOT NULL,
    ErrorMessage VARCHAR(255) NOT NULL,
    ErrorDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TransactionID) REFERENCES Transactions(TransactionID) ON DELETE CASCADE
);

-- Populate Countries table with example data
INSERT INTO Countries (CountryCode, CountryName) VALUES
('US', 'United States'),
('CA', 'Canada'),
('GB', 'United Kingdom'),
('IN', 'India'),
('PH', 'Philippines');

-- Populate Currencies table with example data
INSERT INTO Currencies (CurrencyCode, CurrencyName) VALUES
('USD', 'United States Dollar'),
('CAD', 'Canadian Dollar'),
('GBP', 'British Pound Sterling'),
('INR', 'Indian Rupee'),
('PHP', 'Philippine Peso');
```
