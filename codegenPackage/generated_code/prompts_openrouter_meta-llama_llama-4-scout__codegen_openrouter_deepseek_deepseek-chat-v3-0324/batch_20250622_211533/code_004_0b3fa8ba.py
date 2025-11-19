"""
Generated Code Metadata:
========================
Original URL: https://cashb90.net
Prompt: Implement a cashback system in PHP that rewards users with a percentage of their losses on a betting platform, similar to BaxBet's cashback feature.
Generated: DETERMINISTIC_0b3fa8ba538eb44f
Batch ID: 20250622_211533
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
 * Cashback System for Betting Platform
 * 
 * This script implements a cashback feature that rewards users with a percentage
 * of their losses over a specified period.
 */

class CashbackSystem {
    private $db;
    private $cashbackPercentage;
    private $minLossForCashback;

    /**
     * Constructor
     * 
     * @param PDO $db Database connection
     * @param float $cashbackPercentage Percentage of losses to give as cashback (e.g., 0.1 for 10%)
     * @param float $minLossForCashback Minimum loss amount required to qualify for cashback
     */
    public function __construct(PDO $db, float $cashbackPercentage, float $minLossForCashback) {
        $this->db = $db;
        $this->cashbackPercentage = $cashbackPercentage;
        $this->minLossForCashback = $minLossForCashback;
    }

    /**
     * Calculate cashback for a user based on their losses
     * 
     * @param int $userId User ID to calculate cashback for
     * @param string $startDate Start date for calculation period (YYYY-MM-DD)
     * @param string $endDate End date for calculation period (YYYY-MM-DD)
     * @return array Result containing cashback amount and status
     */
    public function calculateCashback(int $userId, string $startDate, string $endDate): array {
        try {
            // Validate input dates
            if (!$this->validateDate($startDate) || !$this->validateDate($endDate)) {
                throw new InvalidArgumentException("Invalid date format. Use YYYY-MM-DD.");
            }

            // Calculate net loss for the period
            $netLoss = $this->calculateNetLoss($userId, $startDate, $endDate);

            // Check if user qualifies for cashback
            if ($netLoss >= $this->minLossForCashback) {
                $cashbackAmount = $netLoss * $this->cashbackPercentage;
                return [
                    'success' => true,
                    'cashback_amount' => round($cashbackAmount, 2),
                    'net_loss' => round($netLoss, 2),
                    'message' => 'Cashback calculated successfully'
                ];
            } else {
                return [
                    'success' => true,
                    'cashback_amount' => 0,
                    'net_loss' => round($netLoss, 2),
                    'message' => 'User does not qualify for cashback'
                ];
            }
        } catch (Exception $e) {
            return [
                'success' => false,
                'message' => 'Error calculating cashback: ' . $e->getMessage()
            ];
        }
    }

    /**
     * Apply cashback to user's account
     * 
     * @param int $userId User ID to apply cashback to
     * @param float $amount Cashback amount to apply
     * @return array Result of the operation
     */
    public function applyCashback(int $userId, float $amount): array {
        try {
            if ($amount <= 0) {
                throw new InvalidArgumentException("Cashback amount must be positive");
            }

            $this->db->beginTransaction();

            // Update user balance
            $stmt = $this->db->prepare("UPDATE users SET balance = balance + ? WHERE id = ?");
            $stmt->execute([$amount, $userId]);

            if ($stmt->rowCount() === 0) {
                throw new RuntimeException("User not found");
            }

            // Record transaction
            $stmt = $this->db->prepare("
                INSERT INTO cashback_transactions 
                (user_id, amount, transaction_date) 
                VALUES (?, ?, NOW())
            ");
            $stmt->execute([$userId, $amount]);

            $this->db->commit();

            return [
                'success' => true,
                'message' => 'Cashback applied successfully',
                'amount' => $amount
            ];
        } catch (Exception $e) {
            $this->db->rollBack();
            return [
                'success' => false,
                'message' => 'Error applying cashback: ' . $e->getMessage()
            ];
        }
    }

    /**
     * Calculate net loss for a user in the given period
     * 
     * @param int $userId User ID
     * @param string $startDate Start date (YYYY-MM-DD)
     * @param string $endDate End date (YYYY-MM-DD)
     * @return float Net loss amount
     */
    private function calculateNetLoss(int $userId, string $startDate, string $endDate): float {
        $stmt = $this->db->prepare("
            SELECT 
                COALESCE(SUM(CASE WHEN bet_type = 'win' THEN amount ELSE 0 END), 0) AS total_wins,
                COALESCE(SUM(CASE WHEN bet_type = 'loss' THEN amount ELSE 0 END), 0) AS total_losses
            FROM bets
            WHERE user_id = ? 
            AND bet_date BETWEEN ? AND ?
        ");
        $stmt->execute([$userId, $startDate, $endDate]);
        $result = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$result) {
            return 0;
        }

        return max(0, $result['total_losses'] - $result['total_wins']);
    }

    /**
     * Validate date format
     * 
     * @param string $date Date string to validate
     * @param string $format Expected date format
     * @return bool True if valid, false otherwise
     */
    private function validateDate(string $date, string $format = 'Y-m-d'): bool {
        $d = DateTime::createFromFormat($format, $date);
        return $d && $d->format($format) === $date;
    }
}

// Example usage:
/*
$db = new PDO('mysql:host=localhost;dbname=betting_platform', 'username', 'password');
$cashbackSystem = new CashbackSystem($db, 0.1, 50); // 10% cashback, min €50 loss

// Calculate cashback for user 123 from Jan 1 to Jan 31
$result = $cashbackSystem->calculateCashback(123, '2023-01-01', '2023-01-31');
if ($result['success'] && $result['cashback_amount'] > 0) {
    $applyResult = $cashbackSystem->applyCashback(123, $result['cashback_amount']);
    if (!$applyResult['success']) {
        // Handle error
    }
}
*/
?>
```
