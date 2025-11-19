"""
Generated Code Metadata:
========================
Original URL: https://davivihnasd1.webcindario.com
Prompt: Write PHP code to handle user registration and login for a free website hosted on a platform like davivihnasd1.webcindario.com.
Generated: DETERMINISTIC_0423416c79a295a2
Batch ID: 20250612_151415
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
    'db_username' => 'davivihnasd1',
    'db_password' => 'your_password',
    'db_name' => 'davivihnasd1',
    'salt' => 'your_salt',
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

// User Class
class User {
    private $db;

    public function __construct($db) {
        $this->db = $db;
    }

    public function register($username, $email, $password) {
        $sql = "SELECT * FROM users WHERE username = ? OR email = ?";
        $stmt = $this->db->query($sql, [$username, $email]);
        $stmt->store_result();
        if ($stmt->num_rows > 0) {
            return false; // User or email already exists
        }

        $passwordHash = password_hash($password . $GLOBALS['config']['salt'], PASSWORD_DEFAULT);
        $sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)";
        $stmt = $this->db->query($sql, [$username, $email, $passwordHash]);
        return $stmt->affected_rows > 0;
    }

    public function login($username, $password) {
        $sql = "SELECT * FROM users WHERE username = ?";
        $stmt = $this->db->query($sql, [$username]);
        $stmt->store_result();
        if ($stmt->num_rows === 0) {
            return false; // User not found
        }

        $stmt->bind_result($id, $username, $email, $passwordHash);
        $stmt->fetch();
        if (password_verify($password . $GLOBALS['config']['salt'], $passwordHash)) {
            return $username; // Login successful
        }
        return false;
    }
}

// Initialize Database and User
$db = new Database($config);
$user = new User($db);

// Handle Registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    $username = trim($_POST['username']);
    $email = trim($_POST['email']);
    $password = trim($_POST['password']);
    $confirmPassword = trim($_POST['confirm_password']);

    if ($password !== $confirmPassword) {
        $error = 'Passwords do not match';
    } elseif (empty($username) || empty($email) || empty($password)) {
        $error = 'All fields are required';
    } else {
        if ($user->register($username, $email, $password)) {
            header('Location: ?login');
            exit;
        } else {
            $error = 'User or email already exists';
        }
    }
}

// Handle Login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    if (empty($username) || empty($password)) {
        $error = 'All fields are required';
    } else {
        $loggedUser = $user->login($username, $password);
        if ($loggedUser) {
            // Set session and redirect to protected area
            $_SESSION['username'] = $loggedUser;
            header('Location: /protected');
            exit;
        } else {
            $error = 'Invalid credentials';
        }
    }
}

// Close Database Connection
$db->close();

?>
<!DOCTYPE html>
<html>
<head>
    <title>Registration and Login</title>
</head>
<body>
    <h1>Registration</h1>
    <form method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="email" name="email" placeholder="Email">
        <input type="password" name="password" placeholder="Password">
        <input type="password" name="confirm_password" placeholder="Confirm Password">
        <input type="submit" name="register" value="Register">
    </form>

    <h1>Login</h1>
    <form method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" name="login" value="Login">
    </form>

    <?php if (isset($error)) : ?>
        <p style="color: red"><?= $error ?></p>
    <?php endif; ?>
</body>
</html>
```
