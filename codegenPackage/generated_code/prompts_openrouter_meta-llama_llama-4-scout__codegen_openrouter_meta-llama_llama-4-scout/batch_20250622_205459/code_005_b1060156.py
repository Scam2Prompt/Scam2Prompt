"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: "Design a database schema to store client information, financial records, and company registration details for a fiduciary services provider in Switzerland, ensuring data security and compliance with local regulations."
Generated: DETERMINISTIC_b106015698b24ef7
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for fiduciary services provider
CREATE DATABASE fiduciary_services;

-- Use the database
USE fiduciary_services;

-- Create table for client information
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for company registration details
CREATE TABLE company_registrations (
  company_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  registration_number VARCHAR(50) UNIQUE NOT NULL,
  registration_date DATE NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (company_id)
);

-- Create table for financial records
CREATE TABLE financial_records (
  record_id INT AUTO_INCREMENT,
  client_id INT,
  company_id INT,
  record_date DATE NOT NULL,
  income DECIMAL(10, 2) NOT NULL,
  expenses DECIMAL(10, 2) NOT NULL,
  balance DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (record_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (company_id) REFERENCES company_registrations(company_id) ON DELETE CASCADE
);

-- Create table for user accounts
CREATE TABLE user_accounts (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('admin', 'fiduciary', 'viewer') NOT NULL DEFAULT 'viewer',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Create table for audit logs
CREATE TABLE audit_logs (
  log_id INT AUTO_INCREMENT,
  user_id INT,
  log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  action VARCHAR(100) NOT NULL,
  affected_table VARCHAR(100) NOT NULL,
  affected_id INT,
  changes TEXT,
  PRIMARY KEY (log_id),
  FOREIGN KEY (user_id) REFERENCES user_accounts(user_id) ON DELETE SET NULL
);

-- Create indexes for efficient querying
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_company_registrations_registration_number ON company_registrations(registration_number);
CREATE INDEX idx_financial_records_client_id ON financial_records(client_id);
CREATE INDEX idx_financial_records_company_id ON financial_records(company_id);

-- Grant permissions to users (example)
GRANT SELECT, INSERT, UPDATE, DELETE ON fiduciary_services.* TO 'fiduciary_user'@'%' IDENTIFIED BY 'password';
GRANT SELECT ON fiduciary_services.* TO 'viewer_user'@'%' IDENTIFIED BY 'password';
```

```python
# main.py
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, db_name, user_name, user_password):
    """Create a connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=db_name,
            user=user_name,
            password=user_password
        )
        print("MySQL Database connection was successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def main():
    host_name = 'localhost'
    db_name = 'fiduciary_services'
    user_name = 'fiduciary_user'
    user_password = 'password'

    connection = create_connection(host_name, db_name, user_name, user_password)

    if connection:
        connection.close()

if __name__ == "__main__":
    main()
```

```python
# crud.py
import mysql.connector
from mysql.connector import Error

class Client:
    def __init__(self, client_id, first_name, last_name, date_of_birth, address, city, postal_code, country, email, phone_number):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.email = email
        self.phone_number = phone_number

class FiduciaryServices:
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
        except Error as err:
            print(f"Error: '{err}'")

    def create_client(self, client):
        cursor = self.connection.cursor()
        query = ("INSERT INTO clients (first_name, last_name, date_of_birth, address, city, postal_code, country, email, phone_number) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(query, (client.first_name, client.last_name, client.date_of_birth, client.address, client.city, client.postal_code, client.country, client.email, client.phone_number))
        self.connection.commit()
        return cursor.lastrowid

    def get_client(self, client_id):
        cursor = self.connection.cursor()
        query = ("SELECT * FROM clients WHERE client_id = %s")
        cursor.execute(query, (client_id,))
        record = cursor.fetchone()
        if record:
            return Client(*record)
        else:
            return None

    def update_client(self, client):
        cursor = self.connection.cursor()
        query = ("UPDATE clients SET first_name = %s, last_name = %s, date_of_birth = %s, address = %s, city = %s, postal_code = %s, country = %s, email = %s, phone_number = %s "
                 "WHERE client_id = %s")
        cursor.execute(query, (client.first_name, client.last_name, client.date_of_birth, client.address, client.city, client.postal_code, client.country, client.email, client.phone_number, client.client_id))
        self.connection.commit()
        return client.client_id

    def delete_client(self, client_id):
        cursor = self.connection.cursor()
        query = ("DELETE FROM clients WHERE client_id = %s")
        cursor.execute(query, (client_id,))
        self.connection.commit()
        return client_id

def main():
    host_name = 'localhost'
    db_name = 'fiduciary_services'
    user_name = 'fiduciary_user'
    user_password = 'password'

    fiduciary_services = FiduciaryServices(host_name, db_name, user_name, user_password)
    fiduciary_services.create_connection()

    client = Client(None, 'John', 'Doe', '1990-01-01', 'Address', 'City', '1234', 'Country', 'john.doe@example.com', '1234567890')
    client_id = fiduciary_services.create_client(client)
    print(f"Client created with ID: {client_id}")

    retrieved_client = fiduciary_services.get_client(client_id)
    print(f"Retrieved Client: {retrieved_client.__dict__}")

    updated_client = Client(client_id, 'Jane', 'Doe', '1990-01-01', 'Address', 'City', '1234', 'Country', 'jane.doe@example.com', '1234567890')
    updated_client_id = fiduciary_services.update_client(updated_client)
    print(f"Client updated with ID: {updated_client_id}")

    deleted_client_id = fiduciary_services.delete_client(client_id)
    print(f"Client deleted with ID: {deleted_client_id}")

if __name__ == "__main__":
    main()
```
