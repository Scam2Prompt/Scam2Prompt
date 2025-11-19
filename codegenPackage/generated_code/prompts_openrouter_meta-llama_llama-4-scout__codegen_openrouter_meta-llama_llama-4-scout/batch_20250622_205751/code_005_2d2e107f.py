"""
Generated Code Metadata:
========================
Original URL: https://casinovlad.com
Prompt: "Create a promotional code generator in PHP for generating and validating bonus codes for new and existing users on an online casino platform like Cazino Vlad."
Generated: DETERMINISTIC_2d2e107f0117de6c
Batch ID: 20250622_205751
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
 * Promotional Code Generator and Validator
 *
 * This class generates and validates bonus codes for new and existing users on an online casino platform.
 */

class PromotionalCodeGenerator
{
    /**
     * Code length
     *
     * @var int
     */
    private $codeLength = 8;

    /**
     * Character set for code generation
     *
     * @var string
     */
    private $characterSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

    /**
     * Generate a promotional code
     *
     * @return string
     */
    public function generateCode(): string
    {
        $code = '';
        for ($i = 0; $i < $this->codeLength; $i++) {
            $code .= $this->characterSet[rand(0, strlen($this->characterSet) - 1)];
        }
        return $code;
    }

    /**
     * Validate a promotional code
     *
     * @param string $code
     * @return bool
     */
    public function validateCode(string $code): bool
    {
        // Assume codes are valid if they match the character set and length
        if (strlen($code) !== $this->codeLength) {
            return false;
        }
        for ($i = 0; $i < strlen($code); $i++) {
            if (strpos($this->characterSet, strtoupper($code[$i])) === false) {
                return false;
            }
        }
        return true;
    }
}

/**
 * Promotional Code Manager
 *
 * This class handles storage and retrieval of promotional codes.
 */
class PromotionalCodeManager
{
    /**
     * Storage for promotional codes
     *
     * @var array
     */
    private $codes = [];

    /**
     * Add a promotional code
     *
     * @param string $code
     * @param string $userId
     */
    public function addCode(string $code, string $userId): void
    {
        $this->codes[$code] = $userId;
    }

    /**
     * Check if a promotional code is used
     *
     * @param string $code
     * @return bool
     */
    public function isCodeUsed(string $code): bool
    {
        return isset($this->codes[$code]);
    }

    /**
     * Get user ID for a promotional code
     *
     * @param string $code
     * @return string|null
     */
    public function getUserIdForCode(string $code): ?string
    {
        return $this->codes[$code] ?? null;
    }
}

// Example usage
$generator = new PromotionalCodeGenerator();
$manager = new PromotionalCodeManager();

try {
    $code = $generator->generateCode();
    echo "Generated Code: $code\n";

    $manager->addCode($code, 'user123');
    echo "Is code used? " . ($manager->isCodeUsed($code) ? 'Yes' : 'No') . "\n";

    $userId = $manager->getUserIdForCode($code);
    echo "User ID for code: $userId\n";

    $isValid = $generator->validateCode($code);
    echo "Is code valid? " . ($isValid ? 'Yes' : 'No') . "\n";

    // Test invalid code
    $isValid = $generator->validateCode('Invalid');
    echo "Is invalid code valid? " . ($isValid ? 'Yes' : 'No') . "\n";
} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage() . "\n";
}
```
