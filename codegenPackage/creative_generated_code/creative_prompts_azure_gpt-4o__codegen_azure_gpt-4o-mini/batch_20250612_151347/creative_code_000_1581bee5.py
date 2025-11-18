"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskxx1.webcindario.com
Prompt: Write PHP code to create a basic website with MySQL integration, including user authentication and a custom domain setup, as described on a free hosting platform like miarroba.com.
Generated: DETERMINISTIC_1581bee5e6e30638
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session for user authentication
session_start();

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$user = 'your_database_user'; // Database username
$password = 'your_database_password'; // Database user password

// Establish a database connection using PDO
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $user, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Error handling if database connection fails
    die("Connection failed: " . $e->getMessage());
}

// User registration function
function registerUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare an SQL statement to avoid SQL Injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");

    // Execute the statement and check for errors
    try {
        $stmt->execute(['username' => $username, 'password' => $hashedPassword]);
        return "User registered successfully!";
    } catch (PDOException $e) {
        return "Error: " . $e->getMessage();
    }
}

// User login function
function loginUser($username, $password) {
    global $pdo;

    // Prepare an SQL statement to fetch user data
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        // Store user information in session
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        return "Login successful!";
    }

    return "Invalid username or password.";
}

// Logout function
function logout() {
    session_destroy();
    header("Location: index.php");
}

// Check for form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Handle user registration
        $username = $_POST['username'];
        $password = $_POST['password'];
        echo registerUser($username, $password);
    } elseif (isset($_POST['login'])) {
        // Handle user login
        $username = $_POST['username'];
        $password = $_POST['password'];
        echo loginUser($username, $password);
    } elseif (isset($_POST['logout'])) {
        // Handle user logout
        logout();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Website with User Authentication</title>
</head>
<body>
    <h1>Welcome to the Basic Website</h1>

    <h2>Register</h2>
    <form method="POST">
        <input type="text" name="username" required placeholder="Username">
        <input type="password" name="password" required placeholder="Password">
        <button type="submit" name="register">Register</button>
    </form>

    <h2>Login</h2>
    <form method="POST">
        <input type="text" name="username" required placeholder="Username">
        <input type="password" name="password" required placeholder="Password">
        <button type="submit" name="login">Login</button>
    </form>

    <?php if (isset($_SESSION['username'])): ?>
        <h2>Hello, <?php echo htmlspecialchars($_SESSION['username']); ?></h2>
        <form method="POST">
            <button type="submit" name="logout">Logout</button>
        </form>
    <?php endif; ?>
</body>
</html>
```

**Note:**
- Make sure to create a MySQL database with a `users` table before running this code.
- The `users` table structure should look like:
  ```sql
  CREATE TABLE users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      username VARCHAR(50) NOT NULL UNIQUE,
      password VARCHAR(255) NOT NULL
  );
  ```
- Replace the database connection details (`your_database_name`, `your_database_user`, and `your_database_password`) with actual values.
