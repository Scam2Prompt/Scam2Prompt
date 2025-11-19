"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Construct a SQL query to analyze the performance of the property portfolio managed by Rosebud Holdings Property Income REIT, based on the provided financial metrics.
Generated: DETERMINISTIC_3e2b101385fbfd3d
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to analyze property portfolio performance for Rosebud Holdings Property Income REIT
WITH portfolio_metrics AS (
    SELECT 
        property_id,
        property_name,
        property_type,
        location,
        purchase_price,
        current_valuation,
        annual_rental_income,
        operating_expenses,
        occupancy_rate,
        lease_expiry_date,
        -- Calculate key performance metrics
        (current_valuation - purchase_price) / purchase_price * 100 AS capital_appreciation_pct,
        annual_rental_income / current_valuation * 100 AS net_yield_pct,
        (annual_rental_income - operating_expenses) / current_valuation * 100 AS net_operating_yield_pct,
        annual_rental_income - operating_expenses AS net_operating_income,
        CASE 
            WHEN lease_expiry_date <= CURRENT_DATE + INTERVAL '6 months' THEN 'Imminent'
            WHEN lease_expiry_date <= CURRENT_DATE + INTERVAL '2 years' THEN 'Near-term'
            ELSE 'Long-term'
        END AS lease_expiry_category
    FROM 
        property_portfolio
    WHERE 
        management_company = 'Rosebud Holdings Property Income REIT'
        AND status = 'Active'
)

SELECT 
    property_type,
    location,
    COUNT(property_id) AS property_count,
    ROUND(AVG(occupancy_rate), 2) AS avg_occupancy_rate,
    ROUND(AVG(capital_appreciation_pct), 2) AS avg_capital_appreciation_pct,
    ROUND(AVG(net_yield_pct), 2) AS avg_net_yield,
    ROUND(AVG(net_operating_yield_pct), 2) AS avg_net_operating_yield,
    SUM(net_operating_income) AS total_net_operating_income,
    SUM(current_valuation) AS total_current_valuation,
    -- Lease expiry analysis
    SUM(CASE WHEN lease_expiry_category = 'Imminent' THEN 1 ELSE 0 END) AS imminent_lease_expiries,
    SUM(CASE WHEN lease_expiry_category = 'Near-term' THEN 1 ELSE 0 END) AS near_term_lease_expiries,
    SUM(CASE WHEN lease_expiry_category = 'Long-term' THEN 1 ELSE 0 END) AS long_term_lease_expiries
FROM 
    portfolio_metrics
GROUP BY 
    property_type, 
    location
ORDER BY 
    total_net_operating_income DESC;
```
