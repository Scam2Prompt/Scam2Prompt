"""
Generated Code Metadata:
========================
Original URL: https://mywanderloop.com
Prompt: Write a script in PHP to manage user accounts and track promotional bonuses for online casinos, inspired by the features discussed on myWanderLoop.
Generated: DETERMINISTIC_8f900b401e1fe04a
Batch ID: 20250612_153246
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
 * User Account and Promotional Bonus Management System for Online Casinos
 * 
 * This script provides functionality to manage user accounts and track promotional bonuses.
 * It includes features for user registration, login, bonus assignment, and tracking.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'casino_bonus_system');
define('SECRET_KEY', 'your-secret-key-here');

// Error reporting
error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', __DIR__ . '/error.log');

// Start session
session_start();

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->connection->connect_error) {
            $this->logError("Database connection failed: " . $this->connection->connect_error);
            die("Database connection failed. Please try again later.");
        }
    }

    public function getConnection() {
        return $this->connection;
    }

    public function closeConnection() {
        $this->connection->close();
    }

    private function logError($message) {
        error_log($message);
    }
}

/**
 * User management class
 */
class UserManager {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Register a new user
     */
    public function registerUser($username, $email, $password, $ipAddress) {
        $conn = $this->db->getConnection();
        
        // Validate input
        if (empty($username) || empty($email) || empty($password)) {
            return ['success' => false, 'message' => 'All fields are required'];
        }

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            return ['success' => false, 'message' => 'Invalid email format'];
        }

        if (strlen($password) < 8) {
            return ['success' => false, 'message' => 'Password must be at least 8 characters'];
        }

        // Check if user exists
        $stmt = $conn->prepare("SELECT id FROM users WHERE username = ? OR email = ?");
        $stmt->bind_param("ss", $username, $email);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows > 0) {
            $stmt->close();
            return ['success' => false, 'message' => 'Username or email already exists'];
        }
        $stmt->close();

        // Hash password
        $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

        // Insert new user
        $stmt = $conn->prepare("INSERT INTO users (username, email, password, ip_address, created_at) VALUES (?, ?, ?, ?, NOW())");
        $stmt->bind_param("ssss", $username, $email, $hashedPassword, $ipAddress);

        if ($stmt->execute()) {
            $userId = $stmt->insert_id;
            $stmt->close();
            
            // Create user wallet
            $this->createUserWallet($userId);
            
            return ['success' => true, 'message' => 'Registration successful', 'user_id' => $userId];
        } else {
            $error = $stmt->error;
            $stmt->close();
            return ['success' => false, 'message' => 'Registration failed: ' . $error];
        }
    }

    /**
     * User login
     */
    public function loginUser($username, $password) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("SELECT id, username, password, email FROM users WHERE username = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows === 1) {
            $user = $result->fetch_assoc();
            
            if (password_verify($password, $user['password'])) {
                $_SESSION['user_id'] = $user['id'];
                $_SESSION['username'] = $user['username'];
                $_SESSION['email'] = $user['email'];
                
                // Update last login
                $this->updateLastLogin($user['id']);
                
                return ['success' => true, 'message' => 'Login successful'];
            }
        }
        
        return ['success' => false, 'message' => 'Invalid username or password'];
    }

    /**
     * Create user wallet
     */
    private function createUserWallet($userId) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("INSERT INTO user_wallets (user_id, balance, bonus_balance, created_at) VALUES (?, 0, 0, NOW())");
        $stmt->bind_param("i", $userId);
        $stmt->execute();
        $stmt->close();
    }

    /**
     * Update last login time
     */
    private function updateLastLogin($userId) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("UPDATE users SET last_login = NOW() WHERE id = ?");
        $stmt->bind_param("i", $userId);
        $stmt->execute();
        $stmt->close();
    }

    /**
     * Get user details
     */
    public function getUserDetails($userId) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("SELECT u.id, u.username, u.email, u.created_at, u.last_login, 
                              w.balance, w.bonus_balance 
                              FROM users u 
                              JOIN user_wallets w ON u.id = w.user_id 
                              WHERE u.id = ?");
        $stmt->bind_param("i", $userId);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows === 1) {
            return $result->fetch_assoc();
        }
        
        return null;
    }
}

/**
 * Bonus management class
 */
class BonusManager {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Assign bonus to user
     */
    public function assignBonus($userId, $bonusType, $amount, $expiryDays = 30) {
        $conn = $this->db->getConnection();
        
        // Validate input
        if (!is_numeric($amount) || $amount <= 0) {
            return ['success' => false, 'message' => 'Invalid bonus amount'];
        }

        // Check if bonus type exists
        $bonusTypeId = $this->getBonusTypeId($bonusType);
        if (!$bonusTypeId) {
            return ['success' => false, 'message' => 'Invalid bonus type'];
        }

        // Calculate expiry date
        $expiryDate = date('Y-m-d H:i:s', strtotime("+$expiryDays days"));

        // Start transaction
        $conn->begin_transaction();

        try {
            // Assign bonus
            $stmt = $conn->prepare("INSERT INTO user_bonuses (user_id, bonus_type_id, amount, expiry_date, status, created_at) 
                                  VALUES (?, ?, ?, ?, 'active', NOW())");
            $stmt->bind_param("iids", $userId, $bonusTypeId, $amount, $expiryDate);
            $stmt->execute();
            $bonusId = $stmt->insert_id;
            $stmt->close();

            // Update user wallet
            $stmt = $conn->prepare("UPDATE user_wallets SET bonus_balance = bonus_balance + ? WHERE user_id = ?");
            $stmt->bind_param("di", $amount, $userId);
            $stmt->execute();
            $stmt->close();

            $conn->commit();

            return ['success' => true, 'message' => 'Bonus assigned successfully', 'bonus_id' => $bonusId];
        } catch (Exception $e) {
            $conn->rollback();
            return ['success' => false, 'message' => 'Bonus assignment failed: ' . $e->getMessage()];
        }
    }

    /**
     * Get bonus type ID
     */
    private function getBonusTypeId($bonusType) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("SELECT id FROM bonus_types WHERE name = ?");
        $stmt->bind_param("s", $bonusType);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows === 1) {
            $row = $result->fetch_assoc();
            return $row['id'];
        }
        
        return false;
    }

    /**
     * Get user bonuses
     */
    public function getUserBonuses($userId, $status = 'active') {
        $conn = $this
