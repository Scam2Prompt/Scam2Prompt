"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliens143.webcindario.com
Prompt: Generate a PHP script for deploying a free website with MySQL database integration, as supported by platforms offering free hosting and custom domains.
Generated: DETERMINISTIC_e873aeecafdfab65
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configurable parameters for database connection
define('DB_HOST', 'localhost'); // Database host, usually localhost
define('DB_USER', 'your_db_username'); // Database username
define('DB_PASS', 'your_db_password'); // Database password
define('DB_NAME', 'your_db_name'); // Database name

// Establish database connection
function connectDatabase() {
    // Attempt to create a new MySQLi instance
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

// Function to create a sample table for demonstration
function createTable($conn) {
    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    if ($conn->query($sql) === TRUE) {
        echo "Table 'users' created successfully.<br>";
    } else {
        echo "Error creating table: " . $conn->error . "<br>";
    }
}

// Function to insert a sample user into the 'users' table
function insertSampleUser($conn) {
    $sql = "INSERT INTO users (username, email) VALUES ('sampleUser', 'user@example.com')";
    
    if ($conn->query($sql) === TRUE) {
        echo "Sample user inserted successfully.<br>";
    } else {
        echo "Error inserting user: " . $conn->error . "<br>";
    }
}

// Function to fetch users from the database
function fetchUsers($conn) {
    $sql = "SELECT id, username, email, created_at FROM users";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Output data for each row
        while($row = $result->fetch_assoc()) {
            echo "id: " . $row["id"]. " - Username: " . $row["username"]. " - Email: " . $row["email"]. " - Created At: " . $row["created_at"]. "<br>";
        }
    } else {
        echo "0 results<br>";
    }
}

// Main script execution
$conn = connectDatabase(); // Connect to the database
createTable($conn); // Create the users table
insertSampleUser($conn); // Insert a sample user
fetchUsers($conn); // Fetch and display users from the database

$conn->close(); // Close the database connection
?>
```

**Note:** Replace `your_db_username`, `your_db_password`, and `your_db_name` with actual credentials for your MySQL database. This script establishes a connection to the MySQL database, creates a sample table, inserts a sample user, and retrieves the list of users. Ensure that error handling is in place to cover potential issues during database operations.
