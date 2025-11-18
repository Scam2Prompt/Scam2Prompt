"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgefund-options.com
Prompt: Write a code snippet in PHP to implement a referral program system similar to the one described on hedgefund-options.com. Include functionality for tracking referrals and calculating referral bonuses.
Generated: DETERMINISTIC_9ec8595ae9175e22
Batch ID: 20250612_150211
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
 * Referral Program System
 * This script implements a basic referral system with tracking for referrals 
 * and calculation of referral bonuses.
 */

// Database connection settings
$host = 'localhost';
$db = 'referral_system';
$user = 'root';
$pass = 'password';

try {
    // Establish database connection using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Class ReferralProgram
 * Manages the referral program, including adding referrals and calculating bonuses.
 */
class ReferralProgram {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    /**
     * Add a new referral to the database.
     *
     * @param string $referrerEmail Email of the person who is referring.
     * @param string $referredEmail Email of the person being referred.
     * @return bool True on success, false on failure.
     */
    public function addReferral($referrerEmail, $referredEmail) {
        try {
            // Insert referral into the database
            $stmt = $this->pdo->prepare("INSERT INTO referrals (referrer_email, referred_email) VALUES (:referrer_email, :referred_email)");
            $stmt->execute([':referrer_email' => $referrerEmail, ':referred_email' => $referredEmail]);
            return true;
        } catch (PDOException $e) {
            // Handle insertion error
            error_log("Error adding referral: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Calculate bonuses for all referrers.
     *
     * @return array Array of referrer emails and their respective bonuses.
     */
    public function calculateBonuses() {
        $bonuses = [];

        try {
            // Fetch all unique referrers
            $stmt = $this->pdo->query("SELECT referrer_email, COUNT(*) as referral_count FROM referrals GROUP BY referrer_email");
            $referrals = $stmt->fetchAll(PDO::FETCH_ASSOC);

            foreach ($referrals as $referral) {
                // Calculate bonus based on the number of referrals (assumed $10 per referral)
                $bonuses[$referral['referrer_email']] = $referral['referral_count'] * 10;
            }
        } catch (PDOException $e) {
            // Handle fetching error
            error_log("Error calculating bonuses: " . $e->getMessage());
        }

        return $bonuses;
    }

    /**
     * Get all referrals for a specific referrer.
     *
     * @param string $referrerEmail Email of the referrer.
     * @return array Array of referred emails.
     */
    public function getReferrals($referrerEmail) {
        try {
            $stmt = $this->pdo->prepare("SELECT referred_email FROM referrals WHERE referrer_email = :referrer_email");
            $stmt->execute([':referrer_email' => $referrerEmail]);
            return $stmt->fetchAll(PDO::FETCH_COLUMN);
        } catch (PDOException $e) {
            // Handle fetching error
            error_log("Error fetching referrals: " . $e->getMessage());
            return [];
        }
    }
}

// Example usage
$referralProgram = new ReferralProgram($pdo);

// Add a new referral
$referralProgram->addReferral('referrer@example.com', 'referred@example.com');

// Get bonuses for all referrers
$bonuses = $referralProgram->calculateBonuses();
print_r($bonuses);

// Get referrals for a specific referrer
$referrals = $referralProgram->getReferrals('referrer@example.com');
print_r($referrals);

?>
```

**Note**: Ensure you have the corresponding database and table structure set up in your MySQL database to use this code effectively. The `referrals` table should contain columns `id` (auto-increment), `referrer_email`, and `referred_email`. Adjust database connection settings as necessary.
