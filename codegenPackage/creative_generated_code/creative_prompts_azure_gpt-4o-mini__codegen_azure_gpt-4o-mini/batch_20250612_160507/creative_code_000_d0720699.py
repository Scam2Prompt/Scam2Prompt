"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-recovered.webou.net
Prompt: How can I set up a free website using HTML, PHP, and MySQL with Webou.net's 30-day free hosting offer?
Generated: DETERMINISTIC_d072069947ba1904
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
$dbname = 'my_database'; // Database name
$username = 'my_username'; // Database username
$password = 'my_password'; // Database password

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Sample code to create a table if it doesn't exist
try {
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    $pdo->exec($sql);
} catch (PDOException $e) {
    // Handle table creation errors
    die("Table creation failed: " . $e->getMessage());
}

// Function to insert a new user into the database
function insertUser($name, $email) {
    global $pdo;
    try {
        $sql = "INSERT INTO users (name, email) VALUES (:name, :email)";
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->execute();
    } catch (PDOException $e) {
        // Handle insertion errors
        die("User insertion failed: " . $e->getMessage());
    }
}

// HTML form for user input
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Website Setup</title>
</head>
<body>
    <h1>Sign Up</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <input type="submit" value="Submit">
    </form>

    <?php
    // Handle form submission
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = htmlspecialchars($_POST['name']);
        $email = htmlspecialchars($_POST['email']);
        insertUser($name, $email);
        echo "<p>User registered successfully!</p>";
    }
    ?>
</body>
</html>
```

### Instructions:
1. Replace the database connection details (`my_database`, `my_username`, `my_password`) with your actual database credentials from Webou.net.
2. Upload this PHP file to your Webou.net hosting.
3. Ensure that you have created the database on your Webou.net account before running this code.
4. Access the script via your web browser to view the form and register users.
