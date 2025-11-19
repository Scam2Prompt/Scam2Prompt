"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myflowfoundationke.org
Prompt: Design a data model in SQL to manage the records of girls impacted by menstrual health initiatives, similar to the tracking done by My Flow Foundation.
Generated: DETERMINISTIC_3a1543f3ceb01dfb
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema to manage records of girls impacted by menstrual health initiatives

-- Ensure a clean slate by dropping the table if it exists
DROP TABLE IF EXISTS GirlsImpacted;

-- Create the table to store records of impacted girls
CREATE TABLE GirlsImpacted (
    -- Unique identifier for each record
    ID INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Full name of the girl
    FullName VARCHAR(100) NOT NULL,
    
    -- Age of the girl
    Age INT NOT NULL CHECK (Age > 0),
    
    -- Geographical location (e.g., city, village, etc.)
    Location VARCHAR(100),
    
    -- Contact information (optional, e.g., guardian's phone number)
    ContactInfo VARCHAR(15),
    
    -- Date the initiative impacted the individual
    DateImpacted DATE NOT NULL,
    
    -- Type of initiative (e.g., "Education", "Donation", "Workshop")
    InitiativeType VARCHAR(50) NOT NULL,
    
    -- Details of the initiative (e.g., description, materials provided, etc.)
    InitiativeDetails TEXT,

    -- Notes (e.g., observations, follow-up details, etc.)
    Notes TEXT,

    -- Timestamp for when the record was created
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Timestamp for the last update to the record
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Index for faster querying of impacted girls by location
CREATE INDEX idx_location ON GirlsImpacted(Location);

-- Index for faster querying by initiative type
CREATE INDEX idx_initiative_type ON GirlsImpacted(InitiativeType);

-- Example of adding a foreign-key relationship
-- If you have a table tracking initiatives specifically:
-- FOREIGN KEY (InitiativeType) REFERENCES Initiatives(InitiativeType)

-- Proper error handling and validations should be added at the application layer when inserting data
```
