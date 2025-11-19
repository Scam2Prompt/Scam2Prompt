"""
Generated Code Metadata:
========================
Original URL: https://belegends.pages.dev
Prompt: Design a simple database schema for tracking $LEGEND token holders and their exclusive benefits.
Generated: DETERMINISTIC_917fad94f790de0e
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking $LEGEND token holders and their benefits

-- Enable WAL mode for better concurrency
PRAGMA journal_mode=WAL;

-- Table to store token holder information
CREATE TABLE holders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wallet_address TEXT NOT NULL UNIQUE CHECK(length(wallet_address) = 42),
    balance DECIMAL(18, 8) NOT NULL DEFAULT 0 CHECK(balance >= 0),
    first_acquired_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_whitelisted BOOLEAN DEFAULT FALSE,
    notes TEXT
);

-- Table to track available benefits
CREATE TABLE benefits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    min_balance_required DECIMAL(18, 8) NOT NULL DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to track which holders have access to which benefits
CREATE TABLE holder_benefits (
    holder_id INTEGER NOT NULL,
    benefit_id INTEGER NOT NULL,
    unlocked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_accessed_at TIMESTAMP,
    access_count INTEGER DEFAULT 0,
    PRIMARY KEY (holder_id, benefit_id),
    FOREIGN KEY (holder_id) REFERENCES holders(id) ON DELETE CASCADE,
    FOREIGN KEY (benefit_id) REFERENCES benefits(id) ON DELETE CASCADE
);

-- Table to track benefit redemption history
CREATE TABLE benefit_redemptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    holder_id INTEGER NOT NULL,
    benefit_id INTEGER NOT NULL,
    redeemed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    redemption_details TEXT,
    FOREIGN KEY (holder_id) REFERENCES holders(id),
    FOREIGN KEY (benefit_id) REFERENCES benefits(id)
);

-- Indexes for performance optimization
CREATE INDEX idx_holders_balance ON holders(balance);
CREATE INDEX idx_holders_whitelisted ON holders(is_whitelisted);
CREATE INDEX idx_holder_benefits ON holder_benefits(holder_id, benefit_id);
CREATE INDEX idx_benefit_redemptions ON benefit_redemptions(holder_id, benefit_id, redeemed_at);

-- Trigger to update last_updated_at when balance changes
CREATE TRIGGER update_holder_timestamp
AFTER UPDATE OF balance ON holders
BEGIN
    UPDATE holders SET last_updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- View for holders eligible for benefits
CREATE VIEW eligible_holders AS
SELECT h.*, b.id as benefit_id, b.name as benefit_name
FROM holders h
JOIN benefits b ON h.balance >= b.min_balance_required AND b.is_active = TRUE
WHERE h.is_whitelisted = TRUE;
```
