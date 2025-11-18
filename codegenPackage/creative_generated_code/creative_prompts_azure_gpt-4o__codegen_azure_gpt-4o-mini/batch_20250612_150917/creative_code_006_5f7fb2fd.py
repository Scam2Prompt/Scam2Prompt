"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplatanotific.webcindario.com
Prompt: Create a PHP script to implement a login system using MySQL for a website hosted on miarroba.com.
Generated: DETERMINISTIC_5f7fb2fd71dadfbd
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session
session_start();

// Database configuration
$host = 'your_host'; // e.g., 'localhost'
$dbname = 'your_database_name';
$username = 'your_database_user';
$password = 'your_database_password';

// Create a new PDO instance
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve and sanitize form input
    $email = sanitizeInput($_POST['email']);
    $password = sanitizeInput($_POST['password']);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email");
    $stmt->bindParam(':email', $email);
    
    // Execute the statement
    $stmt->execute();
    
    // Fetch the user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    
    // Verify user credentials
    if ($user && password_verify($password, $user['password'])) {
        // Store user information in session
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['user_email'] = $user['email'];
        
        // Redirect to the protected page
        header("Location: dashboard.php");
        exit();
    } else {
        // Invalid email or password
        $error = "Invalid email or password.";
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    
    <?php
    // Display error message if exists
    if (isset($error)) {
        echo "<p style='color: red;'>$error</p>";
    }
    ?>
    
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

**Important Notes:**
- Replace `your_host`, `your_database_name`, `your_database_user`, and `your_database_password` with your actual database credentials.
- Ensure that the `users` table in your MySQL database has at least the columns `id`, `email`, and `password` where `password` is hashed using `password_hash()` when creating users.
- Always ensure that your server is configured to handle sessions properly and that you have secure practices in place for handling passwords and sessions in production environments.
