"""
Generated Code Metadata:
========================
Original URL: https://liveonlinetv.org
Prompt: Generate code in PHP to create a backend system that organizes and displays live TV channels and sports streams, similar to the functionality of LiveOnlineTv.org.
Generated: DETERMINISTIC_a5eadc5624019801
Batch ID: 20250612_154946
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
 * Live TV and Sports Streams Backend System
 * 
 * This script provides functionality to organize and display live TV channels and sports streams.
 * It includes features for adding, updating, deleting, and retrieving streams.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'livetv_streams');

// Error reporting
error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', __DIR__ . '/error.log');

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connect();
    }

    private function connect() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

        if ($this->connection->connect_error) {
            error_log("Database connection failed: " . $this->connection->connect_error);
            die("Database connection failed. Please try again later.");
        }

        $this->connection->set_charset("utf8mb4");
    }

    public function getConnection() {
        if (!$this->connection || $this->connection->ping() === false) {
            $this->connect();
        }
        return $this->connection;
    }

    public function __destruct() {
        if ($this->connection) {
            $this->connection->close();
        }
    }
}

/**
 * Stream management class
 */
class StreamManager {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Add a new stream
     */
    public function addStream($name, $url, $category, $thumbnail = null, $is_sports = false) {
        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("INSERT INTO streams (name, url, category, thumbnail, is_sports, created_at) VALUES (?, ?, ?, ?, ?, NOW())");
        
        if (!$stmt) {
            error_log("Prepare failed: " . $conn->error);
            return false;
        }

        $stmt->bind_param("ssssi", $name, $url, $category, $thumbnail, $is_sports);
        $result = $stmt->execute();
        $stmt->close();

        return $result;
    }

    /**
     * Update an existing stream
     */
    public function updateStream($id, $name, $url, $category, $thumbnail = null, $is_sports = false) {
        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("UPDATE streams SET name = ?, url = ?, category = ?, thumbnail = ?, is_sports = ?, updated_at = NOW() WHERE id = ?");
        
        if (!$stmt) {
            error_log("Prepare failed: " . $conn->error);
            return false;
        }

        $stmt->bind_param("ssssii", $name, $url, $category, $thumbnail, $is_sports, $id);
        $result = $stmt->execute();
        $stmt->close();

        return $result;
    }

    /**
     * Delete a stream
     */
    public function deleteStream($id) {
        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("DELETE FROM streams WHERE id = ?");
        
        if (!$stmt) {
            error_log("Prepare failed: " . $conn->error);
            return false;
        }

        $stmt->bind_param("i", $id);
        $result = $stmt->execute();
        $stmt->close();

        return $result;
    }

    /**
     * Get all streams
     */
    public function getAllStreams($category = null, $is_sports = null) {
        $conn = $this->db->getConnection();
        $query = "SELECT * FROM streams WHERE 1=1";
        $params = [];
        $types = "";

        if ($category !== null) {
            $query .= " AND category = ?";
            $params[] = $category;
            $types .= "s";
        }

        if ($is_sports !== null) {
            $query .= " AND is_sports = ?";
            $params[] = $is_sports;
            $types .= "i";
        }

        $query .= " ORDER BY name ASC";
        $stmt = $conn->prepare($query);

        if (!$stmt) {
            error_log("Prepare failed: " . $conn->error);
            return [];
        }

        if (!empty($params)) {
            $stmt->bind_param($types, ...$params);
        }

        $stmt->execute();
        $result = $stmt->get_result();
        $streams = $result->fetch_all(MYSQLI_ASSOC);
        $stmt->close();

        return $streams;
    }

    /**
     * Get stream by ID
     */
    public function getStreamById($id) {
        $conn = $this->db->getConnection();
        $stmt = $conn->prepare("SELECT * FROM streams WHERE id = ?");
        
        if (!$stmt) {
            error_log("Prepare failed: " . $conn->error);
            return null;
        }

        $stmt->bind_param("i", $id);
        $stmt->execute();
        $result = $stmt->get_result();
        $stream = $result->fetch_assoc();
        $stmt->close();

        return $stream;
    }

    /**
     * Get all categories
     */
    public function getCategories() {
        $conn = $this->db->getConnection();
        $result = $conn->query("SELECT DISTINCT category FROM streams ORDER BY category ASC");
        
        if (!$result) {
            error_log("Query failed: " . $conn->error);
            return [];
        }

        $categories = [];
        while ($row = $result->fetch_assoc()) {
            $categories[] = $row['category'];
        }

        return $categories;
    }
}

/**
 * API Response Handler
 */
class ApiResponse {
    public static function success($data = null, $message = 'Success') {
        header('Content-Type: application/json');
        echo json_encode([
            'success' => true,
            'message' => $message,
            'data' => $data
        ]);
        exit;
    }

    public static function error($message = 'Error', $code = 400) {
        http_response_code($code);
        header('Content-Type: application/json');
        echo json_encode([
            'success' => false,
            'message' => $message
        ]);
        exit;
    }
}

// Initialize database and stream manager
$database = new Database();
$streamManager = new StreamManager($database);

// Handle API requests
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $action = $_GET['action'] ?? '';
    
    switch ($action) {
        case 'get_streams':
            $category = $_GET['category'] ?? null;
            $is_sports = isset($_GET['is_sports']) ? (int)$_GET['is_sports'] : null;
            $streams = $streamManager->getAllStreams($category, $is_sports);
            ApiResponse::success($streams);
            break;
            
        case 'get_stream':
            $id = $_GET['id'] ?? 0;
            if (!$id) {
                ApiResponse::error('Stream ID is required');
            }
            $stream = $streamManager->getStreamById($id);
            if (!$stream) {
                ApiResponse::error('Stream not found', 404);
            }
            ApiResponse::success($stream);
            break;
            
        case 'get_categories':
            $categories = $streamManager->getCategories();
            ApiResponse::success($categories);
            break;
            
        default:
            ApiResponse::error('Invalid action');
    }
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'] ?? '';
    $data = json_decode(file_get_contents('php://input'), true) ?? $_POST;
    
    switch ($action) {
        case 'add_stream':
            $required = ['name', 'url', 'category'];
            foreach ($required as $field) {
                if (empty($data[$field])) {
                    ApiResponse::error("$field is required");
                }
            }
            
            $result = $streamManager->addStream(
                $data['name'],
                $data['url'],
                $data['category'],
                $data['thumbnail'] ?? null,
                $data['is_sports'] ?? false
            );
            
            if ($result) {
                ApiResponse::success(null, 'Stream added successfully');
            } else {
                ApiResponse::error('Failed to add stream');
            }
            break;
            
        case 'update_stream':
            if (empty($data['id'])) {
                ApiResponse::error('Stream ID is required');
            }
            
            $result = $streamManager->updateStream(
                $data['id'],
                $data['name'] ?? '',
                $data['url'] ?? '',
                $data['category'] ?? '',
                $data['thumbnail'] ?? null,
                $data['is
