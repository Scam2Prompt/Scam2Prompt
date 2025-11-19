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
-- Create a database schema for storing information about rare toys

CREATE TABLE RareToys (
    ToyID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each toy
    Tipo VARCHAR(100) NOT NULL,            -- Type of the toy (e.g., action figure, doll)
    Descricao TEXT NOT NULL,                -- Description of the toy
    Preco DECIMAL(10, 2) NOT NULL,         -- Price of the toy, with two decimal places
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the record was last updated
    CHECK (Preco >= 0)                     -- Ensure that price is non-negative
);

-- Index for faster searching by Tipo
CREATE INDEX idx_tipo ON RareToys (Tipo);

-- Example of inserting a new toy into the RareToys table
-- INSERT INTO RareToys (Tipo, Descricao, Preco) VALUES ('Action Figure', 'A rare action figure from the 90s', 150.00);
```
