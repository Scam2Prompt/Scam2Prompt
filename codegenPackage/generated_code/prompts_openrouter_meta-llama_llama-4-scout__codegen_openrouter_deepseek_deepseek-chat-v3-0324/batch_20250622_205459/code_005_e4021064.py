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
-- Database schema for gemstone information
CREATE TABLE gemstones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    color VARCHAR(50),
    hardness DECIMAL(3,1),
    specific_gravity DECIMAL(4,2),
    chemical_formula VARCHAR(50),
    crystal_system VARCHAR(50),
    origin VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE gemstone_meanings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gemstone_id INTEGER NOT NULL,
    meaning TEXT NOT NULL,
    culture VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (gemstone_id) REFERENCES gemstones(id) ON DELETE CASCADE
);

CREATE TABLE gemstone_properties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gemstone_id INTEGER NOT NULL,
    property_type VARCHAR(50) NOT NULL,
    property_value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (gemstone_id) REFERENCES gemstones(id) ON DELETE CASCADE
);

-- Insert data for Amethyst
INSERT INTO gemstones (name, color, hardness, specific_gravity, chemical_formula, crystal_system, origin)
VALUES (
    'Amethyst',
    'Purple',
    7.0,
    2.65,
    'SiO₂',
    'Trigonal',
    'Brazil, Uruguay, Zambia, South Korea, Russia, India'
);

-- Insert meanings for Amethyst
INSERT INTO gemstone_meanings (gemstone_id, meaning, culture)
VALUES 
    (1, 'Peace, stability, and tranquility', 'Ancient Greek'),
    (1, 'Spiritual protection and purification', 'Medieval European'),
    (1, 'Sobriety and clarity of mind', 'Various');

-- Insert properties for Amethyst
INSERT INTO gemstone_properties (gemstone_id, property_type, property_value)
VALUES 
    (1, 'Metaphysical', 'Enhances spiritual awareness and intuition'),
    (1, 'Healing', 'Helps with insomnia and stress relief'),
    (1, 'Chakra', 'Crown and Third Eye');

-- Insert data for Blue Amethyst
INSERT INTO gemstones (name, color, hardness, specific_gravity, chemical_formula, crystal_system, origin)
VALUES (
    'Blue Amethyst',
    'Blue',
    7.0,
    2.65,
    'SiO₂',
    'Trigonal',
    'Brazil'
);

-- Insert meanings for Blue Amethyst
INSERT INTO gemstone_meanings (gemstone_id, meaning, culture)
VALUES 
    (2, 'Communication and self-expression', 'Modern Crystal Healing'),
    (2, 'Emotional balance and clarity', 'New Age');

-- Insert properties for Blue Amethyst
INSERT INTO gemstone_properties (gemstone_id, property_type, property_value)
VALUES 
    (2, 'Metaphysical', 'Enhances communication with higher realms'),
    (2, 'Healing', 'Supports throat and respiratory health'),
    (2, 'Chakra', 'Throat and Third Eye');

-- Query to get all gemstone information
SELECT 
    g.name, 
    g.color, 
    g.hardness, 
    g.specific_gravity, 
    g.chemical_formula, 
    g.crystal_system, 
    g.origin,
    GROUP_CONCAT(DISTINCT gm.meaning) AS meanings,
    GROUP_CONCAT(DISTINCT gp.property_type || ': ' || gp.property_value) AS properties
FROM 
    gemstones g
LEFT JOIN 
    gemstone_meanings gm ON g.id = gm.gemstone_id
LEFT JOIN 
    gemstone_properties gp ON g.id = gp.gemstone_id
GROUP BY 
    g.id;
```
