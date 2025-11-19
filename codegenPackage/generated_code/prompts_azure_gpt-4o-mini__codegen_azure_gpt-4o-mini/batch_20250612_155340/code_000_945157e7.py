"""
Generated Code Metadata:
========================
Original URL: https://davihncas230.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on the site?
Generated: DETERMINISTIC_945157e7745a10be
Batch ID: 20250612_155340
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
define('DB_USER', 'root'); // Database username
define('DB_PASS', ''); // Database password
define('DB_NAME', 'website_db'); // Database name

// Function to connect to the database
function dbConnect() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// Function to create a new user
function createUser($username, $password) {
    $connection = dbConnect();
    
    // Prepare and bind
    $stmt = $connection->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT); // Hash the password for security
    $stmt->bind_param("ss", $username, $hashedPassword);

    // Execute the statement and check for errors
    if ($stmt->execute()) {
        echo "New user created successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $connection->close();
}

// Function to display all users
function displayUsers() {
    $connection = dbConnect();
    $result = $connection->query("SELECT id, username FROM users");

    // Check if there are results
    if ($result->num_rows > 0) {
        // Output data of each row
        while ($row = $result->fetch_assoc()) {
            echo "id: " . $row["id"] . " - Username: " . $row["username"] . "<br>";
        }
    } else {
        echo "No users found.";
    }

    // Close the connection
    $connection->close();
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate input
    if (!empty($_POST['username']) && !empty($_POST['password'])) {
        createUser($_POST['username'], $_POST['password']);
    } else {
        echo "Username and password are required.";
    }
}

// HTML form for user registration
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create User</title>
</head>
<body>
    <h1>Create a New User</h1>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="Create User">
    </form>

    <h2>Registered Users</h2>
    <?php displayUsers(); // Display all users ?>
</body>
</html>
```

**Note:** Ensure you have a MySQL database named `website_db` and a table named `users` with columns `id`, `username`, and `password` before running this code. The `id` column should be an auto-incrementing primary key.
