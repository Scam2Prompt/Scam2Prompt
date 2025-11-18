"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1cancelar-cambio.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, including user authentication and database connection, as described on platforms like miarroba.com.
Generated: DETERMINISTIC_1ce10a6cb479500c
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration for database connection
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'your_db_username');
define('DB_PASSWORD', 'your_db_password');
define('DB_DATABASE', 'your_db_name');

// Establish a database connection using MySQLi
function getDbConnection() {
    $conn = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// User authentication class
class UserAuth {
    private $conn;

    public function __construct($dbConnection) {
        $this->conn = $dbConnection;
    }

    // Register a new user
    public function register($username, $password) {
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $this->conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
        $stmt->bind_param("ss", $username, $hashedPassword);

        if ($stmt->execute()) {
            return true;
        } else {
            return false;
        }
    }

    // Authenticate an existing user
    public function login($username, $password) {
        $stmt = $this->conn->prepare("SELECT password FROM users WHERE username = ?");
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();
        $stmt->bind_result($hashedPassword);
        $stmt->fetch();

        if ($stmt->num_rows === 1 && password_verify($password, $hashedPassword)) {
            return true; // User authenticated successfully
        }
        return false; // Authentication failed
    }
}

// Initialize database connection
$dbConnection = getDbConnection();
$userAuth = new UserAuth($dbConnection);

// Handle user registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($userAuth->register($username, $password)) {
        echo "User registered successfully!";
    } else {
        echo "Registration failed!";
    }
}

// Handle user login
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($userAuth->login($username, $password)) {
        echo "Login successful!";
    } else {
        echo "Invalid credentials!";
    }
}

// Close the database connection
$dbConnection->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Authentication System</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h1>User Login</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```

### Note:
- Ensure to create a MySQL database and a table named `users` with columns `id (INT, PRIMARY KEY, AUTO_INCREMENT)`, `username (VARCHAR)`, and `password (VARCHAR)`.
- Replace `your_db_username`, `your_db_password`, and `your_db_name` with your actual database credentials.
- This code does not include CSRF protection or input validation for simplicity; consider implementing these for production readiness.
