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
 * Class CashbackSystem
 * This class handles the cashback calculation for users based on their betting losses.
 */
class CashbackSystem
{
    private $cashbackPercentage; // Percentage of cashback to be awarded
    private $userBets; // Array to store user bets and their outcomes

    /**
     * CashbackSystem constructor.
     * 
     * @param float $cashbackPercentage Percentage of cashback to be awarded (0-100)
     */
    public function __construct(float $cashbackPercentage)
    {
        if ($cashbackPercentage < 0 || $cashbackPercentage > 100) {
            throw new InvalidArgumentException('Cashback percentage must be between 0 and 100.');
        }
        $this->cashbackPercentage = $cashbackPercentage / 100; // Convert to decimal
        $this->userBets = [];
    }

    /**
     * Record a user's bet.
     * 
     * @param string $userId The ID of the user placing the bet
     * @param float $betAmount The amount of the bet
     * @param bool $won Indicates if the user won the bet
     */
    public function recordBet(string $userId, float $betAmount, bool $won): void
    {
        if ($betAmount <= 0) {
            throw new InvalidArgumentException('Bet amount must be greater than zero.');
        }

        $this->userBets[] = [
            'userId' => $userId,
            'betAmount' => $betAmount,
            'won' => $won
        ];
    }

    /**
     * Calculate cashback for all users based on their losses.
     * 
     * @return array An associative array of user IDs and their respective cashback amounts
     */
    public function calculateCashback(): array
    {
        $cashbackResults = [];

        foreach ($this->userBets as $bet) {
            $userId = $bet['userId'];
            $betAmount = $bet['betAmount'];
            $won = $bet['won'];

            // Only calculate cashback for losses
            if (!$won) {
                if (!isset($cashbackResults[$userId])) {
                    $cashbackResults[$userId] = 0; // Initialize cashback for user
                }
                // Calculate cashback based on the loss
                $cashbackResults[$userId] += $betAmount * $this->cashbackPercentage;
            }
        }

        return $cashbackResults;
    }
}

// Example usage
try {
    // Create a cashback system with a 10% cashback rate
    $cashbackSystem = new CashbackSystem(10.0);

    // Record some bets
    $cashbackSystem->recordBet('user1', 100, false); // User 1 lost $100
    $cashbackSystem->recordBet('user1', 50, true);  // User 1 won $50
    $cashbackSystem->recordBet('user2', 200, false); // User 2 lost $200
    $cashbackSystem->recordBet('user2', 150, false); // User 2 lost $150

    // Calculate cashback
    $cashback = $cashbackSystem->calculateCashback();

    // Output the cashback results
    foreach ($cashback as $userId => $amount) {
        echo "User ID: $userId, Cashback Amount: $" . number_format($amount, 2) . PHP_EOL;
    }
} catch (Exception $e) {
    // Handle any exceptions that occur
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
?>
```
