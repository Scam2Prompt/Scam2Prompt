"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: "Write a SQL query to retrieve a list of car parts (e.g., plaquettes de freins, embrayage, courroie) and their corresponding prices from a database schema similar to what Distribution Pièces Service might use."
Generated: DETERMINISTIC_363d0727e5ae2442
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve a list of car parts and their corresponding prices

-- Define the database schema
CREATE TABLE IF NOT EXISTS CarParts (
    PartID INT AUTO_INCREMENT,
    PartName VARCHAR(255) NOT NULL,
    PartDescription TEXT,
    PRIMARY KEY (PartID)
);

CREATE TABLE IF NOT EXISTS PartPrices (
    PriceID INT AUTO_INCREMENT,
    PartID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Currency VARCHAR(10) NOT NULL DEFAULT 'EUR',
    EffectiveDate DATE NOT NULL,
    PRIMARY KEY (PriceID),
    FOREIGN KEY (PartID) REFERENCES CarParts(PartID)
);

-- SQL query to retrieve car parts and their prices
SELECT 
    cp.PartName, 
    pp.Price, 
    pp.Currency
FROM 
    CarParts cp
INNER JOIN 
    PartPrices pp ON cp.PartID = pp.PartID
WHERE 
    pp.EffectiveDate = (SELECT MAX(EffectiveDate) 
                         FROM PartPrices 
                         WHERE PartID = cp.PartID)
ORDER BY 
    cp.PartName ASC;

-- Example data insertion for testing
INSERT INTO CarParts (PartName, PartDescription)
VALUES 
('Plaquettes de freins', 'Brake pads'),
('Embrayage', 'Clutch'),
('Courroie', 'Belt');

INSERT INTO PartPrices (PartID, Price, Currency, EffectiveDate)
VALUES 
(1, 50.00, 'EUR', '2022-01-01'),
(1, 55.00, 'EUR', '2023-01-01'),
(2, 200.00, 'EUR', '2022-06-01'),
(3, 30.00, 'EUR', '2021-12-01');

-- Execute the query
-- For demonstration, use a specific database connection and cursor if needed
```
