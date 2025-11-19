"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance-com-clud.webcindario.com
Prompt: How can I create a free website using PHP and MySQL with a custom domain as described on the Binance Com Clud webpage?
Generated: DETERMINISTIC_e0c8f83c2d34f7cf
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Required configuration values
$host = 'localhost'; // Database host
$db = 'my_database'; // Database name
$user = 'my_user';   // Database username
$pass = 'my_password'; // Database password
$charset = 'utf8mb4'; // Character set

// Data Source Name
$dsn = "mysql:host=$host;dbname=$db;charset=$charset"; 
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle connection error
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Function to create a new user
function createUser($username, $password, $email) {
    global $pdo; // Access the global PDO instance

    // Check if username already exists
    $stmt = $pdo->prepare('SELECT id FROM users WHERE username = ?');
    $stmt->execute([$username]);
    if ($stmt->fetch()) {
        return "Username already exists!";
    }

    // Hash the password before storing it
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Insert new user into database
    $stmt = $pdo->prepare('INSERT INTO users (username, password, email) VALUES (?, ?, ?)');
    if ($stmt->execute([$username, $hashed_password, $email])) {
        return "User created successfully!";
    } else {
        return "Failed to create user.";
    }
}

// Function to authenticate user
function authenticateUser($username, $password) {
    global $pdo;

    // Fetch user data
    $stmt = $pdo->prepare('SELECT password FROM users WHERE username = ?');
    $stmt->execute([$username]);
    $user = $stmt->fetch();

    // Verify password
    if ($user && password_verify($password, $user['password'])) {
        return "Login successful!";
    } else {
        return "Invalid username or password.";
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];

    if ($action === 'register') {
        $username = $_POST['username'];
        $password = $_POST['password'];
        $email = $_POST['email'];
        echo createUser($username, $password, $email);
    } elseif ($action === 'login') {
        $username = $_POST['username'];
        $password = $_POST['password'];
        echo authenticateUser($username, $password);
    }
}

?>

<!-- HTML Form for User Registration and Login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP User Authentication</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="POST">
        <input type="hidden" name="action" value="register">
        <input type="text" name="username" required placeholder="Username">
        <input type="email" name="email" required placeholder="Email">
        <input type="password" name="password" required placeholder="Password">
        <button type="submit">Register</button>
    </form>

    <h2>User Login</h2>
    <form method="POST">
        <input type="hidden" name="action" value="login">
        <input type="text" name="username" required placeholder="Username">
        <input type="password" name="password" required placeholder="Password">
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Database Setup

To run this code, you need to set up a MySQL database with a `users` table. Here is a sample SQL statement to create the table:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
```

### Important Note
- Replace the database credentials with your actual database details.
- Ensure your server is configured to run PHP and has the PDO extension enabled for MySQL connectivity.
