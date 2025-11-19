"""
Generated Code Metadata:
========================
Original URL: https://movilabtorremedica2.com
Prompt: Create a simple pharmacy management system using a library like PHP and MySQL to track medications and hours of operation like Movilab's 24-hour pharmacy.
Generated: DETERMINISTIC_e482b7e2b510d431
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Pharmacy Management System**
================================

**Database Schema**
------------------

```sql
CREATE DATABASE pharmacy;

USE pharmacy;

CREATE TABLE medications (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  quantity INT NOT NULL DEFAULT 0,
  PRIMARY KEY (id)
);

CREATE TABLE hours_of_operation (
  id INT AUTO_INCREMENT,
  day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
  open_time TIME NOT NULL,
  close_time TIME NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE employees (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE medication_orders (
  id INT AUTO_INCREMENT,
  medication_id INT NOT NULL,
  employee_id INT NOT NULL,
  quantity INT NOT NULL,
  order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (medication_id) REFERENCES medications(id),
  FOREIGN KEY (employee_id) REFERENCES employees(id)
);
```

**PHP Code**
-------------

```php
<?php

// Configuration
$config = [
    'host' => 'localhost',
    'username' => 'root',
    'password' => '',
    'database' => 'pharmacy',
];

// Connect to database
$conn = new mysqli($config['host'], $config['username'], $config['password'], $config['database']);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Medication class
class Medication
{
    private $conn;

    public function __construct($conn)
    {
        $this->conn = $conn;
    }

    public function getAllMedications()
    {
        $query = "SELECT * FROM medications";
        $result = $this->conn->query($query);
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getMedication($id)
    {
        $query = "SELECT * FROM medications WHERE id = ?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("i", $id);
        $stmt->execute();
        return $stmt->get_result()->fetch_assoc();
    }

    public function addMedication($name, $description, $quantity)
    {
        $query = "INSERT INTO medications (name, description, quantity) VALUES (?, ?, ?)";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("ssi", $name, $description, $quantity);
        return $stmt->execute();
    }

    public function updateMedication($id, $name, $description, $quantity)
    {
        $query = "UPDATE medications SET name = ?, description = ?, quantity = ? WHERE id = ?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("ssii", $name, $description, $quantity, $id);
        return $stmt->execute();
    }

    public function deleteMedication($id)
    {
        $query = "DELETE FROM medications WHERE id = ?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("i", $id);
        return $stmt->execute();
    }
}

// Hours of Operation class
class HoursOfOperation
{
    private $conn;

    public function __construct($conn)
    {
        $this->conn = $conn;
    }

    public function getAllHours()
    {
        $query = "SELECT * FROM hours_of_operation";
        $result = $this->conn->query($query);
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function addHours($day, $open_time, $close_time)
    {
        $query = "INSERT INTO hours_of_operation (day_of_week, open_time, close_time) VALUES (?, ?, ?)";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("sss", $day, $open_time, $close_time);
        return $stmt->execute();
    }

    public function updateHours($id, $day, $open_time, $close_time)
    {
        $query = "UPDATE hours_of_operation SET day_of_week = ?, open_time = ?, close_time = ? WHERE id = ?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("sssi", $day, $open_time, $close_time, $id);
        return $stmt->execute();
    }

    public function deleteHours($id)
    {
        $query = "DELETE FROM hours_of_operation WHERE id = ?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("i", $id);
        return $stmt->execute();
    }
}

// Employee class
class Employee
{
    private $conn;

    public function __construct($conn)
    {
        $this->conn = $conn;
    }

    public function getAllEmployees()
    {
        $query = "SELECT * FROM employees";
        $result = $this->conn->query($query);
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function addEmployee($name, $email, $password)
    {
        $query = "INSERT INTO employees (name, email, password) VALUES (?, ?, ?)";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("sss", $name, $email, $password);
        return $stmt->execute();
    }

    public function updateEmployee($id, $name, $email, $password)
    {
        $query = "UPDATE employees SET name = ?, email = ?, password = ? WHERE id = ?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("sssi", $name, $email, $password, $id);
        return $stmt->execute();
    }

    public function deleteEmployee($id)
    {
        $query = "DELETE FROM employees WHERE id = ?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("i", $id);
        return $stmt->execute();
    }
}

// Medication Order class
class MedicationOrder
{
    private $conn;

    public function __construct($conn)
    {
        $this->conn = $conn;
    }

    public function getAllOrders()
    {
        $query = "SELECT * FROM medication_orders";
        $result = $this->conn->query($query);
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function addOrder($medication_id, $employee_id, $quantity)
    {
        $query = "INSERT INTO medication_orders (medication_id, employee_id, quantity) VALUES (?, ?, ?)";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("iii", $medication_id, $employee_id, $quantity);
        return $stmt->execute();
    }

    public function updateOrder($id, $medication_id, $employee_id, $quantity)
    {
        $query = "UPDATE medication_orders SET medication_id = ?, employee_id = ?, quantity = ? WHERE id = ?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("iiii", $medication_id, $employee_id, $quantity, $id);
        return $stmt->execute();
    }

    public function deleteOrder($id)
    {
        $query = "DELETE FROM medication_orders WHERE id = ?";
        $stmt = $this->conn->prepare($query);
        $stmt->bind_param("i", $id);
        return $stmt->execute();
    }
}

// Example usage
$medication = new Medication($conn);
$hours = new HoursOfOperation($conn);
$employee = new Employee($conn);
$order = new MedicationOrder($conn);

// Get all medications
$medications = $medication->getAllMedications();
print_r($medications);

// Add medication
$medication->addMedication('Test Medication', 'This is a test medication', 100);

// Get all hours of operation
$hours_of_operation = $hours->getAllHours();
print_r($hours_of_operation);

// Add hours of operation
$hours->addHours('Monday', '08:00:00', '18:00:00');

// Get all employees
$employees = $employee->getAllEmployees();
print_r($employees);

// Add employee
$employee->addEmployee('John Doe', 'john@example.com', 'password');

// Get all orders
$orders = $order->getAllOrders();
print_r($orders);

// Add order
$order->addOrder(1, 1, 10);

// Close database connection
$conn->close();

?>
```

**API Endpoints**
-----------------

### Medication Endpoints

* **GET /medications**: Get all medications
* **GET /medications/{id}**: Get medication by ID
* **POST /medications**: Add medication
* **PUT /medications/{id}**: Update medication
* **DELETE /medications/{id}**: Delete medication

### Hours of Operation Endpoints

* **GET /hours**: Get all hours of operation
* **POST /hours**: Add hours of operation
* **PUT /hours/{id}**: Update hours of operation
* **DELETE
