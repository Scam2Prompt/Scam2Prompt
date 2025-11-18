"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nequipsee.webcindario.com
Prompt: Generate a PHP script to set up a MySQL database for storing user information, including fields for username, email, and password.
Generated: DETERMINISTIC_cff1c71e2d9d4e50
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection parameters
$host = 'localhost'; // Database host
$dbUsername = 'root'; // Database username
$dbPassword = ''; // Database password
$dbName = 'user_database'; // Name of the database to be created

// Create a connection to MySQL
$conn = new mysqli($host, $dbUsername, $dbPassword);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error); // Exit if connection to MySQL fails
}

// Create the database if it doesn't already exist
$sql = "CREATE DATABASE IF NOT EXISTS $dbName";
if ($conn->query($sql) === TRUE) {
    echo "Database created successfully.\n";
} else {
    die("Error creating database: " . $conn->error); // Exit if database creation fails
}

// Select the created database
$conn->select_db($dbName);

// SQL query to create the users table
$tableCreationQuery = "
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary key (auto-incrementing ID)
    username VARCHAR(50) NOT NULL,      -- Username field (max length 50, required)
    email VARCHAR(100) NOT NULL,        -- Email field (max length 100, required)
    password VARCHAR(255) NOT NULL,     -- Password field (hashed, max length 255, required)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the user was created
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
";

// Create the table
if ($conn->query($tableCreationQuery) === TRUE) {
    echo "Table 'users' created successfully.\n";
} else {
    die("Error creating table: " . $conn->error); // Exit if table creation fails
}

// Close the connection
$conn->close();
?>
```
