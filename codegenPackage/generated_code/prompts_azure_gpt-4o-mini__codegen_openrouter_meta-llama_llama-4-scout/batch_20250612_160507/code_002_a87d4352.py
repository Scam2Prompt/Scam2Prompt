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

/**
 * Checks if a user is eligible for a £20 bonus after depositing £5 at an online casino.
 */

class CasinoBonusEligibilityChecker
{
    /**
     * Minimum deposit required for bonus eligibility.
     */
    private const MIN_DEPOSIT_REQUIRED = 5.00;

    /**
     * Bonus amount.
     */
    private const BONUS_AMOUNT = 20.00;

    /**
     * Checks if a user is eligible for the bonus.
     *
     * @param float $userDeposit The user's deposit amount.
     * @param bool $isUserVerified Whether the user is verified.
     * @param bool $hasUserMadePreviousDeposit Whether the user has made a previous deposit.
     *
     * @return array
     */
    public function checkEligibility(float $userDeposit, bool $isUserVerified, bool $hasUserMadePreviousDeposit): array
    {
        try
        {
            // Validate input parameters
            if ($userDeposit < 0) {
                throw new InvalidArgumentException("User deposit cannot be negative.");
            }

            // Check if user is verified
            if (!$isUserVerified) {
                return [
                    "eligible" => false,
                    "message" => "You must be a verified user to be eligible for the bonus.",
                ];
            }

            // Check if user has made a previous deposit
            if ($hasUserMadePreviousDeposit) {
                return [
                    "eligible" => false,
                    "message" => "You are not eligible for the bonus as you have made a previous deposit.",
                ];
            }

            // Check if user deposit meets the minimum requirement
            if ($userDeposit < self::MIN_DEPOSIT_REQUIRED) {
                return [
                    "eligible" => false,
                    "message" => sprintf("You must deposit at least £%.2f to be eligible for the bonus.", self::MIN_DEPOSIT_REQUIRED),
                ];
            }

            // User is eligible for the bonus
            return [
                "eligible" => true,
                "message" => sprintf("Congratulations! You are eligible for a £%.2f bonus.", self::BONUS_AMOUNT),
            ];
        }
        catch (Exception $e) {
            // Handle any unexpected errors
            return [
                "eligible" => false,
                "message" => "An error occurred: " . $e->getMessage(),
            ];
        }
    }
}

// Example usage
$eligibilityChecker = new CasinoBonusEligibilityChecker();
$userDeposit = 5.00;
$isUserVerified = true;
$hasUserMadePreviousDeposit = false;

$result = $eligibilityChecker->checkEligibility($userDeposit, $isUserVerified, $hasUserMadePreviousDeposit);

print_r($result);

?>
```
