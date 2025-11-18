"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asasdasd.pages.dev
Prompt: Generate PHP code to implement a pre-check validation for API parameters like `key`, `strictness`, and `user_agent` using the methods outlined in the provided documentation.
Generated: DETERMINISTIC_1f1fc26b03526e99
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

class ApiValidator
{
    private const VALID_KEYS = ['key1', 'key2', 'key3']; // Example of valid API keys
    private const VALID_STRICTNESS_LEVELS = ['low', 'medium', 'high']; // Example strictness levels

    /**
     * Validates API parameters.
     *
     * @param array $params Array of API parameters.
     * @return array Array containing validation results.
     * @throws InvalidArgumentException When parameters are invalid.
     */
    public function validate(array $params): array
    {
        $this->validateKey($params['key'] ?? null);
        $this->validateStrictness($params['strictness'] ?? null);
        $this->validateUserAgent($params['user_agent'] ?? null);

        return ['status' => 'success', 'message' => 'All parameters are valid.'];
    }

    /**
     * Validates the API key.
     *
     * @param string|null $key The API key to validate.
     * @throws InvalidArgumentException When the API key is invalid.
     */
    private function validateKey(?string $key): void
    {
        if (is_null($key) || !in_array($key, self::VALID_KEYS)) {
            throw new InvalidArgumentException('Invalid API key provided.');
        }
    }

    /**
     * Validates the strictness level.
     *
     * @param string|null $strictness The strictness level to validate.
     * @throws InvalidArgumentException When the strictness level is invalid.
     */
    private function validateStrictness(?string $strictness): void
    {
        if (is_null($strictness) || !in_array($strictness, self::VALID_STRICTNESS_LEVELS)) {
            throw new InvalidArgumentException('Invalid strictness level provided.');
        }
    }

    /**
     * Validates the user agent.
     *
     * @param string|null $userAgent The user agent to validate.
     * @throws InvalidArgumentException When the user agent is invalid.
     */
    private function validateUserAgent(?string $userAgent): void
    {
        if (is_null($userAgent) || empty(trim($userAgent))) {
            throw new InvalidArgumentException('Invalid user agent provided.');
        }
    }
}

// Example usage
try {
    $apiValidator = new ApiValidator();
    $params = [
        'key' => 'key1',
        'strictness' => 'medium',
        'user_agent' => 'Mozilla/5.0'
    ];
    $result = $apiValidator->validate($params);
    echo json_encode($result);
} catch (InvalidArgumentException $e) {
    http_response_code(400); // Bad Request
    echo json_encode(['status' => 'error', 'message' => $e->getMessage()]);
}
?>
```
