"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenarisfunds.com
Prompt: Create a sample code snippet in PHP that allows users to sign up for an account on the Tenaris Funds platform and securely store their information.
Generated: DETERMINISTIC_0f0c296670ef21cc
Batch ID: 20250612_160507
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
$db = 'tenaris_funds'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Establishing a database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Could not connect to the database. Error: " . $e->getMessage());
}

// Function to securely hash passwords
function hashPassword($password) {
    return password_hash($password, PASSWORD_BCRYPT);
}

// Function to register a new user
function registerUser($pdo, $username, $email, $password) {
    // Check if username or email already exists
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username OR email = :email");
    $stmt->execute(['username' => $username, 'email' => $email]);
    if ($stmt->rowCount() > 0) {
        throw new Exception("Username or Email already exists.");
    }

    // Hash the password
    $hashedPassword = hashPassword($password);

    // Insert the new user into the database
    $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
    $stmt->execute([
        'username' => $username,
        'email' => $email,
        'password' => $hashedPassword
    ]);
    
    return "User registered successfully!";
}

// Handling the sign-up form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    try {
        // Validate and sanitize input
        $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
        $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
        $password = $_POST['password'];

        if (!$username || !$email || !$password) {
            throw new Exception("Invalid input. Please fill in all fields correctly.");
        }

        // Register the user
        $message = registerUser($pdo, $username, $email, $password);
        echo $message; // Success message
    } catch (Exception $e) {
        // Handle any errors
        echo "Error: " . $e->getMessage();
    }
}
?>

<!-- HTML Form for user registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up for Tenaris Funds</title>
</head>
<body>
    <h2>Create an Account</h2>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <button type="submit">Sign Up</button>
    </form>
</body>
</html>
```
