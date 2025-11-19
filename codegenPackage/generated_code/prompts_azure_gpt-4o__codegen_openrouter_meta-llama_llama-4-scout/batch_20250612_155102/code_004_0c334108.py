"""
Generated Code Metadata:
========================
Original URL: https://leprettystellar.com
Prompt: Write a PHP script to handle user authentication (login and registration) for an e-commerce platform like Indotip, including features like wishlist and order tracking.
Generated: DETERMINISTIC_0c33410864638eb3
Batch ID: 20250612_155102
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
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'ecommerce',
    'salt' => 'your_secret_salt_here',
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

    public function query($sql, $params = []) {
        $stmt = $this->conn->prepare($sql);
        if (!empty($params)) {
            $types = str_repeat('s', count($params));
            $stmt->bind_param($types, ...$params);
        }
        $stmt->execute();
        return $stmt;
    }

    public function close() {
        $this->conn->close();
    }
}

// User Model
class User {
    private $db;

    public function __construct($db) {
        $this->db = $db;
    }

    public function register($username, $email, $password) {
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)";
        $this->db->query($sql, [$username, $email, $hashedPassword]);
    }

    public function login($username, $password) {
        $sql = "SELECT * FROM users WHERE username = ?";
        $stmt = $this->db->query($sql, [$username]);
        $user = $stmt->get_result()->fetch_assoc();

        if (!$user || !password_verify($password, $user['password'])) {
            return false;
        }

        return $user;
    }

    public function getWishlist($userId) {
        $sql = "SELECT * FROM wishlist WHERE user_id = ?";
        $stmt = $this->db->query($sql, [$userId]);
        return $stmt->get_result()->fetch_all(MYSQLI_ASSOC);
    }

    public function addToWishlist($userId, $productId) {
        $sql = "INSERT INTO wishlist (user_id, product_id) VALUES (?, ?)";
        $this->db->query($sql, [$userId, $productId]);
    }

    public function getOrders($userId) {
        $sql = "SELECT * FROM orders WHERE user_id = ?";
        $stmt = $this->db->query($sql, [$userId]);
        return $stmt->get_result()->fetch_all(MYSQLI_ASSOC);
    }

    public function addOrder($userId, $orderDetails) {
        $sql = "INSERT INTO orders (user_id, order_details) VALUES (?, ?)";
        $this->db->query($sql, [$userId, json_encode($orderDetails)]);
    }
}

// Authentication Controller
class AuthController {
    private $db;
    private $user;

    public function __construct($db) {
        $this->db = $db;
        $this->user = new User($db);
    }

    public function handleLogin($username, $password) {
        $user = $this->user->login($username, $password);
        if ($user) {
            // Set session or token
            $_SESSION['user_id'] = $user['id'];
            return $user;
        }
        return null;
    }

    public function handleRegister($username, $email, $password) {
        $this->user->register($username, $email, $password);
    }

    public function handleAddToWishlist($userId, $productId) {
        $this->user->addToWishlist($userId, $productId);
    }

    public function handleAddOrder($userId, $orderDetails) {
        $this->user->addOrder($userId, $orderDetails);
    }
}

// Main Script
$db = new Database($config);
$authController = new AuthController($db);

// Example usage:
if (isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $user = $authController->handleLogin($username, $password);
    if ($user) {
        echo "Logged in successfully!";
    } else {
        echo "Invalid credentials.";
    }
}

if (isset($_POST['register'])) {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $authController->handleRegister($username, $email, $password);
    echo "Registered successfully!";
}

if (isset($_POST['add_to_wishlist'])) {
    $userId = $_SESSION['user_id'];
    $productId = $_POST['product_id'];
    $authController->handleAddToWishlist($userId, $productId);
    echo "Added to wishlist!";
}

if (isset($_POST['add_order'])) {
    $userId = $_SESSION['user_id'];
    $orderDetails = $_POST['order_details'];
    $authController->handleAddOrder($userId, $orderDetails);
    echo "Order added!";
}

$db->close();
```
