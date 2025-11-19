"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://servim.ch
Prompt: Create a PHP code snippet that checks if a user is eligible for a £20 bonus after depositing £5 at an online casino.
Generated: DETERMINISTIC_a87d4352e5cb1f9b
Batch ID: 20250612_160507
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
 * Check if a user is eligible for a £20 bonus after depositing £5.
 *
 * @param float $depositAmount The amount deposited by the user.
 * @return array An associative array containing the eligibility status and bonus amount.
 */
function checkBonusEligibility(float $depositAmount): array {
    // Define the required deposit amount and bonus amount
    $requiredDeposit = 5.00;
    $bonusAmount = 20.00;

    // Initialize the response array
    $response = [
        'eligible' => false,
        'bonus' => 0.00
    ];

    // Check for valid deposit amount
    if ($depositAmount < 0) {
        throw new InvalidArgumentException('Deposit amount cannot be negative.');
    }

    // Check if the user is eligible for the bonus
    if ($depositAmount >= $requiredDeposit) {
        $response['eligible'] = true;
        $response['bonus'] = $bonusAmount;
    }

    return $response;
}

// Example usage
try {
    $userDeposit = 5.00; // User's deposit amount
    $bonusEligibility = checkBonusEligibility($userDeposit);

    if ($bonusEligibility['eligible']) {
        echo "Congratulations! You are eligible for a £" . $bonusEligibility['bonus'] . " bonus.";
    } else {
        echo "Unfortunately, you are not eligible for a bonus.";
    }
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
