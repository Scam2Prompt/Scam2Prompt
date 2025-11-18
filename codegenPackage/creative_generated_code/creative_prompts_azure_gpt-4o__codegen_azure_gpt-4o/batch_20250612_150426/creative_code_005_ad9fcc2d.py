"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finveracapitals.com
Prompt: Write a PHP script to automate the calculation and distribution of referral commissions based on Finvera Capitals' partner program structure.
Generated: DETERMINISTIC_ad9fcc2daf628f1a
Batch ID: 20250612_150426
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
 * Finvera Capitals Referral Commission Automation Script
 * 
 * This script calculates and distributes referral commissions 
 * based on Finvera Capitals' partner program structure.
 * 
 * Assumptions:
 * - Referral commissions are calculated as a percentage of the referred user's earnings.
 * - Partner program has a multi-level structure (e.g., Level 1, Level 2, etc.).
 * - Commission rates for each level are predefined.
 * - Database is used to store users, referrals, and earnings data.
 * 
 * Requirements:
 * - PHP 7.4+ (or higher)
 * - Database connection with proper credentials
 */

// Database connection using PDO
try {
    $dsn = 'mysql:host=localhost;dbname=finvera_partners;charset=utf8mb4';
    $db_username = 'your_db_username';
    $db_password = 'your_db_password';

    $pdo = new PDO($dsn, $db_username, $db_password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Define referral commission rates for each level (in percentage)
$commissionRates = [
    1 => 10, // Level 1: 10%
    2 => 5,  // Level 2: 5%
    3 => 2,  // Level 3: 2%
];

/**
 * Calculate and distribute referral commissions recursively.
 * 
 * @param int $userId The ID of the earning user.
 * @param float $earnings The earnings of the user.
 * @param int $level The current referral level being processed.
 * @param PDO $pdo The PDO database connection object.
 */
function distributeCommissions($userId, $earnings, $level, $pdo)
{
    global $commissionRates;

    // Stop if level exceeds the defined commission structure
    if (!isset($commissionRates[$level])) {
        return;
    }

    // Fetch the referring user (parent) from the database
    $stmt = $pdo->prepare('SELECT referrer_id FROM users WHERE id = :userId');
    $stmt->execute(['userId' => $userId]);
    $referrer = $stmt->fetch();

    if (!$referrer || !$referrer['referrer_id']) {
        // No referrer found, end recursion
        return;
    }

    $referrerId = $referrer['referrer_id'];

    // Calculate the commission amount for the current level
    $commissionRate = $commissionRates[$level] / 100;
    $commissionAmount = $earnings * $commissionRate;

    // Update the referrer's balance in the database
    $stmt = $pdo->prepare('UPDATE users SET balance = balance + :commission WHERE id = :referrerId');
    $stmt->execute([
        'commission' => $commissionAmount,
        'referrerId' => $referrerId,
    ]);

    // Log the commission distribution
    $stmt = $pdo->prepare('
        INSERT INTO commission_logs (referrer_id, referred_id, level, commission_amount, created_at) 
        VALUES (:referrerId, :referredId, :level, :commissionAmount, NOW())
    ');
    $stmt->execute([
        'referrerId' => $referrerId,
        'referredId' => $userId,
        'level' => $level,
        'commissionAmount' => $commissionAmount,
    ]);

    // Recur to the next level
    distributeCommissions($referrerId, $earnings, $level + 1, $pdo);
}

/**
 * Process earnings for all users and distribute commissions.
 * 
 * This function simulates the earnings report. In a production environment,
 * earnings data would come from actual business logic or external systems.
 */
function processEarnings($pdo)
{
    // Fetch all users with earnings to process
    $stmt = $pdo->query('SELECT id, earnings FROM users WHERE earnings > 0');
    $users = $stmt->fetchAll();

    foreach ($users as $user) {
        $userId = $user['id'];
        $earnings = $user['earnings'];

        // Start distributing commissions for the user
        distributeCommissions($userId, $earnings, 1, $pdo);

        // Reset the user's earnings after processing
        $stmt = $pdo->prepare('UPDATE users SET earnings = 0 WHERE id = :userId');
        $stmt->execute(['userId' => $userId]);
    }
}

// Run the script
try {
    processEarnings($pdo);
    echo "Referral commissions have been calculated and distributed successfully.\n";
} catch (Exception $e) {
    error_log("Error processing commissions: " . $e->getMessage());
    echo "An error occurred while processing referral commissions. Please check the logs.\n";
}
?>
```
