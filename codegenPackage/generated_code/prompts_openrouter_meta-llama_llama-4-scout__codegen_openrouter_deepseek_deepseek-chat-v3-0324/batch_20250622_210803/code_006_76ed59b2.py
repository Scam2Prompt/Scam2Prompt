"""
Generated Code Metadata:
========================
Original URL: https://calanguteescorts.com
Prompt: Write a PHP script to interact with a database and perform CRUD operations on escort listings, similar to those found on https://calanguteescorts.com, and provide an example of secure coding practices.
Generated: DETERMINISTIC_76ed59b2c6496190
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'secure_user');
define('DB_PASS', 'complex_password_123!');
define('DB_NAME', 'escorts_db');

// Establish database connection
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

// Escort class for CRUD operations
class EscortService {
    private $db;
    
    public function __construct() {
        $this->db = getDbConnection();
    }
    
    // Create new escort listing with input validation
    public function createEscort($data) {
        $errors = $this->validateEscortData($data);
        if (!empty($errors)) {
            return ['success' => false, 'errors' => $errors];
        }
        
        $stmt = $this->db->prepare("INSERT INTO escorts (name, age, location, services, description, phone, email) VALUES (?, ?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("sisssss", 
            $data['name'],
            $data['age'],
            $data['location'],
            $data['services'],
            $data['description'],
            $data['phone'],
            $data['email']
        );
        
        if ($stmt->execute()) {
            return ['success' => true, 'id' => $stmt->insert_id];
        } else {
            return ['success' => false, 'error' => $stmt->error];
        }
    }
    
    // Read escort by ID with prepared statement
    public function getEscort($id) {
        $stmt = $this->db->prepare("SELECT * FROM escorts WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows > 0) {
            return $result->fetch_assoc();
        }
        
        return null;
    }
    
    // Update escort listing
    public function updateEscort($id, $data) {
        $errors = $this->validateEscortData($data);
        if (!empty($errors)) {
            return ['success' => false, 'errors' => $errors];
        }
        
        $stmt = $this->db->prepare("UPDATE escorts SET name=?, age=?, location=?, services=?, description=?, phone=?, email=? WHERE id=?");
        $stmt->bind_param("sisssssi", 
            $data['name'],
            $data['age'],
            $data['location'],
            $data['services'],
            $data['description'],
            $data['phone'],
            $data['email'],
            $id
        );
        
        if ($stmt->execute()) {
            return ['success' => true];
        } else {
            return ['success' => false, 'error' => $stmt->error];
        }
    }
    
    // Delete escort listing
    public function deleteEscort($id) {
        $stmt = $this->db->prepare("DELETE FROM escorts WHERE id = ?");
        $stmt->bind_param("i", $id);
        
        if ($stmt->execute()) {
            return ['success' => true];
        } else {
            return ['success' => false, 'error' => $stmt->error];
        }
    }
    
    // Get all escorts with pagination
    public function getAllEscorts($page = 1, $perPage = 10) {
        $offset = ($page - 1) * $perPage;
        $stmt = $this->db->prepare("SELECT * FROM escorts LIMIT ?, ?");
        $stmt->bind_param("ii", $offset, $perPage);
        $stmt->execute();
        $result = $stmt->get_result();
        
        $escorts = [];
        while ($row = $result->fetch_assoc()) {
            $escorts[] = $row;
        }
        
        return $escorts;
    }
    
    // Input validation
    private function validateEscortData($data) {
        $errors = [];
        
        if (empty($data['name'])) {
            $errors[] = 'Name is required';
        }
        
        if (!is_numeric($data['age']) || $data['age'] < 18 || $data['age'] > 99) {
            $errors[] = 'Age must be between 18 and 99';
        }
        
        if (empty($data['location'])) {
            $errors[] = 'Location is required';
        }
        
        if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
            $errors[] = 'Invalid email format';
        }
        
        if (!preg_match('/^\+?[0-9]{10,15}$/', $data['phone'])) {
            $errors[] = 'Invalid phone number format';
        }
        
        return $errors;
    }
    
    // Close connection
    public function __destruct() {
        $this->db->close();
    }
}

// Example usage
$escortService = new EscortService();

// Create example
$newEscort = [
    'name' => 'Jessica',
    'age' => 25,
    'location' => 'Calangute',
    'services' => 'Companionship, Dinner Dates',
    'description' => 'Professional escort with 3 years experience',
    'phone' => '+919876543210',
    'email' => 'jessica@example.com'
];

$result = $escortService->createEscort($newEscort);
if ($result['success']) {
    echo "Escort created with ID: " . $result['id'];
} else {
    echo "Error: " . print_r($result['errors'] ?? $result['error'], true);
}

// Get example
$escort = $escortService->getEscort(1);
if ($escort) {
    echo "Escort found: " . htmlspecialchars($escort['name']);
} else {
    echo "Escort not found";
}

// Security headers
header("X-Frame-Options: DENY");
header("X-Content-Type-Options: nosniff");
header("X-XSS-Protection: 1; mode=block");
header("Content-Security-Policy: default-src 'self'");
header("Strict-Transport-Security: max-age=31536000; includeSubDomains");
header("Referrer-Policy: strict-origin-when-cross-origin");
?>
```
