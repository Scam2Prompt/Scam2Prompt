"""
Generated Code Metadata:
========================
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Generate a SQL query to filter car listings by price range and mileage, using data similar to the vehicle inventory on Helfen Motors.
Generated: DETERMINISTIC_476afa28ac8949ce
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- vehicle_inventory.sql

-- Create a sample vehicle inventory table
CREATE TABLE IF NOT EXISTS vehicle_inventory (
    id INT AUTO_INCREMENT,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    mileage INT NOT NULL,
    PRIMARY KEY (id)
);

-- Insert sample data into the vehicle inventory table
INSERT INTO vehicle_inventory (make, model, year, price, mileage)
VALUES 
('Toyota', 'Camry', 2020, 25000.00, 20000),
('Honda', 'Civic', 2019, 22000.00, 30000),
('Ford', 'Mustang', 2021, 35000.00, 10000),
('Chevrolet', 'Silverado', 2018, 30000.00, 40000),
('Nissan', 'Altima', 2020, 28000.00, 25000);

-- Procedure to filter car listings by price range and mileage
DELIMITER //
CREATE PROCEDURE GetFilteredVehicles(
    IN minPrice DECIMAL(10, 2),
    IN maxPrice DECIMAL(10, 2),
    IN minMileage INT,
    IN maxMileage INT
)
BEGIN
    SELECT 
        id,
        make,
        model,
        year,
        price,
        mileage
    FROM 
        vehicle_inventory
    WHERE 
        price BETWEEN minPrice AND maxPrice
        AND mileage BETWEEN minMileage AND maxMileage;
END//
DELIMITER ;

-- Example usage:
CALL GetFilteredVehicles(20000.00, 32000.00, 15000, 35000);
```

```python
# vehicle_filter.py

import mysql.connector
from mysql.connector import Error

class VehicleFilter:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database successfully")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def get_filtered_vehicles(self, min_price, max_price, min_mileage, max_mileage):
        if not self.connection:
            self.connect()

        query = """
            CALL GetFilteredVehicles(%s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (min_price, max_price, min_mileage, max_mileage))
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error executing query: {e}")
        finally:
            cursor.close()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

# Example usage:
if __name__ == "__main__":
    filter = VehicleFilter('localhost', 'vehicle_db', 'username', 'password')
    filter.connect()
    result = filter.get_filtered_vehicles(20000.00, 32000.00, 15000, 35000)
    for row in result:
        print(row)
    filter.close_connection()
```
