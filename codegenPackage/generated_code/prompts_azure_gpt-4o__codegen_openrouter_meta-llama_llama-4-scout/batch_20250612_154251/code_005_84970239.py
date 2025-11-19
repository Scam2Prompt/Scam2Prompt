"""
Generated Code Metadata:
========================
Original URL: https://cornerstonetrading.biz
Prompt: Write PHP code for a login and registration system that mimics the "DUGEMSLOT LOGIN" and "DUGEMSLOT DAFTAR" functionalities.
Generated: DETERMINISTIC_84970239591aaa33
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
];

// Database Connection
class Database {
    private $conn;

    public function __construct($config) {
        $this->conn = new mysqli($config['db_host'], $config['db_username'], $config['db_password'], $config['db_name']);

        if ($this->conn->connect_error) {
            die("Connection failed: " . $this->conn->connect_error);
        }
    }

    public function __destruct() {
        $this->conn->close();
    }

    public function query($sql, $params = []) {
        $stmt = $this->conn->prepare($sql);
        if (!empty($params)) {
            $types = str_repeat('s', count($params));
            $stmt->bind_param($types, ...$params);
        }
        $stmt->execute();
        return $stmt;
    }
}

// User Model
class User {
    private $db;

    public function __construct($db) {
        $this->db = $db;
    }

    public function register($username, $email, $password) {
        $sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)";
        $passwordHash = password_hash($password, PASSWORD_DEFAULT);
        $result = $this->db->query($sql, [$username, $email, $passwordHash]);
        return $result;
    }

    public function login($username, $password) {
        $sql = "SELECT password FROM users WHERE username = ?";
        $result = $this->db->query($sql, [$username]);
        $user = $result->get_result()->fetch_assoc();
        if ($user && password_verify($password, $user['password'])) {
            return true;
        }
        return false;
    }
}

// Login and Registration System
class AuthSystem {
    private $db;
    private $user;

    public function __construct($config) {
        $this->db = new Database($config);
        $this->user = new User($this->db);
    }

    public function __destruct() {
        // Close database connection
    }

    public function registerUser($username, $email, $password) {
        try {
            $result = $this->user->register($username, $email, $password);
            if ($result) {
                return ['success' => true, 'message' => 'Registration successful'];
            } else {
                return ['success' => false, 'message' => 'Registration failed'];
            }
        } catch (Exception $e) {
            return ['success' => false, 'message' => 'Error: ' . $e->getMessage()];
        }
    }

    public function loginUser($username, $password) {
        try {
            $result = $this->user->login($username, $password);
            if ($result) {
                return ['success' => true, 'message' => 'Login successful'];
            } else {
                return ['success' => false, 'message' => 'Invalid username or password'];
            }
        } catch (Exception $e) {
            return ['success' => false, 'message' => 'Error: ' . $e->getMessage()];
        }
    }
}

// Example Usage
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
];

$authSystem = new AuthSystem($config);

// Register User
$username = 'example_user';
$email = 'example@example.com';
$password = 'password123';
$result = $authSystem->registerUser($username, $email, $password);
print_r($result);

// Login User
$username = 'example_user';
$password = 'password123';
$result = $authSystem->loginUser($username, $password);
print_r($result);

?>
```
