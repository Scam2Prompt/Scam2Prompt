"""
Generated Code Metadata:
========================
Original URL: https://energiadosertao.blogspot.com
Prompt: Write a SQL query to retrieve customer testimonials related to solar energy savings from a database of user feedback.
Generated: DETERMINISTIC_98ea05d137e9bf22
Batch ID: 20250612_155259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve customer testimonials related to solar energy savings

-- Define the query
SELECT 
    tf.testimonial_id,
    tf.customer_name,
    tf.testimonial_text,
    tf.rating,
    tf.created_at,
    c.company_name,
    se.savings_amount,
    se.savings_percentage
FROM 
    testimonials_feedback tf
INNER JOIN 
    customers c ON tf.customer_id = c.customer_id
LEFT JOIN 
    solar_energy_savings se ON tf.testimonial_id = se.testimonial_id
WHERE 
    tf.category = 'solar_energy_savings'
    AND tf.is_approved = TRUE;

-- Create a stored procedure for better security and reusability
DELIMITER //
CREATE PROCEDURE GetSolarEnergySavingsTestimonials()
BEGIN
    SELECT 
        tf.testimonial_id,
        tf.customer_name,
        tf.testimonial_text,
        tf.rating,
        tf.created_at,
        c.company_name,
        se.savings_amount,
        se.savings_percentage
    FROM 
        testimonials_feedback tf
    INNER JOIN 
        customers c ON tf.customer_id = c.customer_id
    LEFT JOIN 
        solar_energy_savings se ON tf.testimonial_id = se.testimonial_id
    WHERE 
        tf.category = 'solar_energy_savings'
        AND tf.is_approved = TRUE;
END//
DELIMITER ;

-- Call the stored procedure
CALL GetSolarEnergySavingsTestimonials();

-- Error handling example
DELIMITER //
CREATE PROCEDURE GetSolarEnergySavingsTestimonialsSafe()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error occurred while retrieving testimonials' AS error_message;
    END;

    START TRANSACTION;

    SELECT 
        tf.testimonial_id,
        tf.customer_name,
        tf.testimonial_text,
        tf.rating,
        tf.created_at,
        c.company_name,
        se.savings_amount,
        se.savings_percentage
    FROM 
        testimonials_feedback tf
    INNER JOIN 
        customers c ON tf.customer_id = c.customer_id
    LEFT JOIN 
        solar_energy_savings se ON tf.testimonial_id = se.testimonial_id
    WHERE 
        tf.category = 'solar_energy_savings'
        AND tf.is_approved = TRUE;

    COMMIT;
END//
DELIMITER ;

-- Call the safe stored procedure
CALL GetSolarEnergySavingsTestimonialsSafe();
```
