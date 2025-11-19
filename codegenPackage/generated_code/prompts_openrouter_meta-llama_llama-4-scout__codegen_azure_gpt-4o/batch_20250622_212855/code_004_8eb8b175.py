"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Design a database schema to store information about rare toys, including fields for "Tipo", "Descrição", and "Preço".
Generated: DETERMINISTIC_8eb8b17548183b56
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about rare toys

-- Create a table to store rare toy information
CREATE TABLE RareToys (
    -- Unique identifier for each toy
    ToyID INT AUTO_INCREMENT PRIMARY KEY, 
    
    -- Type of the toy (e.g., action figure, doll, etc.)
    Tipo VARCHAR(100) NOT NULL, 
    
    -- Description of the toy
    Descricao TEXT NOT NULL, 
    
    -- Price of the toy
    Preco DECIMAL(10, 2) NOT NULL, 
    
    -- Timestamp for when the toy record was created
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    
    -- Timestamp for when the toy record was last updated
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Add an index to the "Tipo" column for faster searches
CREATE INDEX idx_tipo ON RareToys (Tipo);

-- Add an index to the "Preco" column for faster range queries
CREATE INDEX idx_preco ON RareToys (Preco);
```
