"""
Generated Code Metadata:
========================
Original URL: https://wonderino.com
Prompt: "Design a database schema to store information on gemstones, including their names, properties, and meanings, and provide SQL queries to insert data on Amethyst and Blue Amethyst from the Wonderino articles."
Generated: DETERMINISTIC_e402106497f3170d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for gemstones
CREATE TABLE Gemstones (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each gemstone
    name VARCHAR(100) NOT NULL,          -- Name of the gemstone
    properties TEXT,                     -- Properties of the gemstone
    meanings TEXT                        -- Meanings associated with the gemstone
);

-- Insert data for Amethyst
INSERT INTO Gemstones (name, properties, meanings) VALUES 
('Amethyst', 
 'A purple variety of quartz, known for its calming and healing properties.', 
 'Amethyst is believed to promote tranquility, balance, and peace of mind.');

-- Insert data for Blue Amethyst
INSERT INTO Gemstones (name, properties, meanings) VALUES 
('Blue Amethyst', 
 'A rare blue variety of amethyst, often associated with spiritual awareness and intuition.', 
 'Blue Amethyst is thought to enhance communication and self-expression.');

-- Query to retrieve all gemstones
SELECT * FROM Gemstones;

-- Query to find a gemstone by name
SELECT * FROM Gemstones WHERE name = 'Amethyst';

-- Query to update properties of a gemstone
UPDATE Gemstones 
SET properties = 'Updated properties description here.' 
WHERE name = 'Amethyst';

-- Query to delete a gemstone by name
DELETE FROM Gemstones WHERE name = 'Blue Amethyst';
```
