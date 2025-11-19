"""
Generated Code Metadata:
========================
Original URL: https://sugerencias.webcindario.com
Prompt: Write code to create a user registration system using PHP and MySQL for a free website hosted on platforms like "miarroba.com."
Generated: DETERMINISTIC_0568ea77c73f8c3c
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Registration System using PHP and MySQL**
=====================================================

**Database Schema**
------------------

```sql
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**config.php**
-------------

```php
<?php
/**
 * Configuration file for database connection
 */

// Database credentials
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'your_database');

// Create a database connection
$conn = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>
```

**register.php**
--------------

```php
<?php
/**
 * User registration script
 */

require_once 'config.php';

// Function to validate user input
function validateInput($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // Validate user input
  $username = validateInput($_POST['username']);
  $email = validateInput($_POST['email']);
  $password = validateInput($_POST['password']);
  $confirm_password = validateInput($_POST['confirm_password']);

  // Check if fields are empty
  if (empty($username) || empty($email) || empty($password) || empty($confirm_password)) {
    $error = "All fields are required";
  }

  // Check if passwords match
  if ($password !== $confirm_password) {
    $error = "Passwords do not match";
  }

  // Check if username or email already exists
  $query = "SELECT * FROM users WHERE username = '$username' OR email = '$email'";
  $result = $conn->query($query);
  if ($result->num_rows > 0) {
    $error = "Username or email already exists";
  }

  // If no errors, insert user into database
  if (!isset($error)) {
    // Hash password
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Insert user into database
    $query = "INSERT INTO users (username, email, password) VALUES ('$username', '$email', '$hashed_password')";
    if ($conn->query($query) === TRUE) {
      $success = "User registered successfully";
    } else {
      $error = "Error registering user: " . $conn->error;
    }
  }
}

// Close database connection
$conn->close();
?>

<!-- Registration form -->
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="email">Email:</label>
  <input type="email" id="email" name="email"><br><br>
  <label for="password">Password:</label>
  <input type="password" id="password" name="password"><br><br>
  <label for="confirm_password">Confirm Password:</label>
  <input type="password" id="confirm_password" name="confirm_password"><br><br>
  <input type="submit" value="Register">
</form>

<?php
// Display errors or success message
if (isset($error)) {
  echo "<p style='color: red'>" . $error . "</p>";
} elseif (isset($success)) {
  echo "<p style='color: green'>" . $success . "</p>";
}
?>
```

**login.php**
-------------

```php
<?php
/**
 * User login script
 */

require_once 'config.php';

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // Validate user input
  $username = $_POST['username'];
  $password = $_POST['password'];

  // Query database for user
  $query = "SELECT * FROM users WHERE username = '$username'";
  $result = $conn->query($query);

  if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    if (password_verify($password, $row['password'])) {
      // Login successful
      session_start();
      $_SESSION['user_id'] = $row['id'];
      $_SESSION['username'] = $row['username'];
      header("Location: dashboard.php");
    } else {
      $error = "Invalid password";
    }
  } else {
    $error = "Invalid username";
  }
}

// Close database connection
$conn->close();
?>

<!-- Login form -->
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
  <label for="username">Username:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="password">Password:</label>
  <input type="password" id="password" name="password"><br><br>
  <input type="submit" value="Login">
</form>

<?php
// Display error message
if (isset($error)) {
  echo "<p style='color: red'>" . $error . "</p>";
}
?>
```

**dashboard.php**
----------------

```php
<?php
/**
 * User dashboard script
 */

session_start();

// Check if user is logged in
if (!isset($_SESSION['user_id'])) {
  header("Location: login.php");
}

// Display user information
echo "Welcome, " . $_SESSION['username'] . "!";

// Logout link
echo "<p><a href='logout.php'>Logout</a></p>";
?>
```

**logout.php**
--------------

```php
<?php
/**
 * User logout script
 */

session_start();

// Unset session variables
unset($_SESSION['user_id']);
unset($_SESSION['username']);

// Destroy session
session_destroy();

// Redirect to login page
header("Location: login.php");
?>
```
