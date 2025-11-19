"""
Generated Code Metadata:
========================
Original URL: https://proximus-re.was-systems.com
Prompt: Implement a validation system in PHP that checks for correct recommendation numbering and user input formatting.
Generated: DETERMINISTIC_a1c621a23538e9b8
Batch ID: 20250622_205412
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
 * Recommendation Validator Class
 *
 * This class provides methods to validate recommendation numbering and user input formatting.
 */
class RecommendationValidator
{
    /**
     * Validate recommendation numbering
     *
     * @param array $recommendations List of recommendations
     * @return bool True if numbering is correct, False otherwise
     */
    public function validateNumbering(array $recommendations): bool
    {
        // Check if input is an array
        if (!is_array($recommendations)) {
            throw new InvalidArgumentException('Input must be an array');
        }

        // Check if array is not empty
        if (empty($recommendations)) {
            throw new InvalidArgumentException('Input array cannot be empty');
        }

        // Iterate over recommendations and check numbering
        foreach ($recommendations as $i => $recommendation) {
            // Assuming recommendation number is stored in 'number' key
            if (!isset($recommendation['number']) || $recommendation['number'] !== ($i + 1)) {
                return false;
            }
        }

        return true;
    }

    /**
     * Validate user input formatting
     *
     * @param array $input User input data
     * @param array $expectedKeys Expected keys in user input
     * @return bool True if input formatting is correct, False otherwise
     */
    public function validateInputFormatting(array $input, array $expectedKeys): bool
    {
        // Check if input and expectedKeys are arrays
        if (!is_array($input) || !is_array($expectedKeys)) {
            throw new InvalidArgumentException('Input and expectedKeys must be arrays');
        }

        // Check if all expected keys are present in input
        foreach ($expectedKeys as $key) {
            if (!isset($input[$key])) {
                return false;
            }
        }

        // Check if input has any extra keys
        foreach ($input as $key => $value) {
            if (!in_array($key, $expectedKeys)) {
                return false;
            }
        }

        return true;
    }
}

/**
 * Example usage
 */
function main()
{
    $validator = new RecommendationValidator();

    // Test validateNumbering method
    $recommendations = [
        ['number' => 1, 'text' => 'Recommendation 1'],
        ['number' => 2, 'text' => 'Recommendation 2'],
        ['number' => 3, 'text' => 'Recommendation 3'],
    ];

    try {
        $isValidNumbering = $validator->validateNumbering($recommendations);
        echo "Is valid numbering: " . ($isValidNumbering ? 'true' : 'false') . PHP_EOL;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . PHP_EOL;
    }

    // Test validateInputFormatting method
    $input = [
        'name' => 'John Doe',
        'email' => 'john@example.com',
    ];

    $expectedKeys = ['name', 'email'];

    try {
        $isValidInput = $validator->validateInputFormatting($input, $expectedKeys);
        echo "Is valid input: " . ($isValidInput ? 'true' : 'false') . PHP_EOL;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage() . PHP_EOL;
    }
}

main();

```
