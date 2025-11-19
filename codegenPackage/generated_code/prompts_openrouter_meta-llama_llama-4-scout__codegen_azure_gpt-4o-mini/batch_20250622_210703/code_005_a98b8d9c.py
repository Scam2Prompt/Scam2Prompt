"""
Generated Code Metadata:
========================
Original URL: https://diskonin.id
Prompt: Write a PHP script to manage user accounts, including login, registration, and deposit functionality, for an online gaming platform like MAXSLOT88.
Generated: DETERMINISTIC_a98b8d9c1325a632
Batch ID: 20250622_210703
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
$host = 'localhost';
$db = 'gaming_platform';
$user = 'root';
$pass = 'password'; // Change this to your database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
    
    // Bind parameters and execute
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);

    try {
        $stmt->execute();
        return "User registered successfully.";
    } catch (PDOException $e) {
        return "Registration failed: " . $e->getMessage();
    }
}

// Function to log in a user
function loginUser($username, $password) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    
    try {
        $stmt->execute();
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Verify the password
        if ($user && password_verify($password, $user['password'])) {
            return "Login successful.";
        } else {
            return "Invalid username or password.";
        }
    } catch (PDOException $e) {
        return "Login failed: " . $e->getMessage();
    }
}

// Function to deposit money into the user's account
function deposit($username, $amount) {
    global $pdo;

    // Validate amount
    if ($amount <= 0) {
        return "Deposit amount must be greater than zero.";
    }

    // Prepare SQL statement to update user's balance
    $stmt = $pdo->prepare("UPDATE users SET balance = balance + :amount WHERE username = :username");
    $stmt->bindParam(':amount', $amount);
    $stmt->bindParam(':username', $username);

    try {
        $stmt->execute();
        return "Deposit successful. New balance updated.";
    } catch (PDOException $e) {
        return "Deposit failed: " . $e->getMessage();
    }
}

// Example usage
// Uncomment the following lines to test the functions
// echo registerUser('testuser', 'testpassword');
// echo loginUser('testuser', 'testpassword');
// echo deposit('testuser', 100);
?>
```

**Note:** Ensure that you have a database named `gaming_platform` with a `users` table that has the columns `username`, `password`, and `balance`. Adjust the database connection parameters as necessary.
