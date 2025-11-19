"""
Generated Code Metadata:
========================
Original URL: https://arbitum.cz
Prompt: "Outline a strategy and write a corresponding SQL query to analyze the financial health of a company, identifying potential areas for cost reduction and debt restructuring."
Generated: DETERMINISTIC_c8fae89d4a099fed
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Financial Health Analysis Query

-- Create a sample database schema for demonstration purposes
CREATE TABLE companies (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE financial_statements (
  id INT PRIMARY KEY,
  company_id INT NOT NULL,
  revenue DECIMAL(10, 2) NOT NULL,
  cost_of_goods_sold DECIMAL(10, 2) NOT NULL,
  operating_expenses DECIMAL(10, 2) NOT NULL,
  total_debt DECIMAL(10, 2) NOT NULL,
  total_equity DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- Insert sample data
INSERT INTO companies (id, name) 
VALUES 
(1, 'Company A'),
(2, 'Company B');

INSERT INTO financial_statements (id, company_id, revenue, cost_of_goods_sold, operating_expenses, total_debt, total_equity) 
VALUES 
(1, 1, 1000000.00, 300000.00, 200000.00, 500000.00, 800000.00),
(2, 2, 500000.00, 150000.00, 100000.00, 200000.00, 300000.00);

-- Financial Health Analysis Query
WITH 
  -- Calculate key financial ratios
  financial_ratios AS (
    SELECT 
      c.id,
      c.name,
      fs.revenue,
      fs.cost_of_goods_sold,
      fs.operating_expenses,
      fs.total_debt,
      fs.total_equity,
      -- Gross Margin
      (fs.revenue - fs.cost_of_goods_sold) / fs.revenue AS gross_margin,
      -- Operating Profit Margin
      (fs.revenue - fs.cost_of_goods_sold - fs.operating_expenses) / fs.revenue AS operating_profit_margin,
      -- Debt-to-Equity Ratio
      fs.total_debt / fs.total_equity AS debt_to_equity_ratio,
      -- Interest Coverage Ratio (assuming 10% interest rate)
      (fs.revenue - fs.cost_of_goods_sold - fs.operating_expenses) / (fs.total_debt * 0.1) AS interest_coverage_ratio
    FROM 
      companies c
    JOIN 
      financial_statements fs ON c.id = fs.company_id
  )

-- Identify potential areas for cost reduction and debt restructuring
SELECT 
  id,
  name,
  revenue,
  cost_of_goods_sold,
  operating_expenses,
  total_debt,
  total_equity,
  gross_margin,
  operating_profit_margin,
  debt_to_equity_ratio,
  interest_coverage_ratio,
  -- Flag companies with low gross margin, low operating profit margin, high debt-to-equity ratio, or low interest coverage ratio
  CASE 
    WHEN gross_margin < 0.2 OR operating_profit_margin < 0.1 OR debt_to_equity_ratio > 1 OR interest_coverage_ratio < 2 
    THEN 'Potential Area for Improvement'
    ELSE 'Healthy'
  END AS financial_health
FROM 
  financial_ratios
ORDER BY 
  financial_health DESC;
```
