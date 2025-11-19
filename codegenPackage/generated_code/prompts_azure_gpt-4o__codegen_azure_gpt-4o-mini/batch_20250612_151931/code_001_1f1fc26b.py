"""
Generated Code Metadata:
========================
Original URL: https://asasdasd.pages.dev
Prompt: Generate PHP code to implement a pre-check validation for API parameters like `key`, `strictness`, and `user_agent` using the methods outlined in the provided documentation.
Generated: DETERMINISTIC_1f1fc26b03526e99
Batch ID: 20250612_151931
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
 * Class ApiValidator
 * This class handles the validation of API parameters.
 */
class ApiValidator
{
    private $requiredParams = ['key', 'strictness', 'user_agent'];

    /**
     * Validates the API parameters.
     *
     * @param array $params The parameters to validate.
     * @return array An array containing validation results.
     * @throws InvalidArgumentException If required parameters are missing.
     */
    public function validate(array $params)
    {
        // Check for missing required parameters
        foreach ($this->requiredParams as $param) {
            if (!array_key_exists($param, $params)) {
                throw new InvalidArgumentException("Missing required parameter: $param");
            }
        }

        // Validate 'key' format
        if (!$this->isValidKey($params['key'])) {
            throw new InvalidArgumentException("Invalid format for parameter: key");
        }

        // Validate 'strictness' value
        if (!$this->isValidStrictness($params['strictness'])) {
            throw new InvalidArgumentException("Invalid value for parameter: strictness");
        }

        // Validate 'user_agent' format
        if (!$this->isValidUserAgent($params['user_agent'])) {
            throw new InvalidArgumentException("Invalid format for parameter: user_agent");
        }

        return ['status' => 'success', 'message' => 'All parameters are valid.'];
    }

    /**
     * Checks if the API key is valid.
     *
     * @param string $key The API key to validate.
     * @return bool True if valid, false otherwise.
     */
    private function isValidKey($key)
    {
        // Example validation: check if the key is a non-empty string
        return is_string($key) && !empty($key);
    }

    /**
     * Checks if the strictness value is valid.
     *
     * @param mixed $strictness The strictness value to validate.
     * @return bool True if valid, false otherwise.
     */
    private function isValidStrictness($strictness)
    {
        // Example validation: check if strictness is an integer between 0 and 10
        return is_int($strictness) && $strictness >= 0 && $strictness <= 10;
    }

    /**
     * Checks if the user agent format is valid.
     *
     * @param string $userAgent The user agent string to validate.
     * @return bool True if valid, false otherwise.
     */
    private function isValidUserAgent($userAgent)
    {
        // Example validation: check if user agent is a non-empty string
        return is_string($userAgent) && !empty($userAgent);
    }
}

// Example usage
try {
    $validator = new ApiValidator();
    $params = [
        'key' => 'your_api_key',
        'strictness' => 5,
        'user_agent' => 'Mozilla/5.0'
    ];
    $result = $validator->validate($params);
    echo json_encode($result);
} catch (InvalidArgumentException $e) {
    // Handle validation errors
    echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
}
?>
```
