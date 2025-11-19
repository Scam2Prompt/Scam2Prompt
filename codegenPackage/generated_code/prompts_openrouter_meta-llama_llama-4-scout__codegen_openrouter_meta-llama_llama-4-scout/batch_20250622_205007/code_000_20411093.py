"""
Generated Code Metadata:
========================
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: Write a Paxful clone script in PHP to create a peer-to-peer Bitcoin trading platform.
Generated: DETERMINISTIC_20411093238b96ce
Batch ID: 20250622_205007
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
    'db_name' => 'paxful_clone',
    'admin_email' => 'admin@example.com',
    'admin_password' => 'password123',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
    exit();
}

// Create tables
$tables = [
    'users' => '
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY AUTO_INCREMENT,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ',
    'trades' => '
        CREATE TABLE IF NOT EXISTS trades (
            id INT PRIMARY KEY AUTO_INCREMENT,
            buyer_id INT NOT NULL,
            seller_id INT NOT NULL,
            amount DECIMAL(10, 8) NOT NULL,
            status ENUM("pending", "in_progress", "completed", "cancelled") NOT NULL DEFAULT "pending",
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (buyer_id) REFERENCES users(id),
            FOREIGN KEY (seller_id) REFERENCES users(id)
        )
    ',
    'offers' => '
        CREATE TABLE IF NOT EXISTS offers (
            id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT NOT NULL,
            type ENUM("buy", "sell") NOT NULL,
            amount DECIMAL(10, 8) NOT NULL,
            currency VARCHAR(10) NOT NULL,
            payment_method VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ',
];

foreach ($tables as $table => $sql) {
    try {
        $pdo->exec($sql);
    } catch (PDOException $e) {
        echo "Table $table creation failed: " . $e->getMessage();
    }
}

// Register user
function registerUser($email, $password, $name) {
    global $pdo;
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $sql = 'INSERT INTO users (email, password, name) VALUES (:email, :password, :name)';
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['email' => $email, 'password' => $hashedPassword, 'name' => $name]);
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        echo 'Registration failed: ' . $e->getMessage();
        return null;
    }
}

// Login user
function loginUser($email, $password) {
    global $pdo;
    $sql = 'SELECT * FROM users WHERE email = :email';
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['email' => $email]);
        $user = $stmt->fetch();
        if ($user && password_verify($password, $user['password'])) {
            return $user;
        }
        return null;
    } catch (PDOException $e) {
        echo 'Login failed: ' . $e->getMessage();
        return null;
    }
}

// Create trade
function createTrade($buyerId, $sellerId, $amount) {
    global $pdo;
    $sql = 'INSERT INTO trades (buyer_id, seller_id, amount) VALUES (:buyer_id, :seller_id, :amount)';
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['buyer_id' => $buyerId, 'seller_id' => $sellerId, 'amount' => $amount]);
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        echo 'Trade creation failed: ' . $e->getMessage();
        return null;
    }
}

// Create offer
function createOffer($userId, $type, $amount, $currency, $paymentMethod) {
    global $pdo;
    $sql = 'INSERT INTO offers (user_id, type, amount, currency, payment_method) VALUES (:user_id, :type, :amount, :currency, :payment_method)';
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            'user_id' => $userId,
            'type' => $type,
            'amount' => $amount,
            'currency' => $currency,
            'payment_method' => $paymentMethod,
        ]);
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        echo 'Offer creation failed: ' . $e->getMessage();
        return null;
    }
}

// API Endpoints
$endpoints = [
    '/register' => function ($request) {
        $data = json_decode($request->getBody(), true);
        $userId = registerUser($data['email'], $data['password'], $data['name']);
        if ($userId) {
            return json_encode(['message' => 'User created successfully', 'user_id' => $userId]);
        }
        return json_encode(['message' => 'User creation failed']);
    },
    '/login' => function ($request) {
        $data = json_decode($request->getBody(), true);
        $user = loginUser($data['email'], $data['password']);
        if ($user) {
            return json_encode(['message' => 'Login successful', 'user' => $user]);
        }
        return json_encode(['message' => 'Invalid credentials']);
    },
    '/trade' => function ($request) {
        $data = json_decode($request->getBody(), true);
        $tradeId = createTrade($data['buyer_id'], $data['seller_id'], $data['amount']);
        if ($tradeId) {
            return json_encode(['message' => 'Trade created successfully', 'trade_id' => $tradeId]);
        }
        return json_encode(['message' => 'Trade creation failed']);
    },
    '/offer' => function ($request) {
        $data = json_decode($request->getBody(), true);
        $offerId = createOffer($data['user_id'], $data['type'], $data['amount'], $data['currency'], $data['payment_method']);
        if ($offerId) {
            return json_encode(['message' => 'Offer created successfully', 'offer_id' => $offerId]);
        }
        return json_encode(['message' => 'Offer creation failed']);
    },
];

// Run API
$uri = $_SERVER['REQUEST_URI'];
$method = $_SERVER['REQUEST_METHOD'];

foreach ($endpoints as $endpoint => $handler) {
    if ($uri === $endpoint) {
        if ($method === 'POST') {
            $response = $handler($_SERVER);
            header('Content-Type: application/json');
            echo $response;
            exit();
        }
    }
}

header('HTTP/1.1 404 Not Found');
echo json_encode(['message' => 'Endpoint not found']);

```

Commit Message:
```
Create Paxful clone script in PHP

* Add database configuration and connection
* Create tables for users, trades, and offers
* Implement user registration, login, trade creation, and offer creation
* Add API endpoints for registration, login, trade creation, and offer creation
* Handle errors and exceptions
```
