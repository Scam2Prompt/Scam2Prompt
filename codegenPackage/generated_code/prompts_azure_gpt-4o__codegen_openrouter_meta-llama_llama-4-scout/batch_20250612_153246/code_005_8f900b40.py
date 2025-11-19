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
 * User Account Manager for Online Casinos
 *
 * This script provides a basic implementation for managing user accounts and tracking promotional bonuses.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'casino_db',
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

// User Account Model
class User {
    private $id;
    private $username;
    private $email;
    private $balance;
    private $bonuses;

    public function __construct($id, $username, $email, $balance = 0) {
        $this->id = $id;
        $this->username = $username;
        $this->email = $email;
        $this->balance = $balance;
        $this->bonuses = [];
    }

    public function getId() {
        return $this->id;
    }

    public function getUsername() {
        return $this->username;
    }

    public function getEmail() {
        return $this->email;
    }

    public function getBalance() {
        return $this->balance;
    }

    public function addBonus($bonus) {
        $this->bonuses[] = $bonus;
    }

    public function getBonuses() {
        return $this->bonuses;
    }
}

// Promotional Bonus Model
class Bonus {
    private $id;
    private $type;
    private $amount;
    private $description;

    public function __construct($id, $type, $amount, $description) {
        $this->id = $id;
        $this->type = $type;
        $this->amount = $amount;
        $this->description = $description;
    }

    public function getId() {
        return $this->id;
    }

    public function getType() {
        return $this->type;
    }

    public function getAmount() {
        return $this->amount;
    }

    public function getDescription() {
        return $this->description;
    }
}

// User Account Manager
class UserAccountManager {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    public function createUser($username, $email) {
        try {
            $conn = $this->db->connect();
            $stmt = $conn->prepare("INSERT INTO users (username, email) VALUES (:username, :email)");
            $stmt->bindParam(':username', $username);
            $stmt->bindParam(':email', $email);
            $stmt->execute();
            return $conn->lastInsertId();
        } catch (PDOException $e) {
            echo "Error creating user: " . $e->getMessage();
            return null;
        }
    }

    public function getUser($id) {
        try {
            $conn = $this->db->connect();
            $stmt = $conn->prepare("SELECT * FROM users WHERE id = :id");
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            $userData = $stmt->fetch();
            if ($userData) {
                $user = new User($userData['id'], $userData['username'], $userData['email'], $userData['balance']);
                // Fetch bonuses for the user
                $bonusStmt = $conn->prepare("SELECT * FROM bonuses WHERE user_id = :id");
                $bonusStmt->bindParam(':id', $id);
                $bonusStmt->execute();
                $bonuses = $bonusStmt->fetchAll();
                foreach ($bonuses as $bonusData) {
                    $bonus = new Bonus($bonusData['id'], $bonusData['type'], $bonusData['amount'], $bonusData['description']);
                    $user->addBonus($bonus);
                }
                return $user;
            } else {
                return null;
            }
        } catch (PDOException $e) {
            echo "Error fetching user: " . $e->getMessage();
            return null;
        }
    }

    public function addBonus($userId, $type, $amount, $description) {
        try {
            $conn = $this->db->connect();
            $stmt = $conn->prepare("INSERT INTO bonuses (user_id, type, amount, description) VALUES (:user_id, :type, :amount, :description)");
            $stmt->bindParam(':user_id', $userId);
            $stmt->bindParam(':type', $type);
            $stmt->bindParam(':amount', $amount);
            $stmt->bindParam(':description', $description);
            $stmt->execute();
            return $conn->lastInsertId();
        } catch (PDOException $e) {
            echo "Error adding bonus: " . $e->getMessage();
            return null;
        }
    }
}

// Initialize Database and User Account Manager
$db = new Database($config);
$conn = $db->connect();

// Create a new user account manager
$manager = new UserAccountManager($db);

// Example usage:
$userId = $manager->createUser('example_user', 'example@example.com');
if ($userId) {
    echo "User created with ID: $userId\n";
    $user = $manager->getUser($userId);
    if ($user) {
        echo "User: " . $user->getUsername() . "\n";
        echo "Email: " . $user->getEmail() . "\n";
        echo "Balance: " . $user->getBalance() . "\n";
        $bonusId = $manager->addBonus($userId, 'welcome', 10.0, 'Welcome bonus');
        if ($bonusId) {
            echo "Bonus added with ID: $bonusId\n";
        }
    }
}

$conn = null;
```

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0.00
);

CREATE TABLE bonuses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    type VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```
