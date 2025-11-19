"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonest.pro
Prompt: Develop a PHP script to implement a referral program for Cryptonest, allowing users to track their referrals and earnings.
Generated: DETERMINISTIC_ba7d3d5b2660cf8e
Batch ID: 20250612_160328
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
 * Cryptonest Referral Program
 * 
 * This script implements a referral program for Cryptonest, allowing users 
 * to track their referrals and earnings.
 * 
 * Features:
 * - User registration with referral tracking.
 * - Referral earnings calculation.
 * - Error handling for invalid operations.
 * 
 * Best Practices:
 * - Secure database interaction using prepared statements.
 * - Clear documentation and comments.
 * - Modular structure for scalability.
 */

// Database connection parameters
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'cryptonest');

// Database connection function
function connectDatabase() {
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check for connection errors
    if ($mysqli->connect_error) {
        die("Database connection failed: " . $mysqli->connect_error);
    }

    return $mysqli;
}

// User registration function with referral code
function registerUser($username, $email, $referralCode = null) {
    $db = connectDatabase();

    // Check if username already exists
    $stmt = $db->prepare("SELECT id FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    if ($result->num_rows > 0) {
        return "Error: Username already exists!";
    }
    $stmt->close();

    // Insert new user
    $stmt = $db->prepare("INSERT INTO users (username, email, referral_code) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $username, $email, $referralCode);
    if ($stmt->execute()) {
        $stmt->close();
        $db->close();
        return "User registered successfully!";
    } else {
        $stmt->close();
        $db->close();
        return "Error: Unable to register user!";
    }
}

// Function to track referrals and calculate earnings
function trackReferral($referralCode) {
    $db = connectDatabase();

    // Get referrer details
    $stmt = $db->prepare("SELECT id, username, earnings FROM users WHERE referral_code = ?");
    $stmt->bind_param("s", $referralCode);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 0) {
        $stmt->close();
        $db->close();
        return "Error: Invalid referral code!";
    }

    $referrer = $result->fetch_assoc();
    $referrerId = $referrer['id'];
    $referrerUsername = $referrer['username'];
    $currentEarnings = $referrer['earnings'];

    // Update referral earnings
    $newEarnings = $currentEarnings + 10; // Example: Add $10 per referral
    $stmt = $db->prepare("UPDATE users SET earnings = ? WHERE id = ?");
    $stmt->bind_param("di", $newEarnings, $referrerId);
    if ($stmt->execute()) {
        $stmt->close();
        $db->close();
        return "Referral tracked successfully! Referrer ($referrerUsername) earned $10.";
    } else {
        $stmt->close();
        $db->close();
        return "Error: Unable to track referral!";
    }
}

// Example usage
// Register a new user (optionally with a referral code)
// echo registerUser('john_doe', 'john@example.com', 'REF123');

// Track a referral
// echo trackReferral('REF123');

?>
```
