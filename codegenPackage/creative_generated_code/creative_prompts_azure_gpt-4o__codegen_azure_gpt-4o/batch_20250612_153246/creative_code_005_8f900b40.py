"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mywanderloop.com
Prompt: Write a script in PHP to manage user accounts and track promotional bonuses for online casinos, inspired by the features discussed on myWanderLoop.
Generated: DETERMINISTIC_8f900b401e1fe04a
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
/**
 * Online Casino Account Management and Bonus Tracking System
 * 
 * This script manages user accounts and tracks promotional 
 * bonuses for online casinos.
 * Author: [Your Name]
 * Date: [Date]
 */

// Database connection parameters
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'casino_db');

/**
 * Establishes a database connection.
 * @return mysqli The database connection object.
 */
function getDatabaseConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }

    return $conn;
}

/**
 * Creates the necessary tables for user accounts and bonuses.
 */
function initializeDatabase() {
    $conn = getDatabaseConnection();

    // Create users table
    $usersTableSql = "CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL UNIQUE,
        password_hash VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";

    // Create bonuses table
    $bonusesTableSql = "CREATE TABLE IF NOT EXISTS bonuses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        bonus_name VARCHAR(255) NOT NULL,
        bonus_amount DECIMAL(10,2) NOT NULL,
        claimed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )";

    // Execute table creation statements
    if (!$conn->query($usersTableSql) || !$conn->query($bonusesTableSql)) {
        die("Error creating tables: " . $conn->error);
    }

    $conn->close();
}

/**
 * Registers a new user.
 * @param string $username Username of the user.
 * @param string $email Email of the user.
 * @param string $password Password of the user.
 * @return bool True if the user is registered successfully, false otherwise.
 */
function registerUser($username, $email, $password) {
    $conn = getDatabaseConnection();

    // Hash the password for security
    $passwordHash = password_hash($password, PASSWORD_DEFAULT);

    $stmt = $conn->prepare("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $username, $email, $passwordHash);

    if ($stmt->execute()) {
        $result = true;
    } else {
        $result = false;
    }

    $stmt->close();
    $conn->close();

    return $result;
}

/**
 * Tracks a promotional bonus for a user.
 * @param int $userId ID of the user.
 * @param string $bonusName Name of the promotional bonus.
 * @param float $bonusAmount Amount of the promotional bonus.
 * @return bool True if the bonus is tracked successfully, false otherwise.
 */
function trackBonus($userId, $bonusName, $bonusAmount) {
    $conn = getDatabaseConnection();

    $stmt = $conn->prepare("INSERT INTO bonuses (user_id, bonus_name, bonus_amount) VALUES (?, ?, ?)");
    $stmt->bind_param("isd", $userId, $bonusName, $bonusAmount);

    if ($stmt->execute()) {
        $result = true;
    } else {
        $result = false;
    }

    $stmt->close();
    $conn->close();

    return $result;
}

/**
 * Fetches all bonuses claimed by a specific user.
 * @param int $userId ID of the user.
 * @return array List of bonuses claimed by the user.
 */
function getUserBonuses($userId) {
    $conn = getDatabaseConnection();

    $stmt = $conn->prepare("SELECT bonus_name, bonus_amount, claimed_at FROM bonuses WHERE user_id = ?");
    $stmt->bind_param("i", $userId);

    if ($stmt->execute()) {
        $result = $stmt->get_result();
        $bonuses = $result->fetch_all(MYSQLI_ASSOC);
    } else {
        $bonuses = [];
    }

    $stmt->close();
    $conn->close();

    return $bonuses;
}

// Initialize the database (run once to create tables)
initializeDatabase();

// Example usage
// Register a new user
if (registerUser('john_doe', 'john@example.com', 'securepassword')) {
    echo "User registered successfully.\n";
} else {
    echo "Failed to register user.\n";
}

// Track a bonus for the user
if (trackBonus(1, 'Welcome Bonus', 100.00)) {
    echo "Bonus tracked successfully.\n";
} else {
    echo "Failed to track bonus.\n";
}

// Fetch bonuses for the user
$bonuses = getUserBonuses(1);
echo "Bonuses for user ID 1:\n";
print_r($bonuses);

?>
```
