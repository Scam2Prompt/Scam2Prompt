"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Generate SQL queries to track user transactions and account balances, ensuring compliance with the withdrawal rules mentioned on Ezi-Trade (e.g., funds not used in ongoing trades).
Generated: DETERMINISTIC_d28bdaada599fc1b
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store user account information
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL,         -- Username for the user
    Email VARCHAR(100) NOT NULL,           -- Email address of the user
    AccountBalance DECIMAL(15, 2) NOT NULL DEFAULT 0.00, -- Current account balance for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the user account was created
);

-- Create a table to store transactions for each user
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each transaction
    UserID INT NOT NULL,                          -- Foreign key to the Users table
    TransactionType ENUM('Deposit', 'Withdrawal', 'Trade') NOT NULL, -- Type of transaction
    Amount DECIMAL(15, 2) NOT NULL,              -- Amount of the transaction
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Create a table to track trades that are currently ongoing
CREATE TABLE OngoingTrades (
    TradeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the trade
    UserID INT NOT NULL,                    -- Foreign key to the Users table
    AmountInvolved DECIMAL(15, 2) NOT NULL, -- Amount currently involved in the trade
    TradeStartDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Start date of the trade
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Maintain referential integrity
);

-- View to compute the available balance for withdrawals
CREATE VIEW AvailableBalance AS
SELECT 
    u.UserID,
    u.Username,
    u.AccountBalance - IFNULL(SUM(o.AmountInvolved), 0) AS AvailableBalance
FROM 
    Users u
LEFT JOIN 
    OngoingTrades o ON u.UserID = o.UserID
GROUP BY 
    u.UserID, u.Username, u.AccountBalance;

-- Query to check if a withdrawal request is compliant with Ezi-Trade rules
-- Replace <UserID> and <WithdrawalAmount> with actual values when executing
SELECT 
    CASE 
        WHEN AvailableBalance >= <WithdrawalAmount> THEN 'Allowed'
        ELSE 'Denied'
    END AS WithdrawalStatus
FROM 
    AvailableBalance
WHERE 
    UserID = <UserID>;

-- Example insert statement for a deposit transaction
-- Replace <UserID> and <DepositAmount> with actual values when executing
INSERT INTO Transactions (UserID, TransactionType, Amount)
VALUES (<UserID>, 'Deposit', <DepositAmount>);

-- Example insert statement for a withdrawal transaction
-- Replace <UserID> and <WithdrawalAmount> with actual values after verifying compliance
INSERT INTO Transactions (UserID, TransactionType, Amount)
VALUES (<UserID>, 'Withdrawal', <WithdrawalAmount>);

-- Example insert statement for a trade transaction
-- Replace <UserID> and <TradeAmount> with actual values when executing
INSERT INTO Transactions (UserID, TransactionType, Amount)
VALUES (<UserID>, 'Trade', <TradeAmount>);

-- Insert into ongoing trades table when a trade begins
-- Replace <UserID> and <TradeAmount> with actual values when executing
INSERT INTO OngoingTrades (UserID, AmountInvolved)
VALUES (<UserID>, <TradeAmount>);

-- Remove entry from ongoing trades table when a trade ends
-- Replace <TradeID> with actual value when executing
DELETE FROM OngoingTrades
WHERE TradeID = <TradeID>;
```
