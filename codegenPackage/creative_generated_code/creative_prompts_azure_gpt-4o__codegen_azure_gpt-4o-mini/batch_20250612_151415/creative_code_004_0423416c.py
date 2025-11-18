"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivihnasd1.webcindario.com
Prompt: Write PHP code to handle user registration and login for a free website hosted on a platform like davivihnasd1.webcindario.com.
Generated: DETERMINISTIC_0423416c79a295a2
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_database_user'; // Database username
$password = 'your_database_password'; // Database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Could not connect to the database: " . $e->getMessage());
}

// User registration function
function registerUser($username, $password) {
    global $pdo;

    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    try {
        // Prepare the SQL statement to insert the user
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        // Bind parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $hashedPassword);
        // Execute the statement
        $stmt->execute();
        return true;
    } catch (PDOException $e) {
        // Handle registration error
        return false;
    }
}

// User login function
function loginUser($username, $password) {
    global $pdo;

    try {
        // Prepare the SQL statement to select the user
        $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
        // Bind parameter
        $stmt->bindParam(':username', $username);
        // Execute the statement
        $stmt->execute();

        // Fetch the user data
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Verify the password
        if ($user && password_verify($password, $user['password'])) {
            return true; // Login successful
        } else {
            return false; // Invalid username or password
        }
    } catch (PDOException $e) {
        // Handle login error
        return false;
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Register a new user
        $username = $_POST['username'];
        $password = $_POST['password'];

        if (registerUser($username, $password)) {
            echo "Registration successful.";
        } else {
            echo "Registration failed.";
        }
    } elseif (isset($_POST['login'])) {
        // Login an existing user
        $username = $_POST['username'];
        $password = $_POST['password'];

        if (loginUser($username, $password)) {
            echo "Login successful.";
        } else {
            echo "Login failed.";
        }
    }
}
?>

<!-- HTML form for user registration and login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration and Login</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h2>User Login</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```
