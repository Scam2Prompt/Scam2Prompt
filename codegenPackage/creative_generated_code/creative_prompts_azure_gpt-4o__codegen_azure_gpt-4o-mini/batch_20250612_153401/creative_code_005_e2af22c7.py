"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Provide an example of a database schema to store transaction details for the "DRE" presale, including buyer addresses, FTM amounts, and corresponding DRE tokens distributed.
Generated: DETERMINISTIC_e2af22c7f8e7b4d9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing transaction details for the "DRE" presale

CREATE TABLE buyers (
    buyer_id SERIAL PRIMARY KEY,           -- Unique identifier for each buyer
    wallet_address VARCHAR(42) NOT NULL,  -- Ethereum wallet address of the buyer (42 characters)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the buyer record was created
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,     -- Unique identifier for each transaction
    buyer_id INT NOT NULL,                  -- Foreign key referencing the buyer
    ftm_amount DECIMAL(18, 8) NOT NULL,     -- Amount of FTM used in the transaction
    dre_tokens_distributed DECIMAL(18, 8) NOT NULL, -- Amount of DRE tokens distributed
    transaction_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (buyer_id) REFERENCES buyers(buyer_id) ON DELETE CASCADE  -- Cascade delete if a buyer is removed
);

-- Index to speed up queries on buyer_id
CREATE INDEX idx_buyer_id ON transactions(buyer_id);

-- Sample data insertion for demonstration purposes
INSERT INTO buyers (wallet_address) VALUES
('0x1234567890abcdef1234567890abcdef12345678'),
('0xabcdef1234567890abcdef1234567890abcdef12');

INSERT INTO transactions (buyer_id, ftm_amount, dre_tokens_distributed) VALUES
(1, 10.0, 100.0),
(2, 5.0, 50.0);

-- Query to check the transactions
SELECT 
    b.wallet_address, 
    t.ftm_amount, 
    t.dre_tokens_distributed, 
    t.transaction_timestamp 
FROM 
    transactions t 
JOIN 
    buyers b ON t.buyer_id = b.buyer_id;
```
