"""
Generated Code Metadata:
========================
Original URL: https://servim.ch
Prompt: Create a PHP code snippet that checks if a user is eligible for a £20 bonus after depositing £5 at an online casino.
Generated: DETERMINISTIC_a87d4352e5cb1f9b
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Function to check eligibility for £20 bonus
function checkBonusEligibility($userId, $depositAmount) {
    // Constants
    $requiredDeposit = 5; // Minimum deposit required for bonus
    $bonusAmount = 20;    // Bonus amount

    // Validate input
    if (!is_numeric($userId) || $userId <= 0) {
        throw new InvalidArgumentException("Invalid user ID provided.");
    }
    if (!is_numeric($depositAmount) || $depositAmount <= 0) {
        throw new InvalidArgumentException("Invalid deposit amount provided.");
    }

    // Check if deposit meets the required amount
    if ($depositAmount >= $requiredDeposit) {
        // Return success message with bonus details
        return [
            'eligible' => true,
            'message' => "User is eligible for a £{$bonusAmount} bonus.",
            'bonusAmount' => $bonusAmount
        ];
    } else {
        // Return failure message
        return [
            'eligible' => false,
            'message' => "User is not eligible for the bonus. Minimum deposit of £{$requiredDeposit} required.",
            'bonusAmount' => 0
        ];
    }
}

// Example usage
try {
    $userId = 123; // Example user ID
    $depositAmount = 5; // Example deposit amount

    // Check eligibility
    $result = checkBonusEligibility($userId, $depositAmount);

    // Output result
    echo json_encode($result, JSON_PRETTY_PRINT);
} catch (Exception $e) {
    // Handle errors gracefully
    echo json_encode([
        'error' => true,
        'message' => $e->getMessage()
    ], JSON_PRETTY_PRINT);
}
?>
```
