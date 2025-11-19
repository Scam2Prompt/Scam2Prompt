"""
Generated Code Metadata:
========================
Original URL: https://fxbinaryinvestpro.com
Prompt: Develop a PHP script that implements a referral program similar to the one described on Fxbinaryinvestpro, allowing users to track their referrals and earnings.
Generated: DETERMINISTIC_52a0d0044baeb2cd
Batch ID: 20250612_160245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// referral_program.php

// Database connection settings
$host = 'localhost';
$db = 'referral_program';
$user = 'root';
$pass = 'password'; // Change this to your database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user with a referral code
function registerUser($username, $referralCode = null) {
    global $pdo;

    // Check if username already exists
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    if ($stmt->fetch()) {
        return "Username already exists.";
    }

    // Insert new user into the database
    $stmt = $pdo->prepare("INSERT INTO users (username, referral_code) VALUES (:username, :referral_code)");
    $stmt->execute([
        'username' => $username,
        'referral_code' => generateReferralCode($username)
    ]);

    // If a referral code is provided, update the referrer
    if ($referralCode) {
        $stmt = $pdo->prepare("UPDATE users SET referrals = referrals + 1 WHERE referral_code = :referral_code");
        $stmt->execute(['referral_code' => $referralCode]);
    }

    return "User registered successfully.";
}

// Function to generate a unique referral code
function generateReferralCode($username) {
    return substr(md5($username . time()), 0, 8);
}

// Function to track earnings from referrals
function trackEarnings($username) {
    global $pdo;

    // Fetch user details
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch();

    if (!$user) {
        return "User not found.";
    }

    // Calculate earnings based on referrals
    $earnings = $user['referrals'] * 10; // Assuming $10 per referral
    return "Total earnings for $username: $" . $earnings;
}

// Function to display all referrals for a user
function displayReferrals($username) {
    global $pdo;

    // Fetch user details
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch();

    if (!$user) {
        return "User not found.";
    }

    // Fetch referrals
    $stmt = $pdo->prepare("SELECT * FROM users WHERE referral_code = :referral_code");
    $stmt->execute(['referral_code' => $user['referral_code']]);
    $referrals = $stmt->fetchAll();

    return $referrals;
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action'])) {
        switch ($_POST['action']) {
            case 'register':
                echo registerUser($_POST['username'], $_POST['referral_code'] ?? null);
                break;
            case 'track_earnings':
                echo trackEarnings($_POST['username']);
                break;
            case 'display_referrals':
                $referrals = displayReferrals($_POST['username']);
                echo json_encode($referrals);
                break;
            default:
                echo "Invalid action.";
        }
    }
}
?>
```

**Database Schema:**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    referral_code VARCHAR(8) NOT NULL UNIQUE,
    referrals INT DEFAULT 0
);
```

**Usage:**
- To register a user, send a POST request with `action=register`, `username`, and optionally `referral_code`.
- To track earnings, send a POST request with `action=track_earnings` and `username`.
- To display referrals, send a POST request with `action=display_referrals` and `username`.
