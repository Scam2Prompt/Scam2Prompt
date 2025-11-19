"""
Generated Code Metadata:
========================
Original URL: https://rjbmudanzas.es
Prompt: Design a simple database schema to store information about clients, moving services, and storage facilities for a company like RJB Moving, and provide a brief explanation of the schema.
Generated: DETERMINISTIC_8ab16837a1ca1e2a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the moving company
CREATE DATABASE moving_company;

-- Use the moving company database
USE moving_company;

-- Create a table to store client information
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table to store moving services
CREATE TABLE moving_services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create a table to store storage facilities
CREATE TABLE storage_facilities (
  facility_id INT AUTO_INCREMENT,
  facility_name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(10) NOT NULL,
  capacity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (facility_id)
);

-- Create a table to store client moves
CREATE TABLE client_moves (
  move_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  facility_id INT,
  move_date DATE NOT NULL,
  move_details TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (move_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES moving_services(service_id) ON DELETE CASCADE,
  FOREIGN KEY (facility_id) REFERENCES storage_facilities(facility_id) ON DELETE SET NULL
);

-- Create a table to store move status updates
CREATE TABLE move_status_updates (
  update_id INT AUTO_INCREMENT,
  move_id INT NOT NULL,
  status VARCHAR(100) NOT NULL,
  update_date DATE NOT NULL,
  update_details TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (update_id),
  FOREIGN KEY (move_id) REFERENCES client_moves(move_id) ON DELETE CASCADE
);

-- Create a stored procedure to insert a new client
DELIMITER //
CREATE PROCEDURE insert_client(
  IN p_first_name VARCHAR(255),
  IN p_last_name VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_phone_number VARCHAR(20),
  IN p_address VARCHAR(255),
  IN p_city VARCHAR(100),
  IN p_state VARCHAR(100),
  IN p_zip_code VARCHAR(10)
)
BEGIN
  INSERT INTO clients (first_name, last_name, email, phone_number, address, city, state, zip_code)
  VALUES (p_first_name, p_last_name, p_email, p_phone_number, p_address, p_city, p_state, p_zip_code);
END//
DELIMITER ;

-- Create a stored procedure to insert a new move
DELIMITER //
CREATE PROCEDURE insert_move(
  IN p_client_id INT,
  IN p_service_id INT,
  IN p_facility_id INT,
  IN p_move_date DATE,
  IN p_move_details TEXT
)
BEGIN
  INSERT INTO client_moves (client_id, service_id, facility_id, move_date, move_details)
  VALUES (p_client_id, p_service_id, p_facility_id, p_move_date, p_move_details);
END//
DELIMITER ;

-- Example usage:
CALL insert_client('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345');
CALL insert_move(1, 1, 1, '2022-01-01', 'Moved client''s belongings to storage');

-- Insert sample data
INSERT INTO moving_services (service_name, service_description, price)
VALUES 
('Local Move', 'Local moving services', 100.00),
('Long Distance Move', 'Long distance moving services', 500.00),
('Storage', 'Storage services', 50.00);

INSERT INTO storage_facilities (facility_name, address, city, state, zip_code, capacity)
VALUES 
('Facility 1', '123 Main St', 'Anytown', 'CA', '12345', 10000.00),
('Facility 2', '456 Elm St', 'Othertown', 'NY', '67890', 20000.00);
```
