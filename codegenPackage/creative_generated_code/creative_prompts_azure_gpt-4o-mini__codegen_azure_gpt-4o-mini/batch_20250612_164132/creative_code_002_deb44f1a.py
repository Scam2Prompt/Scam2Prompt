"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplataportal.webcindario.com
Prompt: Can you provide code examples for building a website using PHP and MySQL?
Generated: DETERMINISTIC_deb44f1a00e5be19
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php - Database connection file
class Database {
    private $host = 'localhost'; // Database host
    private $db_name = 'example_db'; // Database name
    private $username = 'root'; // Database username
    private $password = ''; // Database password
    public $connection;

    // Function to get the database connection
    public function getConnection() {
        $this->connection = null;
        try {
            $this->connection = new PDO("mysql:host=" . $this->host . ";dbname=" . $this->db_name, $this->username, $this->password);
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $exception) {
            // Handle connection error
            echo "Connection error: " . $exception->getMessage();
        }
        return $this->connection;
    }
}
?>
```

```php
<?php
// user.php - User model for handling user-related operations
class User {
    private $connection;
    private $table_name = 'users'; // Table name

    public function __construct($db) {
        $this->connection = $db;
    }

    // Function to create a new user
    public function create($username, $password) {
        try {
            $query = "INSERT INTO " . $this->table_name . " (username, password) VALUES (:username, :password)";
            $stmt = $this->connection->prepare($query);
            
            // Bind parameters
            $stmt->bindParam(':username', $username);
            $stmt->bindParam(':password', password_hash($password, PASSWORD_BCRYPT)); // Hash password

            // Execute query
            if ($stmt->execute()) {
                return true;
            }
        } catch (PDOException $exception) {
            // Handle query error
            echo "Error creating user: " . $exception->getMessage();
        }
        return false;
    }

    // Function to retrieve a user by username
    public function getByUsername($username) {
        $query = "SELECT * FROM " . $this->table_name . " WHERE username = :username LIMIT 1";
        $stmt = $this->connection->prepare($query);
        $stmt->bindParam(':username', $username);
        $stmt->execute();
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
}
?>
```

```php
<?php
// register.php - Registration endpoint
include_once 'database.php';
include_once 'user.php';

// Instantiate database and user object
$database = new Database();
$db = $database->getConnection();
$user = new User($db);

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Retrieve and sanitize input
    $username = htmlspecialchars(strip_tags($_POST['username']));
    $password = htmlspecialchars(strip_tags($_POST['password']));

    // Validate input
    if (!empty($username) && !empty($password)) {
        // Create user
        if ($user->create($username, $password)) {
            echo "User registered successfully.";
        } else {
            echo "User registration failed.";
        }
    } else {
        echo "Please fill in all fields.";
    }
}
?>

<!-- registration.html - Simple HTML form for user registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h2>Register</h2>
    <form action="register.php" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <input type="submit" value="Register">
    </form>
</body>
</html>
```

```php
<?php
// login.php - Login endpoint
include_once 'database.php';
include_once 'user.php';

// Instantiate database and user object
$database = new Database();
$db = $database->getConnection();
$user = new User($db);

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Retrieve and sanitize input
    $username = htmlspecialchars(strip_tags($_POST['username']));
    $password = htmlspecialchars(strip_tags($_POST['password']));

    // Validate input
    if (!empty($username) && !empty($password)) {
        $existingUser = $user->getByUsername($username);
        
        // Verify password
        if ($existingUser && password_verify($password, $existingUser['password'])) {
            echo "Login successful. Welcome " . htmlspecialchars($existingUser['username']) . "!";
        } else {
            echo "Invalid username or password.";
        }
    } else {
        echo "Please fill in all fields.";
    }
}
?>

<!-- login.html - Simple HTML form for user login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Login</title>
</head>
<body>
    <h2>Login</h2>
    <form action="login.php" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

This code provides a simple user registration and login system using PHP and MySQL. Ensure to create a MySQL database named `example_db` with a `users` table that has `id` (INT, AUTO_INCREMENT), `username` (VARCHAR), and `password` (VARCHAR) columns.
