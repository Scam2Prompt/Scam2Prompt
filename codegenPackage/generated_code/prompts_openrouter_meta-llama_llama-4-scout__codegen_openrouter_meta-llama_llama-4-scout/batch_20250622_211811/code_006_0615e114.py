"""
Generated Code Metadata:
========================
Original URL: https://beltsmania.com
Prompt: Create a database schema to store information about different types of championship belts, including WWE, UFC, and custom designs.
Generated: DETERMINISTIC_0615e11460b1ccc8
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- championship_belts_schema.sql

-- Create a database schema to store information about championship belts

CREATE TABLE IF NOT EXISTS championship_belts (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS belt_types (
  id SERIAL PRIMARY KEY,
  belt_type VARCHAR(50) NOT NULL CHECK (belt_type IN ('WWE', 'UFC', 'CUSTOM')),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS championship_belts_belt_types (
  championship_belt_id INTEGER NOT NULL,
  belt_type_id INTEGER NOT NULL,
  PRIMARY KEY (championship_belt_id, belt_type_id),
  FOREIGN KEY (championship_belt_id) REFERENCES championship_belts(id) ON DELETE CASCADE,
  FOREIGN KEY (belt_type_id) REFERENCES belt_types(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS belt_designs (
  id SERIAL PRIMARY KEY,
  championship_belt_id INTEGER NOT NULL,
  design_name VARCHAR(255) NOT NULL,
  design_description TEXT,
  material VARCHAR(100) NOT NULL,
  weight DECIMAL(10, 2) NOT NULL,
  dimensions VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (championship_belt_id) REFERENCES championship_belts(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS belt_plates (
  id SERIAL PRIMARY KEY,
  belt_design_id INTEGER NOT NULL,
  plate_name VARCHAR(255) NOT NULL,
  plate_description TEXT,
  plate_material VARCHAR(100) NOT NULL,
  plate_weight DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (belt_design_id) REFERENCES belt_designs(id) ON DELETE CASCADE
);

-- Indexes for better query performance
CREATE INDEX idx_championship_belts_name ON championship_belts (name);
CREATE INDEX idx_belt_types_belt_type ON belt_types (belt_type);
CREATE INDEX idx_championship_belts_belt_types_championship_belt_id ON championship_belts_belt_types (championship_belt_id);
CREATE INDEX idx_championship_belts_belt_types_belt_type_id ON championship_belts_belt_types (belt_type_id);
CREATE INDEX idx_belt_designs_championship_belt_id ON belt_designs (championship_belt_id);
CREATE INDEX idx_belt_plates_belt_design_id ON belt_plates (belt_design_id);

-- Example data for testing
INSERT INTO championship_belts (name, description)
VALUES 
  ('WWE Championship', 'The WWE Championship belt'),
  ('UFC Heavyweight Championship', 'The UFC Heavyweight Championship belt'),
  ('Custom Design Belt', 'A custom designed championship belt');

INSERT INTO belt_types (belt_type, description)
VALUES 
  ('WWE', 'WWE championship belt type'),
  ('UFC', 'UFC championship belt type'),
  ('CUSTOM', 'Custom championship belt type');

INSERT INTO championship_belts_belt_types (championship_belt_id, belt_type_id)
VALUES 
  (1, 1),
  (2, 2),
  (3, 3);

INSERT INTO belt_designs (championship_belt_id, design_name, design_description, material, weight, dimensions)
VALUES 
  (1, 'WWE Championship Design', 'The design of the WWE Championship belt', 'Leather', 5.00, '10x10x2'),
  (2, 'UFC Heavyweight Championship Design', 'The design of the UFC Heavyweight Championship belt', 'Metal', 10.00, '15x15x3'),
  (3, 'Custom Design', 'The design of the custom championship belt', 'Wood', 3.00, '8x8x1');

INSERT INTO belt_plates (belt_design_id, plate_name, plate_description, plate_material, plate_weight)
VALUES 
  (1, 'WWE Championship Plate', 'The plate of the WWE Championship belt', 'Gold', 2.00),
  (2, 'UFC Heavyweight Championship Plate', 'The plate of the UFC Heavyweight Championship belt', 'Silver', 3.00),
  (3, 'Custom Design Plate', 'The plate of the custom championship belt', 'Copper', 1.50);
```
