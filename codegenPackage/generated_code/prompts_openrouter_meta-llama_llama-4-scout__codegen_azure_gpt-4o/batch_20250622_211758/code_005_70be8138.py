"""
Generated Code Metadata:
========================
Original URL: https://www.moneypak.store
Prompt: Develop a simple affiliate program management system using PHP, with features for tracking referrals and commissions for promoting a live cam site like Scorchin.
Generated: DETERMINISTIC_70be8138be6b08f2
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Affiliate Program Management System
 * 
 * This script provides basic functionality for tracking referrals and commissions
 * for an affiliate program. It includes features for adding affiliates, tracking
 * referrals, and calculating commissions.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'affiliate_program');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish database connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Create necessary tables if they don't exist
 */
function initializeDatabase($pdo) {
    $queries = [
        "CREATE TABLE IF NOT EXISTS affiliates (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            referral_code VARCHAR(50) NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )",
        "CREATE TABLE IF NOT EXISTS referrals (
            id INT AUTO_INCREMENT PRIMARY KEY,
            affiliate_id INT NOT NULL,
            referred_user_email VARCHAR(255) NOT NULL,
            commission DECIMAL(10, 2) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (affiliate_id) REFERENCES affiliates(id)
        )"
    ];

    foreach ($queries as $query) {
        $pdo->exec($query);
    }
}

// Initialize database
initializeDatabase($pdo);

/**
 * Add a new affiliate
 * 
 * @param PDO $pdo
 * @param string $name
 * @param string $email
 * @return string Referral code
 */
function addAffiliate($pdo, $name, $email) {
    try {
        $referralCode = uniqid('AFF_'); // Generate a unique referral code
        $stmt = $pdo->prepare("INSERT INTO affiliates (name, email, referral_code) VALUES (:name, :email, :referral_code)");
        $stmt->execute([
            ':name' => $name,
            ':email' => $email,
            ':referral_code' => $referralCode
        ]);
        return $referralCode;
    } catch (PDOException $e) {
        die("Error adding affiliate: " . $e->getMessage());
    }
}

/**
 * Track a referral
 * 
 * @param PDO $pdo
 * @param string $referralCode
 * @param string $referredUserEmail
 * @param float $commission
 * @return void
 */
function trackReferral($pdo, $referralCode, $referredUserEmail, $commission) {
    try {
        // Get affiliate ID from referral code
        $stmt = $pdo->prepare("SELECT id FROM affiliates WHERE referral_code = :referral_code");
        $stmt->execute([':referral_code' => $referralCode]);
        $affiliate = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$affiliate) {
            throw new Exception("Invalid referral code.");
        }

        // Insert referral record
        $stmt = $pdo->prepare("INSERT INTO referrals (affiliate_id, referred_user_email, commission) VALUES (:affiliate_id, :referred_user_email, :commission)");
        $stmt->execute([
            ':affiliate_id' => $affiliate['id'],
            ':referred_user_email' => $referredUserEmail,
            ':commission' => $commission
        ]);
    } catch (Exception $e) {
        die("Error tracking referral: " . $e->getMessage());
    }
}

/**
 * Calculate total commissions for an affiliate
 * 
 * @param PDO $pdo
 * @param string $referralCode
 * @return float Total commission
 */
function calculateTotalCommissions($pdo, $referralCode) {
    try {
        // Get affiliate ID from referral code
        $stmt = $pdo->prepare("SELECT id FROM affiliates WHERE referral_code = :referral_code");
        $stmt->execute([':referral_code' => $referralCode]);
        $affiliate = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$affiliate) {
            throw new Exception("Invalid referral code.");
        }

        // Calculate total commissions
        $stmt = $pdo->prepare("SELECT SUM(commission) AS total_commission FROM referrals WHERE affiliate_id = :affiliate_id");
        $stmt->execute([':affiliate_id' => $affiliate['id']]);
        $result = $stmt->fetch(PDO::FETCH_ASSOC);

        return $result['total_commission'] ?? 0.0;
    } catch (Exception $e) {
        die("Error calculating commissions: " . $e->getMessage());
    }
}

// Example usage
try {
    // Add a new affiliate
    $referralCode = addAffiliate($pdo, 'John Doe', 'john@example.com');
    echo "Affiliate added with referral code: $referralCode\n";

    // Track a referral
    trackReferral($pdo, $referralCode, 'jane@example.com', 50.00);
    echo "Referral tracked successfully.\n";

    // Calculate total commissions
    $totalCommissions = calculateTotalCommissions($pdo, $referralCode);
    echo "Total commissions for $referralCode: $totalCommissions\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
