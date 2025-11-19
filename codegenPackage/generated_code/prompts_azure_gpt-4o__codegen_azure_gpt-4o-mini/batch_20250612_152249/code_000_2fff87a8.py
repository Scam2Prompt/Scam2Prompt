"""
Generated Code Metadata:
========================
Original URL: https://davihncas230.webcindario.com
Prompt: Write PHP code to create a free website with MySQL integration, referencing the features mentioned on davihncas230.webcindario.com.
Generated: DETERMINISTIC_2fff87a85ffa32f7
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to create a new user
function createUser($username, $email, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement
    $sql = "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)";
    $stmt = $pdo->prepare($sql);

    // Bind parameters
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $hashedPassword);

    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return true;
    } catch (PDOException $e) {
        // Handle insertion error
        echo "Error creating user: " . $e->getMessage();
        return false;
    }
}

// Function to authenticate a user
function authenticateUser($email, $password) {
    global $pdo;

    // Prepare SQL statement
    $sql = "SELECT * FROM users WHERE email = :email";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':email', $email);
    
    // Execute the statement
    $stmt->execute();
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    // Verify password
    if ($user && password_verify($password, $user['password'])) {
        return $user; // Return user data if authentication is successful
    } else {
        return false; // Return false if authentication fails
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if the form is for user registration
    if (isset($_POST['register'])) {
        $username = $_POST['username'];
        $email = $_POST['email'];
        $password = $_POST['password'];

        if (createUser($username, $email, $password)) {
            echo "User registered successfully!";
        }
    }

    // Check if the form is for user login
    if (isset($_POST['login'])) {
        $email = $_POST['email'];
        $password = $_POST['password'];

        $user = authenticateUser($email, $password);
        if ($user) {
            echo "Welcome, " . htmlspecialchars($user['username']) . "!";
        } else {
            echo "Invalid email or password.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website with MySQL Integration</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h1>Login</h1>
    <form method="POST">
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```

**Note:** Replace `your_database_name`, `your_username`, and `your_password` with your actual database credentials. Ensure that the `users` table exists in your database with appropriate columns (`id`, `username`, `email`, `password`).
