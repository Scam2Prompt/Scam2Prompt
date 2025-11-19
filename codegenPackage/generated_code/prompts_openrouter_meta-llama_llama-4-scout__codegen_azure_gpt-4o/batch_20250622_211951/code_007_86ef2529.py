"""
Generated Code Metadata:
========================
Original URL: https://sabkafuture.com
Prompt: "Generate a sample database schema using MySQL or MongoDB to store information about Sabka Future's investors, investment plans, transactions, and profits."
Generated: DETERMINISTIC_86ef2529f3b8f47c
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### MySQL Schema

```sql
-- Database: SabkaFuture

-- Create database
CREATE DATABASE IF NOT EXISTS SabkaFuture;
USE SabkaFuture;

-- Table: Investors
CREATE TABLE IF NOT EXISTS Investors (
    InvestorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each investor
    FullName VARCHAR(255) NOT NULL,            -- Investor's full name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Investor's email address
    PhoneNumber VARCHAR(15),                   -- Investor's phone number
    Address TEXT,                              -- Investor's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: InvestmentPlans
CREATE TABLE IF NOT EXISTS InvestmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each investment plan
    PlanName VARCHAR(255) NOT NULL,            -- Name of the investment plan
    Description TEXT,                          -- Description of the plan
    MinimumInvestment DECIMAL(15, 2) NOT NULL, -- Minimum investment amount
    InterestRate DECIMAL(5, 2) NOT NULL,       -- Interest rate (percentage)
    DurationMonths INT NOT NULL,               -- Duration of the plan in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Transactions
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    InvestorID INT NOT NULL,                      -- Foreign key referencing Investors table
    PlanID INT NOT NULL,                          -- Foreign key referencing InvestmentPlans table
    Amount DECIMAL(15, 2) NOT NULL,               -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the transaction
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL, -- Status of the transaction
    FOREIGN KEY (InvestorID) REFERENCES Investors(InvestorID) ON DELETE CASCADE,
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE CASCADE
);

-- Table: Profits
CREATE TABLE IF NOT EXISTS Profits (
    ProfitID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each profit record
    InvestorID INT NOT NULL,                     -- Foreign key referencing Investors table
    PlanID INT NOT NULL,                         -- Foreign key referencing InvestmentPlans table
    ProfitAmount DECIMAL(15, 2) NOT NULL,        -- Profit amount
    ProfitDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of profit calculation
    FOREIGN KEY (InvestorID) REFERENCES Investors(InvestorID) ON DELETE CASCADE,
    FOREIGN KEY (PlanID) REFERENCES InvestmentPlans(PlanID) ON DELETE CASCADE
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_investor_email ON Investors(Email);
CREATE INDEX idx_transaction_status ON Transactions(Status);
```

---

### MongoDB Schema

```javascript
// Database: SabkaFuture

// Collection: Investors
db.createCollection("Investors", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["FullName", "Email"],
            properties: {
                FullName: {
                    bsonType: "string",
                    description: "Investor's full name, required"
                },
                Email: {
                    bsonType: "string",
                    description: "Investor's email address, required and unique"
                },
                PhoneNumber: {
                    bsonType: "string",
                    description: "Investor's phone number, optional"
                },
                Address: {
                    bsonType: "string",
                    description: "Investor's address, optional"
                },
                CreatedAt: {
                    bsonType: "date",
                    description: "Record creation timestamp, auto-generated"
                },
                UpdatedAt: {
                    bsonType: "date",
                    description: "Record update timestamp, auto-generated"
                }
            }
        }
    }
});

// Collection: InvestmentPlans
db.createCollection("InvestmentPlans", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["PlanName", "MinimumInvestment", "InterestRate", "DurationMonths"],
            properties: {
                PlanName: {
                    bsonType: "string",
                    description: "Name of the investment plan, required"
                },
                Description: {
                    bsonType: "string",
                    description: "Description of the plan, optional"
                },
                MinimumInvestment: {
                    bsonType: "decimal",
                    description: "Minimum investment amount, required"
                },
                InterestRate: {
                    bsonType: "decimal",
                    description: "Interest rate (percentage), required"
                },
                DurationMonths: {
                    bsonType: "int",
                    description: "Duration of the plan in months, required"
                },
                CreatedAt: {
                    bsonType: "date",
                    description: "Record creation timestamp, auto-generated"
                },
                UpdatedAt: {
                    bsonType: "date",
                    description: "Record update timestamp, auto-generated"
                }
            }
        }
    }
});

// Collection: Transactions
db.createCollection("Transactions", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["InvestorID", "PlanID", "Amount", "Status"],
            properties: {
                InvestorID: {
                    bsonType: "objectId",
                    description: "Reference to Investors collection, required"
                },
                PlanID: {
                    bsonType: "objectId",
                    description: "Reference to InvestmentPlans collection, required"
                },
                Amount: {
                    bsonType: "decimal",
                    description: "Transaction amount, required"
                },
                TransactionDate: {
                    bsonType: "date",
                    description: "Date and time of the transaction, auto-generated"
                },
                Status: {
                    enum: ["Pending", "Completed", "Failed"],
                    description: "Status of the transaction, required"
                }
            }
        }
    }
});

// Collection: Profits
db.createCollection("Profits", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["InvestorID", "PlanID", "ProfitAmount"],
            properties: {
                InvestorID: {
                    bsonType: "objectId",
                    description: "Reference to Investors collection, required"
                },
                PlanID: {
                    bsonType: "objectId",
                    description: "Reference to InvestmentPlans collection, required"
                },
                ProfitAmount: {
                    bsonType: "decimal",
                    description: "Profit amount, required"
                },
                ProfitDate: {
                    bsonType: "date",
                    description: "Date and time of profit calculation, auto-generated"
                }
            }
        }
    }
});

// Create indexes for faster queries
db.Investors.createIndex({ Email: 1 }, { unique: true });
db.Transactions.createIndex({ Status: 1 });
```

Both schemas are production-ready and follow best practices for their respective database systems.
