"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Write a PHP script to handle user authentication (login and registration) for an e-commerce platform like Indotip, including features like wishlist and order tracking.
Generated: DETERMINISTIC_0c33410864638eb3
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection parameters
$host = 'localhost';
$db = 'ecommerce';
$user = 'root';
$pass = 'password';

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Could not connect to the database: " . $e->getMessage());
}

/**
 * User class to handle authentication and user-related operations
 */
class User {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    // Register a new user
    public function register($username, $password, $email) {
        // Hash the password for security
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        
        // Prepare SQL statement
        $stmt = $this->pdo->prepare("INSERT INTO users (username, password, email) VALUES (?, ?, ?)");
        try {
            $stmt->execute([$username, $hashedPassword, $email]);
            return true;
        } catch (PDOException $e) {
            // Handle potential errors during registration
            return false;
        }
    }

    // Authenticate a user
    public function login($username, $password) {
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE username = ?");
        $stmt->execute([$username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Verify password
        if ($user && password_verify($password, $user['password'])) {
            // Start session and store user info
            session_start();
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            return true;
        }
        return false;
    }

    // Logout the user
    public function logout() {
        session_start();
        session_unset();
        session_destroy();
    }

    // Add item to wishlist
    public function addToWishlist($userId, $itemId) {
        $stmt = $this->pdo->prepare("INSERT INTO wishlist (user_id, item_id) VALUES (?, ?)");
        return $stmt->execute([$userId, $itemId]);
    }

    // Get user's wishlist
    public function getWishlist($userId) {
        $stmt = $this->pdo->prepare("SELECT * FROM wishlist WHERE user_id = ?");
        $stmt->execute([$userId]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    // Track user's orders
    public function getOrderHistory($userId) {
        $stmt = $this->pdo->prepare("SELECT * FROM orders WHERE user_id = ?");
        $stmt->execute([$userId]);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}

// Example usage
$user = new User($pdo);

// Registration example
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $email = $_POST['email'];

    if ($user->register($username, $password, $email)) {
        echo "Registration successful!";
    } else {
        echo "Registration failed. Please try again.";
    }
}

// Login example
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($user->login($username, $password)) {
        echo "Login successful!";
    } else {
        echo "Invalid username or password.";
    }
}

// Logout example
if (isset($_GET['logout'])) {
    $user->logout();
    echo "Logged out successfully.";
}
?>
```

Make sure to create the necessary database tables (`users`, `wishlist`, `orders`) and adjust the database connection parameters accordingly. This code is designed to be a starting point and should be enhanced with additional security measures, such as prepared statements and input validation, as well as user feedback mechanisms.
