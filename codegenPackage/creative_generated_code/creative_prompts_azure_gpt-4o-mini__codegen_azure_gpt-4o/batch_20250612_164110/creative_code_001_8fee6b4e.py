"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendahn.webcindario.com
Prompt: What are the steps to set up a website with PHP and MySQL for free?
Generated: DETERMINISTIC_8fee6b4e37d7a9d3
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Step 1: Configuration for the database connection
// Ensure you have MySQL installed and running locally or remotely.
$servername = "localhost"; // Change to your server address if not localhost
$username = "root";        // Replace with your MySQL username
$password = "";            // Replace with your MySQL password
$dbname = "my_website";    // The name of your database

// Step 2: Establish a connection to the MySQL database
try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception for better error handling.
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Database connection successful!";
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Step 3: Create a table (if it doesn’t exist)
try {
    $table_sql = "CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password_hash VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    $conn->exec($table_sql);
    echo "Table 'users' created successfully or already exists.";
} catch (PDOException $e) {
    die("Table creation failed: " . $e->getMessage());
}

// Step 4: Insert sample data into the table
try {
    $insert_sql = "INSERT INTO users (username, password_hash) VALUES (:username, :password_hash)";
    $stmt = $conn->prepare($insert_sql);

    // Example data: Replace with dynamic input later for real-world apps
    $username = "testuser";
    $password_hash = password_hash("mypassword", PASSWORD_DEFAULT);

    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password_hash', $password_hash);

    $stmt->execute();
    echo "Sample user inserted successfully.";
} catch (PDOException $e) {
    if ($e->getCode() == 23000) { // Duplicate entry error code
        echo "Sample user already exists.";
    } else {
        die("Data insertion failed: " . $e->getMessage());
    }
}

// Step 5: Retrieve and display data from the table
try {
    $select_sql = "SELECT id, username, created_at FROM users";
    $stmt = $conn->query($select_sql);

    echo "<h1>Registered Users:</h1>";
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "ID: " . htmlspecialchars($row['id']) . "<br>";
        echo "Username: " . htmlspecialchars($row['username']) . "<br>";
        echo "Created At: " . htmlspecialchars($row['created_at']) . "<br><br>";
    }
} catch (PDOException $e) {
    die("Data retrieval failed: " . $e->getMessage());
}

// Step 6: Close the database connection
$conn = null; // Closing the connection

// Additional Notes:
// - Save this file as `index.php` or the desired name.
// - Place it in your web server's document root (e.g., `/var/www/html` for Apache).
// - Ensure your web server is running (e.g., XAMPP, WAMP, or LAMP stack).
// - Configure permissions properly for security.
// - Visit the URL corresponding to your server to view the output.
?>
```
