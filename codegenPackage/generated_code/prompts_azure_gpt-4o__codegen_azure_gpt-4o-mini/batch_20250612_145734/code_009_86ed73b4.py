"""
Generated Code Metadata:
========================
Original URL: https://piscorealestate.com
Prompt: Recommend a database schema for storing real estate property data, including fields like "Soba," "Kupatila," "Kvadratura," "Cijena," and "Tip nekretnine," based on the structure of https://piscorealestate.com.
Generated: DETERMINISTIC_86ed73b4d83fe10d
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing real estate property data

CREATE TABLE Properties (
    PropertyID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each property
    Soba INT NOT NULL,                          -- Number of rooms
    Kupatila INT NOT NULL,                      -- Number of bathrooms
    Kvadratura DECIMAL(10, 2) NOT NULL,        -- Area in square meters
    Cijena DECIMAL(15, 2) NOT NULL,            -- Price in the local currency
    TipNekretnine ENUM('Stan', 'Kuca', 'Zemljiste', 'Komercijalno') NOT NULL, -- Type of property
    Opis TEXT,                                  -- Description of the property
    Lokacija VARCHAR(255) NOT NULL,             -- Location of the property
    DatumKreiranja TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the property was added
    DatumIzmjene TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Date when the property was last updated
    SlikaURL VARCHAR(255),                      -- URL for the property image
    CONSTRAINT chk_Kvadratura CHECK (Kvadratura > 0), -- Ensure area is positive
    CONSTRAINT chk_Cijena CHECK (Cijena >= 0)  -- Ensure price is non-negative
);

-- Index for faster searches on location and price
CREATE INDEX idx_Lokacija ON Properties (Lokacija);
CREATE INDEX idx_Cijena ON Properties (Cijena);
```
