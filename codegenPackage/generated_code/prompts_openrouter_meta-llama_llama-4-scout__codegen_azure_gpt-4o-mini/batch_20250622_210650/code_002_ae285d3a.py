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
<?php

/**
 * Validates and sanitizes user input for a contact form.
 *
 * @param array $data The user input data from the contact form.
 * @return array An associative array containing the sanitized data and any errors.
 */
function validateAndSanitizeContactForm(array $data): array {
    // Initialize an array to hold sanitized data and errors
    $sanitizedData = [];
    $errors = [];

    // Define expected fields
    $expectedFields = ['name', 'email', 'message'];

    // Loop through each expected field
    foreach ($expectedFields as $field) {
        // Check if the field is present in the input data
        if (!isset($data[$field])) {
            $errors[$field] = "The $field field is required.";
            continue;
        }

        // Trim whitespace and sanitize the input
        $input = trim($data[$field]);

        // Validate and sanitize based on field type
        switch ($field) {
            case 'name':
                // Check if name is valid (only letters and whitespace)
                if (empty($input) || !preg_match("/^[a-zA-Z\s]+$/", $input)) {
                    $errors[$field] = "The name field must contain only letters and spaces.";
                } else {
                    $sanitizedData[$field] = htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
                }
                break;

            case 'email':
                // Validate email format
                if (empty($input) || !filter_var($input, FILTER_VALIDATE_EMAIL)) {
                    $errors[$field] = "The email field must contain a valid email address.";
                } else {
                    $sanitizedData[$field] = htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
                }
                break;

            case 'message':
                // Check if message is valid (not empty)
                if (empty($input)) {
                    $errors[$field] = "The message field cannot be empty.";
                } else {
                    $sanitizedData[$field] = htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
                }
                break;
        }
    }

    // Return sanitized data and errors
    return [
        'sanitizedData' => $sanitizedData,
        'errors' => $errors,
    ];
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $result = validateAndSanitizeContactForm($_POST);

    if (empty($result['errors'])) {
        // Process the sanitized data (e.g., send an email)
        // mail($to, $subject, $result['sanitizedData']['message'], $headers);
        echo "Form submitted successfully!";
    } else {
        // Handle errors (e.g., display them to the user)
        foreach ($result['errors'] as $error) {
            echo "<p>Error: $error</p>";
        }
    }
}
?>
```
