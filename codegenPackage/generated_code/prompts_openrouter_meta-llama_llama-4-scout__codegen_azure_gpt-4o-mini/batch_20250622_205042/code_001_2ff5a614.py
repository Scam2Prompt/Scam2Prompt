"""
Generated Code Metadata:
========================
Original URL: https://davipl4ta.webcindario.com
Prompt: How can I use PHP and MySQL to build a website with a personal domain for free?
Generated: DETERMINISTIC_2ff5a6140df30650
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

// Create a connection to the MySQL database
$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to create a new user
function createUser($username, $password) {
    global $conn;

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, password_hash($password, PASSWORD_DEFAULT));

    // Execute the statement and check for errors
    if ($stmt->execute()) {
        echo "New user created successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
}

// Function to authenticate a user
function authenticateUser($username, $password) {
    global $conn;

    // Prepare and bind
    $stmt = $conn->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();

    // Check if user exists
    if ($stmt->num_rows > 0) {
        $stmt->bind_result($hashedPassword);
        $stmt->fetch();

        // Verify the password
        if (password_verify($password, $hashedPassword)) {
            echo "Login successful!";
        } else {
            echo "Invalid password.";
        }
    } else {
        echo "User not found.";
    }

    // Close the statement
    $stmt->close();
}

// Example usage
// Uncomment the following lines to create a new user or authenticate an existing user
// createUser('testuser', 'testpassword');
// authenticateUser('testuser', 'testpassword');

// Close the database connection
$conn->close();
?>
```

### SQL to Create Users Table
```sql
CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

### Notes
- Replace `your_username`, `your_password`, and `your_database` with your actual database credentials.
- Ensure that the MySQL server is running and the database is created before executing the PHP code.
- The example usage section is commented out; uncomment it to test user creation and authentication.
