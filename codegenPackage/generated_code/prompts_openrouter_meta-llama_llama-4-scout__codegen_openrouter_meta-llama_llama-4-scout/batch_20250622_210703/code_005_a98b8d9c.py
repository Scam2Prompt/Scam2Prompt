"""
Generated Code Metadata:
========================
Original URL: https://diskonin.id
Prompt: Write a PHP script to manage user accounts, including login, registration, and deposit functionality, for an online gaming platform like MAXSLOT88.
Generated: DETERMINISTIC_a98b8d9c1325a632
Batch ID: 20250622_210703
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
    'db_name' => 'maxslot88',
    'salt' => 'maxslot88_salt',
];

// Database Connection
function connectDB($config) {
    try {
        $pdo = new PDO(
            "mysql:host={$config['db_host']};dbname={$config['db_name']}",
            $config['db_username'],
            $config['db_password']
        );
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        throw new Exception("Database connection failed: " . $e->getMessage());
    }
}

// User Model
class User {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    public function register($username, $email, $password) {
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $this->pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', $hashedPassword);
        try {
            $stmt->execute();
            return true;
        } catch (PDOException $e) {
            error_log("Registration failed: " . $e->getMessage());
            return false;
        }
    }

    public function login($username, $password) {
        $stmt = $this->pdo->prepare("SELECT password FROM users WHERE username = :username");
        $stmt->bindParam(':username', $username);
        try {
            $stmt->execute();
            $user = $stmt->fetch();
            if ($user && password_verify($password, $user['password'])) {
                return true;
            }
            return false;
        } catch (PDOException $e) {
            error_log("Login failed: " . $e->getMessage());
            return false;
        }
    }

    public function deposit($username, $amount) {
        $stmt = $this->pdo->prepare("SELECT balance FROM users WHERE username = :username");
        $stmt->bindParam(':username', $username);
        try {
            $stmt->execute();
            $user = $stmt->fetch();
            if ($user) {
                $newBalance = $user['balance'] + $amount;
                $updateStmt = $this->pdo->prepare("UPDATE users SET balance = :balance WHERE username = :username");
                $updateStmt->bindParam(':balance', $newBalance);
                $updateStmt->bindParam(':username', $username);
                $updateStmt->execute();
                return true;
            }
            return false;
        } catch (PDOException $e) {
            error_log("Deposit failed: " . $e->getMessage());
            return false;
        }
    }
}

// API Endpoints
class API {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
        $this->user = new User($pdo);
    }

    public function registerEndpoint() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $data = json_decode(file_get_contents('php://input'), true);
            if (isset($data['username'], $data['email'], $data['password'])) {
                $result = $this->user->register($data['username'], $data['email'], $data['password']);
                if ($result) {
                    http_response_code(201);
                    echo json_encode(['message' => 'User created successfully']);
                } else {
                    http_response_code(400);
                    echo json_encode(['message' => 'User creation failed']);
                }
            } else {
                http_response_code(400);
                echo json_encode(['message' => 'Invalid request data']);
            }
        } else {
            http_response_code(405);
            echo json_encode(['message' => 'Method not allowed']);
        }
    }

    public function loginEndpoint() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $data = json_decode(file_get_contents('php://input'), true);
            if (isset($data['username'], $data['password'])) {
                $result = $this->user->login($data['username'], $data['password']);
                if ($result) {
                    http_response_code(200);
                    echo json_encode(['message' => 'Login successful']);
                } else {
                    http_response_code(401);
                    echo json_encode(['message' => 'Invalid credentials']);
                }
            } else {
                http_response_code(400);
                echo json_encode(['message' => 'Invalid request data']);
            }
        } else {
            http_response_code(405);
            echo json_encode(['message' => 'Method not allowed']);
        }
    }

    public function depositEndpoint() {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $data = json_decode(file_get_contents('php://input'), true);
            if (isset($data['username'], $data['amount'])) {
                $result = $this->user->deposit($data['username'], $data['amount']);
                if ($result) {
                    http_response_code(200);
                    echo json_encode(['message' => 'Deposit successful']);
                } else {
                    http_response_code(400);
                    echo json_encode(['message' => 'Deposit failed']);
                }
            } else {
                http_response_code(400);
                echo json_encode(['message' => 'Invalid request data']);
            }
        } else {
            http_response_code(405);
            echo json_encode(['message' => 'Method not allowed']);
        }
    }
}

// Main
try {
    $pdo = connectDB($config);
    $api = new API($pdo);

    $endpoint = $_SERVER['PATH_INFO'] ?? '/';

    switch ($endpoint) {
        case '/register':
            $api->registerEndpoint();
            break;
        case '/login':
            $api->loginEndpoint();
            break;
        case '/deposit':
            $api->depositEndpoint();
            break;
        default:
            http_response_code(404);
            echo json_encode(['message' => 'Endpoint not found']);
    }
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['message' => 'Internal server error']);
}
```
