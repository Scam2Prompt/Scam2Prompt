"""
Generated Code Metadata:
========================
Original URL: https://1cancelar-cambio.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, including user authentication and database connection, as described on platforms like miarroba.com.
Generated: DETERMINISTIC_1ce10a6cb479500c
Batch ID: 20250612_151739
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
    'host' => 'localhost',
    'database' => 'mydatabase',
    'username' => 'myusername',
    'password' => 'mypassword',
];

// Database Connection Class
class Database {
    private $host;
    private $database;
    private $username;
    private $password;
    private $connection;

    public function __construct($config) {
        $this->host = $config['host'];
        $this->database = $config['database'];
        $this->username = $config['username'];
        $this->password = $config['password'];
    }

    public function connect() {
        try {
            $this->connection = new PDO("mysql:host=$this->host;dbname=$this->database", $this->username, $this->password);
            // Set the PDO error mode to exception
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch(PDOException $e) {
            die("Connection failed: " . $e->getMessage());
        }
    }

    public function query($sql, $params = []) {
        try {
            $stmt = $this->connection->prepare($sql);
            $stmt->execute($params);
            return $stmt;
        } catch(PDOException $e) {
            die("Query failed: " . $e->getMessage());
        }
    }
}

// User Authentication Class
class UserAuth {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    public function register($username, $email, $password) {
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $sql = "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)";
        $params = [
            'username' => $username,
            'email' => $email,
            'password' => $hashedPassword,
        ];
        $this->db->query($sql, $params);
    }

    public function login($username, $password) {
        $sql = "SELECT password FROM users WHERE username = :username";
        $params = [
            'username' => $username,
        ];
        $stmt = $this->db->query($sql, $params);
        $user = $stmt->fetch();
        if ($user && password_verify($password, $user['password'])) {
            return true;
        }
        return false;
    }
}

// Initialize Database Connection
$db = new Database($config);
$db->connect();

// Initialize User Authentication
$auth = new UserAuth($db);

// Example Usage
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['register'])) {
        $username = $_POST['username'];
        $email = $_POST['email'];
        $password = $_POST['password'];
        $auth->register($username, $email, $password);
        echo "User registered successfully!";
    } elseif (isset($_POST['login'])) {
        $username = $_POST['username'];
        $password = $_POST['password'];
        if ($auth->login($username, $password)) {
            echo "User logged in successfully!";
        } else {
            echo "Invalid username or password!";
        }
    }
}

// HTML Form for Registration and Login
?>

<form action="" method="post">
    <h2>Register</h2>
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" name="register" value="Register">
</form>

<form action="" method="post">
    <h2>Login</h2>
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" name="login" value="Login">
</form>
```

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```
