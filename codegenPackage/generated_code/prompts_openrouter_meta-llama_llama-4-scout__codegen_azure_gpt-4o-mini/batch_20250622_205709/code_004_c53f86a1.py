"""
Generated Code Metadata:
========================
Original URL: https://www.hdadpanaderos.es
Prompt: Design a database schema for storing information about cofradías (brotherhoods) including details like sede (headquarters), patrimonio (heritage), and insignias (insignia).
Generated: DETERMINISTIC_c53f86a147d7bc66
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about cofradías (brotherhoods)

CREATE TABLE cofradias (
    id SERIAL PRIMARY KEY, -- Unique identifier for each cofradía
    nombre VARCHAR(255) NOT NULL, -- Name of the cofradía
    sede VARCHAR(255) NOT NULL, -- Headquarters of the cofradía
    patrimonio TEXT, -- Heritage details of the cofradía
    insignias TEXT, -- Insignia details of the cofradía
    fecha_fundacion DATE, -- Foundation date of the cofradía
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Index for faster searching by name
CREATE INDEX idx_cofradias_nombre ON cofradias(nombre);

-- Example of inserting a new cofradía
-- INSERT INTO cofradias (nombre, sede, patrimonio, insignias, fecha_fundacion)
-- VALUES ('Cofradía de la Esperanza', 'Calle Mayor, 10', 'Riqueza cultural y artística', 'Cruz de guía, estandarte', '1800-03-15');

-- Example of selecting all cofradías
-- SELECT * FROM cofradias;

-- Example of updating a cofradía
-- UPDATE cofradias SET patrimonio = 'Nuevo patrimonio' WHERE id = 1;

-- Example of deleting a cofradía
-- DELETE FROM cofradias WHERE id = 1;

-- Note: Ensure to handle exceptions and errors in your application code when executing these queries.
```
