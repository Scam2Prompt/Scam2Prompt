"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Develop a code for a basic database schema to store information about poultry farms, including their location, size, and cleaning and disinfection history, using a programming language of your choice.
Generated: DETERMINISTIC_ae3fbe1a419cc50a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for poultry farms
CREATE DATABASE poultry_farms;

-- Use the poultry_farms database
USE poultry_farms;

-- Create a table for farm locations
CREATE TABLE farm_locations (
    id INT AUTO_INCREMENT,
    farm_name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    PRIMARY KEY (id)
);

-- Create a table for farm sizes
CREATE TABLE farm_sizes (
    id INT AUTO_INCREMENT,
    farm_id INT NOT NULL,
    size_in_acres DECIMAL(10, 2) NOT NULL,
    number_of_birds INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (farm_id) REFERENCES farm_locations(id)
);

-- Create a table for cleaning and disinfection history
CREATE TABLE cleaning_disinfection_history (
    id INT AUTO_INCREMENT,
    farm_id INT NOT NULL,
    cleaning_date DATE NOT NULL,
    disinfection_date DATE,
    cleaning_method VARCHAR(255),
    disinfectant_used VARCHAR(255),
    PRIMARY KEY (id),
    FOREIGN KEY (farm_id) REFERENCES farm_locations(id)
);

-- Create a stored procedure to insert a new farm location
DELIMITER //
CREATE PROCEDURE insert_farm_location(
    IN p_farm_name VARCHAR(255),
    IN p_address VARCHAR(255),
    IN p_city VARCHAR(100),
    IN p_state VARCHAR(100),
    IN p_country VARCHAR(100),
    IN p_postal_code VARCHAR(20),
    IN p_latitude DECIMAL(10, 8),
    IN p_longitude DECIMAL(11, 8)
)
BEGIN
    INSERT INTO farm_locations (farm_name, address, city, state, country, postal_code, latitude, longitude)
    VALUES (p_farm_name, p_address, p_city, p_state, p_country, p_postal_code, p_latitude, p_longitude);
END//
DELIMITER ;

-- Create a stored procedure to insert a new farm size
DELIMITER //
CREATE PROCEDURE insert_farm_size(
    IN p_farm_id INT,
    IN p_size_in_acres DECIMAL(10, 2),
    IN p_number_of_birds INT
)
BEGIN
    INSERT INTO farm_sizes (farm_id, size_in_acres, number_of_birds)
    VALUES (p_farm_id, p_size_in_acres, p_number_of_birds);
END//
DELIMITER ;

-- Create a stored procedure to insert a new cleaning and disinfection history
DELIMITER //
CREATE PROCEDURE insert_cleaning_disinfection_history(
    IN p_farm_id INT,
    IN p_cleaning_date DATE,
    IN p_disinfection_date DATE,
    IN p_cleaning_method VARCHAR(255),
    IN p_disinfectant_used VARCHAR(255)
)
BEGIN
    INSERT INTO cleaning_disinfection_history (farm_id, cleaning_date, disinfection_date, cleaning_method, disinfectant_used)
    VALUES (p_farm_id, p_cleaning_date, p_disinfection_date, p_cleaning_method, p_disinfectant_used);
END//
DELIMITER ;

-- Example usage:
CALL insert_farm_location('Farm1', '123 Main St', 'Anytown', 'CA', 'USA', '12345', 37.7749, -122.4194);
CALL insert_farm_size(1, 100.00, 10000);
CALL insert_cleaning_disinfection_history(1, '2022-01-01', '2022-01-15', 'High-pressure wash', 'Quaternary ammonium');

-- Select all data from farm_locations table
SELECT * FROM farm_locations;

-- Select all data from farm_sizes table
SELECT * FROM farm_sizes;

-- Select all data from cleaning_disinfection_history table
SELECT * FROM cleaning_disinfection_history;
```
