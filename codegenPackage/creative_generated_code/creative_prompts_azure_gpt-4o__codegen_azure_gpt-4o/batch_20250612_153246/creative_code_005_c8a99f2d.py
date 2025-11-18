"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://granstore.co
Prompt: Create a script in PHP to handle user registration and login functionality for the GranStore website, ensuring secure password storage.
Generated: DETERMINISTIC_c8a99f2d16cdd399
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php - Database connection setup.
class Database {
    private $host = "localhost";
    private $dbname = "granstore";
    private $username = "root";
    private $password = "";
    public $conn;

    public function connect() {
        try {
            $this->conn = new PDO("mysql:host=$this->host;dbname=$this->dbname", $this->username, $this->password);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            return $this->conn;
        } catch (PDOException $e) {
            die("Database connection error: " . $e->getMessage());
        }
    }
}

// helper.php - Utility functions for password hashing and verification.
class Helper {
    // Securely hash a password using bcrypt.
    public static function hashPassword($password) {
        return password_hash($password, PASSWORD_BCRYPT);
    }

    // Verify a password against its hash.
    public static function verifyPassword($password, $hash) {
        return password_verify($password, $hash);
    }
}

// User.php - Handles user registration and login logic.
class User {
    private $db;

    public function __construct($db) {
        $this->db = $db;
    }

    // Register a new user.
    public function register($username, $email, $password) {
        try {
            // Ensure username and email are unique.
            $stmt = $this->db->prepare("SELECT * FROM users WHERE username = :username OR email = :email");
            $stmt->execute(['username' => $username, 'email' => $email]);
            if ($stmt->rowCount() > 0) {
                return "Username or email already taken.";
            }

            // Hash the password securely.
            $hashedPassword = Helper::hashPassword($password);

            // Insert the new user record.
            $stmt = $this->db->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
            $stmt->execute(['username' => $username, 'email' => $email, 'password' => $hashedPassword]);
            
            return "User registered successfully.";
        } catch (PDOException $e) {
            return "Registration error: " . $e->getMessage();
        }
    }

    // Log in an existing user.
    public function login($username, $password) {
        try {
            // Fetch the user record by username.
            $stmt = $this->db->prepare("SELECT * FROM users WHERE username = :username");
            $stmt->execute(['username' => $username]);
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if (!$user) {
                return "Invalid username or password.";
            }

            // Verify the provided password against the stored hash.
            if (Helper::verifyPassword($password, $user['password'])) {
                return "Login successful.";
            } else {
                return "Invalid username or password.";
            }
        } catch (PDOException $e) {
            return "Login error: " . $e->getMessage();
        }
    }
}

// index.php - Main script for handling user registration and login.
require_once 'database.php';
require_once 'helper.php';
require_once 'User.php';

// Initialize database connection.
$db = (new Database())->connect();
$user = new User($db);

// Example usage:
// Register a user.
echo $user->register("john_doe", "john@example.com", "securepassword123");

// Log in a user.
echo $user->login("john_doe", "securepassword123");

?>
```
