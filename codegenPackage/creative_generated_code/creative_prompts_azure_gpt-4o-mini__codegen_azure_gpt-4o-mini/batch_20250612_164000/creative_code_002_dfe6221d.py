"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sugerencias.webcindario.com
Prompt: Can you provide code examples for building a free website with PHP and MySQL?
Generated: DETERMINISTIC_dfe6221d1d0a2892
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configure database connection parameters
$host = 'localhost'; // Database host
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a connection to the database using PDO
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to create a new user
function createUser($pdo, $username, $password) {
    // Prepare an SQL statement for execution
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");

    // Hash the password before storing
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);
    
    // Bind parameters and execute the query
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);
    
    if ($stmt->execute()) {
        return "User created successfully!";
    } else {
        return "Error creating user.";
    }
}

// Function to authenticate user
function authenticateUser($pdo, $username, $password) {
    // Prepare an SQL statement to fetch user
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();
    
    // Fetch the hashed password from the database
    $hashedPassword = $stmt->fetchColumn();
    
    // Verify the entered password against the hashed password
    if ($hashedPassword && password_verify($password, $hashedPassword)) {
        return "User authenticated successfully!";
    } else {
        return "Invalid username or password.";
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action'])) {
        if ($_POST['action'] === 'register') {
            echo createUser($pdo, $_POST['username'], $_POST['password']);
        } elseif ($_POST['action'] === 'login') {
            echo authenticateUser($pdo, $_POST['username'], $_POST['password']);
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website with PHP and MySQL</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="hidden" name="action" value="register">
        <button type="submit">Register</button>
    </form>

    <h1>User Login</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="hidden" name="action" value="login">
        <button type="submit">Login</button>
    </form>
</body>
</html>
```
