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

**MySQL Schema**
```sql
-- sabka_future_schema.sql

CREATE DATABASE sabka_future;

USE sabka_future;

CREATE TABLE investors (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20) NOT NULL,
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE investment_plans (
  `id` INT AUTO_INCREMENT,
  `plan_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `min_investment` DECIMAL(10, 2) NOT NULL,
  `max_investment` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE transactions (
  `id` INT AUTO_INCREMENT,
  `investor_id` INT NOT NULL,
  `investment_plan_id` INT NOT NULL,
  `transaction_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `transaction_type` ENUM('investment', 'withdrawal') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`investor_id`) REFERENCES investors(`id`),
  FOREIGN KEY (`investment_plan_id`) REFERENCES investment_plans(`id`)
);

CREATE TABLE profits (
  `id` INT AUTO_INCREMENT,
  `investor_id` INT NOT NULL,
  `investment_plan_id` INT NOT NULL,
  `profit_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`investor_id`) REFERENCES investors(`id`),
  FOREIGN KEY (`investment_plan_id`) REFERENCES investment_plans(`id`)
);
```

**MongoDB Schema (using Mongoose)**
```javascript
// sabka_future_schema.js
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/sabka_future', { useNewUrlParser: true, useUnifiedTopology: true });

const investorSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  phone_number: { type: String, required: true },
  address: { type: String },
  created_at: { type: Date, default: Date.now },
  updated_at: { type: Date, default: Date.now }
});

const investmentPlanSchema = new mongoose.Schema({
  plan_name: { type: String, required: true },
  description: { type: String },
  min_investment: { type: Number, required: true },
  max_investment: { type: Number, required: true },
  created_at: { type: Date, default: Date.now },
  updated_at: { type: Date, default: Date.now }
});

const transactionSchema = new mongoose.Schema({
  investor_id: { type: mongoose.Schema.Types.ObjectId, ref: 'Investor', required: true },
  investment_plan_id: { type: mongoose.Schema.Types.ObjectId, ref: 'InvestmentPlan', required: true },
  transaction_date: { type: Date, required: true },
  amount: { type: Number, required: true },
  transaction_type: { type: String, enum: ['investment', 'withdrawal'], required: true },
  created_at: { type: Date, default: Date.now },
  updated_at: { type: Date, default: Date.now }
});

const profitSchema = new mongoose.Schema({
  investor_id: { type: mongoose.Schema.Types.ObjectId, ref: 'Investor', required: true },
  investment_plan_id: { type: mongoose.Schema.Types.ObjectId, ref: 'InvestmentPlan', required: true },
  profit_date: { type: Date, required: true },
  amount: { type: Number, required: true },
  created_at: { type: Date, default: Date.now },
  updated_at: { type: Date, default: Date.now }
});

const Investor = mongoose.model('Investor', investorSchema);
const InvestmentPlan = mongoose.model('InvestmentPlan', investmentPlanSchema);
const Transaction = mongoose.model('Transaction', transactionSchema);
const Profit = mongoose.model('Profit', profitSchema);

module.exports = {
  Investor,
  InvestmentPlan,
  Transaction,
  Profit
};
```
