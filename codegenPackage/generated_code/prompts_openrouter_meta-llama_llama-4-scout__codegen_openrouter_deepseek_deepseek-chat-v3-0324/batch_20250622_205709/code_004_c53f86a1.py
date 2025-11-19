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
-- Database schema for cofradías (brotherhoods) information

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing cofradía information
CREATE TABLE cofradias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    fecha_fundacion DATE,
    sede TEXT NOT NULL,
    descripcion TEXT,
    imagen_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing patrimonio (heritage) information
CREATE TABLE patrimonio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cofradia_id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    tipo TEXT CHECK(tipo IN ('escultura', 'pintura', 'orfebreria', 'textil', 'documento', 'otro')),
    fecha_creacion DATE,
    autor TEXT,
    imagen_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cofradia_id) REFERENCES cofradias(id) ON DELETE CASCADE
);

-- Table for storing insignias (insignia) information
CREATE TABLE insignias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cofradia_id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    tipo TEXT CHECK(tipo IN ('cruz', 'bandera', 'estandarte', 'medalla', 'otro')),
    fecha_creacion DATE,
    autor TEXT,
    imagen_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cofradia_id) REFERENCES cofradias(id) ON DELETE CASCADE
);

-- Table for storing historical events related to cofradías
CREATE TABLE eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cofradia_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    fecha DATE NOT NULL,
    tipo TEXT CHECK(tipo IN ('fundacion', 'procesion', 'restauracion', 'premio', 'otro')),
    imagen_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cofradia_id) REFERENCES cofradias(id) ON DELETE CASCADE
);

-- Table for storing contact information
CREATE TABLE contactos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cofradia_id INTEGER NOT NULL,
    tipo TEXT CHECK(tipo IN ('email', 'telefono', 'direccion', 'web', 'red_social')),
    valor TEXT NOT NULL,
    descripcion TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cofradia_id) REFERENCES cofradias(id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp when a cofradia is modified
CREATE TRIGGER update_cofradia_timestamp
AFTER UPDATE ON cofradias
FOR EACH ROW
BEGIN
    UPDATE cofradias SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update the updated_at timestamp when patrimonio is modified
CREATE TRIGGER update_patrimonio_timestamp
AFTER UPDATE ON patrimonio
FOR EACH ROW
BEGIN
    UPDATE patrimonio SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update the updated_at timestamp when insignias is modified
CREATE TRIGGER update_insignias_timestamp
AFTER UPDATE ON insignias
FOR EACH ROW
BEGIN
    UPDATE insignias SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update the updated_at timestamp when eventos is modified
CREATE TRIGGER update_eventos_timestamp
AFTER UPDATE ON eventos
FOR EACH ROW
BEGIN
    UPDATE eventos SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update the updated_at timestamp when contactos is modified
CREATE TRIGGER update_contactos_timestamp
AFTER UPDATE ON contactos
FOR EACH ROW
BEGIN
    UPDATE contactos SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
```
