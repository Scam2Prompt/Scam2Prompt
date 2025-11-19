"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Create a simple database schema to store information about pipe cleaning and maintenance services, inspired by the offerings of Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_58482445d27a219d
Batch ID: 20250622_212309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for pipe cleaning and maintenance services
CREATE DATABASE PipeCleaningServices;

-- Use the database
USE PipeCleaningServices;

-- Create a table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create a table for services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ServiceName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceID)
);

-- Create a table for technicians
CREATE TABLE Technicians (
    TechnicianID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TechnicianID)
);

-- Create a table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    TechnicianID INT NOT NULL,
    ServiceID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentTime TIME NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (TechnicianID) REFERENCES Technicians(TechnicianID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Create a table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    PaymentMethod VARCHAR(255) NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);

-- Create a table for reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    Rating TINYINT NOT NULL,
    Review TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);
```

```python
import mysql.connector
from mysql.connector import Error

class PipeCleaningServices:
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
            print("Connection to database established")
        except Error as e:
            print(f"Error: '{e}'")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error: '{e}'")

    def read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: '{e}'")

# Example usage
if __name__ == "__main__":
    pipe_cleaning_services = PipeCleaningServices(
        host_name="localhost",
        db_name="PipeCleaningServices",
        user_name="your_username",
        user_password="your_password"
    )
    pipe_cleaning_services.create_connection()

    # Create tables
    queries = [
        """
            CREATE TABLE IF NOT EXISTS Customers (
                CustomerID INT AUTO_INCREMENT,
                Name VARCHAR(255) NOT NULL,
                Email VARCHAR(255) UNIQUE NOT NULL,
                Phone VARCHAR(20) NOT NULL,
                Address VARCHAR(255) NOT NULL,
                CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                PRIMARY KEY (CustomerID)
            );
        """,
        """
            CREATE TABLE IF NOT EXISTS Services (
                ServiceID INT AUTO_INCREMENT,
                ServiceName VARCHAR(255) NOT NULL,
                Description TEXT,
                Price DECIMAL(10, 2) NOT NULL,
                CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                PRIMARY KEY (ServiceID)
            );
        """,
        """
            CREATE TABLE IF NOT EXISTS Technicians (
                TechnicianID INT AUTO_INCREMENT,
                Name VARCHAR(255) NOT NULL,
                Email VARCHAR(255) UNIQUE NOT NULL,
                Phone VARCHAR(20) NOT NULL,
                CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                PRIMARY KEY (TechnicianID)
            );
        """,
        """
            CREATE TABLE IF NOT EXISTS Appointments (
                AppointmentID INT AUTO_INCREMENT,
                CustomerID INT NOT NULL,
                TechnicianID INT NOT NULL,
                ServiceID INT NOT NULL,
                AppointmentDate DATE NOT NULL,
                AppointmentTime TIME NOT NULL,
                Address VARCHAR(255) NOT NULL,
                CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                PRIMARY KEY (AppointmentID),
                FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
                FOREIGN KEY (TechnicianID) REFERENCES Technicians(TechnicianID),
                FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
            );
        """,
        """
            CREATE TABLE IF NOT EXISTS Payments (
                PaymentID INT AUTO_INCREMENT,
                AppointmentID INT NOT NULL,
                PaymentMethod VARCHAR(255) NOT NULL,
                PaymentDate DATE NOT NULL,
                Amount DECIMAL(10, 2) NOT NULL,
                CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                PRIMARY KEY (PaymentID),
                FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
            );
        """,
        """
            CREATE TABLE IF NOT EXISTS Reviews (
                ReviewID INT AUTO_INCREMENT,
                AppointmentID INT NOT NULL,
                Rating TINYINT NOT NULL,
                Review TEXT,
                CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                PRIMARY KEY (ReviewID),
                FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
            );
        """
    ]

    for query in queries:
        pipe_cleaning_services.execute_query(query)

    # Insert example data
    insert_queries = [
        """
            INSERT INTO Customers (Name, Email, Phone, Address)
            VALUES ('John Doe', 'john@example.com', '1234567890', '123 Main St');
        """,
        """
            INSERT INTO Services (ServiceName, Description, Price)
            VALUES ('Pipe Cleaning', 'Cleaning of pipes', 100.00);
        """,
        """
            INSERT INTO Technicians (Name, Email, Phone)
            VALUES ('Jane Doe', 'jane@example.com', '0987654321');
        """,
        """
            INSERT INTO Appointments (CustomerID, TechnicianID, ServiceID, AppointmentDate, AppointmentTime, Address)
            VALUES (1, 1, 1, '2024-09-16', '10:00:00', '123 Main St');
        """,
        """
            INSERT INTO Payments (AppointmentID, PaymentMethod, PaymentDate, Amount)
            VALUES (1, 'Cash', '2024-09-16', 100.00);
        """,
        """
            INSERT INTO Reviews (AppointmentID, Rating, Review)
            VALUES (1, 5, 'Excellent service!');
        """
    ]

    for query in insert_queries:
        pipe_cleaning_services.execute_query(query)

    # Read example data
    select_query = """
        SELECT * FROM Customers;
    """
    result = pipe_cleaning_services.read_query(select_query)
    for row in result:
        print(row)
```
