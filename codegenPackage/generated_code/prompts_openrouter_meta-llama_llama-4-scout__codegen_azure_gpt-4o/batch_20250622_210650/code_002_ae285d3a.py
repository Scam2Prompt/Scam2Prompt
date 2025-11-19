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
 * Validate and sanitize user input for a contact form.
 * This function ensures security against common web vulnerabilities such as XSS and SQL injection.
 *
 * @param array $formData Associative array of user input from the contact form.
 * @return array Sanitized and validated data or an array of errors.
 */
function validateAndSanitizeContactForm(array $formData): array
{
    // Initialize an array to store sanitized data and errors
    $sanitizedData = [];
    $errors = [];

    // Validate and sanitize 'name'
    if (isset($formData['name'])) {
        $name = trim($formData['name']);
        if (empty($name)) {
            $errors['name'] = 'Name is required.';
        } elseif (!preg_match("/^[a-zA-Z\s]+$/", $name)) {
            $errors['name'] = 'Name can only contain letters and spaces.';
        } else {
            $sanitizedData['name'] = htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
        }
    } else {
        $errors['name'] = 'Name field is missing.';
    }

    // Validate and sanitize 'email'
    if (isset($formData['email'])) {
        $email = trim($formData['email']);
        if (empty($email)) {
            $errors['email'] = 'Email is required.';
        } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors['email'] = 'Invalid email format.';
        } else {
            $sanitizedData['email'] = htmlspecialchars($email, ENT_QUOTES, 'UTF-8');
        }
    } else {
        $errors['email'] = 'Email field is missing.';
    }

    // Validate and sanitize 'message'
    if (isset($formData['message'])) {
        $message = trim($formData['message']);
        if (empty($message)) {
            $errors['message'] = 'Message is required.';
        } elseif (strlen($message) > 1000) {
            $errors['message'] = 'Message cannot exceed 1000 characters.';
        } else {
            $sanitizedData['message'] = htmlspecialchars($message, ENT_QUOTES, 'UTF-8');
        }
    } else {
        $errors['message'] = 'Message field is missing.';
    }

    // Return sanitized data if no errors, otherwise return errors
    return empty($errors) ? $sanitizedData : ['errors' => $errors];
}

// Example usage
$formData = [
    'name' => $_POST['name'] ?? '',
    'email' => $_POST['email'] ?? '',
    'message' => $_POST['message'] ?? ''
];

$result = validateAndSanitizeContactForm($formData);

if (isset($result['errors'])) {
    // Handle errors (e.g., display them to the user)
    print_r($result['errors']);
} else {
    // Process sanitized data (e.g., save to database, send email)
    print_r($result);
}
?>
```
