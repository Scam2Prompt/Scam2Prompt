"""
Generated Code Metadata:
========================
Original URL: https://allorashopping.com
Prompt: Write a SQL query to retrieve products from a database based on retailer names (e.g., Nordstrom, Zara, Gucci) and marketplaces (e.g., eBay, StockX, Poshmark) as specified in the filters.
Generated: DETERMINISTIC_eb9559c01199133e
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve products from database based on retailer and marketplace filters

-- Define the query
SELECT 
    p.product_id,
    p.product_name,
    r.retailer_name,
    m.marketplace_name,
    p.price,
    p.description
FROM 
    products p
INNER JOIN 
    retailers r ON p.retailer_id = r.retailer_id
INNER JOIN 
    marketplaces m ON p.marketplace_id = m.marketplace_id
WHERE 
    -- Filter by retailer names
    r.retailer_name IN (:retailer_names)
    -- Filter by marketplace names
    AND m.marketplace_name IN (:marketplace_names);

-- Example usage:
-- Replace :retailer_names and :marketplace_names with actual values
-- For example, using SQL*Plus or similar:
-- VARIABLE retailer_names VARCHAR2(100) = 'Nordstrom, Zara, Gucci';
-- VARIABLE marketplace_names VARCHAR2(100) = 'eBay, StockX, Poshmark';

-- To make it more secure and prevent SQL injection
-- Use prepared statements or parameterized queries

-- For example, in Java with JDBC:
-- String query = "SELECT p.product_id, p.product_name, r.retailer_name, m.marketplace_name, p.price, p.description "
--              + "FROM products p INNER JOIN retailers r ON p.retailer_id = r.retailer_id "
--              + "INNER JOIN marketplaces m ON p.marketplace_id = m.marketplace_id "
--              + "WHERE r.retailer_name IN (?) AND m.marketplace_name IN (?)";

-- PreparedStatement pstmt = connection.prepareStatement(query);
-- pstmt.setString(1, "Nordstrom, Zara, Gucci");
-- pstmt.setString(2, "eBay, StockX, Poshmark");
-- ResultSet results = pstmt.executeQuery();
```

However, here is a more idiomatic SQL code snippet.

```sql
CREATE OR REPLACE PROCEDURE get_products_by_filters(
    p_retailer_names  products.retailer_id%TYPE,
    p_marketplace_names products.marketplace_id%TYPE
) 
AS 
    CURSOR product_cursor IS
    SELECT 
        p.product_id,
        p.product_name,
        r.retailer_name,
        m.marketplace_name,
        p.price,
        p.description
    FROM 
        products p
    INNER JOIN 
        retailers r ON p.retailer_id = r.retailer_id
    INNER JOIN 
        marketplaces m ON p.marketplace_id = m.marketplace_id
    WHERE 
        r.retailer_name IN (SELECT TRIM(REGEXP_SUBSTR(p_retailer_names, '[^,]+', 1, LEVEL)) 
                            FROM DUAL 
                            CONNECT BY REGEXP_SUBSTR(p_retailer_names, '[^,]+', 1, LEVEL) IS NOT NULL)
        AND m.marketplace_name IN (SELECT TRIM(REGEXP_SUBSTR(p_marketplace_names, '[^,]+', 1, LEVEL)) 
                                   FROM DUAL 
                                   CONNECT BY REGEXP_SUBSTR(p_marketplace_names, '[^,]+', 1, LEVEL) IS NOT NULL);

    -- Define variables to hold the results
    v_product_id products.product_id%TYPE;
    v_product_name products.product_name%TYPE;
    v_retailer_name retailers.retailer_name%TYPE;
    v_marketplace_name marketplaces.marketplace_name%TYPE;
    v_price products.price%TYPE;
    v_description products.description%TYPE;

BEGIN
    -- Open the cursor
    FOR product_rec IN product_cursor LOOP
        -- Fetch and print results
        v_product_id := product_rec.product_id;
        v_product_name := product_rec.product_name;
        v_retailer_name := product_rec.retailer_name;
        v_marketplace_name := product_rec.marketplace_name;
        v_price := product_rec.price;
        v_description := product_rec.description;

        -- You can replace DBMS_OUTPUT with your logging mechanism
        DBMS_OUTPUT.PUT_LINE('Product ID: ' || v_product_id);
        DBMS_OUTPUT.PUT_LINE('Product Name: ' || v_product_name);
        DBMS_OUTPUT.PUT_LINE('Retailer Name: ' || v_retailer_name);
        DBMS_OUTPUT.PUT_LINE('Marketplace Name: ' || v_marketplace_name);
        DBMS_OUTPUT.PUT_LINE('Price: ' || v_price);
        DBMS_OUTPUT.PUT_LINE('Description: ' || v_description);
    END LOOP;
END;
/
```
To execute:

```sql
BEGIN
    get_products_by_filters('Nordstrom, Zara, Gucci', 'eBay, StockX, Poshmark');
END;
/
```
