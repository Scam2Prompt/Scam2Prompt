"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fodyem.com
Prompt: Generate a database schema for managing travel packages, including fields for destinations like "Abidjan" and "Maroc & CAN," pricing, and availability.
Generated: DETERMINISTIC_c66b0a91b99c12ff
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL schema for managing travel packages
-- This schema is designed to store information about travel packages, including destinations, pricing, and availability.

CREATE TABLE TravelPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each travel package
    Destination VARCHAR(255) NOT NULL,         -- Name of the destination (e.g., "Abidjan", "Maroc & CAN")
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the travel package (e.g., 1200.50)
    IsAvailable BOOLEAN NOT NULL DEFAULT TRUE, -- Availability status of the package (TRUE = available, FALSE = not available)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Creating an index on Destination for faster lookups
CREATE INDEX IDX_Destination ON TravelPackages(Destination);

-- Example of inserting data into the TravelPackages table
-- INSERT INTO TravelPackages (Destination, Price, IsAvailable) VALUES ('Abidjan', 1200.50, TRUE);
-- INSERT INTO TravelPackages (Destination, Price, IsAvailable) VALUES ('Maroc & CAN', 900.00, TRUE);
```
