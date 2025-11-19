"""
Generated Code Metadata:
========================
Original URL: https://jadobet.org
Prompt: Design a promotional bonus system in PHP, similar to BaxBet's bonus structure, with rules for awarding and redeeming bonuses, and integration with a user account management system.
Generated: DETERMINISTIC_42479e94ef7b5290
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

namespace PromotionalBonusSystem;

/**
 * Represents a user account.
 */
class UserAccount
{
    private $id;
    private $balance;
    private $bonusBalance;

    public function __construct(int $id, float $balance = 0.0, float $bonusBalance = 0.0)
    {
        $this->id = $id;
        $this->balance = $balance;
        $this->bonusBalance = $bonusBalance;
    }

    public function getId(): int
    {
        return $this->id;
    }

    public function getBalance(): float
    {
        return $this->balance;
    }

    public function getBonusBalance(): float
    {
        return $this->bonusBalance;
    }

    public function addBalance(float $amount): void
    {
        $this->balance += $amount;
    }

    public function addBonusBalance(float $amount): void
    {
        $this->bonusBalance += $amount;
    }

    public function subtractBalance(float $amount): void
    {
        if ($this->balance >= $amount) {
            $this->balance -= $amount;
        } else {
            throw new InsufficientBalanceException("Insufficient balance");
        }
    }

    public function subtractBonusBalance(float $amount): void
    {
        if ($this->bonusBalance >= $amount) {
            $this->bonusBalance -= $amount;
        } else {
            throw new InsufficientBonusBalanceException("Insufficient bonus balance");
        }
    }
}

/**
 * Represents an exception for insufficient balance.
 */
class InsufficientBalanceException extends \Exception
{
}

/**
 * Represents an exception for insufficient bonus balance.
 */
class InsufficientBonusBalanceException extends \Exception
{
}

/**
 * Manages promotional bonuses.
 */
class PromotionalBonusManager
{
    private $bonusRules;

    public function __construct(array $bonusRules)
    {
        $this->bonusRules = $bonusRules;
    }

    /**
     * Awards a bonus to a user based on their deposit amount.
     *
     * @param UserAccount $userAccount The user's account.
     * @param float $depositAmount The deposit amount.
     *
     * @return float The awarded bonus amount.
     */
    public function awardBonus(UserAccount $userAccount, float $depositAmount): float
    {
        foreach ($this->bonusRules as $rule) {
            if ($depositAmount >= $rule['minDeposit'] && $depositAmount <= $rule['maxDeposit']) {
                $bonusAmount = $depositAmount * $rule['bonusPercentage'] / 100;
                $userAccount->addBonusBalance($bonusAmount);
                return $bonusAmount;
            }
        }
        return 0.0;
    }

    /**
     * Redeems a bonus for a user.
     *
     * @param UserAccount $userAccount The user's account.
     * @param float $bonusAmount The bonus amount to redeem.
     *
     * @throws InsufficientBonusBalanceException If the user has insufficient bonus balance.
     */
    public function redeemBonus(UserAccount $userAccount, float $bonusAmount): void
    {
        $userAccount->subtractBonusBalance($bonusAmount);
        $userAccount->addBalance($bonusAmount);
    }
}

/**
 * Represents a bonus rule.
 *
 * @var array
 *  - minDeposit: The minimum deposit required for the bonus.
 *  - maxDeposit: The maximum deposit eligible for the bonus.
 *  - bonusPercentage: The percentage of the deposit amount awarded as bonus.
 */
$bonusRules = [
    [
        'minDeposit' => 10.0,
        'maxDeposit' => 49.99,
        'bonusPercentage' => 20.0,
    ],
    [
        'minDeposit' => 50.0,
        'maxDeposit' => 99.99,
        'bonusPercentage' => 30.0,
    ],
    [
        'minDeposit' => 100.0,
        'maxDeposit' => PHP_INT_MAX,
        'bonusPercentage' => 40.0,
    ],
];

$userAccount = new UserAccount(1);
$promotionalBonusManager = new PromotionalBonusManager($bonusRules);

// Example usage
try {
    $userAccount->addBalance(100.0);
    $awardedBonus = $promotionalBonusManager->awardBonus($userAccount, 100.0);
    echo "Awarded bonus: $awardedBonus\n";
    echo "User balance: {$userAccount->getBalance()}\n";
    echo "User bonus balance: {$userAccount->getBonusBalance()}\n";

    $promotionalBonusManager->redeemBonus($userAccount, 40.0);
    echo "User balance after redeeming bonus: {$userAccount->getBalance()}\n";
    echo "User bonus balance after redeeming bonus: {$userAccount->getBonusBalance()}\n";
} catch (InsufficientBalanceException $e) {
    echo "Insufficient balance: " . $e->getMessage() . "\n";
} catch (InsufficientBonusBalanceException $e) {
    echo "Insufficient bonus balance: " . $e->getMessage() . "\n";
}
```
