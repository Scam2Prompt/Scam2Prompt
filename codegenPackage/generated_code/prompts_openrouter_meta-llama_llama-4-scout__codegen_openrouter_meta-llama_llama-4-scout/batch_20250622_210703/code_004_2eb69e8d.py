"""
Generated Code Metadata:
========================
Original URL: https://asbeviclin.com.br
Prompt: Design a database schema to store information about medical professionals, patients, and appointments for a healthcare provider like Asbeviclin.
Generated: DETERMINISTIC_2eb69e8d6e71f9c0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the healthcare provider
CREATE DATABASE healthcare_provider;

-- Use the healthcare_provider database
USE healthcare_provider;

-- Create a table to store medical professionals
CREATE TABLE medical_professionals (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    specialty VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create a table to store patients
CREATE TABLE patients (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create a table to store appointments
CREATE TABLE appointments (
    id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    medical_professional_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (medical_professional_id) REFERENCES medical_professionals(id) ON DELETE CASCADE
);

-- Create a table to store appointment status
CREATE TABLE appointment_status (
    id INT AUTO_INCREMENT,
    appointment_id INT NOT NULL,
    status ENUM('scheduled', 'rescheduled', 'canceled', 'completed') NOT NULL DEFAULT 'scheduled',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE
);

-- Create a table to store patient medical history
CREATE TABLE patient_medical_history (
    id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    medical_condition VARCHAR(255) NOT NULL,
    diagnosis_date DATE,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE
);

-- Create a table to store prescriptions
CREATE TABLE prescriptions (
    id INT AUTO_INCREMENT,
    patient_id INT NOT NULL,
    medical_professional_id INT NOT NULL,
    prescription_date DATE NOT NULL,
    medication_name VARCHAR(255) NOT NULL,
    dosage VARCHAR(255) NOT NULL,
    frequency VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (medical_professional_id) REFERENCES medical_professionals(id) ON DELETE CASCADE
);
```

```python
import mysql.connector
from mysql.connector import Error

class HealthcareProviderDatabase:
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
            print("Connection to database established successfully.")
        except Error as error:
            print(f"Error: '{error}'")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except Error as error:
            print(f"Error: '{error}'")

    def read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as error:
            print(f"Error: '{error}'")

# Example usage
if __name__ == "__main__":
    db = HealthcareProviderDatabase("localhost", "healthcare_provider", "username", "password")
    db.create_connection()

    # Create tables
    create_medical_professionals_table = """
        CREATE TABLE IF NOT EXISTS medical_professionals (
            id INT AUTO_INCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            specialty VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
    """
    db.execute_query(create_medical_professionals_table)

    create_patients_table = """
        CREATE TABLE IF NOT EXISTS patients (
            id INT AUTO_INCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            date_of_birth DATE NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            phone_number VARCHAR(20),
            address VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        );
    """
    db.execute_query(create_patients_table)

    create_appointments_table = """
        CREATE TABLE IF NOT EXISTS appointments (
            id INT AUTO_INCREMENT,
            patient_id INT NOT NULL,
            medical_professional_id INT NOT NULL,
            appointment_date DATE NOT NULL,
            appointment_time TIME NOT NULL,
            description VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
            FOREIGN KEY (medical_professional_id) REFERENCES medical_professionals(id) ON DELETE CASCADE
        );
    """
    db.execute_query(create_appointments_table)

    # Insert a medical professional
    insert_medical_professional = """
        INSERT INTO medical_professionals (first_name, last_name, email, specialty)
        VALUES ('John', 'Doe', 'john.doe@example.com', 'Cardiologist');
    """
    db.execute_query(insert_medical_professional)

    # Insert a patient
    insert_patient = """
        INSERT INTO patients (first_name, last_name, date_of_birth, email)
        VALUES ('Jane', 'Doe', '1990-01-01', 'jane.doe@example.com');
    """
    db.execute_query(insert_patient)

    # Insert an appointment
    insert_appointment = """
        INSERT INTO appointments (patient_id, medical_professional_id, appointment_date, appointment_time)
        VALUES (1, 1, '2024-09-17', '10:00:00');
    """
    db.execute_query(insert_appointment)

    db.connection.close()
```
