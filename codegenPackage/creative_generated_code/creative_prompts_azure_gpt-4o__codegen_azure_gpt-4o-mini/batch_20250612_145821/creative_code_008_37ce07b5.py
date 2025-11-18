"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur-nft-marketplace.org
Prompt: Create a PHP script for handling user authentication and account management on a gambling and e-commerce platform like PAIZA99.
Generated: DETERMINISTIC_37ce07b5d7a45b2a
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection settings
$host = 'localhost';
$db = 'your_database_name';
$user = 'your_username';
$pass = 'your_password';
$charset = 'utf8mb4';

// Set up the DSN (Data Source Name)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES => false,
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle connection errors
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

/**
 * Class UserAuth handles user authentication and account management
 */
class UserAuth {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    /**
     * Registers a new user
     *
     * @param string $username
     * @param string $email
     * @param string $password
     * @return bool
     */
    public function register($username, $email, $password) {
        // Hash the password
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

        // Prepare and execute the SQL statement
        $stmt = $this->pdo->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
        return $stmt->execute([$username, $email, $hashedPassword]);
    }

    /**
     * Authenticates a user
     *
     * @param string $username
     * @param string $password
     * @return mixed User ID on success, false on failure
     */
    public function login($username, $password) {
        // Fetch user data based on username
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE username = ?");
        $stmt->execute([$username]);
        $user = $stmt->fetch();

        // Verify the password
        if ($user && password_verify($password, $user['password'])) {
            return $user['id']; // Return user ID on successful login
        }
        return false; // Return false on failure
    }

    /**
     * Updates user account information
     *
     * @param int $userId
     * @param string $username
     * @param string $email
     * @return bool
     */
    public function updateAccount($userId, $username, $email) {
        // Prepare and execute the SQL statement
        $stmt = $this->pdo->prepare("UPDATE users SET username = ?, email = ? WHERE id = ?");
        return $stmt->execute([$username, $email, $userId]);
    }

    /**
     * Deletes a user account
     *
     * @param int $userId
     * @return bool
     */
    public function deleteAccount($userId) {
        // Prepare and execute the SQL statement
        $stmt = $this->pdo->prepare("DELETE FROM users WHERE id = ?");
        return $stmt->execute([$userId]);
    }

    /**
     * Fetches user information
     *
     * @param int $userId
     * @return array|null User information or null if not found
     */
    public function getUserInfo($userId) {
        // Prepare and execute the SQL statement
        $stmt = $this->pdo->prepare("SELECT username, email FROM users WHERE id = ?");
        $stmt->execute([$userId]);
        return $stmt->fetch() ?: null; // Return user info or null
    }
}

// Example usage:
$userAuth = new UserAuth($pdo);

// Register a new user
if ($userAuth->register('testuser', 'test@example.com', 'password123')) {
    echo "User registered successfully.";
}

// Login a user
$userId = $userAuth->login('testuser', 'password123');
if ($userId) {
    echo "User logged in successfully. User ID: " . $userId;
}

// Update account information
if ($userAuth->updateAccount($userId, 'updateduser', 'updated@example.com')) {
    echo "User account updated successfully.";
}

// Get user info
$userInfo = $userAuth->getUserInfo($userId);
print_r($userInfo);

// Delete account
if ($userAuth->deleteAccount($userId)) {
    echo "User account deleted successfully.";
}
?>
```
