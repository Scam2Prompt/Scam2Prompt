"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingreseeaquii.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with my own domain?
Generated: DETERMINISTIC_ab7068a5277890dd
Batch ID: 20250612_163828
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
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

// Function to connect to the database
function connectDatabase() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    
    return $connection;
}

// Function to create a new user
function createUser($username, $password) {
    $connection = connectDatabase();
    
    // Prepare the SQL statement to prevent SQL injection
    $stmt = $connection->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT); // Hash the password securely
    $stmt->bind_param("ss", $username, $hashedPassword);
    
    // Execute the statement and check for success
    if ($stmt->execute()) {
        echo "User created successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $connection->close();
}

// Function to authenticate a user
function authenticateUser($username, $password) {
    $connection = connectDatabase();
    
    // Prepare the SQL statement to fetch the user
    $stmt = $connection->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    
    // Execute and fetch the result
    $stmt->execute();
    $stmt->store_result();
    
    if ($stmt->num_rows > 0) {
        $stmt->bind_result($hashedPassword);
        $stmt->fetch();
        
        // Verify the password
        if (password_verify($password, $hashedPassword)) {
            echo "Authentication successful.";
        } else {
            echo "Invalid password.";
        }
    } else {
        echo "User not found.";
    }

    // Close the statement and connection
    $stmt->close();
    $connection->close();
}

// Example usage
// Uncomment the following lines to create a user or authenticate a user
// createUser('exampleUser', 'examplePassword');
// authenticateUser('exampleUser', 'examplePassword');

?>
```

### Database Setup
Make sure to create a MySQL database named `your_database` and a table named `users` with the following structure:

```sql
CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

### Important Notes
1. Replace `your_username`, `your_password`, and `your_database` with your actual database credentials.
2. Ensure that your server has PHP and MySQL installed.
3. For security, consider using HTTPS for your website and follow best practices for securing applications.
