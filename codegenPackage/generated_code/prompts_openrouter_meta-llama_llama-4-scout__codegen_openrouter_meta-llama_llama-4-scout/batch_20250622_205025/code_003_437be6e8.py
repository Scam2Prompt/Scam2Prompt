"""
Generated Code Metadata:
========================
Original URL: https://japkasai.net
Prompt: "Design a database schema for storing client information, appointment schedules, and service details for a men's grooming salon, considering factors like data privacy and scalability."
Generated: DETERMINISTIC_437be6e8d7ddf18d
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the men's grooming salon
CREATE DATABASE mens_grooming_salon;

-- Use the database
USE mens_grooming_salon;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(100) NOT NULL,
  service_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create a table for appointment schedules
CREATE TABLE appointments (
  appointment_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create a table for service providers
CREATE TABLE service_providers (
  provider_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (provider_id)
);

-- Create a table for appointment providers
CREATE TABLE appointment_providers (
  appointment_id INT NOT NULL,
  provider_id INT NOT NULL,
  PRIMARY KEY (appointment_id, provider_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE,
  FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id) ON DELETE CASCADE
);

-- Create a table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  appointment_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_appointments_client_id ON appointments(client_id);
CREATE INDEX idx_appointments_service_id ON appointments(service_id);
CREATE INDEX idx_appointments_appointment_date ON appointments(appointment_date);
CREATE INDEX idx_payments_appointment_id ON payments(appointment_id);
```

```python
import mysql.connector
from mysql.connector import Error

class SalonDatabase:
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
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
        if self.connection:
            cursor = self.connection.cursor()
            # SQL queries to create tables
            queries = [
                """
                CREATE TABLE IF NOT EXISTS clients (
                    client_id INT AUTO_INCREMENT,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    phone_number VARCHAR(20) NOT NULL,
                    address VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    PRIMARY KEY (client_id)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS services (
                    service_id INT AUTO_INCREMENT,
                    service_name VARCHAR(100) NOT NULL,
                    service_description TEXT,
                    price DECIMAL(10, 2) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    PRIMARY KEY (service_id)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS appointments (
                    appointment_id INT AUTO_INCREMENT,
                    client_id INT NOT NULL,
                    service_id INT NOT NULL,
                    appointment_date DATE NOT NULL,
                    appointment_time TIME NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    PRIMARY KEY (appointment_id),
                    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
                    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS service_providers (
                    provider_id INT AUTO_INCREMENT,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    phone_number VARCHAR(20) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    PRIMARY KEY (provider_id)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS appointment_providers (
                    appointment_id INT NOT NULL,
                    provider_id INT NOT NULL,
                    PRIMARY KEY (appointment_id, provider_id),
                    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE,
                    FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id) ON DELETE CASCADE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS payments (
                    payment_id INT AUTO_INCREMENT,
                    appointment_id INT NOT NULL,
                    payment_date DATE NOT NULL,
                    payment_amount DECIMAL(10, 2) NOT NULL,
                    payment_method VARCHAR(50) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    PRIMARY KEY (payment_id),
                    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE
                );
                """
            ]
            for query in queries:
                cursor.execute(query)
            self.connection.commit()
            print("Tables created")
        else:
            print("Not connected to database")

    def insert_client(self, first_name, last_name, email, phone_number, address):
        if self.connection:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO clients (first_name, last_name, email, phone_number, address)
                VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(query, (first_name, last_name, email, phone_number, address))
            self.connection.commit()
            print("Client inserted")
        else:
            print("Not connected to database")

    def insert_service(self, service_name, service_description, price):
        if self.connection:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO services (service_name, service_description, price)
                VALUES (%s, %s, %s);
            """
            cursor.execute(query, (service_name, service_description, price))
            self.connection.commit()
            print("Service inserted")
        else:
            print("Not connected to database")

    def insert_appointment(self, client_id, service_id, appointment_date, appointment_time):
        if self.connection:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO appointments (client_id, service_id, appointment_date, appointment_time)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(query, (client_id, service_id, appointment_date, appointment_time))
            self.connection.commit()
            print("Appointment inserted")
        else:
            print("Not connected to database")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

# Example usage
if __name__ == "__main__":
    db = SalonDatabase("localhost", "mens_grooming_salon", "root", "password")
    db.connect()
    db.create_tables()
    db.insert_client("John", "Doe", "john.doe@example.com", "123-456-7890", "123 Main St")
    db.insert_service("Haircut", "A standard haircut", 20.00)
    db.insert_appointment(1, 1, "2024-09-16", "10:00:00")
    db.close_connection()
```
