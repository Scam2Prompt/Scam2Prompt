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
 * Check if a user is eligible for a £20 bonus after depositing £5 at an online casino.
 * Assumptions:
 * - The user must have deposited exactly £5.
 * - The user must not have claimed the bonus previously.
 */

// Function to check user eligibility for the bonus
function isEligibleForBonus($userId, $depositAmount, $userBonusClaimed) {
    // Validate input parameters
    if (!is_numeric($depositAmount) || $depositAmount <= 0) {
        throw new InvalidArgumentException("Invalid deposit amount.");
    }
    if (!is_bool($userBonusClaimed)) {
        throw new InvalidArgumentException("Invalid bonus claimed flag.");
    }

    // Check if the deposit amount is exactly £5
    if ($depositAmount === 5.00) {
        // Check if the user has already claimed the bonus
        if (!$userBonusClaimed) {
            return true; // User is eligible for the £20 bonus
        }
    }
    return false; // User is not eligible
}

// Example usage (Replace with actual data in production)
try {
    // Sample user data
    $userId = 101;                  // User's unique identifier
    $depositAmount = 5.00;          // Amount deposited by the user
    $userBonusClaimed = false;      // Whether the user has already claimed the bonus

    // Check eligibility
    $isEligible = isEligibleForBonus($userId, $depositAmount, $userBonusClaimed);

    // Output result
    if ($isEligible) {
        echo "User is eligible for the £20 bonus.";
    } else {
        echo "User is not eligible for the £20 bonus.";
    }
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage();
}
?>
```
