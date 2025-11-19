"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Create a database schema for storing information about tools and equipment, including fields for "material," "mechanism," "implemento," and "aparelho," inspired by the Geyciane Ferramentas content.
Generated: DETERMINISTIC_78a793b0088e017c
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about tools and equipment

CREATE TABLE ToolsAndEquipment (
    id SERIAL PRIMARY KEY, -- Unique identifier for each tool/equipment
    material VARCHAR(255) NOT NULL, -- Material of the tool/equipment
    mechanism VARCHAR(255) NOT NULL, -- Mechanism used in the tool/equipment
    implemento VARCHAR(255) NOT NULL, -- Implemento associated with the tool/equipment
    aparelho VARCHAR(255) NOT NULL, -- Aparelho associated with the tool/equipment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    CONSTRAINT chk_material CHECK (material <> ''), -- Ensure material is not empty
    CONSTRAINT chk_mechanism CHECK (mechanism <> ''), -- Ensure mechanism is not empty
    CONSTRAINT chk_implemento CHECK (implemento <> ''), -- Ensure implemento is not empty
    CONSTRAINT chk_aparelho CHECK (aparelho <> '') -- Ensure aparelho is not empty
);

-- Index for faster searching by material
CREATE INDEX idx_material ON ToolsAndEquipment(material);

-- Index for faster searching by mechanism
CREATE INDEX idx_mechanism ON ToolsAndEquipment(mechanism);
```
