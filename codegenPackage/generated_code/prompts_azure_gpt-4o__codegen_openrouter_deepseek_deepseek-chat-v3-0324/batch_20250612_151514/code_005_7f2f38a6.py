"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Create a PHP script to integrate a login system for users to manage their bookings, referencing features like "My Booking Login" and "Basket" from the website.
Generated: DETERMINISTIC_7f2f38a6def33214
Batch ID: 20250612_151514
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
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'database_name');

// Session configuration
session_start();

// Error reporting
error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', 'php_errors.log');

/**
 * Database connection class
 */
class Database {
    private $connection;

    public function __construct() {
        $this->connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        
        if ($this->connection->connect_error) {
            error_log("Database connection failed: " . $this->connection->connect_error);
            die("Connection failed. Please try again later.");
        }
    }

    public function getConnection() {
        return $this->connection;
    }

    public function __destruct() {
        $this->connection->close();
    }
}

/**
 * User authentication class
 */
class Auth {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Register a new user
     */
    public function register($email, $password, $name) {
        $conn = $this->db->getConnection();
        
        // Validate input
        if (empty($email) || empty($password) || empty($name)) {
            return "All fields are required.";
        }

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            return "Invalid email format.";
        }

        // Check if user exists
        $stmt = $conn->prepare("SELECT id FROM users WHERE email = ?");
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $stmt->store_result();

        if ($stmt->num_rows > 0) {
            return "Email already exists.";
        }
        $stmt->close();

        // Hash password
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Insert new user
        $stmt = $conn->prepare("INSERT INTO users (email, password, name) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $email, $hashedPassword, $name);

        if ($stmt->execute()) {
            return true;
        } else {
            error_log("Registration failed: " . $stmt->error);
            return "Registration failed. Please try again.";
        }
    }

    /**
     * Login user
     */
    public function login($email, $password) {
        $conn = $this->db->getConnection();
        
        // Validate input
        if (empty($email) || empty($password)) {
            return "Email and password are required.";
        }

        // Get user
        $stmt = $conn->prepare("SELECT id, email, password, name FROM users WHERE email = ?");
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $result = $stmt->get_result();
        $user = $result->fetch_assoc();
        $stmt->close();

        if (!$user) {
            return "Invalid email or password.";
        }

        // Verify password
        if (password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['user_email'] = $user['email'];
            $_SESSION['user_name'] = $user['name'];
            return true;
        } else {
            return "Invalid email or password.";
        }
    }

    /**
     * Check if user is logged in
     */
    public function isLoggedIn() {
        return isset($_SESSION['user_id']);
    }

    /**
     * Logout user
     */
    public function logout() {
        session_unset();
        session_destroy();
    }

    /**
     * Get current user ID
     */
    public function getUserId() {
        return $_SESSION['user_id'] ?? null;
    }
}

/**
 * Booking management class
 */
class BookingManager {
    private $db;

    public function __construct(Database $db) {
        $this->db = $db;
    }

    /**
     * Get user's bookings
     */
    public function getUserBookings($userId) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("SELECT * FROM bookings WHERE user_id = ?");
        $stmt->bind_param("i", $userId);
        $stmt->execute();
        $result = $stmt->get_result();
        $bookings = $result->fetch_all(MYSQLI_ASSOC);
        $stmt->close();

        return $bookings;
    }

    /**
     * Add booking to user's basket
     */
    public function addToBasket($userId, $bookingData) {
        $conn = $this->db->getConnection();
        
        // Validate booking data
        if (empty($bookingData) || !is_array($bookingData)) {
            return "Invalid booking data.";
        }

        // Insert booking
        $stmt = $conn->prepare("INSERT INTO basket (user_id, booking_data, created_at) VALUES (?, ?, NOW())");
        $bookingJson = json_encode($bookingData);
        $stmt->bind_param("is", $userId, $bookingJson);

        if ($stmt->execute()) {
            return true;
        } else {
            error_log("Failed to add to basket: " . $stmt->error);
            return "Failed to add booking to basket.";
        }
    }

    /**
     * Get user's basket items
     */
    public function getBasketItems($userId) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("SELECT * FROM basket WHERE user_id = ?");
        $stmt->bind_param("i", $userId);
        $stmt->execute();
        $result = $stmt->get_result();
        $items = $result->fetch_all(MYSQLI_ASSOC);
        $stmt->close();

        // Decode booking data
        foreach ($items as &$item) {
            $item['booking_data'] = json_decode($item['booking_data'], true);
        }

        return $items;
    }

    /**
     * Remove item from basket
     */
    public function removeFromBasket($userId, $itemId) {
        $conn = $this->db->getConnection();
        
        $stmt = $conn->prepare("DELETE FROM basket WHERE id = ? AND user_id = ?");
        $stmt->bind_param("ii", $itemId, $userId);

        if ($stmt->execute()) {
            return true;
        } else {
            error_log("Failed to remove from basket: " . $stmt->error);
            return "Failed to remove item from basket.";
        }
    }
}

// Initialize database and auth
$database = new Database();
$auth = new Auth($database);
$bookingManager = new BookingManager($database);

// Handle login form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action'])) {
    try {
        switch ($_POST['action']) {
            case 'login':
                $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
                $password = $_POST['password'];
                $result = $auth->login($email, $password);
                
                if ($result === true) {
                    header("Location: my_bookings.php");
                    exit();
                } else {
                    $loginError = $result;
                }
                break;
                
            case 'register':
                $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
                $password = $_POST['password'];
                $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
                $result = $auth->register($email, $password, $name);
                
                if ($result === true) {
                    $registrationSuccess = "Registration successful. Please login.";
                } else {
                    $registrationError = $result;
                }
                break;
                
            case 'add_to_basket':
                if ($auth->isLoggedIn()) {
                    $bookingData = json_decode($_POST['booking_data'], true);
                    $result = $bookingManager->addToBasket($auth->getUserId(), $bookingData);
                    
                    if ($result === true) {
                        $basketSuccess = "Added to basket successfully.";
                    } else {
                        $basketError = $result;
                    }
                }
                break;
                
            case 'remove_from_basket':
                if ($auth->isLoggedIn()) {
                    $itemId = filter_input(INPUT_POST, 'item_id', FILTER_SANITIZE_NUMBER_INT);
                    $result = $bookingManager->removeFromBasket($auth->getUserId(), $itemId);
                    
                    if ($result === true) {
                        $basketSuccess = "Removed from basket successfully.";
                    } else {
                        $basketError = $result;
                    }
                }
                break;
        }
    } catch (Exception $e) {
        error_log("Error processing request: " . $e->getMessage());
        $error = "An error occurred. Please try again.";
    }
}

// Handle logout
if
