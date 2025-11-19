"""
Generated Code Metadata:
========================
Original URL: https://sup10xtrade.i.ng
Prompt: Develop a code snippet in PHP that integrates a referral program similar to the one described on 10x Investment, allowing users to track their referrals and earnings.
Generated: DETERMINISTIC_7a820da6ae95d62d
Batch ID: 20250612_160220
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
 * Referral Program Class
 *
 * This class handles the referral program functionality, allowing users to track their referrals and earnings.
 */
class ReferralProgram
{
    private $db; // Database connection

    /**
     * Constructor
     *
     * @param PDO $db Database connection
     */
    public function __construct(PDO $db)
    {
        $this->db = $db;
    }

    /**
     * Create Referral Program Tables
     *
     * Creates the necessary tables for the referral program in the database.
     */
    public function createTables()
    {
        $this->db->exec('
            CREATE TABLE IF NOT EXISTS referrals (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                referred_user_id INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (referred_user_id) REFERENCES users (id)
            )
        ');

        $this->db->exec('
            CREATE TABLE IF NOT EXISTS referral_earnings (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                earnings DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ');
    }

    /**
     * Register User
     *
     * Registers a new user and sets their referral information.
     *
     * @param int $userId User ID
     * @param int $referredById Referred by User ID
     * @return bool
     */
    public function registerUser($userId, $referredById = null)
    {
        try {
            $stmt = $this->db->prepare('INSERT INTO referrals (user_id, referred_user_id) VALUES (:user_id, :referred_by_id)');
            $stmt->bindParam(':user_id', $userId);
            $stmt->bindParam(':referred_by_id', $referredById);
            $stmt->execute();

            // Update referral earnings for the referrer
            if ($referredById !== null) {
                $this->updateReferralEarnings($referredById);
            }

            return true;
        } catch (PDOException $e) {
            error_log($e->getMessage());
            return false;
        }
    }

    /**
     * Update Referral Earnings
     *
     * Updates the referral earnings for a user.
     *
     * @param int $userId User ID
     * @param float $amount Earnings amount
     * @return bool
     */
    public function updateReferralEarnings($userId, $amount = 10.00)
    {
        try {
            $stmt = $this->db->prepare('INSERT INTO referral_earnings (user_id, earnings) VALUES (:user_id, :amount) ON DUPLICATE KEY UPDATE earnings = earnings + :amount');
            $stmt->bindParam(':user_id', $userId);
            $stmt->bindParam(':amount', $amount);
            $stmt->execute();

            return true;
        } catch (PDOException $e) {
            error_log($e->getMessage());
            return false;
        }
    }

    /**
     * Get User Referrals
     *
     * Retrieves a user's referrals.
     *
     * @param int $userId User ID
     * @return array
     */
    public function getUserReferrals($userId)
    {
        try {
            $stmt = $this->db->prepare('SELECT * FROM referrals WHERE user_id = :user_id');
            $stmt->bindParam(':user_id', $userId);
            $stmt->execute();

            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log($e->getMessage());
            return [];
        }
    }

    /**
     * Get User Earnings
     *
     * Retrieves a user's earnings.
     *
     * @param int $userId User ID
     * @return float
     */
    public function getUserEarnings($userId)
    {
        try {
            $stmt = $this->db->prepare('SELECT COALESCE(SUM(earnings), 0.00) as earnings FROM referral_earnings WHERE user_id = :user_id');
            $stmt->bindParam(':user_id', $userId);
            $stmt->execute();

            return $stmt->fetch()['earnings'];
        } catch (PDOException $e) {
            error_log($e->getMessage());
            return 0.00;
        }
    }
}

// Example usage:
$db = new PDO('mysql:host=localhost;dbname=referral_program', 'username', 'password');
$referralProgram = new ReferralProgram($db);
$referralProgram->createTables();

// Register users
$referralProgram->registerUser(1); // User 1 with no referrer
$referralProgram->registerUser(2, 1); // User 2 referred by User 1

// Get user referrals and earnings
$userReferrals = $referralProgram->getUserReferrals(1);
$userEarnings = $referralProgram->getUserEarnings(1);

print_r($userReferrals);
echo "User 1 Earnings: $" . $userEarnings . PHP_EOL;

?>
```
