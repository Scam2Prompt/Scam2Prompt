"""
Generated Code Metadata:
========================
Original URL: https://regency-towel.com
Prompt: Design a database schema to store information about different types of cotton used in textile production, including carded, combed, Egyptian, Turkish, and American cotton, as mentioned in Regency Towel's product range.
Generated: DETERMINISTIC_905abe60147f182c
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about different types of cotton used in textile production

CREATE TABLE CottonTypes (
    CottonTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each cotton type
    Name VARCHAR(50) NOT NULL,                    -- Name of the cotton type (e.g., Carded, Combed)
    Description TEXT,                              -- Description of the cotton type
    Origin VARCHAR(50),                           -- Origin of the cotton (e.g., Egyptian, Turkish, American)
    Characteristics JSON,                         -- JSON field to store various characteristics (e.g., softness, durability)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Index to improve search performance on cotton type name
CREATE INDEX idx_cotton_name ON CottonTypes (Name);

-- Sample data insertion for different types of cotton
INSERT INTO CottonTypes (Name, Description, Origin, Characteristics) VALUES
('Carded Cotton', 'Cotton that has been carded to remove impurities and align fibers.', 'Various', '{"softness": "medium", "durability": "high"}'),
('Combed Cotton', 'Cotton that has been combed to remove shorter fibers, resulting in a finer texture.', 'Various', '{"softness": "high", "durability": "medium"}'),
('Egyptian Cotton', 'High-quality cotton known for its long fibers and luxurious feel.', 'Egypt', '{"softness": "very high", "durability": "high"}'),
('Turkish Cotton', 'Cotton known for its absorbency and softness, often used in towels.', 'Turkey', '{"softness": "high", "durability": "medium"}'),
('American Cotton', 'Cotton produced in the USA, known for its versatility and quality.', 'USA', '{"softness": "medium", "durability": "high"}');

-- Function to retrieve cotton types by origin
DELIMITER //
CREATE FUNCTION GetCottonByOrigin(origin VARCHAR(50))
RETURNS TABLE (CottonTypeID INT, Name VARCHAR(50), Description TEXT, Characteristics JSON)
BEGIN
    RETURN SELECT CottonTypeID, Name, Description, Characteristics
    FROM CottonTypes
    WHERE Origin = origin;
END //
DELIMITER ;

-- Error handling: Ensure that the cotton type name is unique
CREATE UNIQUE INDEX idx_unique_cotton_name ON CottonTypes (Name);
```
