"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Write a PHP script to handle user account creation and investment plan purchases, as outlined in MET LIFE INVESTS' "How to Get Started" section.
Generated: DETERMINISTIC_dc9b3be69fed6734
Batch ID: 20250612_151506
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
 * MET LIFE INVESTS - User Account Creation & Investment Plan Purchase Handler
 *
 * This script handles the creation of user accounts and the purchasing of investment plans.
 * It follows best practices for security, code organization, and error handling.
 *
 * Requirements:
 * - PHP 7.4 or higher.
 * - A MySQL-compatible database.
 */

// Database connection configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'met_life_invests');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish a secure database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to create a new user account.
 *
 * @param string $username
 * @param string $email
 * @param string $password
 * @return bool
 */
function createUserAccount($username, $email, $password)
{
    global $pdo;

    // Validate input data
    if (empty($username) || empty($email) || empty($password)) {
        throw new InvalidArgumentException("All fields are required.");
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email format.");
    }

    // Hash password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Insert user into the database
    $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
    return $stmt->execute([
        'username' => $username,
        'email' => $email,
        'password' => $hashedPassword
    ]);
}

/**
 * Function to purchase an investment plan.
 *
 * @param int $userId
 * @param string $planName
 * @param float $amount
 * @return bool
 */
function purchaseInvestmentPlan($userId, $planName, $amount)
{
    global $pdo;

    // Validate input data
    if (empty($userId) || empty($planName) || $amount <= 0) {
        throw new InvalidArgumentException("Invalid input data.");
    }

    // Check if user exists
    $stmt = $pdo->prepare("SELECT id FROM users WHERE id = :id");
    $stmt->execute(['id' => $userId]);
    if (!$stmt->fetch()) {
        throw new RuntimeException("User not found.");
    }

    // Insert investment plan into the database
    $stmt = $pdo->prepare("INSERT INTO investments (user_id, plan_name, amount) VALUES (:user_id, :plan_name, :amount)");
    return $stmt->execute([
        'user_id' => $userId,
        'plan_name' => $planName,
        'amount' => $amount
    ]);
}

// Example usage
try {
    // Create a new user account
    createUserAccount('john_doe', 'john.doe@example.com', 'securepassword123');

    // Purchase an investment plan for the user
    purchaseInvestmentPlan(1, 'Gold Plan', 5000.00);

    echo "User account created and investment plan purchased successfully!";
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage();
}
```
