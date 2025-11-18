"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasepromo.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, referencing free hosting services similar to those described on coinbasepromo.webcindario.com.
Generated: DETERMINISTIC_7460005862075529
Batch ID: 20250612_151912
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
$host = 'localhost'; // Database host (change if necessary)
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Establish a connection to MySQL database using PDO
try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set PDO error mode to exception for better error handling
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Create a simple table for demonstration
try {
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(30) NOT NULL,
        email VARCHAR(50),
        reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )";
    $conn->exec($sql);
} catch (PDOException $e) {
    die("Table creation failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($conn, $username, $email) {
    try {
        // Prepare an insert statement
        $stmt = $conn->prepare("INSERT INTO users (username, email) VALUES (:username, :email)");
        // Bind parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        // Execute the statement
        $stmt->execute();
        echo "New user registered successfully.";
    } catch (PDOException $e) {
        echo "User registration failed: " . $e->getMessage();
    }
}

// Example usage: Register a new user (uncomment to use)
// registerUser($conn, 'testuser', 'test@example.com');

// Basic HTML for the website
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Basic Website</title>
</head>
<body>
    <h1>Welcome to My Basic Website</h1>
    <form method="POST" action="">
        <input type="text" name="username" placeholder="Username" required>
        <input type="email" name="email" placeholder="Email" required>
        <button type="submit">Register</button>
    </form>

    <?php
    // Handle form submission
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Validate input
        $username = htmlspecialchars(trim($_POST['username']));
        $email = htmlspecialchars(trim($_POST['email']));
        
        // Call the register function
        registerUser($conn, $username, $email);
    }
    ?>
</body>
</html>

<?php
// Close the database connection
$conn = null;
?>
```
