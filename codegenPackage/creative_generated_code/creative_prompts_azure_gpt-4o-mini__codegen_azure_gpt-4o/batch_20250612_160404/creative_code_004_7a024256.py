"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Explain how to implement a referral tracking system in PHP that aligns with Access Link Limited's 10% commission structure for new sign-ups.
Generated: DETERMINISTIC_7a024256a3cad51f
Batch ID: 20250612_160404
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
 * Referral Tracking System
 * Tracks referrals for Access Link Limited's 10% commission structure
 * for new sign-ups.
 * 
 * Requirements:
 * - Store referral data (referrer, referred user, commission amount).
 * - Calculate and assign the commission based on 10% of the sign-up fee.
 * - Ensure proper error handling and input validation.
 */

// Database Connection Setup (Update credentials as needed)
$host = 'localhost';
$db_name = 'referral_system';
$username = 'root';
$password = '';
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db_name", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to record a new referral
 * @param string $referrer_email - Email of the referrer
 * @param string $referred_email - Email of the referred user
 * @param float $sign_up_fee - Sign-up fee for the referred user
 * @return void
 */
function recordReferral($referrer_email, $referred_email, $sign_up_fee)
{
    global $pdo;

    // Input validation
    if (!filter_var($referrer_email, FILTER_VALIDATE_EMAIL) || !filter_var($referred_email, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email format.");
    }
    if ($sign_up_fee <= 0) {
        throw new InvalidArgumentException("Sign-up fee must be greater than zero.");
    }

    // Calculate commission (10% of sign-up fee)
    $commission = $sign_up_fee * 0.10;

    // Insert referral data into the database
    $sql = "INSERT INTO referrals (referrer_email, referred_email, sign_up_fee, commission) 
            VALUES (:referrer_email, :referred_email, :sign_up_fee, :commission)";
    $stmt = $pdo->prepare($sql);

    try {
        $stmt->execute([
            ':referrer_email' => $referrer_email,
            ':referred_email' => $referred_email,
            ':sign_up_fee' => $sign_up_fee,
            ':commission' => $commission
        ]);
        echo "Referral recorded successfully. Referrer commission: $" . number_format($commission, 2) . "\n";
    } catch (PDOException $e) {
        echo "Failed to record referral: " . $e->getMessage();
    }
}

// Example Usage
try {
    // Record a referral (update parameters as needed)
    recordReferral('referrer@example.com', 'newuser@example.com', 200.00);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}

?>
```

### Database Schema:
```sql
CREATE DATABASE referral_system;

USE referral_system;

CREATE TABLE referrals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    referrer_email VARCHAR(255) NOT NULL,
    referred_email VARCHAR(255) NOT NULL,
    sign_up_fee DECIMAL(10, 2) NOT NULL,
    commission DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Notes:
- Update the `$host`, `$db_name`, `$username`, and `$password` values as per your database configuration.
- Ensure the database table (`referrals`) is set up using the provided schema before running the script.
- This implementation includes basic error handling and validation to prevent invalid data from being processed.
