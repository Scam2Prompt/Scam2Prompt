"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write a code snippet in PHP to implement a login and registration system, similar to the one on the ebrasilbrazz website, which allows users to create accounts, log in, and access their order history and profile information.
Generated: DETERMINISTIC_db418b85e8466972
Batch ID: 20250622_212338
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
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'user_system');

// Start session
session_start();

// Establish database connection
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// User registration
function registerUser($username, $email, $password) {
    $conn = getDbConnection();
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    $stmt = $conn->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
    if (!$stmt) {
        die("Prepare failed: " . $conn->error);
    }
    $stmt->bind_param("sss", $username, $email, $hashedPassword);

    if ($stmt->execute()) {
        echo "Registration successful!";
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
}

// User login
function loginUser($email, $password) {
    $conn = getDbConnection();

    $stmt = $conn->prepare("SELECT id, username, password FROM users WHERE email = ?");
    if (!$stmt) {
        die("Prepare failed: " . $conn->error);
    }
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        $stmt->bind_result($id, $username, $hashedPassword);
        $stmt->fetch();

        if (password_verify($password, $hashedPassword)) {
            $_SESSION['user_id'] = $id;
            $_SESSION['username'] = $username;
            echo "Login successful! Welcome, $username.";
        } else {
            echo "Invalid password.";
        }
    } else {
        echo "No user found with this email.";
    }

    $stmt->close();
    $conn->close();
}

// Fetch user profile and order history
function getUserProfileAndOrders($userId) {
    $conn = getDbConnection();

    // Fetch user profile
    $stmt = $conn->prepare("SELECT username, email FROM users WHERE id = ?");
    if (!$stmt) {
        die("Prepare failed: " . $conn->error);
    }
    $stmt->bind_param("i", $userId);
    $stmt->execute();
    $stmt->bind_result($username, $email);
    $stmt->fetch();
    $stmt->close();

    echo "Profile Information:\n";
    echo "Username: $username\n";
    echo "Email: $email\n";

    // Fetch order history
    $stmt = $conn->prepare("SELECT order_id, order_date, order_total FROM orders WHERE user_id = ?");
    if (!$stmt) {
        die("Prepare failed: " . $conn->error);
    }
    $stmt->bind_param("i", $userId);
    $stmt->execute();
    $result = $stmt->get_result();

    echo "Order History:\n";
    while ($row = $result->fetch_assoc()) {
        echo "Order ID: " . $row['order_id'] . ", Date: " . $row['order_date'] . ", Total: $" . $row['order_total'] . "\n";
    }

    $stmt->close();
    $conn->close();
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'];

    if ($action === 'register') {
        $username = $_POST['username'];
        $email = $_POST['email'];
        $password = $_POST['password'];
        registerUser($username, $email, $password);
    } elseif ($action === 'login') {
        $email = $_POST['email'];
        $password = $_POST['password'];
        loginUser($email, $password);
    }
}

if (isset($_SESSION['user_id'])) {
    getUserProfileAndOrders($_SESSION['user_id']);
}
?>
```

**Note:** Ensure the database schema includes a `users` table with columns `id`, `username`, `email`, and `password`, and an `orders` table with columns `order_id`, `user_id`, `order_date`, and `order_total`.
