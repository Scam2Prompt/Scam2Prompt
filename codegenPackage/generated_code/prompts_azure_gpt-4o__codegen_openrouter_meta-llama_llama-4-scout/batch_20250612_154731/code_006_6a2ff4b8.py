"""
Generated Code Metadata:
========================
Original URL: https://balajitravelsonline.com
Prompt: Write a script to create a database schema for storing tour package details (e.g., package name, destination, and price) and car rental options (e.g., car model, AC/non-AC) for Balaji Tours & Travels.
Generated: DETERMINISTIC_6a2ff4b841ce6eea
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Balaji Tours & Travels
CREATE DATABASE balaji_tours;

-- Use the balaji_tours database
USE balaji_tours;

-- Create a table for tour packages
CREATE TABLE tour_packages (
    package_id INT AUTO_INCREMENT,
    package_name VARCHAR(255) NOT NULL,
    destination VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (package_id)
);

-- Create a table for car rental options
CREATE TABLE car_rentals (
    rental_id INT AUTO_INCREMENT,
    car_model VARCHAR(100) NOT NULL,
    ac_non_ac ENUM('AC', 'Non-AC') NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (rental_id)
);

-- Create a table for package-car rental associations
CREATE TABLE package_rentals (
    package_id INT NOT NULL,
    rental_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (package_id, rental_id),
    FOREIGN KEY (package_id) REFERENCES tour_packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (rental_id) REFERENCES car_rentals(rental_id) ON DELETE CASCADE
);

-- Create a stored procedure to insert tour package details
DELIMITER //
CREATE PROCEDURE insert_tour_package(
    IN p_package_name VARCHAR(255),
    IN p_destination VARCHAR(255),
    IN p_price DECIMAL(10, 2)
)
BEGIN
    INSERT INTO tour_packages (package_name, destination, price)
    VALUES (p_package_name, p_destination, p_price);
END //
DELIMITER ;

-- Create a stored procedure to insert car rental options
DELIMITER //
CREATE PROCEDURE insert_car_rental(
    IN p_car_model VARCHAR(100),
    IN p_ac_non_ac ENUM('AC', 'Non-AC'),
    IN p_price DECIMAL(10, 2)
)
BEGIN
    INSERT INTO car_rentals (car_model, ac_non_ac, price)
    VALUES (p_car_model, p_ac_non_ac, p_price);
END //
DELIMITER ;

-- Create a stored procedure to associate a package with car rental options
DELIMITER //
CREATE PROCEDURE associate_package_rental(
    IN p_package_id INT,
    IN p_rental_id INT
)
BEGIN
    INSERT INTO package_rentals (package_id, rental_id)
    VALUES (p_package_id, p_rental_id);
END //
DELIMITER ;
```

```python
import mysql.connector
from mysql.connector import Error

class BalajiToursDB:
    def __init__(self, host_name, db_name, user_name, user_password):
        self.host_name = host_name
        self.db_name = db_name
        self.user_name = user_name
        self.user_password = user_password
        self.connection = None

    def create_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                database=self.db_name,
                user=self.user_name,
                password=self.user_password
            )
            print("Connection to Balaji Tours DB established")
        except Error as e:
            print(f"Error: '{e}'")

    def insert_tour_package(self, package_name, destination, price):
        try:
            cursor = self.connection.cursor()
            query = "CALL insert_tour_package(%s, %s, %s)"
            cursor.execute(query, (package_name, destination, price))
            self.connection.commit()
            print("Tour package inserted successfully")
        except Error as e:
            print(f"Error: '{e}'")

    def insert_car_rental(self, car_model, ac_non_ac, price):
        try:
            cursor = self.connection.cursor()
            query = "CALL insert_car_rental(%s, %s, %s)"
            cursor.execute(query, (car_model, ac_non_ac, price))
            self.connection.commit()
            print("Car rental option inserted successfully")
        except Error as e:
            print(f"Error: '{e}'")

    def associate_package_rental(self, package_id, rental_id):
        try:
            cursor = self.connection.cursor()
            query = "CALL associate_package_rental(%s, %s)"
            cursor.execute(query, (package_id, rental_id))
            self.connection.commit()
            print("Package-rental association created successfully")
        except Error as e:
            print(f"Error: '{e}'")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

# Example usage
if __name__ == "__main__":
    db = BalajiToursDB("localhost", "balaji_tours", "your_username", "your_password")
    db.create_connection()

    db.insert_tour_package("Kerala Tour", "Kerala", 10000.00)
    db.insert_car_rental("Toyota Innova", "AC", 2000.00)
    db.associate_package_rental(1, 1)

    db.close_connection()
```
