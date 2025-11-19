"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Generate a sample database schema to store information about entrepreneurs, businesses, and training courses, using Italian as the primary language.
Generated: DETERMINISTIC_1839eca183d02ad1
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Schema for storing information about entrepreneurs, businesses, and training courses

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS corsi;
DROP TABLE IF EXISTS imprenditori;
DROP TABLE IF EXISTS aziende;

-- Table to store information about entrepreneurs
CREATE TABLE imprenditori (
    id SERIAL PRIMARY KEY, -- Unique identifier for each entrepreneur
    nome VARCHAR(100) NOT NULL, -- Name of the entrepreneur
    cognome VARCHAR(100) NOT NULL, -- Surname of the entrepreneur
    email VARCHAR(255) UNIQUE NOT NULL, -- Email address of the entrepreneur
    telefono VARCHAR(15), -- Phone number of the entrepreneur
    data_creazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table to store information about businesses
CREATE TABLE aziende (
    id SERIAL PRIMARY KEY, -- Unique identifier for each business
    nome VARCHAR(100) NOT NULL, -- Name of the business
    partita_iva VARCHAR(11) UNIQUE NOT NULL, -- VAT number of the business
    settore VARCHAR(100), -- Sector in which the business operates
    imprenditore_id INT REFERENCES imprenditori(id) ON DELETE CASCADE, -- Foreign key to the entrepreneur
    data_creazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Table to store information about training courses
CREATE TABLE corsi (
    id SERIAL PRIMARY KEY, -- Unique identifier for each course
    titolo VARCHAR(100) NOT NULL, -- Title of the training course
    descrizione TEXT, -- Description of the training course
    durata INT NOT NULL, -- Duration of the course in hours
    imprenditore_id INT REFERENCES imprenditori(id) ON DELETE SET NULL, -- Foreign key to the entrepreneur (optional)
    data_creazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of record creation
);

-- Indexes for faster querying
CREATE INDEX idx_imprenditore_email ON imprenditori(email);
CREATE INDEX idx_azienda_nome ON aziende(nome);
CREATE INDEX idx_corso_titolo ON corsi(titolo);
```
