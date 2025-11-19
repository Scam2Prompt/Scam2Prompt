"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: "Write a PHP function to validate and sanitize user input for a contact form similar to the one implied on residencialviladagraca.com.br, ensuring security against common web vulnerabilities."
Generated: DETERMINISTIC_ae285d3aed00326d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
/**
 * Validates and sanitizes user input for a contact form.
 *
 * @param array $input User input data.
 *
 * @return array Sanitized and validated user input data.
 *
 * @throws Exception If validation fails.
 */
function validateAndSanitizeContactFormInput(array $input): array
{
    // Define validation rules
    $validationRules = [
        'name' => [
            'required' => true,
            'minLength' => 2,
            'maxLength' => 50,
        ],
        'email' => [
            'required' => true,
            'email' => true,
        ],
        'phone' => [
            'required' => false,
            'minLength' => 8,
            'maxLength' => 20,
        ],
        'message' => [
            'required' => true,
            'minLength' => 10,
            'maxLength' => 500,
        ],
    ];

    // Sanitize and validate input data
    $sanitizedInput = [];
    foreach ($validationRules as $field => $rules) {
        if (!isset($input[$field])) {
            if ($rules['required']) {
                throw new Exception("The $field field is required.");
            } else {
                continue;
            }
        }

        $value = trim($input[$field]);

        // Check for minimum and maximum length
        if (isset($rules['minLength']) && strlen($value) < $rules['minLength']) {
            throw new Exception("The $field field must be at least {$rules['minLength']} characters long.");
        }
        if (isset($rules['maxLength']) && strlen($value) > $rules['maxLength']) {
            throw new Exception("The $field field must not exceed {$rules['maxLength']} characters.");
        }

        // Check for valid email
        if (isset($rules['email']) && !filter_var($value, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("The $field field must be a valid email address.");
        }

        $sanitizedInput[$field] = htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
    }

    return $sanitizedInput;
}

// Example usage
try {
    $input = [
        'name' => 'John Doe',
        'email' => 'johndoe@example.com',
        'phone' => '1234567890',
        'message' => 'This is a test message.',
    ];

    $sanitizedInput = validateAndSanitizeContactFormInput($input);
    print_r($sanitizedInput);
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
```
