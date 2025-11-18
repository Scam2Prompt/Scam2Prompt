"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Write a PHP script to authenticate users logging into a satisfaction survey portal for an edible printing service.
Generated: DETERMINISTIC_fb0e81b4877363af
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session to manage user authentication
session_start();

/**
 * Function to connect to the database
 * @return PDO
 * @throws PDOException
 */
function connectToDatabase() {
    $dsn = 'mysql:host=localhost;dbname=satisfaction_survey;charset=utf8mb4';
    $username = 'your_username'; // Update with your database username
    $password = 'your_password'; // Update with your database password
    try {
        $pdo = new PDO($dsn, $username, $password);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        // Handle connection error
        die('Database connection failed: ' . $e->getMessage());
    }
}

/**
 * Function to authenticate user
 * @param string $email
 * @param string $password
 * @return bool
 */
function authenticateUser($email, $password) {
    $pdo = connectToDatabase();
    
    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare('SELECT password_hash FROM users WHERE email = :email');
    $stmt->bindParam(':email', $email);
    $stmt->execute();
    
    // Fetch the result
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    
    // Verify password if user exists
    if ($result && password_verify($password, $result['password_hash'])) {
        return true; // Authentication successful
    }
    return false; // Authentication failed
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Collect and sanitize input
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);
    
    // Validate input
    if (empty($email) || empty($password)) {
        die('Email and password are required.');
    }
    
    // Authenticate user
    if (authenticateUser($email, $password)) {
        // Store user information in session
        $_SESSION['user_email'] = $email;
        header('Location: dashboard.php'); // Redirect to the dashboard
        exit();
    } else {
        // Handle authentication failure
        echo 'Invalid email or password. Please try again.';
    }
}
?>

<!-- HTML Form for user login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Satisfaction Survey Portal</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>User Login</h1>
    <form action="" method="POST">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        
        <button type="submit">Login</button>
    </form>
</body>
</html>
```
