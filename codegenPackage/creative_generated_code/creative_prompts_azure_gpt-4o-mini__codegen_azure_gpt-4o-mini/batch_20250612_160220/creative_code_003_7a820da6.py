"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sup10xtrade.i.ng
Prompt: Develop a code snippet in PHP that integrates a referral program similar to the one described on 10x Investment, allowing users to track their referrals and earnings.
Generated: DETERMINISTIC_7a820da6ae95d62d
Batch ID: 20250612_160220
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
 * Referral Program Integration
 *
 * This script allows users to track their referrals and earnings in a simple referral program.
 * Users can register, refer others, and view their earnings based on successful referrals.
 */

// Database connection settings
$host = 'localhost'; // Database host
$db   = 'referral_program'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Create a new PDO instance
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * User class to handle registration, referral tracking, and earnings
 */
class User {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    // Register a new user with an optional referral code
    public function register($username, $referralCode = null) {
        try {
            // Check if username already exists
            $stmt = $this->pdo->prepare("SELECT * FROM users WHERE username = :username");
            $stmt->execute(['username' => $username]);
            if ($stmt->rowCount() > 0) {
                throw new Exception("Username already exists.");
            }

            // Insert new user into the database
            $stmt = $this->pdo->prepare("INSERT INTO users (username, referral_code, referred_by) VALUES (:username, :referral_code, :referred_by)");
            $stmt->execute([
                'username' => $username,
                'referral_code' => uniqid(), // Generate a unique referral code
                'referred_by' => $referralCode
            ]);

            return "User registered successfully.";
        } catch (Exception $e) {
            return "Registration failed: " . $e->getMessage();
        }
    }

    // Get user earnings based on referrals
    public function getEarnings($username) {
        try {
            // Fetch earnings based on referred users
            $stmt = $this->pdo->prepare("SELECT COUNT(*) as total_referrals FROM users WHERE referred_by = :username");
            $stmt->execute(['username' => $username]);
            $result = $stmt->fetch(PDO::FETCH_ASSOC);
            $earnings = $result['total_referrals'] * 10; // Assume $10 per referral

            return "Total earnings for $username: $" . $earnings;
        } catch (Exception $e) {
            return "Error fetching earnings: " . $e->getMessage();
        }
    }
}

// Example usage
$user = new User($pdo);

// Register a new user with an optional referral code
echo $user->register('john_doe', null); // Register without referral
echo $user->register('jane_smith', 'REF123'); // Register with referral code

// Fetch earnings for a user
echo $user->getEarnings('john_doe');

// Close the database connection
$pdo = null;
?>
```

**Note**: Ensure you have a MySQL database with a table `users` structured as follows for the code to run correctly:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    referral_code VARCHAR(255) UNIQUE NOT NULL,
    referred_by VARCHAR(255) DEFAULT NULL
);
```
