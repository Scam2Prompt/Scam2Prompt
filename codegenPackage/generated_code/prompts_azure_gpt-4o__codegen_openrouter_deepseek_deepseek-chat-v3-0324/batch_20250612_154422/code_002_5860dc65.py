"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: Generate a PHP-based solution for a "三三制直销软件" (three-track direct selling system) that enables simple replication and fast network expansion, as described on JieyaSoft.
Generated: DETERMINISTIC_5860dc65310e2dc3
Batch ID: 20250612_154422
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
 * Three-Track Direct Selling System (三三制直销软件)
 * 
 * This PHP-based solution enables simple replication and fast network expansion
 * for a direct selling business model following the three-track system.
 * 
 * Features:
 * - User registration and authentication
 * - Downline tracking (3 levels deep)
 * - Commission calculation
 * - Network visualization
 * - Performance reporting
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'direct_selling_system');

// Error reporting for development (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Session management
session_start();

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->connection->connect_error) {
            die("Database connection failed: " . $this->connection->connect_error);
        }
        
        $this->connection->set_charset("utf8");
    }

    public function getConnection() {
        return $this->connection;
    }

    public function __destruct() {
        $this->connection->close();
    }
}

/**
 * User management class
 */
class User {
    private $db;
    
    public function __construct(Database $db) {
        $this->db = $db;
    }
    
    /**
     * Register a new user
     */
    public function register($username, $password, $email, $sponsorId = null) {
        $conn = $this->db->getConnection();
        
        // Validate input
        if (empty($username) || empty($password) || empty($email)) {
            throw new Exception("All fields are required");
        }
        
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email format");
        }
        
        // Check if username or email already exists
        $stmt = $conn->prepare("SELECT id FROM users WHERE username = ? OR email = ?");
        $stmt->bind_param("ss", $username, $email);
        $stmt->execute();
        $stmt->store_result();
        
        if ($stmt->num_rows > 0) {
            throw new Exception("Username or email already exists");
        }
        $stmt->close();
        
        // Hash password
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        
        // Insert new user
        $stmt = $conn->prepare("INSERT INTO users (username, password, email, sponsor_id, registration_date) VALUES (?, ?, ?, ?, NOW())");
        $stmt->bind_param("sssi", $username, $hashedPassword, $email, $sponsorId);
        
        if (!$stmt->execute()) {
            throw new Exception("Registration failed: " . $stmt->error);
        }
        
        $userId = $stmt->insert_id;
        $stmt->close();
        
        // Update downline relationships if sponsor exists
        if ($sponsorId) {
            $this->updateDownline($userId, $sponsorId);
        }
        
        return $userId;
    }
    
    /**
     * Update downline relationships (3 levels)
     */
    private function updateDownline($userId, $sponsorId) {
        $conn = $this->db->getConnection();
        
        // Level 1 (direct sponsor)
        $stmt = $conn->prepare("INSERT INTO downline_relationships (user_id, sponsor_id, level) VALUES (?, ?, 1)");
        $stmt->bind_param("ii", $userId, $sponsorId);
        $stmt->execute();
        $stmt->close();
        
        // Level 2 (sponsor's sponsor)
        $stmt = $conn->prepare("SELECT sponsor_id FROM downline_relationships WHERE user_id = ? AND level = 1");
        $stmt->bind_param("i", $sponsorId);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($row = $result->fetch_assoc()) {
            $level2Sponsor = $row['sponsor_id'];
            $stmt = $conn->prepare("INSERT INTO downline_relationships (user_id, sponsor_id, level) VALUES (?, ?, 2)");
            $stmt->bind_param("ii", $userId, $level2Sponsor);
            $stmt->execute();
            $stmt->close();
            
            // Level 3 (sponsor's sponsor's sponsor)
            $stmt = $conn->prepare("SELECT sponsor_id FROM downline_relationships WHERE user_id = ? AND level = 1");
            $stmt->bind_param("i", $level2Sponsor);
            $stmt->execute();
            $result = $stmt->get_result();
            
            if ($row = $result->fetch_assoc()) {
                $level3Sponsor = $row['sponsor_id'];
                $stmt = $conn->prepare("INSERT INTO downline_relationships (user_id, sponsor_id, level) VALUES (?, ?, 3)");
                $stmt->bind_param("ii", $userId, $level3Sponsor);
                $stmt->execute();
                $stmt->close();
            }
        }
    }
    
    /**
     * User login
     */
    public function login($username, $password) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("SELECT id, username, password FROM users WHERE username = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows === 0) {
            throw new Exception("Invalid username or password");
        }
        
        $user = $result->fetch_assoc();
        
        if (!password_verify($password, $user['password'])) {
            throw new Exception("Invalid username or password");
        }
        
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        
        return true;
    }
    
    /**
     * Get user's downline (3 levels)
     */
    public function getDownline($userId) {
        $conn = $this->db->getConnection();
        $downline = [
            'level1' => [],
            'level2' => [],
            'level3' => []
        ];
        
        // Level 1 downline
        $stmt = $conn->prepare("SELECT u.id, u.username, u.email, u.registration_date 
                              FROM users u 
                              JOIN downline_relationships dr ON u.id = dr.user_id 
                              WHERE dr.sponsor_id = ? AND dr.level = 1");
        $stmt->bind_param("i", $userId);
        $stmt->execute();
        $result = $stmt->get_result();
        $downline['level1'] = $result->fetch_all(MYSQLI_ASSOC);
        $stmt->close();
        
        // Level 2 downline
        $stmt = $conn->prepare("SELECT u.id, u.username, u.email, u.registration_date 
                              FROM users u 
                              JOIN downline_relationships dr ON u.id = dr.user_id 
                              WHERE dr.sponsor_id = ? AND dr.level = 2");
        $stmt->bind_param("i", $userId);
        $stmt->execute();
        $result = $stmt->get_result();
        $downline['level2'] = $result->fetch_all(MYSQLI_ASSOC);
        $stmt->close();
        
        // Level 3 downline
        $stmt = $conn->prepare("SELECT u.id, u.username, u.email, u.registration_date 
                              FROM users u 
                              JOIN downline_relationships dr ON u.id = dr.user_id 
                              WHERE dr.sponsor_id = ? AND dr.level = 3");
        $stmt->bind_param("i", $userId);
        $stmt->execute();
        $result = $stmt->get_result();
        $downline['level3'] = $result->fetch_all(MYSQLI_ASSOC);
        $stmt->close();
        
        return $downline;
    }
    
    /**
     * Get user's commission summary
     */
    public function getCommissionSummary($userId) {
        $conn = $this->db->getConnection();
        
        $summary = [
            'total' => 0,
            'level1' => 0,
            'level2' => 0,
            'level3' => 0,
            'pending' => 0,
            'paid' => 0
        ];
        
        $stmt = $conn->prepare("SELECT 
                              SUM(CASE WHEN level = 1 THEN amount ELSE 0 END) as level1,
                              SUM(CASE WHEN level = 2 THEN amount ELSE 0 END) as level2,
                              SUM(CASE WHEN level = 3 THEN amount ELSE 0 END) as level3,
                              SUM(amount) as total,
                              SUM(CASE WHEN status = 'pending' THEN amount ELSE 0 END) as pending,
                              SUM(CASE WHEN status = 'paid' THEN amount ELSE 0
