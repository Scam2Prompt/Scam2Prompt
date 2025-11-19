"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: "Design a database schema to store information about different types of acrylic yarns, such as Grey Yarns, Dyed Yarns, and Milange Yarns."
Generated: DETERMINISTIC_5d10528d529c61cb
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about different types of acrylic yarns

CREATE TABLE YarnTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each yarn type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the yarn type (e.g., Grey, Dyed, Milange)
    description TEXT, -- Description of the yarn type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

CREATE TABLE YarnColors (
    id SERIAL PRIMARY KEY, -- Unique identifier for each color
    yarn_type_id INT NOT NULL, -- Foreign key referencing YarnTypes
    color_name VARCHAR(100) NOT NULL, -- Name of the color
    hex_value VARCHAR(7) NOT NULL, -- Hexadecimal value of the color
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (yarn_type_id) REFERENCES YarnTypes(id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE YarnSpecifications (
    id SERIAL PRIMARY KEY, -- Unique identifier for each yarn specification
    yarn_type_id INT NOT NULL, -- Foreign key referencing YarnTypes
    weight VARCHAR(50) NOT NULL, -- Weight category of the yarn (e.g., DK, Worsted)
    fiber_content VARCHAR(100) NOT NULL, -- Fiber content of the yarn (e.g., 100% Acrylic)
    yardage INT NOT NULL, -- Yardage of the yarn (length in yards)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (yarn_type_id) REFERENCES YarnTypes(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_yarn_type_name ON YarnTypes(name);
CREATE INDEX idx_yarn_color_name ON YarnColors(color_name);
CREATE INDEX idx_yarn_weight ON YarnSpecifications(weight);
```
