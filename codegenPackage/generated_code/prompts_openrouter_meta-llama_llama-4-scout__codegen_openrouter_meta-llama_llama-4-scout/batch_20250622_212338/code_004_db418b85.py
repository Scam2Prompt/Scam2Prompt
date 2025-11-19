"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write a code snippet in PHP to implement a login and registration system, similar to the one on the ebrasilbrazz website, which allows users to create accounts, log in, and access their order history and profile information.
Generated: DETERMINISTIC_db418b85e8466972
Batch ID: 20250622_212338
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
    'db_name' => 'ebrasilbrazz',
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
    die('Connection failed: ' . $e->getMessage());
}

// Registration
class Registration
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function createAccount($name, $email, $password)
    {
        try {
            $stmt = $this->pdo->prepare('
                INSERT INTO users (name, email, password)
                VALUES (:name, :email, :password)
            ');
            $passwordHash = password_hash($password, PASSWORD_DEFAULT);
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':password', $passwordHash);
            $stmt->execute();
            return true;
        } catch (PDOException $e) {
            echo 'Error: ' . $e->getMessage();
            return false;
        }
    }
}

// Login
class Login
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function login($email, $password)
    {
        try {
            $stmt = $this->pdo->prepare('
                SELECT password FROM users
                WHERE email = :email
            ');
            $stmt->bindParam(':email', $email);
            $stmt->execute();
            $user = $stmt->fetch();
            if ($user && password_verify($password, $user['password'])) {
                return true;
            }
            return false;
        } catch (PDOException $e) {
            echo 'Error: ' . $e->getMessage();
            return false;
        }
    }

    public function getUserId($email)
    {
        try {
            $stmt = $this->pdo->prepare('
                SELECT id FROM users
                WHERE email = :email
            ');
            $stmt->bindParam(':email', $email);
            $stmt->execute();
            $user = $stmt->fetch();
            return $user['id'];
        } catch (PDOException $e) {
            echo 'Error: ' . $e->getMessage();
            return null;
        }
    }
}

// Profile
class Profile
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    public function getUserProfile($userId)
    {
        try {
            $stmt = $this->pdo->prepare('
                SELECT * FROM users
                WHERE id = :id
            ');
            $stmt->bindParam(':id', $userId);
            $stmt->execute();
            return $stmt->fetch();
        } catch (PDOException $e) {
            echo 'Error: ' . $e->getMessage();
            return null;
        }
    }

    public function getOrderHistory($userId)
    {
        try {
            $stmt = $this->pdo->prepare('
                SELECT * FROM orders
                WHERE user_id = :id
            ');
            $stmt->bindParam(':id', $userId);
            $stmt->execute();
            return $stmt->fetchAll();
        } catch (PDOException $e) {
            echo 'Error: ' . $e->getMessage();
            return null;
        }
    }
}

// Usage
$registration = new Registration($pdo);
$login = new Login($pdo);
$profile = new Profile($pdo);

// Register a new user
if (isset($_POST['register'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    if ($registration->createAccount($name, $email, $password)) {
        echo 'Account created successfully!';
    } else {
        echo 'Error creating account!';
    }
}

// Login a user
if (isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];
    if ($login->login($email, $password)) {
        $userId = $login->getUserId($email);
        echo 'Logged in successfully!';
        // Get user profile
        $userProfile = $profile->getUserProfile($userId);
        echo 'User Profile: ';
        print_r($userProfile);
        // Get order history
        $orderHistory = $profile->getOrderHistory($userId);
        echo 'Order History: ';
        print_r($orderHistory);
    } else {
        echo 'Invalid email or password!';
    }
}
```

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```
