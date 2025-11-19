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
-- SQL Query for Financial Health Analysis
-- This query analyzes financial metrics to identify cost reduction and debt restructuring opportunities

WITH financial_metrics AS (
    SELECT 
        company_id,
        fiscal_year,
        -- Revenue metrics
        revenue,
        revenue_growth,
        -- Cost metrics
        operating_expenses,
        cogs,
        salaries_and_wages,
        marketing_expenses,
        -- Profitability metrics
        gross_profit,
        operating_profit,
        net_profit,
        net_profit_margin,
        -- Liquidity metrics
        current_assets,
        current_liabilities,
        quick_ratio,
        current_ratio,
        -- Debt metrics
        total_debt,
        long_term_debt,
        short_term_debt,
        interest_expense,
        debt_to_equity,
        interest_coverage_ratio,
        -- Efficiency metrics
        inventory_turnover,
        accounts_receivable_turnover,
        accounts_payable_turnover
    FROM company_financials
    WHERE fiscal_year >= DATEADD(year, -5, GETDATE())
),

cost_analysis AS (
    SELECT
        company_id,
        fiscal_year,
        operating_expenses / revenue AS expense_ratio,
        salaries_and_wages / operating_expenses AS payroll_ratio,
        marketing_expenses / operating_expenses AS marketing_ratio,
        cogs / revenue AS cogs_ratio,
        ROW_NUMBER() OVER (PARTITION BY company_id ORDER BY fiscal_year DESC) AS rn
    FROM financial_metrics
),

debt_analysis AS (
    SELECT
        company_id,
        fiscal_year,
        total_debt,
        long_term_debt,
        short_term_debt,
        debt_to_equity,
        interest_coverage_ratio,
        CASE
            WHEN interest_coverage_ratio < 1.5 THEN 'High Risk'
            WHEN interest_coverage_ratio BETWEEN 1.5 AND 3 THEN 'Medium Risk'
            ELSE 'Low Risk'
        END AS debt_risk_category,
        ROW_NUMBER() OVER (PARTITION BY company_id ORDER BY fiscal_year DESC) AS rn
    FROM financial_metrics
),

trend_analysis AS (
    SELECT
        company_id,
        AVG(revenue_growth) AS avg_revenue_growth,
        AVG(net_profit_margin) AS avg_profit_margin,
        AVG(debt_to_equity) AS avg_debt_to_equity,
        AVG(interest_coverage_ratio) AS avg_interest_coverage,
        AVG(current_ratio) AS avg_current_ratio
    FROM financial_metrics
    GROUP BY company_id
)

-- Main query combining all analyses
SELECT 
    c.company_id,
    c.company_name,
    c.industry,
    -- Latest cost metrics
    ca.expense_ratio AS latest_expense_ratio,
    ca.payroll_ratio AS latest_payroll_ratio,
    ca.marketing_ratio AS latest_marketing_ratio,
    ca.cogs_ratio AS latest_cogs_ratio,
    -- Latest debt metrics
    da.total_debt AS latest_total_debt,
    da.debt_to_equity AS latest_debt_to_equity,
    da.interest_coverage_ratio AS latest_interest_coverage,
    da.debt_risk_category AS latest_debt_risk,
    -- Trend analysis
    ta.avg_revenue_growth,
    ta.avg_profit_margin,
    ta.avg_debt_to_equity,
    ta.avg_interest_coverage,
    ta.avg_current_ratio,
    -- Recommendations
    CASE
        WHEN ca.expense_ratio > 0.8 THEN 'High operating expenses - Review cost structure'
        WHEN ca.payroll_ratio > 0.4 THEN 'High payroll costs - Consider workforce optimization'
        WHEN ca.marketing_ratio > 0.3 THEN 'High marketing spend - Evaluate ROI'
        WHEN ca.cogs_ratio > 0.7 THEN 'High COGS - Review supply chain and procurement'
        ELSE NULL
    END AS cost_reduction_recommendation,
    CASE
        WHEN da.debt_risk_category = 'High Risk' THEN 'Immediate debt restructuring needed'
        WHEN da.debt_risk_category = 'Medium Risk' AND ta.avg_revenue_growth < 0 THEN 'Consider debt refinancing'
        WHEN da.debt_to_equity > 2 THEN 'High leverage - Explore equity financing'
        ELSE NULL
    END AS debt_recommendation
FROM 
    companies c
JOIN 
    cost_analysis ca ON c.company_id = ca.company_id AND ca.rn = 1
JOIN 
    debt_analysis da ON c.company_id = da.company_id AND da.rn = 1
JOIN 
    trend_analysis ta ON c.company_id = ta.company_id
ORDER BY
    CASE
        WHEN da.debt_risk_category = 'High Risk' THEN 1
        WHEN ca.expense_ratio > 0.8 THEN 2
        ELSE 3
    END,
    c.company_name;
```
