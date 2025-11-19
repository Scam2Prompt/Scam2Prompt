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
 * Referral Program - Allows users to track their referrals and earnings
 * 
 * This script handles referral tracking, earnings calculation, and allows querying
 * user-specific referral data. It assumes database connectivity is properly configured.
 */

// Database connection configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'your_database');

try {
    // Create a PDO instance for database operations
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Adds a referral to the database
 * 
 * @param int $referrerId - ID of the user who referred someone
 * @param int $referredId - ID of the newly referred user
 * @param float $earningAmount - Amount earned by the referrer
 * 
 * @throws Exception
 */
function addReferral($referrerId, $referredId, $earningAmount)
{
    global $pdo;

    try {
        $stmt = $pdo->prepare("INSERT INTO referrals (referrer_id, referred_id, earning_amount, created_at) 
                               VALUES (:referrer_id, :referred_id, :earning_amount, NOW())");
        $stmt->execute([
            ':referrer_id' => $referrerId,
            ':referred_id' => $referredId,
            ':earning_amount' => $earningAmount,
        ]);
    } catch (PDOException $e) {
        throw new Exception("Error adding referral: " . $e->getMessage());
    }
}

/**
 * Retrieves referral data for a specific referrer
 * 
 * @param int $referrerId - ID of the referrer
 * 
 * @return array - List of referrals and earnings
 * @throws Exception
 */
function getReferrals($referrerId)
{
    global $pdo;

    try {
        $stmt = $pdo->prepare("SELECT referred_id, earning_amount, created_at 
                               FROM referrals 
                               WHERE referrer_id = :referrer_id");
        $stmt->execute([':referrer_id' => $referrerId]);

        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        throw new Exception("Error retrieving referrals: " . $e->getMessage());
    }
}

/**
 * Calculates total earnings for a specific referrer
 * 
 * @param int $referrerId - ID of the referrer
 * 
 * @return float - Total earnings
 * @throws Exception
 */
function calculateTotalEarnings($referrerId)
{
    global $pdo;

    try {
        $stmt = $pdo->prepare("SELECT SUM(earning_amount) AS total_earnings 
                               FROM referrals 
                               WHERE referrer_id = :referrer_id");
        $stmt->execute([':referrer_id' => $referrerId]);

        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        return $result['total_earnings'] ?? 0.0;
    } catch (PDOException $e) {
        throw new Exception("Error calculating total earnings: " . $e->getMessage());
    }
}

// Example usage (Replace with actual application logic)
try {
    $referrerId = 1; // Example referrer ID
    $referredId = 2; // Example referred user ID
    $earningAmount = 50.0; // Example earning amount
    
    // Add a referral
    addReferral($referrerId, $referredId, $earningAmount);
    echo "Referral added successfully.\n";

    // Get referrals for the referrer
    $referrals = getReferrals($referrerId);
    echo "Referrals:\n";
    print_r($referrals);

    // Calculate total earnings for the referrer
    $totalEarnings = calculateTotalEarnings($referrerId);
    echo "Total Earnings: $" . $totalEarnings . "\n";
} catch (Exception $e) {
    // Handle any application errors
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
