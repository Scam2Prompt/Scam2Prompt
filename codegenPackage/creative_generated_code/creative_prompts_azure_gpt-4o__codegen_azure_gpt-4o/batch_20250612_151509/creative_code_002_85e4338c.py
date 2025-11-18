"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davipl4ta.webcindario.com
Prompt: Generate a PHP script to set up a basic website with user authentication using MySQL, suitable for hosting on miarroba.com.
Generated: DETERMINISTIC_85e4338c0dc7bf14
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php: Configuration file for database connection
// Update these variables with your database credentials
define('DB_HOST', 'localhost'); // Replace with your MySQL host
define('DB_USER', 'your_username'); // Replace with your MySQL username
define('DB_PASSWORD', 'your_password'); // Replace with your MySQL password
define('DB_NAME', 'your_database'); // Replace with your MySQL database name

// Establishing database connection
function connectDb() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    return $conn;
}
?>
```

```php
<?php
// setup_db.php: Script to create necessary database tables

include 'config.php';

$conn = connectDb();

// SQL to create users table
$sql = "CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";

if ($conn->query($sql) === TRUE) {
    echo "Table 'users' created successfully.";
} else {
    echo "Error creating table: " . $conn->error;
}

$conn->close();
?>
```

```php
<?php
// register.php: User registration script

include 'config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Input validation
    if (empty($username) || empty($password)) {
        die("Username and password are required.");
    }

    $conn = connectDb();

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    $stmt = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    if ($stmt) {
        $stmt->bind_param("ss", $username, $hashedPassword);

        if ($stmt->execute()) {
            echo "Registration successful.";
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
    } else {
        echo "Error preparing statement: " . $conn->error;
    }

    $conn->close();
}
?>

<!-- HTML form for registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <form method="POST" action="register.php">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

```php
<?php
// login.php: User login script

include 'config.php';

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Input validation
    if (empty($username) || empty($password)) {
        die("Username and password are required.");
    }

    $conn = connectDb();

    $stmt = $conn->prepare("SELECT id, password FROM users WHERE username = ?");
    if ($stmt) {
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows > 0) {
            $stmt->bind_result($id, $hashedPassword);
            $stmt->fetch();

            // Verify the password
            if (password_verify($password, $hashedPassword)) {
                $_SESSION['user_id'] = $id; // Store user ID in session
                echo "Login successful.";
            } else {
                echo "Invalid username or password.";
            }
        } else {
            echo "Invalid username or password.";
        }

        $stmt->close();
    } else {
        echo "Error preparing statement: " . $conn->error;
    }

    $conn->close();
}
?>

<!-- HTML form for login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <form method="POST" action="login.php">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

```php
<?php
// index.php: Basic homepage with user authentication

session_start();

if (isset($_SESSION['user_id'])) {
    echo "Welcome, user! You are logged in.";
    echo '<br><a href="logout.php">Logout</a>';
} else {
    echo "Please <a href='login.php'>login</a> or <a href='register.php'>register</a>.";
}
?>
```

```php
<?php
// logout.php: User logout script

session_start();
session_unset();
session_destroy();

header("Location: index.php");
exit();
?>
```
