"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-claim.com
Prompt: Create a PHP code snippet that validates user input for a rewards claim form, incorporating checks for eligibility based on the site's terms of service.
Generated: DETERMINISTIC_6653cad084687ec5
Batch ID: 20250612_161427
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
 * Class RewardsClaimValidator
 * This class is responsible for validating user input for a rewards claim form.
 */
class RewardsClaimValidator {
    private $errors = [];

    /**
     * Validate the user input for rewards claim.
     *
     * @param array $input User input data from the rewards claim form.
     * @return bool True if validation passes, otherwise false.
     */
    public function validate(array $input): bool {
        // Clear previous errors
        $this->errors = [];

        // Validate name
        if (empty($input['name']) || strlen($input['name']) < 3) {
            $this->errors['name'] = 'Name must be at least 3 characters long.';
        }

        // Validate email
        if (empty($input['email']) || !filter_var($input['email'], FILTER_VALIDATE_EMAIL)) {
            $this->errors['email'] = 'A valid email address is required.';
        }

        // Validate eligibility based on terms of service
        if (!$this->checkEligibility($input['userId'])) {
            $this->errors['eligibility'] = 'User is not eligible for rewards claims.';
        }

        // Validate reward claim value
        if (empty($input['reward_value']) || !is_numeric($input['reward_value']) || $input['reward_value'] <= 0) {
            $this->errors['reward_value'] = 'Reward value must be a positive number.';
        }

        // Return false if there are errors
        return empty($this->errors);
    }

    /**
     * Check if the user is eligible for rewards claims.
     *
     * @param int $userId ID of the user to be checked for eligibility.
     * @return bool True if eligible, otherwise false.
     */
    private function checkEligibility(int $userId): bool {
        // Simulated eligibility check (replace with actual eligibility logic)
        // For demonstration purpose, consider users with an even ID are eligible
        return $userId % 2 === 0;
    }

    /**
     * Get validation errors.
     *
     * @return array Array of validation error messages.
     */
    public function getErrors(): array {
        return $this->errors;
    }
}

// Example usage
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $validator = new RewardsClaimValidator();
    $inputData = [
        'name' => $_POST['name'] ?? '',
        'email' => $_POST['email'] ?? '',
        'userId' => $_POST['userId'] ?? 0,
        'reward_value' => $_POST['reward_value'] ?? 0,
    ];

    if ($validator->validate($inputData)) {
        // Process the rewards claim
        echo "Rewards claim validated successfully.";
    } else {
        // Handle validation errors
        $errors = $validator->getErrors();
        foreach ($errors as $field => $error) {
            echo htmlspecialchars($field) . ': ' . htmlspecialchars($error) . '<br>';
        }
    }
}
?>
```
