"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Create a simple database schema to store client data, services offered, and billing information for an accounting firm like Atual Contabilidade."
Generated: DETERMINISTIC_420bcd92ab68458f
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for accounting firm
CREATE DATABASE accounting_firm;

-- Use the database
USE accounting_firm;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for services offered
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for client services
CREATE TABLE client_services (
  client_service_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  quantity INT NOT NULL DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_service_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create table for billing information
CREATE TABLE billing (
  bill_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  bill_date DATE NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'paid', 'overdue') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (bill_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for bill items
CREATE TABLE bill_items (
  bill_item_id INT AUTO_INCREMENT,
  bill_id INT NOT NULL,
  service_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (bill_item_id),
  FOREIGN KEY (bill_id) REFERENCES billing(bill_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create index on client email for faster lookup
CREATE INDEX idx_client_email ON clients(email);

-- Create index on bill client_id for faster lookup
CREATE INDEX idx_bill_client_id ON billing(client_id);

-- Create procedure to add new client
DELIMITER //
CREATE PROCEDURE add_client(
  IN p_name VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_phone VARCHAR(20),
  IN p_address VARCHAR(255)
)
BEGIN
  INSERT INTO clients (name, email, phone, address)
  VALUES (p_name, p_email, p_phone, p_address);
END//
DELIMITER ;

-- Create procedure to add new service
DELIMITER //
CREATE PROCEDURE add_service(
  IN p_service_name VARCHAR(255),
  IN p_service_description TEXT,
  IN p_price DECIMAL(10, 2)
)
BEGIN
  INSERT INTO services (service_name, service_description, price)
  VALUES (p_service_name, p_service_description, p_price);
END//
DELIMITER ;

-- Create procedure to add new client service
DELIMITER //
CREATE PROCEDURE add_client_service(
  IN p_client_id INT,
  IN p_service_id INT,
  IN p_quantity INT
)
BEGIN
  INSERT INTO client_services (client_id, service_id, quantity)
  VALUES (p_client_id, p_service_id, p_quantity);
END//
DELIMITER ;

-- Create procedure to generate bill
DELIMITER //
CREATE PROCEDURE generate_bill(
  IN p_client_id INT,
  IN p_bill_date DATE
)
BEGIN
  DECLARE total DECIMAL(10, 2);
  DECLARE done INT DEFAULT FALSE;
  DECLARE cs_cursor CURSOR FOR
    SELECT cs.quantity, s.price
    FROM client_services cs
    JOIN services s ON cs.service_id = s.service_id
    WHERE cs.client_id = p_client_id;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN cs_cursor;

  SET total = 0;

  read_loop: LOOP
    FETCH cs_cursor INTO p_quantity, p_price;
    IF done THEN
      LEAVE read_loop;
    END IF;
    SET total = total + (p_quantity * p_price);
  END LOOP;

  CLOSE cs_cursor;

  INSERT INTO billing (client_id, bill_date, total)
  VALUES (p_client_id, p_bill_date, total);

  -- Get the bill_id of the newly inserted bill
  SET @bill_id = LAST_INSERT_ID();

  -- Insert bill items
  OPEN cs_cursor;

  read_loop2: LOOP
    FETCH cs_cursor INTO p_quantity, p_price;
    IF done THEN
      LEAVE read_loop2;
    END IF;
    INSERT INTO bill_items (bill_id, service_id, quantity, price)
    VALUES (@bill_id, (SELECT service_id FROM client_services WHERE client_id = p_client_id AND quantity = p_quantity LIMIT 1), p_quantity, p_price);
  END LOOP;

  CLOSE cs_cursor;
END//
DELIMITER ;
```
