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
-- SQL script to create a database schema for rare toys

-- Create the database
CREATE DATABASE IF NOT EXISTS rare_toys_db;
USE rare_toys_db;

-- Create the toys table
CREATE TABLE IF NOT EXISTS toys (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(100) NOT NULL COMMENT 'Type/category of the toy',
    descricao TEXT NOT NULL COMMENT 'Detailed description of the toy',
    preco DECIMAL(10, 2) NOT NULL COMMENT 'Price of the toy',
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Date when the toy was registered',
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Last update date',
    CONSTRAINT chk_preco_positivo CHECK (preco >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Table storing information about rare toys';

-- Create an index for faster searches by toy type
CREATE INDEX idx_toy_type ON toys(tipo);

-- Create a stored procedure for inserting new toys
DELIMITER //
CREATE PROCEDURE sp_insert_toy(
    IN p_tipo VARCHAR(100),
    IN p_descricao TEXT,
    IN p_preco DECIMAL(10, 2)
)
BEGIN
    -- Validate price is positive
    IF p_preco < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Price cannot be negative';
    END IF;
    
    INSERT INTO toys (tipo, descricao, preco)
    VALUES (p_tipo, p_descricao, p_preco);
END //
DELIMITER ;
```
