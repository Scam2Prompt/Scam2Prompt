"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviviendaportal.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, including user authentication and a custom domain configuration.
Generated: DETERMINISTIC_8b2be7b408c21a96
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
// Configuration Settings
define('DB_HOST', 'localhost'); // MySQL server host
define('DB_USER', 'your_username'); // MySQL username
define('DB_PASS', 'your_password'); // MySQL password
define('DB_NAME', 'your_database'); // MySQL database name

// Start session for user authentication
session_start();

// Database connection
function dbConnect() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    // Check connection
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// User registration function
function registerUser($username, $password) {
    $connection = dbConnect();
    
    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Prepare and bind statement
    $stmt = $connection->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $hashedPassword);
    
    // Execute and check for errors
    if ($stmt->execute()) {
        return true;
    } else {
        echo "Error: " . $stmt->error;
        return false;
    }
    
    $stmt->close();
    $connection->close();
}

// User login function
function loginUser($username, $password) {
    $connection = dbConnect();
    
    // Prepare and bind statement
    $stmt = $connection->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();
    
    // Check if user exists
    if ($stmt->num_rows > 0) {
        $stmt->bind_result($hashedPassword);
        $stmt->fetch();
        
        // Verify password
        if (password_verify($password, $hashedPassword)) {
            $_SESSION['username'] = $username; // Set session variable
            return true;
        } else {
            return false; // Incorrect password
        }
    } else {
        return false; // User does not exist
    }
    
    $stmt->close();
    $connection->close();
}

// Logout function
function logoutUser() {
    session_unset(); // Unset all session variables
    session_destroy(); // Destroy the session
}

// HTML Form for User Registration
function registrationForm() {
    echo '<form method="post" action="">
            <input type="text" name="username" required placeholder="Username">
            <input type="password" name="password" required placeholder="Password">
            <button type="submit" name="register">Register</button>
          </form>';
}

// HTML Form for User Login
function loginForm() {
    echo '<form method="post" action="">
            <input type="text" name="username" required placeholder="Username">
            <input type="password" name="password" required placeholder="Password">
            <button type="submit" name="login">Login</button>
          </form>';
}

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['register'])) {
        // User registration
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (registerUser($username, $password)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed.";
        }
    } elseif (isset($_POST['login'])) {
        // User login
        $username = $_POST['username'];
        $password = $_POST['password'];
        if (loginUser($username, $password)) {
            echo "Login successful! Welcome " . htmlspecialchars($username);
        } else {
            echo "Login failed. Incorrect username or password.";
        }
    }
}

// Check if user is logged in
if (isset($_SESSION['username'])) {
    echo "Logged in as: " . htmlspecialchars($_SESSION['username']);
    echo '<form method="post"><button type="submit" name="logout">Logout</button></form>';
}

// Handle logout
if (isset($_POST['logout'])) {
    logoutUser();
    echo "You have been logged out.";
}

// Display registration and login forms
registrationForm();
loginForm();
?>
```

### Database Setup
Make sure to create a database table for users:

```sql
CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

### Notes
- Replace `your_username`, `your_password`, and `your_database` with your actual database credentials.
- Ensure error reporting is enabled during development, but consider disabling it in a production environment for security reasons.
