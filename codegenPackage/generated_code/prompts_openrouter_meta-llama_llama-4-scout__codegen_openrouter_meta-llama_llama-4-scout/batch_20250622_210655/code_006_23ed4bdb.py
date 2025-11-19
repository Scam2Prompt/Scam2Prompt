"""
Generated Code Metadata:
========================
Original URL: https://spanglerroofingllc.com
Prompt: "Create a scheduling system in PHP for managing appointments and emergency roof services, ensuring efficient allocation of resources."
Generated: DETERMINISTIC_23ed4bdb4e77f07b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Scheduling System for Managing Appointments and Emergency Roof Services
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'scheduling_system',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Connection failed: ' . $e->getMessage());
}

// Tables
$tables = [
    'appointments' => '
        CREATE TABLE IF NOT EXISTS appointments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(255) NOT NULL,
            appointment_date DATE NOT NULL,
            appointment_time TIME NOT NULL,
            service_type VARCHAR(255) NOT NULL,
            status VARCHAR(255) NOT NULL DEFAULT \'pending\'
        )
    ',
    'emergency_services' => '
        CREATE TABLE IF NOT EXISTS emergency_services (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(255) NOT NULL,
            service_date DATE NOT NULL,
            service_time TIME NOT NULL,
            service_type VARCHAR(255) NOT NULL,
            status VARCHAR(255) NOT NULL DEFAULT \'pending\'
        )
    ',
    'technicians' => '
        CREATE TABLE IF NOT EXISTS technicians (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            availability VARCHAR(255) NOT NULL
        )
    ',
];

// Create Tables
foreach ($tables as $table => $sql) {
    try {
        $pdo->exec($sql);
    } catch (PDOException $e) {
        throw new Exception("Table $table creation failed: " . $e->getMessage());
    }
}

// Appointment Class
class Appointment
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function create($customerName, $appointmentDate, $appointmentTime, $serviceType)
    {
        $sql = 'INSERT INTO appointments (customer_name, appointment_date, appointment_time, service_type) VALUES (:customer_name, :appointment_date, :appointment_time, :service_type)';
        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute([
                'customer_name' => $customerName,
                'appointment_date' => $appointmentDate,
                'appointment_time' => $appointmentTime,
                'service_type' => $serviceType,
            ]);
            return $this->pdo->lastInsertId();
        } catch (PDOException $e) {
            throw new Exception('Appointment creation failed: ' . $e->getMessage());
        }
    }

    public function getAll()
    {
        $sql = 'SELECT * FROM appointments';
        try {
            $stmt = $this->pdo->query($sql);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception('Failed to retrieve appointments: ' . $e->getMessage());
        }
    }

    public function updateStatus($id, $status)
    {
        $sql = 'UPDATE appointments SET status = :status WHERE id = :id';
        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute([
                'status' => $status,
                'id' => $id,
            ]);
        } catch (PDOException $e) {
            throw new Exception('Appointment status update failed: ' . $e->getMessage());
        }
    }
}

// Emergency Service Class
class EmergencyService
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function create($customerName, $serviceDate, $serviceTime, $serviceType)
    {
        $sql = 'INSERT INTO emergency_services (customer_name, service_date, service_time, service_type) VALUES (:customer_name, :service_date, :service_time, :service_type)';
        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute([
                'customer_name' => $customerName,
                'service_date' => $serviceDate,
                'service_time' => $serviceTime,
                'service_type' => $serviceType,
            ]);
            return $this->pdo->lastInsertId();
        } catch (PDOException $e) {
            throw new Exception('Emergency service creation failed: ' . $e->getMessage());
        }
    }

    public function getAll()
    {
        $sql = 'SELECT * FROM emergency_services';
        try {
            $stmt = $this->pdo->query($sql);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception('Failed to retrieve emergency services: ' . $e->getMessage());
        }
    }

    public function updateStatus($id, $status)
    {
        $sql = 'UPDATE emergency_services SET status = :status WHERE id = :id';
        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute([
                'status' => $status,
                'id' => $id,
            ]);
        } catch (PDOException $e) {
            throw new Exception('Emergency service status update failed: ' . $e->getMessage());
        }
    }
}

// Technician Class
class Technician
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function create($name, $availability)
    {
        $sql = 'INSERT INTO technicians (name, availability) VALUES (:name, :availability)';
        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute([
                'name' => $name,
                'availability' => $availability,
            ]);
            return $this->pdo->lastInsertId();
        } catch (PDOException $e) {
            throw new Exception('Technician creation failed: ' . $e->getMessage());
        }
    }

    public function getAll()
    {
        $sql = 'SELECT * FROM technicians';
        try {
            $stmt = $this->pdo->query($sql);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception('Failed to retrieve technicians: ' . $e->getMessage());
        }
    }
}

// Usage
$appointment = new Appointment($pdo);
$emergencyService = new EmergencyService($pdo);
$technician = new Technician($pdo);

// Create appointment
$appointmentId = $appointment->create('John Doe', '2024-09-16', '10:00:00', 'roof inspection');
echo "Appointment created with ID: $appointmentId\n";

// Create emergency service
$emergencyServiceId = $emergencyService->create('Jane Doe', '2024-09-16', '11:00:00', 'emergency roof repair');
echo "Emergency service created with ID: $emergencyServiceId\n";

// Create technician
$technicianId = $technician->create('Technician 1', 'Monday - Friday, 9am - 5pm');
echo "Technician created with ID: $technicianId\n";

// Get all appointments
$appointments = $appointment->getAll();
echo "Appointments:\n";
print_r($appointments);

// Get all emergency services
$emergencyServices = $emergencyService->getAll();
echo "Emergency Services:\n";
print_r($emergencyServices);

// Get all technicians
$technicians = $technician->getAll();
echo "Technicians:\n";
print_r($technicians);

// Update appointment status
$appointment->updateStatus($appointmentId, 'in_progress');
echo "Appointment $appointmentId status updated to in_progress\n";

// Update emergency service status
$emergencyService->updateStatus($emergencyServiceId, 'in_progress');
echo "Emergency service $emergencyServiceId status updated to in_progress\n";

// Close database connection
$pdo = null;
```
