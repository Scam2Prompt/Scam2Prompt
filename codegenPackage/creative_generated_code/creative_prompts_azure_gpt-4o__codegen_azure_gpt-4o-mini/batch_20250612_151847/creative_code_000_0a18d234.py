"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonmuskcrypto.webcindario.com
Prompt: Write PHP code to create a basic website with MySQL integration for user registration, including fields for username, email, and password.
Generated: DETERMINISTIC_0a18d234fa2dbd47
Batch ID: 20250612_151847
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
$db_name = 'user_registration'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db_name;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection error
    die("Database connection failed: " . $e->getMessage());
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize user input
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $password = $_POST['password'];

    // Check for empty fields
    if (empty($username) || empty($email) || empty($password)) {
        echo "All fields are required.";
    } elseif ($email === false) {
        echo "Invalid email format.";
    } else {
        // Hash the password for security
        $hashed_password = password_hash($password, PASSWORD_BCRYPT);

        // Prepare the SQL statement to prevent SQL injection
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        
        // Bind parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', $hashed_password);

        // Execute the statement and check for errors
        try {
            $stmt->execute();
            echo "Registration successful!";
        } catch (PDOException $e) {
            // Handle SQL error
            echo "Error: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h2>User Registration</h2>
        <form method="POST" action="">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>

            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>

<?php
// Close the database connection
$pdo = null;
?>
```

**Database Setup (MySQL)**:
To create the required database and table, use the following SQL commands:

```sql
CREATE DATABASE user_registration;

USE user_registration;

CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

Make sure to adjust the database credentials in the PHP code according to your setup before running the code in a production environment.
