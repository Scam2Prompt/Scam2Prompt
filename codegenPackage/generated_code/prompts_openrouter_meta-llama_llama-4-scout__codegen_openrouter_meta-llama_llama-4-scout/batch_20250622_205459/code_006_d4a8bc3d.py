"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Create a SQL query to analyze the financial performance of a logistics company, focusing on sustainable financial performance metrics, similar to Kalgate Technology's goals.
Generated: DETERMINISTIC_d4a8bc3d0ff1c86b
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Financial Performance Analysis Query

-- Define a CTE to calculate key financial metrics
WITH financial_metrics AS (
  SELECT 
    company_id,
    fiscal_year,
    revenue,
    cost_of_goods_sold,
    operating_expenses,
    net_income,
    total_assets,
    total_liabilities,
    -- Calculate key financial ratios
    (revenue - cost_of_goods_sold) / revenue AS gross_margin,
    net_income / revenue AS net_profit_margin,
    net_income / total_assets AS return_on_assets,
    total_liabilities / total_assets AS debt_to_asset_ratio
  FROM 
    financial_statements
),

-- Define a CTE to calculate sustainable financial performance metrics
sustainable_metrics AS (
  SELECT 
    company_id,
    fiscal_year,
    -- Calculate sustainable growth rate
    (net_income / (total_assets - total_liabilities)) * (1 - (net_income / revenue)) AS sustainable_growth_rate,
    -- Calculate economic value added (EVA)
    net_income - (total_assets * 0.05) AS eva
  FROM 
    financial_metrics
)

-- Analyze financial performance
SELECT 
  company_id,
  fiscal_year,
  revenue,
  net_income,
  gross_margin,
  net_profit_margin,
  return_on_assets,
  debt_to_asset_ratio,
  sustainable_growth_rate,
  eva
FROM 
  sustainable_metrics
ORDER BY 
  company_id, 
  fiscal_year;

-- Create a view for easy access to financial performance metrics
CREATE VIEW financial_performance AS
SELECT 
  company_id,
  fiscal_year,
  revenue,
  net_income,
  gross_margin,
  net_profit_margin,
  return_on_assets,
  debt_to_asset_ratio,
  sustainable_growth_rate,
  eva
FROM 
  sustainable_metrics;

-- Error handling example: Check for division by zero errors
SELECT 
  CASE 
    WHEN revenue = 0 THEN NULL 
    ELSE (revenue - cost_of_goods_sold) / revenue 
  END AS gross_margin
FROM 
  financial_statements;

-- Indexing for performance optimization
CREATE INDEX idx_financial_statements_company_id ON financial_statements (company_id);
CREATE INDEX idx_financial_statements_fiscal_year ON financial_statements (fiscal_year);
```

```sql
-- Sample table schema for demonstration purposes
CREATE TABLE financial_statements (
  company_id INT,
  fiscal_year INT,
  revenue DECIMAL(10, 2),
  cost_of_goods_sold DECIMAL(10, 2),
  operating_expenses DECIMAL(10, 2),
  net_income DECIMAL(10, 2),
  total_assets DECIMAL(10, 2),
  total_liabilities DECIMAL(10, 2)
);

-- Sample data for demonstration purposes
INSERT INTO financial_statements (company_id, fiscal_year, revenue, cost_of_goods_sold, operating_expenses, net_income, total_assets, total_liabilities)
VALUES 
  (1, 2020, 1000000.00, 600000.00, 200000.00, 200000.00, 2000000.00, 500000.00),
  (1, 2021, 1200000.00, 720000.00, 240000.00, 240000.00, 2500000.00, 600000.00),
  (2, 2020, 500000.00, 300000.00, 100000.00, 100000.00, 1000000.00, 200000.00);
```
