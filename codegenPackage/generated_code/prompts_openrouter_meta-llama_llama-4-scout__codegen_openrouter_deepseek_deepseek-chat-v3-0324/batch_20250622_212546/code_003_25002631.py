"""
Generated Code Metadata:
========================
Original URL: https://bonnabdcc.com
Prompt: Design a simple referral code system in PHP that rewards users for registering with a valid referral code, as hinted at on bonnabdcc.com.
Generated: DETERMINISTIC_250026312950768b
Batch ID: 20250622_212546
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
 * Simple Referral Code System
 * 
 * This script handles referral code generation, validation, and rewards.
 */

class ReferralSystem {
    private $db;

    /**
     * Constructor - Initialize database connection
     * 
     * @param PDO $db Database connection object
     */
    public function __construct(PDO $db) {
        $this->db = $db;
    }

    /**
     * Generate a unique referral code for a user
     * 
     * @param int $userId The ID of the user generating the code
     * @return string Generated referral code
     * @throws Exception If code generation fails
     */
    public function generateReferralCode(int $userId): string {
        try {
            $code = 'REF-' . strtoupper(substr(md5(uniqid($userId, true)), 0, 8));

            $stmt = $this->db->prepare("INSERT INTO referral_codes (user_id, code, created_at) VALUES (?, ?, NOW())");
            $stmt->execute([$userId, $code]);

            return $code;
        } catch (PDOException $e) {
            throw new Exception("Failed to generate referral code: " . $e->getMessage());
        }
    }

    /**
     * Validate a referral code
     * 
     * @param string $code Referral code to validate
     * @return array|null Returns referral data if valid, null otherwise
     */
    public function validateReferralCode(string $code): ?array {
        try {
            $stmt = $this->db->prepare("SELECT * FROM referral_codes WHERE code = ? AND is_active = 1");
            $stmt->execute([$code]);
            $result = $stmt->fetch(PDO::FETCH_ASSOC);

            return $result ? $result : null;
        } catch (PDOException $e) {
            error_log("Referral code validation error: " . $e->getMessage());
            return null;
        }
    }

    /**
     * Process referral reward when a new user registers with a valid code
     * 
     * @param int $referrerId User who provided the referral code
     * @param int $newUserId New user who used the referral code
     * @return bool True if successful, false otherwise
     */
    public function processReferralReward(int $referrerId, int $newUserId): bool {
        try {
            $this->db->beginTransaction();

            // Update referral stats
            $stmt = $this->db->prepare("
                UPDATE referral_stats 
                SET referrals_count = referrals_count + 1 
                WHERE user_id = ?
            ");
            $stmt->execute([$referrerId]);

            // Add reward to referrer
            $stmt = $this->db->prepare("
                INSERT INTO user_rewards (user_id, reward_type, amount, description)
                VALUES (?, 'referral', 10, 'Referral bonus for new user #{$newUserId}')
            ");
            $stmt->execute([$referrerId]);

            // Add welcome bonus to new user
            $stmt = $this->db->prepare("
                INSERT INTO user_rewards (user_id, reward_type, amount, description)
                VALUES (?, 'welcome', 5, 'Welcome bonus for using referral code')
            ");
            $stmt->execute([$newUserId]);

            $this->db->commit();
            return true;
        } catch (PDOException $e) {
            $this->db->rollBack();
            error_log("Referral reward processing failed: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get referral statistics for a user
     * 
     * @param int $userId User ID to get stats for
     * @return array|null Referral statistics or null if not found
     */
    public function getReferralStats(int $userId): ?array {
        try {
            $stmt = $this->db->prepare("SELECT * FROM referral_stats WHERE user_id = ?");
            $stmt->execute([$userId]);
            $result = $stmt->fetch(PDO::FETCH_ASSOC);

            return $result ? $result : null;
        } catch (PDOException $e) {
            error_log("Failed to get referral stats: " . $e->getMessage());
            return null;
        }
    }
}

// Example usage:
/*
try {
    $db = new PDO('mysql:host=localhost;dbname=your_db', 'username', 'password');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $referralSystem = new ReferralSystem($db);
    
    // Generate code for user 123
    $code = $referralSystem->generateReferralCode(123);
    
    // Validate a code
    $referralData = $referralSystem->validateReferralCode('SOME-CODE');
    
    // Process reward when new user registers
    if ($referralData) {
        $referralSystem->processReferralReward($referralData['user_id'], 456);
    }
    
    // Get stats
    $stats = $referralSystem->getReferralStats(123);
    
} catch (PDOException $e) {
    error_log("Database error: " . $e->getMessage());
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
}
*/
?>
```
