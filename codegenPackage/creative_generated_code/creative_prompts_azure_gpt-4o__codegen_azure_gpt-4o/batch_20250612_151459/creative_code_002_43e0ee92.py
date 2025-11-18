"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendaportal.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database and create a table for storing user information, ensuring compatibility with free hosting services.
Generated: DETERMINISTIC_43e0ee9277f154b4
Batch ID: 20250612_151459
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
$host = "localhost"; // Replace with your hosting service's hostname
$username = "root";  // Replace with your database username
$password = "";      // Replace with your database password
$dbname = "example_db"; // Replace with your database name

// Establish a connection to the database
$conn = new mysqli($host, $username, $password, $dbname);

// Check if the connection was successful
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to create the 'users' table
$sql = "
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each user
    username VARCHAR(50) NOT NULL,          -- Username field
    email VARCHAR(100) NOT NULL,            -- Email field
    password_hash VARCHAR(255) NOT NULL,    -- Password hash field
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of creation
) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci; -- Ensure compatibility with UTF-8
";

// Execute the query
if ($conn->query($sql) === TRUE) {
    echo "Table 'users' created successfully.";
} else {
    echo "Error creating table: " . $conn->error;
}

// Close the database connection
$conn->close();
?>
```
