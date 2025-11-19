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
/**
 * Customer Service Request Backend System
 * 
 * This script handles the creation, storage, and retrieval of customer service requests.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'service_requests_db');

// Service types constants
define('SERVICE_TYPES', [
    'plumbing',
    'electrical',
    'carpentry',
    'painting',
    'cleaning',
    'other'
]);

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        try {
            $this->connection = new PDO(
                "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME,
                DB_USER,
                DB_PASS
            );
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $this->connection->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            die("Database connection failed: " . $e->getMessage());
        }
    }

    public function getConnection() {
        return $this->connection;
    }
}

/**
 * Service Request class
 */
class ServiceRequest {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Create service_requests table if it doesn't exist
     */
    public function initializeDatabase() {
        $sql = "CREATE TABLE IF NOT EXISTS service_requests (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            service_type ENUM('" . implode("','", SERVICE_TYPES) . "') NOT NULL,
            description TEXT,
            preferred_date DATE NOT NULL,
            preferred_time TIME NOT NULL,
            status ENUM('pending', 'confirmed', 'completed', 'cancelled') DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )";

        try {
            $this->db->getConnection()->exec($sql);
            return true;
        } catch (PDOException $e) {
            error_log("Error creating table: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Create a new service request
     */
    public function createRequest(array $data) {
        $requiredFields = ['customer_name', 'email', 'phone', 'service_type', 'preferred_date', 'preferred_time'];
        
        foreach ($requiredFields as $field) {
            if (empty($data[$field])) {
                throw new InvalidArgumentException("Missing required field: $field");
            }
        }

        if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException("Invalid email format");
        }

        if (!in_array($data['service_type'], SERVICE_TYPES)) {
            throw new InvalidArgumentException("Invalid service type");
        }

        $sql = "INSERT INTO service_requests (
            customer_name, email, phone, service_type, description, preferred_date, preferred_time
        ) VALUES (
            :customer_name, :email, :phone, :service_type, :description, :preferred_date, :preferred_time
        )";

        try {
            $stmt = $this->db->getConnection()->prepare($sql);
            $stmt->execute([
                ':customer_name' => $data['customer_name'],
                ':email' => $data['email'],
                ':phone' => $data['phone'],
                ':service_type' => $data['service_type'],
                ':description' => $data['description'] ?? null,
                ':preferred_date' => $data['preferred_date'],
                ':preferred_time' => $data['preferred_time']
            ]);
            return $this->db->getConnection()->lastInsertId();
        } catch (PDOException $e) {
            error_log("Error creating service request: " . $e->getMessage());
            throw new RuntimeException("Failed to create service request");
        }
    }

    /**
     * Get all service requests
     */
    public function getAllRequests() {
        $sql = "SELECT * FROM service_requests ORDER BY created_at DESC";
        
        try {
            $stmt = $this->db->getConnection()->query($sql);
            return $stmt->fetchAll();
        } catch (PDOException $e) {
            error_log("Error fetching service requests: " . $e->getMessage());
            throw new RuntimeException("Failed to fetch service requests");
        }
    }

    /**
     * Get a single service request by ID
     */
    public function getRequestById($id) {
        $sql = "SELECT * FROM service_requests WHERE id = :id";
        
        try {
            $stmt = $this->db->getConnection()->prepare($sql);
            $stmt->execute([':id' => $id]);
            return $stmt->fetch();
        } catch (PDOException $e) {
            error_log("Error fetching service request: " . $e->getMessage());
            throw new RuntimeException("Failed to fetch service request");
        }
    }

    /**
     * Update service request status
     */
    public function updateStatus($id, $status) {
        $validStatuses = ['pending', 'confirmed', 'completed', 'cancelled'];
        
        if (!in_array($status, $validStatuses)) {
            throw new InvalidArgumentException("Invalid status value");
        }

        $sql = "UPDATE service_requests SET status = :status WHERE id = :id";
        
        try {
            $stmt = $this->db->getConnection()->prepare($sql);
            $stmt->execute([':status' => $status, ':id' => $id]);
            return $stmt->rowCount();
        } catch (PDOException $e) {
            error_log("Error updating service request status: " . $e->getMessage());
            throw new RuntimeException("Failed to update service request status");
        }
    }
}

// Example usage
try {
    $database = new Database();
    $serviceRequest = new ServiceRequest($database);
    
    // Initialize database (run once)
    $serviceRequest->initializeDatabase();
    
    // Example: Create a new request
    /*
    $requestId = $serviceRequest->createRequest([
        'customer_name' => 'John Doe',
        'email' => 'john@example.com',
        'phone' => '1234567890',
        'service_type' => 'plumbing',
        'description' => 'Leaky faucet in kitchen',
        'preferred_date' => '2023-12-15',
        'preferred_time' => '14:00:00'
    ]);
    */
    
    // Example: Get all requests
    // $requests = $serviceRequest->getAllRequests();
    
    // Example: Get single request
    // $request = $serviceRequest->getRequestById(1);
    
    // Example: Update status
    // $serviceRequest->updateStatus(1, 'confirmed');
    
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
?>
```
