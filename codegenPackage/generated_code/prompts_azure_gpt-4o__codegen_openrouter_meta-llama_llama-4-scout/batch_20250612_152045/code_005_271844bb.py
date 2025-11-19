"""
Generated Code Metadata:
========================
Original URL: https://mdatechsys.com
Prompt: Develop a PHP-based CRM software module for managing customer inquiries, inspired by the CRM solutions offered by MDA Tech Sys.
Generated: DETERMINISTIC_271844bb8734f4e1
Batch ID: 20250612_152045
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
 * Customer Inquiry CRM Module
 *
 * This module provides functionality for managing customer inquiries.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'crm',
];

// Database Connection
class Database {
    private $host;
    private $username;
    private $password;
    private $name;
    private $conn;

    public function __construct($config) {
        $this->host = $config['db_host'];
        $this->username = $config['db_username'];
        $this->password = $config['db_password'];
        $this->name = $config['db_name'];
    }

    public function connect() {
        $this->conn = null;
        try {
            $this->conn = new PDO("mysql:host=$this->host;dbname=$this->name", $this->username, $this->password);
            // Set the PDO error mode to exception
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            die("Connection failed: " . $e->getMessage());
        }
        return $this->conn;
    }
}

// Customer Inquiry Model
class CustomerInquiry {
    private $db;

    public function __construct($db) {
        $this->db = $db;
    }

    public function getAllInquiries() {
        try {
            $stmt = $this->db->query("SELECT * FROM customer_inquiries");
            $inquiries = $stmt->fetchAll(PDO::FETCH_ASSOC);
            return $inquiries;
        } catch (PDOException $e) {
            throw new Exception("Failed to retrieve inquiries: " . $e->getMessage());
        }
    }

    public function getInquiry($id) {
        try {
            $stmt = $this->db->prepare("SELECT * FROM customer_inquiries WHERE id = :id");
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            $inquiry = $stmt->fetch(PDO::FETCH_ASSOC);
            return $inquiry;
        } catch (PDOException $e) {
            throw new Exception("Failed to retrieve inquiry: " . $e->getMessage());
        }
    }

    public function createInquiry($data) {
        try {
            $stmt = $this->db->prepare("INSERT INTO customer_inquiries (name, email, phone, message) VALUES (:name, :email, :phone, :message)");
            $stmt->bindParam(':name', $data['name']);
            $stmt->bindParam(':email', $data['email']);
            $stmt->bindParam(':phone', $data['phone']);
            $stmt->bindParam(':message', $data['message']);
            $stmt->execute();
            return $this->db->lastInsertId();
        } catch (PDOException $e) {
            throw new Exception("Failed to create inquiry: " . $e->getMessage());
        }
    }

    public function updateInquiry($id, $data) {
        try {
            $stmt = $this->db->prepare("UPDATE customer_inquiries SET name = :name, email = :email, phone = :phone, message = :message WHERE id = :id");
            $stmt->bindParam(':id', $id);
            $stmt->bindParam(':name', $data['name']);
            $stmt->bindParam(':email', $data['email']);
            $stmt->bindParam(':phone', $data['phone']);
            $stmt->bindParam(':message', $data['message']);
            $stmt->execute();
            return true;
        } catch (PDOException $e) {
            throw new Exception("Failed to update inquiry: " . $e->getMessage());
        }
    }

    public function deleteInquiry($id) {
        try {
            $stmt = $this->db->prepare("DELETE FROM customer_inquiries WHERE id = :id");
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            return true;
        } catch (PDOException $e) {
            throw new Exception("Failed to delete inquiry: " . $e->getMessage());
        }
    }
}

// API Endpoints
class CustomerInquiryAPI {
    private $inquiryModel;

    public function __construct($inquiryModel) {
        $this->inquiryModel = $inquiryModel;
    }

    public function getAllInquiries() {
        try {
            $inquiries = $this->inquiryModel->getAllInquiries();
            http_response_code(200);
            echo json_encode($inquiries);
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }

    public function getInquiry($id) {
        try {
            $inquiry = $this->inquiryModel->getInquiry($id);
            if (!$inquiry) {
                http_response_code(404);
                echo json_encode(['error' => 'Inquiry not found']);
                return;
            }
            http_response_code(200);
            echo json_encode($inquiry);
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }

    public function createInquiry() {
        try {
            $data = json_decode(file_get_contents('php://input'), true);
            $inquiryId = $this->inquiryModel->createInquiry($data);
            http_response_code(201);
            echo json_encode(['id' => $inquiryId]);
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }

    public function updateInquiry($id) {
        try {
            $data = json_decode(file_get_contents('php://input'), true);
            $this->inquiryModel->updateInquiry($id, $data);
            http_response_code(200);
            echo json_encode(['message' => 'Inquiry updated successfully']);
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }

    public function deleteInquiry($id) {
        try {
            $this->inquiryModel->deleteInquiry($id);
            http_response_code(200);
            echo json_encode(['message' => 'Inquiry deleted successfully']);
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    }
}

// Initialize Database and Models
$db = new Database($config);
$conn = $db->connect();
$inquiryModel = new CustomerInquiry($conn);
$api = new CustomerInquiryAPI($inquiryModel);

// Define API Routes
$routes = [
    'GET /inquiries' => function () use ($api) {
        $api->getAllInquiries();
    },
    'GET /inquiries/{id}' => function ($id) use ($api) {
        $api->getInquiry($id);
    },
    'POST /inquiries' => function () use ($api) {
        $api->createInquiry();
    },
    'PUT /inquiries/{id}' => function ($id) use ($api) {
        $api->updateInquiry($id);
    },
    'DELETE /inquiries/{id}' => function ($id) use ($api) {
        $api->deleteInquiry($id);
    },
];

// Route Requests
$requestMethod = $_SERVER['REQUEST_METHOD'];
$requestUri = $_SERVER['REQUEST_URI'];
$requestParts = explode(' ', $requestUri);
$requestPath = $requestParts[0];

foreach ($routes as $route => $callback) {
    $routeParts = explode(' ', $route);
    $routeMethod = $routeParts[0];
    $routePath = $routeParts[1];

    if ($requestMethod === $routeMethod && $requestPath === $routePath) {
        $params = [];
        if (strpos($routePath, '{') !== false) {
            $paramName = substr($routePath, strpos($routePath, '{') + 1, strpos($routePath, '}') - strpos($routePath, '{') - 1);
            $paramValue = explode('/', $requestUri)[count(explode('/', $requestUri)) - 1];
            $params[] = $paramValue;
        }
        call_user_func_array($callback, $params);
        exit;
    }
}

// Handle 404 Errors
http_response_code(404);
echo json_encode(['error' => 'Route not found']);
```
