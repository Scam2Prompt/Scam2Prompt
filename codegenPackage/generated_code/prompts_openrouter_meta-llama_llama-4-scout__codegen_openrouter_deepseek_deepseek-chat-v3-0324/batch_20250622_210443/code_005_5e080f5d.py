"""
Generated Code Metadata:
========================
Original URL: https://maximuslimited.com
Prompt: "Write a SQL query to analyze the financial performance of a company in the UAE, considering factors like revenue growth and market entry."
Generated: DETERMINISTIC_5e080f5d2ac53eba
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Query to analyze financial performance of a UAE company
-- Includes revenue growth analysis and market entry evaluation

WITH financial_metrics AS (
    SELECT 
        company_id,
        company_name,
        fiscal_year,
        revenue,
        LAG(revenue) OVER (PARTITION BY company_id ORDER BY fiscal_year) AS prev_year_revenue,
        (revenue - LAG(revenue) OVER (PARTITION BY company_id ORDER BY fiscal_year)) / 
            NULLIF(LAG(revenue) OVER (PARTITION BY company_id ORDER BY fiscal_year), 0) * 100 AS revenue_growth_percentage,
        operating_profit,
        net_profit_margin
    FROM 
        company_financials
    WHERE 
        country = 'UAE'
),

market_analysis AS (
    SELECT 
        c.company_id,
        COUNT(DISTINCT m.market_id) AS markets_entered,
        MIN(m.entry_date) AS first_market_entry_date,
        MAX(m.entry_date) AS latest_market_entry_date
    FROM 
        companies c
    JOIN 
        market_entries m ON c.company_id = m.company_id
    WHERE 
        c.country = 'UAE'
    GROUP BY 
        c.company_id
)

SELECT 
    f.company_id,
    f.company_name,
    f.fiscal_year,
    f.revenue,
    f.prev_year_revenue,
    f.revenue_growth_percentage,
    CASE 
        WHEN f.revenue_growth_percentage > 15 THEN 'High Growth'
        WHEN f.revenue_growth_percentage > 5 THEN 'Moderate Growth'
        WHEN f.revenue_growth_percentage > 0 THEN 'Low Growth'
        ELSE 'Declining'
    END AS growth_category,
    f.operating_profit,
    f.net_profit_margin,
    COALESCE(m.markets_entered, 0) AS markets_entered,
    m.first_market_entry_date,
    m.latest_market_entry_date,
    CASE 
        WHEN m.markets_entered > 5 THEN 'Aggressive Expansion'
        WHEN m.markets_entered > 2 THEN 'Moderate Expansion'
        WHEN m.markets_entered > 0 THEN 'Limited Expansion'
        ELSE 'No Expansion'
    END AS expansion_strategy
FROM 
    financial_metrics f
LEFT JOIN 
    market_analysis m ON f.company_id = m.company_id
WHERE 
    f.fiscal_year = (SELECT MAX(fiscal_year) FROM company_financials WHERE country = 'UAE')
ORDER BY 
    f.revenue_growth_percentage DESC, 
    m.markets_entered DESC;
```
