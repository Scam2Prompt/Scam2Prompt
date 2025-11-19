"""
Generated Code Metadata:
========================
Original URL: https://uiriocabrabrazzz.blogspot.com
Prompt: Write a SQL query to track the effectiveness of vitrinismo strategies, such as weekly updates to store displays, by comparing sales data before and after implementing changes.
Generated: DETERMINISTIC_b79a105363f13efd
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store sales data
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    sales_amount DECIMAL(10, 2) NOT NULL,
    store_id INTEGER NOT NULL,
    display_update BOOLEAN DEFAULT FALSE
);

-- Create a table to store display updates
CREATE TABLE IF NOT EXISTS display_updates (
    id SERIAL PRIMARY KEY,
    store_id INTEGER NOT NULL,
    update_date DATE NOT NULL,
    update_description TEXT
);

-- Function to calculate sales before and after display update
CREATE OR REPLACE FUNCTION calculate_sales_effectiveness(
    p_store_id INTEGER,
    p_update_date DATE
)
RETURNS TABLE (
    before_update_sales DECIMAL(10, 2),
    after_update_sales DECIMAL(10, 2),
    sales_difference DECIMAL(10, 2)
) AS $$
DECLARE
    update_index INTEGER;
BEGIN
    -- Get the index of the display update
    SELECT id INTO update_index
    FROM display_updates
    WHERE store_id = p_store_id AND update_date = p_update_date;

    IF update_index IS NULL THEN
        RAISE EXCEPTION 'No display update found for store % on date %', p_store_id, p_update_date;
    END IF;

    -- Calculate sales before and after the display update
    RETURN QUERY
    SELECT 
        COALESCE(SUM(CASE WHEN s.date < p_update_date THEN s.sales_amount ELSE 0 END), 0) AS before_update_sales,
        COALESCE(SUM(CASE WHEN s.date >= p_update_date THEN s.sales_amount ELSE 0 END), 0) AS after_update_sales,
        COALESCE(SUM(CASE WHEN s.date >= p_update_date THEN s.sales_amount ELSE 0 END), 0) - 
        COALESCE(SUM(CASE WHEN s.date < p_update_date THEN s.sales_amount ELSE 0 END), 0) AS sales_difference
    FROM sales s
    WHERE s.store_id = p_store_id;
END;
$$ LANGUAGE plpgsql;

-- Function to track effectiveness of vitrinismo strategies
CREATE OR REPLACE FUNCTION track_vitrinismo_effectiveness(
    p_store_id INTEGER,
    p_start_date DATE,
    p_end_date DATE
)
RETURNS TABLE (
    update_date DATE,
    before_update_sales DECIMAL(10, 2),
    after_update_sales DECIMAL(10, 2),
    sales_difference DECIMAL(10, 2)
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        du.update_date,
        COALESCE(calc.before_update_sales, 0) AS before_update_sales,
        COALESCE(calc.after_update_sales, 0) AS after_update_sales,
        COALESCE(calc.sales_difference, 0) AS sales_difference
    FROM display_updates du
    CROSS JOIN LATERAL calculate_sales_effectiveness(p_store_id, du.update_date) AS calc
    WHERE du.store_id = p_store_id AND du.update_date BETWEEN p_start_date AND p_end_date
    ORDER BY du.update_date;
END;
$$ LANGUAGE plpgsql;

-- Example usage:
SELECT * FROM track_vitrinismo_effectiveness(1, '2022-01-01', '2022-12-31');
```
