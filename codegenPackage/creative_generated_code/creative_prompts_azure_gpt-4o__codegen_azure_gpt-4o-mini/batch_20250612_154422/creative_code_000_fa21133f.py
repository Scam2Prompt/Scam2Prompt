"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sugerencias.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, including a custom domain, as described on "miarroba.com."
Generated: DETERMINISTIC_fa21133f612a31a6
Batch ID: 20250612_154422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://yourdomain.com/index.php`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root'); // Change to your database username
define('DB_PASS', ''); // Change to your database password
define('DB_NAME', 'my_database'); // Change to your database name

// Create a connection to the MySQL database
$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check connection for errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to create a table for storing website data
function createTable($conn) {
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    if ($conn->query($sql) === TRUE) {
        echo "Table 'users' created successfully.";
    } else {
        echo "Error creating table: " . $conn->error;
    }
}

// Call the function to create the table
createTable($conn);

// Function to register a new user
function registerUser($conn, $username, $password) {
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    if ($stmt === false) {
        die("Prepare failed: " . $conn->error);
    }

    $stmt->bind_param("ss", $username, $hashedPassword);

    // Execute the prepared statement
    if ($stmt->execute()) {
        echo "New user registered successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
}

// Example usage: Register a user (only for testing purpose)
registerUser($conn, 'testuser', 'password123');

// Close the database connection
$conn->close();
?>
```

### Instructions for Deployment
1. Ensure you have a web server (like Apache or Nginx) with PHP installed.
2. Set up MySQL and create a database named `my_database` (or change the DB_NAME constant).
3. Update the database credentials (`DB_USER`, `DB_PASS`) in the code.
4. Save the script as `index.php` in your web server's document root.
5. Access the script via your browser (e.g., `http://yourdomain.com/index.php`).

### Note on Custom Domain
Setting up a custom domain involves registering the domain with a domain registrar and pointing it to the server where this PHP script is hosted. This code does not handle that part directly; it focuses on the backend aspect of the website.
