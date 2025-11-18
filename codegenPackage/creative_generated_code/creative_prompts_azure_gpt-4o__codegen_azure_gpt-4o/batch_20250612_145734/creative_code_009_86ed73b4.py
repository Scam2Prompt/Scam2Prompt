"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piscorealestate.com
Prompt: Recommend a database schema for storing real estate property data, including fields like "Soba," "Kupatila," "Kvadratura," "Cijena," and "Tip nekretnine," based on the structure of https://piscorealestate.com.
Generated: DETERMINISTIC_86ed73b4d83fe10d
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing real estate property data
-- This schema is designed to support fields such as "Soba," "Kupatila," "Kvadratura," "Cijena," and "Tip nekretnine."

-- Create the table to store property data
CREATE TABLE RealEstateProperties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Soba INT NOT NULL,                         -- Number of rooms
    Kupatila INT NOT NULL,                     -- Number of bathrooms
    Kvadratura DECIMAL(10, 2) NOT NULL,        -- Area in square meters (allows for decimals)
    Cijena DECIMAL(15, 2) NOT NULL,            -- Price of the property (high precision for currency)
    TipNekretnine VARCHAR(50) NOT NULL,        -- Type of property (e.g., apartment, house, land)
    Lokacija VARCHAR(255),                     -- Location of the property
    Opis TEXT,                                 -- Detailed description of the property
    DatumUnosa TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property record was added
    Aktivan BOOLEAN DEFAULT TRUE               -- Indicates if the property is active (true for active, false for inactive)
);

-- Add an index on the `TipNekretnine` field for faster lookups by property type
CREATE INDEX idx_tip_nekretnine ON RealEstateProperties (TipNekretnine);

-- Add an index on the `Lokacija` field to optimize location-based queries
CREATE INDEX idx_lokacija ON RealEstateProperties (Lokacija);

-- Add an index on `Cijena` to optimize price range queries
CREATE INDEX idx_cijena ON RealEstateProperties (Cijena);

-- Insert sample data (optional, for testing purposes)
INSERT INTO RealEstateProperties (Soba, Kupatila, Kvadratura, Cijena, TipNekretnine, Lokacija, Opis)
VALUES 
(3, 2, 85.50, 120000.00, 'Apartment', 'Podgorica, Montenegro', 'Spacious apartment in Podgorica city center'),
(5, 3, 250.00, 450000.00, 'House', 'Kotor, Montenegro', 'Beautiful villa with sea view in Kotor Bay'),
(0, 0, 500.00, 70000.00, 'Land', 'Bar, Montenegro', 'Land suitable for construction in Bar');

-- End of schema
```
