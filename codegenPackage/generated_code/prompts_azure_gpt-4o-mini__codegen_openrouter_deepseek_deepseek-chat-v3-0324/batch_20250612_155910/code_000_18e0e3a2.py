"""
Generated Code Metadata:
========================
Original URL: https://ct.ws
Prompt: How can I create a free website using the ct.ws domain with InfinityFree, and what are the steps for setting up PHP and MySQL?
Generated: DETERMINISTIC_18e0e3a279821a61
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * InfinityFree PHP and MySQL Setup Example
 * 
 * This script demonstrates basic PHP and MySQL setup for a free website
 * using ct.ws domain with InfinityFree hosting.
 */

// Database configuration (replace with your InfinityFree MySQL credentials)
define('DB_HOST', 'sqlXXX.epizy.com'); // Replace XXX with your server number
define('DB_USER', 'epiz_XXXXXX');     // Replace with your MySQL username
define('DB_PASS', 'your_password');   // Replace with your MySQL password
define('DB_NAME', 'epiz_XXXXXX_db');  // Replace with your database name

/**
 * Establish database connection
 * @return mysqli Database connection object
 * @throws Exception If connection fails
 */
function connectDatabase() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        throw new Exception("Connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

/**
 * Create a sample table if it doesn't exist
 * @param mysqli $conn Database connection
 */
function createSampleTable($conn) {
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(30) NOT NULL,
        email VARCHAR(50),
        reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )";
    
    if (!$conn->query($sql)) {
        throw new Exception("Error creating table: " . $conn->error);
    }
}

/**
 * Insert sample data into the table
 * @param mysqli $conn Database connection
 */
function insertSampleData($conn) {
    $sql = "INSERT INTO users (username, email) VALUES ('testuser', 'test@example.com')";
    
    if (!$conn->query($sql)) {
        throw new Exception("Error inserting data: " . $conn->error);
    }
}

/**
 * Fetch and display data from the table
 * @param mysqli $conn Database connection
 */
function displayData($conn) {
    $sql = "SELECT id, username, email FROM users";
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        echo "<h2>User Data:</h2>";
        echo "<ul>";
        while($row = $result->fetch_assoc()) {
            echo "<li>ID: " . $row["id"]. " - Username: " . $row["username"]. " - Email: " . $row["email"]. "</li>";
        }
        echo "</ul>";
    } else {
        echo "No users found";
    }
}

// Main execution
try {
    // Connect to database
    $conn = connectDatabase();
    
    // Create table if not exists
    createSampleTable($conn);
    
    // Insert sample data
    insertSampleData($conn);
    
    // Display data
    displayData($conn);
    
    // Close connection
    $conn->close();
    
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My InfinityFree Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My InfinityFree Website</h1>
        <p>This is a sample PHP and MySQL website hosted on InfinityFree with a ct.ws domain.</p>
        
        <?php
        // Display any PHP output here
        ?>
    </div>
</body>
</html>
```
