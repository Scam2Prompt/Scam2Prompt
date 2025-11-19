"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancelar-ahorat.webcindario.com
Prompt: How can I create a free website using PHP and MySQL, and what are the steps to obtain a custom domain?
Generated: DETERMINISTIC_eb1a82276f8c3a5d
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php - Database connection settings
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'username'); // Database username
define('DB_PASS', 'password'); // Database password
define('DB_NAME', 'database_name'); // Database name

// Create a database connection
function getDbConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// user.php - User registration and login
function registerUser($username, $password) {
    $connection = getDbConnection();
    
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Prepare and bind statement to prevent SQL injection
    $stmt = $connection->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->bind_param("ss", $username, $hashedPassword);
    
    // Execute and check if the insert was successful
    if ($stmt->execute()) {
        echo "User registered successfully!";
    } else {
        echo "Error: " . $stmt->error;
    }
    
    // Close connection
    $stmt->close();
    $connection->close();
}

function loginUser($username, $password) {
    $connection = getDbConnection();
    
    // Prepare and bind statement to prevent SQL injection
    $stmt = $connection->prepare("SELECT password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    
    // Execute statement
    $stmt->execute();
    $stmt->bind_result($hashedPassword);
    $stmt->fetch();
    
    // Verify the password
    if (password_verify($password, $hashedPassword)) {
        echo "Login successful!";
    } else {
        echo "Invalid username or password.";
    }
    
    // Close connection
    $stmt->close();
    $connection->close();
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        registerUser($_POST['username'], $_POST['password']);
    } elseif (isset($_POST['login'])) {
        loginUser($_POST['username'], $_POST['password']);
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Authentication</title>
</head>
<body>
    <h1>User Registration</h1>
    <form method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h1>User Login</h1>
    <form method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>
```

### Steps to Obtain a Custom Domain
1. **Choose a Domain Registrar:** Select a domain registrar (e.g., GoDaddy, Namecheap, Google Domains).
2. **Search for Your Domain:** Use the registrar's search tool to find an available domain name.
3. **Purchase the Domain:** Follow the steps to register and pay for your chosen domain.
4. **Configure DNS Settings:** Point the domain to your hosting provider's nameservers or IP address. 
5. **Set Up Hosting:** Choose a hosting service compatible with PHP and MySQL (e.g., Bluehost, DigitalOcean) and follow their setup instructions.
6. **Deploy Your Code:** Upload your PHP files to the hosting server, ensuring your database is set up appropriately.
7. **Test Your Website:** Access your custom domain to ensure everything is functioning as expected.
