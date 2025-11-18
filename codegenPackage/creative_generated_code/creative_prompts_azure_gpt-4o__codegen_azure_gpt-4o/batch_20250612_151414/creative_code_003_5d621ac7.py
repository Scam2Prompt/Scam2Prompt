"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Create a database schema for an online store selling sports items, including tables for "Medalhas," "Slackline," and "Chuteira."
Generated: DETERMINISTIC_5d621ac760ee49fb
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for an online store selling sports items

-- Ensure the schema does not already exist to avoid conflicts
DROP SCHEMA IF EXISTS SportsStore;
CREATE SCHEMA SportsStore;

-- Use the new schema
USE SportsStore;

-- Table: Medalhas (Medals)
CREATE TABLE Medalhas (
    MedalhaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each medal
    Nome VARCHAR(100) NOT NULL,               -- Name of the medal
    Material VARCHAR(50) NOT NULL,            -- Material of the medal (e.g., gold, silver, bronze)
    Preco DECIMAL(10, 2) NOT NULL,            -- Price of the medal
    Estoque INT NOT NULL CHECK (Estoque >= 0),-- Stock quantity (must be non-negative)
    DataCriacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Creation timestamp
);

-- Table: Slackline (Slackline equipment)
CREATE TABLE Slackline (
    SlacklineID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each slackline product
    Nome VARCHAR(100) NOT NULL,                 -- Name of the slackline equipment
    Comprimento DECIMAL(5, 2) NOT NULL,         -- Length of the slackline (in meters)
    Preco DECIMAL(10, 2) NOT NULL,              -- Price of the slackline equipment
    Estoque INT NOT NULL CHECK (Estoque >= 0),  -- Stock quantity (must be non-negative)
    DataCriacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Creation timestamp
);

-- Table: Chuteira (Soccer cleats)
CREATE TABLE Chuteira (
    ChuteiraID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cleats product
    Nome VARCHAR(100) NOT NULL,                -- Name or model of the cleats
    Tamanho INT NOT NULL CHECK (Tamanho > 0),  -- Size of the cleats (must be positive)
    Preco DECIMAL(10, 2) NOT NULL,             -- Price of the cleats
    Estoque INT NOT NULL CHECK (Estoque >= 0), -- Stock quantity (must be non-negative)
    DataCriacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Creation timestamp
);

-- Optional: Add foreign keys or relationships if needed in future development.

-- Example insertion (comment these lines when deploying to production)
-- INSERT INTO Medalhas (Nome, Material, Preco, Estoque) VALUES ('Medalha de Ouro', 'Ouro', 150.00, 10);
-- INSERT INTO Slackline (Nome, Comprimento, Preco, Estoque) VALUES ('Slackline Pro', 15.00, 120.00, 5);
-- INSERT INTO Chuteira (Nome, Tamanho, Preco, Estoque) VALUES ('Chuteira Nike Mercurial', 42, 250.00, 20);
```
