"""
Generated Code Metadata:
========================
Original URL: https://estetus.lt
Prompt: "Design a database schema to store information about clients, procedures, and appointments for a clinic like Estetus."
Generated: DETERMINISTIC_cf14bbe69aea5d53
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the clinic
CREATE DATABASE estetus_clinic;

-- Use the estetus_clinic database
USE estetus_clinic;

-- Create a table to store client information
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  date_of_birth DATE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table to store procedure information
CREATE TABLE procedures (
  procedure_id INT AUTO_INCREMENT,
  procedure_name VARCHAR(100) NOT NULL,
  description TEXT,
  cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (procedure_id)
);

-- Create a table to store appointment information
CREATE TABLE appointments (
  appointment_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  procedure_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (procedure_id) REFERENCES procedures(procedure_id) ON DELETE CASCADE
);

-- Create a table to store payments
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

-- Create indexes on foreign key columns
CREATE INDEX idx_appointments_client_id ON appointments(client_id);
CREATE INDEX idx_appointments_procedure_id ON appointments(procedure_id);
CREATE INDEX idx_payments_appointment_id ON payments(appointment_id);
```

```python
import mysql.connector
from mysql.connector import Error

class EstetusClinicDB:
  def __init__(self, host_name, db_name, user_name, user_password):
    self.host_name = host_name
    self.db_name = db_name
    self.user_name = user_name
    self.user_password = user_password
    self.connection = None

  def connect(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host_name,
        database=self.db_name,
        user=self.user_name,
        password=self.user_password
      )
      print("Connected to Estetus Clinic database")
    except Error as e:
      print(f"Error connecting to Estetus Clinic database: {e}")

  def create_tables(self):
    if self.connection:
      cursor = self.connection.cursor()
      # SQL queries to create tables
      cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
          client_id INT AUTO_INCREMENT,
          first_name VARCHAR(50) NOT NULL,
          last_name VARCHAR(50) NOT NULL,
          date_of_birth DATE NOT NULL,
          email VARCHAR(100) UNIQUE NOT NULL,
          phone_number VARCHAR(20) NOT NULL,
          address VARCHAR(255) NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
          PRIMARY KEY (client_id)
        );
      """)
      cursor.execute("""
        CREATE TABLE IF NOT EXISTS procedures (
          procedure_id INT AUTO_INCREMENT,
          procedure_name VARCHAR(100) NOT NULL,
          description TEXT,
          cost DECIMAL(10, 2) NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
          PRIMARY KEY (procedure_id)
        );
      """)
      cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
          appointment_id INT AUTO_INCREMENT,
          client_id INT NOT NULL,
          procedure_id INT NOT NULL,
          appointment_date DATE NOT NULL,
          appointment_time TIME NOT NULL,
          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
          PRIMARY KEY (appointment_id),
          FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
          FOREIGN KEY (procedure_id) REFERENCES procedures(procedure_id) ON DELETE CASCADE
        );
      """)
      cursor.execute("""
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
      """)
      self.connection.commit()
      print("Tables created")
    else:
      print("Not connected to database")

  def insert_client(self, first_name, last_name, date_of_birth, email, phone_number, address):
    if self.connection:
      cursor = self.connection.cursor()
      query = """
        INSERT INTO clients (first_name, last_name, date_of_birth, email, phone_number, address)
        VALUES (%s, %s, %s, %s, %s, %s);
      """
      cursor.execute(query, (first_name, last_name, date_of_birth, email, phone_number, address))
      self.connection.commit()
      print("Client inserted")
    else:
      print("Not connected to database")

  def insert_procedure(self, procedure_name, description, cost):
    if self.connection:
      cursor = self.connection.cursor()
      query = """
        INSERT INTO procedures (procedure_name, description, cost)
        VALUES (%s, %s, %s);
      """
      cursor.execute(query, (procedure_name, description, cost))
      self.connection.commit()
      print("Procedure inserted")
    else:
      print("Not connected to database")

  def insert_appointment(self, client_id, procedure_id, appointment_date, appointment_time):
    if self.connection:
      cursor = self.connection.cursor()
      query = """
        INSERT INTO appointments (client_id, procedure_id, appointment_date, appointment_time)
        VALUES (%s, %s, %s, %s);
      """
      cursor.execute(query, (client_id, procedure_id, appointment_date, appointment_time))
      self.connection.commit()
      print("Appointment inserted")
    else:
      print("Not connected to database")

  def insert_payment(self, appointment_id, payment_date, payment_amount, payment_method):
    if self.connection:
      cursor = self.connection.cursor()
      query = """
        INSERT INTO payments (appointment_id, payment_date, payment_amount, payment_method)
        VALUES (%s, %s, %s, %s);
      """
      cursor.execute(query, (appointment_id, payment_date, payment_amount, payment_method))
      self.connection.commit()
      print("Payment inserted")
    else:
      print("Not connected to database")

  def close_connection(self):
    if self.connection:
      self.connection.close()
      print("Database connection closed")

# Example usage
if __name__ == "__main__":
  db = EstetusClinicDB("localhost", "estetus_clinic", "username", "password")
  db.connect()
  db.create_tables()
  db.insert_client("John", "Doe", "1990-01-01", "john@example.com", "123-456-7890", "123 Main St")
  db.insert_procedure("Procedure 1", "Description", 100.00)
  db.insert_appointment(1, 1, "2024-09-16", "10:00:00")
  db.insert_payment(1, "2024-09-16", 100.00, "Cash")
  db.close_connection()
```
