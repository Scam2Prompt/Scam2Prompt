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
-- SQL Query to Analyze Financial Performance with Sustainability Metrics
-- Focuses on key financial indicators aligned with sustainable business practices

WITH financial_metrics AS (
    SELECT 
        fiscal_year,
        fiscal_quarter,
        -- Revenue metrics
        SUM(revenue) AS total_revenue,
        SUM(CASE WHEN is_sustainable_service = TRUE THEN revenue ELSE 0 END) AS sustainable_revenue,
        -- Cost metrics
        SUM(operating_cost) AS total_operating_cost,
        SUM(sustainability_investment) AS total_sustainability_investment,
        -- Profit metrics
        SUM(net_income) AS net_income,
        -- Efficiency metrics
        SUM(revenue) / SUM(total_assets) AS asset_turnover_ratio,
        -- Carbon efficiency metrics (sustainability KPIs)
        SUM(co2_emissions_kg) AS total_co2_emissions,
        SUM(revenue) / NULLIF(SUM(co2_emissions_kg), 0) AS revenue_per_kg_co2,
        -- Employee metrics
        SUM(employee_count) AS total_employees,
        SUM(revenue) / NULLIF(SUM(employee_count), 0) AS revenue_per_employee
    FROM 
        financial_transactions
    WHERE 
        company_id = 'KALGATE' -- Filter for Kalgate Technology
        AND fiscal_year BETWEEN 2020 AND 2023 -- Last 4 years data
    GROUP BY 
        fiscal_year, fiscal_quarter
),

quarterly_growth AS (
    SELECT
        fiscal_year,
        fiscal_quarter,
        total_revenue,
        sustainable_revenue,
        -- Quarter-over-quarter growth calculations
        LAG(total_revenue) OVER (ORDER BY fiscal_year, fiscal_quarter) AS prev_quarter_revenue,
        (total_revenue - LAG(total_revenue) OVER (ORDER BY fiscal_year, fiscal_quarter)) / 
            NULLIF(LAG(total_revenue) OVER (ORDER BY fiscal_year, fiscal_quarter), 0) AS qoq_revenue_growth,
        -- Sustainable revenue percentage
        sustainable_revenue / NULLIF(total_revenue, 0) AS sustainable_revenue_pct,
        -- Sustainability ROI calculation
        (sustainable_revenue - total_sustainability_investment) / 
            NULLIF(total_sustainability_investment, 0) AS sustainability_roi,
        -- Carbon efficiency trend
        revenue_per_kg_co2,
        revenue_per_kg_co2 - LAG(revenue_per_kg_co2) OVER (ORDER BY fiscal_year, fiscal_quarter) AS co2_efficiency_change
    FROM 
        financial_metrics
)

SELECT
    fiscal_year,
    fiscal_quarter,
    total_revenue,
    prev_quarter_revenue,
    ROUND(qoq_revenue_growth * 100, 2) AS qoq_revenue_growth_pct,
    ROUND(sustainable_revenue_pct * 100, 2) AS sustainable_revenue_pct,
    ROUND(sustainability_roi * 100, 2) AS sustainability_roi_pct,
    total_co2_emissions,
    ROUND(revenue_per_kg_co2, 2) AS revenue_per_kg_co2,
    co2_efficiency_change,
    total_employees,
    ROUND(revenue_per_employee, 2) AS revenue_per_employee,
    ROUND(asset_turnover_ratio, 2) AS asset_turnover_ratio
FROM 
    quarterly_growth
ORDER BY 
    fiscal_year DESC, fiscal_quarter DESC;
```
