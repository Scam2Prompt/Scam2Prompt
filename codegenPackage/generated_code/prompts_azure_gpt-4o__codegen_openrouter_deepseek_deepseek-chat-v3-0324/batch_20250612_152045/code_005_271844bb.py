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
 * CRM Customer Inquiry Management Module
 * 
 * This module handles customer inquiries including creation, viewing, updating, 
 * and tracking status changes.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'crm_user');
define('DB_PASS', 'secure_password');
define('DB_NAME', 'crm_system');

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->connection->connect_error) {
            throw new Exception("Database connection failed: " . $this->connection->connect_error);
        }
    }

    public function getConnection() {
        return $this->connection;
    }

    public function __destruct() {
        if ($this->connection) {
            $this->connection->close();
        }
    }
}

/**
 * Inquiry management class
 */
class InquiryManager {
    private $db;

    public function __construct(Database $database) {
        $this->db = $database->getConnection();
    }

    /**
     * Create a new customer inquiry
     */
    public function createInquiry($customerId, $subject, $message, $priority = 'medium') {
        $validPriorities = ['low', 'medium', 'high'];
        
        if (!in_array($priority, $validPriorities)) {
            throw new InvalidArgumentException("Invalid priority level");
        }

        $stmt = $this->db->prepare("INSERT INTO inquiries (customer_id, subject, message, priority, status, created_at) 
                                   VALUES (?, ?, ?, ?, 'open', NOW())");
        if (!$stmt) {
            throw new Exception("Database error: " . $this->db->error);
        }

        $stmt->bind_param("isss", $customerId, $subject, $message, $priority);
        $stmt->execute();
        
        if ($stmt->affected_rows === 0) {
            throw new Exception("Failed to create inquiry");
        }

        $inquiryId = $stmt->insert_id;
        $stmt->close();
        
        return $inquiryId;
    }

    /**
     * Get inquiry details by ID
     */
    public function getInquiry($inquiryId) {
        $stmt = $this->db->prepare("SELECT * FROM inquiries WHERE id = ?");
        if (!$stmt) {
            throw new Exception("Database error: " . $this->db->error);
        }

        $stmt->bind_param("i", $inquiryId);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows === 0) {
            throw new Exception("Inquiry not found");
        }

        $inquiry = $result->fetch_assoc();
        $stmt->close();
        
        return $inquiry;
    }

    /**
     * Update inquiry status
     */
    public function updateStatus($inquiryId, $newStatus) {
        $validStatuses = ['open', 'in_progress', 'resolved', 'closed'];
        
        if (!in_array($newStatus, $validStatuses)) {
            throw new InvalidArgumentException("Invalid status");
        }

        $stmt = $this->db->prepare("UPDATE inquiries SET status = ?, updated_at = NOW() WHERE id = ?");
        if (!$stmt) {
            throw new Exception("Database error: " . $this->db->error);
        }

        $stmt->bind_param("si", $newStatus, $inquiryId);
        $stmt->execute();
        
        if ($stmt->affected_rows === 0) {
            throw new Exception("No changes made or inquiry not found");
        }

        $stmt->close();
        return true;
    }

    /**
     * Add a response to an inquiry
     */
    public function addResponse($inquiryId, $userId, $message) {
        $stmt = $this->db->prepare("INSERT INTO inquiry_responses (inquiry_id, user_id, message, created_at) 
                                   VALUES (?, ?, ?, NOW())");
        if (!$stmt) {
            throw new Exception("Database error: " . $this->db->error);
        }

        $stmt->bind_param("iis", $inquiryId, $userId, $message);
        $stmt->execute();
        
        if ($stmt->affected_rows === 0) {
            throw new Exception("Failed to add response");
        }

        $responseId = $stmt->insert_id;
        $stmt->close();
        
        return $responseId;
    }

    /**
     * Get all responses for an inquiry
     */
    public function getResponses($inquiryId) {
        $stmt = $this->db->prepare("SELECT * FROM inquiry_responses WHERE inquiry_id = ? ORDER BY created_at ASC");
        if (!$stmt) {
            throw new Exception("Database error: " . $this->db->error);
        }

        $stmt->bind_param("i", $inquiryId);
        $stmt->execute();
        $result = $stmt->get_result();
        $responses = [];
        
        while ($row = $result->fetch_assoc()) {
            $responses[] = $row;
        }

        $stmt->close();
        return $responses;
    }

    /**
     * Search inquiries with filters
     */
    public function searchInquiries($filters = []) {
        $query = "SELECT * FROM inquiries WHERE 1=1";
        $params = [];
        $types = '';
        
        if (!empty($filters['customer_id'])) {
            $query .= " AND customer_id = ?";
            $params[] = $filters['customer_id'];
            $types .= 'i';
        }
        
        if (!empty($filters['status'])) {
            $query .= " AND status = ?";
            $params[] = $filters['status'];
            $types .= 's';
        }
        
        if (!empty($filters['priority'])) {
            $query .= " AND priority = ?";
            $params[] = $filters['priority'];
            $types .= 's';
        }
        
        if (!empty($filters['date_from'])) {
            $query .= " AND created_at >= ?";
            $params[] = $filters['date_from'];
            $types .= 's';
        }
        
        if (!empty($filters['date_to'])) {
            $query .= " AND created_at <= ?";
            $params[] = $filters['date_to'];
            $types .= 's';
        }
        
        $query .= " ORDER BY created_at DESC";
        
        $stmt = $this->db->prepare($query);
        if (!$stmt) {
            throw new Exception("Database error: " . $this->db->error);
        }
        
        if (!empty($params)) {
            $stmt->bind_param($types, ...$params);
        }
        
        $stmt->execute();
        $result = $stmt->get_result();
        $inquiries = [];
        
        while ($row = $result->fetch_assoc()) {
            $inquiries[] = $row;
        }

        $stmt->close();
        return $inquiries;
    }
}

/**
 * API Controller for handling HTTP requests
 */
class InquiryController {
    private $inquiryManager;

    public function __construct() {
        try {
            $database = new Database();
            $this->inquiryManager = new InquiryManager($database);
        } catch (Exception $e) {
            $this->sendErrorResponse(500, "Database initialization failed: " . $e->getMessage());
        }
    }

    public function handleRequest() {
        $method = $_SERVER['REQUEST_METHOD'];
        $path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
        $parts = explode('/', trim($path, '/'));

        try {
            if ($parts[0] === 'api' && $parts[1] === 'inquiries') {
                switch ($method) {
                    case 'GET':
                        if (isset($parts[2])) {
                            $this->getInquiry($parts[2]);
                        } else {
                            $this->listInquiries();
                        }
                        break;
                    case 'POST':
                        $this->createInquiry();
                        break;
                    case 'PUT':
                        if (isset($parts[2])) {
                            $this->updateInquiryStatus($parts[2]);
                        }
                        break;
                    default:
                        $this->sendErrorResponse(405, "Method not allowed");
                }
            } elseif ($parts[0] === 'api' && $parts[1] === 'responses' && $method === 'POST') {
                $this->addResponse();
            } else {
                $this->sendErrorResponse(404, "Endpoint not found");
            }
        } catch (Exception $e) {
            $this->sendErrorResponse(400, $e->getMessage());
        }
    }

    private function getInquiry($id) {
        try {
            $inquiry = $this->inquiryManager->getInquiry($id);
            $responses = $this->inquiryManager->getResponses($id);
            $inquiry['responses'] = $responses;
            $this->sendResponse(200, $inquiry);
        } catch (Exception $e) {
            $this->send
