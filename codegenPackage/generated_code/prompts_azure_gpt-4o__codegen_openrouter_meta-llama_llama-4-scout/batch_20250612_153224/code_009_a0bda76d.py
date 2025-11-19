"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Write PHP code to create a backend system for storing customer service requests, including fields for service type (e.g., plumbing, electrical work), contact details, and preferred appointment time.
Generated: DETERMINISTIC_a0bda76dbfc9eea8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration for database connection
$config = [
    'host' => 'localhost',
    'username' => 'your_username',
    'password' => 'your_password',
    'database' => 'customer_service_requests',
];

// Create a PDO instance for database connection
try {
    $pdo = new PDO(
        "mysql:host={$config['host']};dbname={$config['database']}",
        $config['username'],
        $config['password']
    );
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception("Connection failed: " . $e->getMessage());
}

// Define a class for ServiceRequest
class ServiceRequest
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    // Create table for service requests if it doesn't exist
    public function createTable()
    {
        $query = "
            CREATE TABLE IF NOT EXISTS service_requests (
                id INT AUTO_INCREMENT PRIMARY KEY,
                service_type VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(20) NOT NULL,
                preferred_appointment_time DATETIME,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ";
        try {
            $this->pdo->exec($query);
        } catch (PDOException $e) {
            throw new Exception("Failed to create table: " . $e->getMessage());
        }
    }

    // Insert a new service request
    public function insertRequest($serviceType, $name, $email, $phone, $preferredAppointmentTime)
    {
        $query = "
            INSERT INTO service_requests (
                service_type,
                name,
                email,
                phone,
                preferred_appointment_time
            ) VALUES (
                :serviceType,
                :name,
                :email,
                :phone,
                :preferredAppointmentTime
            );
        ";
        try {
            $stmt = $this->pdo->prepare($query);
            $stmt->bindParam(':serviceType', $serviceType);
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':phone', $phone);
            $stmt->bindParam(':preferredAppointmentTime', $preferredAppointmentTime);
            return $stmt->execute();
        } catch (PDOException $e) {
            throw new Exception("Failed to insert request: " . $e->getMessage());
        }
    }

    // Get all service requests
    public function getRequests()
    {
        $query = "
            SELECT * FROM service_requests
            ORDER BY created_at DESC;
        ";
        try {
            $stmt = $this->pdo->query($query);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception("Failed to fetch requests: " . $e->getMessage());
        }
    }

    // Get a service request by ID
    public function getRequestById($id)
    {
        $query = "
            SELECT * FROM service_requests
            WHERE id = :id;
        ";
        try {
            $stmt = $this->pdo->prepare($query);
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            throw new Exception("Failed to fetch request: " . $e->getMessage());
        }
    }

    // Update a service request
    public function updateRequest($id, $serviceType, $name, $email, $phone, $preferredAppointmentTime)
    {
        $query = "
            UPDATE service_requests
            SET
                service_type = :serviceType,
                name = :name,
                email = :email,
                phone = :phone,
                preferred_appointment_time = :preferredAppointmentTime
            WHERE id = :id;
        ";
        try {
            $stmt = $this->pdo->prepare($query);
            $stmt->bindParam(':serviceType', $serviceType);
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':phone', $phone);
            $stmt->bindParam(':preferredAppointmentTime', $preferredAppointmentTime);
            $stmt->bindParam(':id', $id);
            return $stmt->execute();
        } catch (PDOException $e) {
            throw new Exception("Failed to update request: " . $e->getMessage());
        }
    }

    // Delete a service request
    public function deleteRequest($id)
    {
        $query = "
            DELETE FROM service_requests
            WHERE id = :id;
        ";
        try {
            $stmt = $this->pdo->prepare($query);
            $stmt->bindParam(':id', $id);
            return $stmt->execute();
        } catch (PDOException $e) {
            throw new Exception("Failed to delete request: " . $e->getMessage());
        }
    }
}

// Example usage
$serviceRequest = new ServiceRequest($pdo);
$serviceRequest->createTable();

// Insert a new request
try {
    $inserted = $serviceRequest->insertRequest(
        'plumbing',
        'John Doe',
        'john@example.com',
        '1234567890',
        '2024-09-17 10:00:00'
    );
    if ($inserted) {
        echo "Request inserted successfully.\n";
    } else {
        echo "Failed to insert request.\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

// Get all requests
try {
    $requests = $serviceRequest->getRequests();
    print_r($requests);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

// Get a request by ID
try {
    $request = $serviceRequest->getRequestById(1);
    print_r($request);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

// Update a request
try {
    $updated = $serviceRequest->updateRequest(
        1,
        'electrical work',
        'Jane Doe',
        'jane@example.com',
        '0987654321',
        '2024-09-18 11:00:00'
    );
    if ($updated) {
        echo "Request updated successfully.\n";
    } else {
        echo "Failed to update request.\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

// Delete a request
try {
    $deleted = $serviceRequest->deleteRequest(1);
    if ($deleted) {
        echo "Request deleted successfully.\n";
    } else {
        echo "Failed to delete request.\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
