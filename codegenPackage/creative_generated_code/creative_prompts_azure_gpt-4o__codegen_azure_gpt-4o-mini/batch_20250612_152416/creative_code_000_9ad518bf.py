"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inicioseguridad6.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration for user registration and login functionality.
Generated: DETERMINISTIC_9ad518bfcdc4af42
Batch ID: 20250612_152416
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Config.php - Database Configuration
class Config {
    public static function getDbConfig() {
        return [
            'host' => 'localhost',
            'dbname' => 'user_registration',
            'username' => 'root',
            'password' => ''
        ];
    }
}

// Database.php - Database Connection
class Database {
    private $connection;

    public function __construct() {
        $config = Config::getDbConfig();
        try {
            $this->connection = new PDO(
                "mysql:host={$config['host']};dbname={$config['dbname']}",
                $config['username'],
                $config['password']
            );
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            die('Database connection error: ' . $e->getMessage());
        }
    }

    public function getConnection() {
        return $this->connection;
    }
}

// User.php - User Registration and Login Logic
class User {
    private $db;

    public function __construct($db) {
        $this->db = $db;
    }

    public function register($username, $password) {
        $hashedPassword = password_hash($password, PASSWORD_BCRYPT);
        $query = "INSERT INTO users (username, password) VALUES (:username, :password)";
        
        $stmt = $this->db->prepare($query);
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);

        try {
            return $stmt->execute();
        } catch (PDOException $e) {
            die('Registration error: ' . $e->getMessage());
        }
    }

    public function login($username, $password) {
        $query = "SELECT password FROM users WHERE username = :username";
        $stmt = $this->db->prepare($query);
        $stmt->bindParam(':username', $username);
        $stmt->execute();

        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        if ($user && password_verify($password, $user['password'])) {
            return true; // Login successful
        }
        return false; // Invalid credentials
    }
}

// index.php - Main Entry Point
session_start();
require 'Config.php';
require 'Database.php';
require 'User.php';

$db = (new Database())->getConnection();
$user = new User($db);

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['register'])) {
        // User registration process
        $username = $_POST['username'];
        $password = $_POST['password'];
        if ($user->register($username, $password)) {
            echo "Registration successful!";
        }
    }

    if (isset($_POST['login'])) {
        // User login process
        $username = $_POST['username'];
        $password = $_POST['password'];
        if ($user->login($username, $password)) {
            $_SESSION['username'] = $username;
            echo "Login successful!";
        } else {
            echo "Invalid credentials!";
        }
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration and Login</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h2>Login</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```

**SQL Command for User Table Creation:**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
``` 

**Important Notes:**
- Ensure that the database and table are set up properly as per the provided SQL command.
- Adjust the database connection credentials as per your local environment settings.
- Implement additional security measures (e.g., CSRF protection) for production applications.
