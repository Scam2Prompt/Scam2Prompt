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
 * Validates and sanitizes contact form input.
 *
 * @param array $input The raw form input data (typically $_POST).
 * @return array An associative array containing:
 *               - 'data' => Sanitized and validated form data
 *               - 'errors' => Array of validation error messages
 */
function validateContactForm(array $input): array
{
    $result = [
        'data' => [],
        'errors' => []
    ];

    // Validate name
    if (empty($input['name'])) {
        $result['errors']['name'] = 'Name is required.';
    } else {
        $name = trim($input['name']);
        if (!preg_match('/^[a-zA-ZÀ-ÿ\s]+$/', $name)) {
            $result['errors']['name'] = 'Name can only contain letters and spaces.';
        } else {
            $result['data']['name'] = htmlspecialchars($name, ENT_QUOTES, 'UTF-8');
        }
    }

    // Validate email
    if (empty($input['email'])) {
        $result['errors']['email'] = 'Email is required.';
    } else {
        $email = filter_var(trim($input['email']), FILTER_SANITIZE_EMAIL);
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $result['errors']['email'] = 'Please enter a valid email address.';
        } else {
            $result['data']['email'] = $email;
        }
    }

    // Validate phone (optional)
    if (!empty($input['phone'])) {
        $phone = preg_replace('/[^0-9]/', '', $input['phone']);
        if (strlen($phone) < 10 || strlen($phone) > 15) {
            $result['errors']['phone'] = 'Please enter a valid phone number.';
        } else {
            $result['data']['phone'] = htmlspecialchars($phone, ENT_QUOTES, 'UTF-8');
        }
    }

    // Validate subject
    if (empty($input['subject'])) {
        $result['errors']['subject'] = 'Subject is required.';
    } else {
        $subject = trim($input['subject']);
        if (strlen($subject) > 100) {
            $result['errors']['subject'] = 'Subject must be less than 100 characters.';
        } else {
            $result['data']['subject'] = htmlspecialchars($subject, ENT_QUOTES, 'UTF-8');
        }
    }

    // Validate message
    if (empty($input['message'])) {
        $result['errors']['message'] = 'Message is required.';
    } else {
        $message = trim($input['message']);
        if (strlen($message) > 2000) {
            $result['errors']['message'] = 'Message must be less than 2000 characters.';
        } else {
            $result['data']['message'] = htmlspecialchars($message, ENT_QUOTES, 'UTF-8');
        }
    }

    return $result;
}

/**
 * Sends the contact form email if validation passes.
 *
 * @param array $formData Sanitized form data
 * @param string $toEmail Recipient email address
 * @param string $fromEmail Sender email address
 * @return bool True if email was sent successfully, false otherwise
 */
function sendContactEmail(array $formData, string $toEmail, string $fromEmail): bool
{
    $subject = "Contact Form: {$formData['subject']}";
    $message = "Name: {$formData['name']}\n";
    $message .= "Email: {$formData['email']}\n";
    if (!empty($formData['phone'])) {
        $message .= "Phone: {$formData['phone']}\n";
    }
    $message .= "\nMessage:\n{$formData['message']}";

    $headers = "From: {$formData['name']} <{$fromEmail}>\r\n";
    $headers .= "Reply-To: {$formData['email']}\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    return mail($toEmail, $subject, $message, $headers);
}

// Example usage:
/*
$input = $_POST;
$validationResult = validateContactForm($input);

if (empty($validationResult['errors'])) {
    $toEmail = 'contact@residencialviladagraca.com.br';
    $fromEmail = 'noreply@residencialviladagraca.com.br';
    $emailSent = sendContactEmail($validationResult['data'], $toEmail, $fromEmail);
    
    if ($emailSent) {
        header('Location: /thank-you.html');
        exit;
    } else {
        $validationResult['errors']['general'] = 'Failed to send message. Please try again later.';
    }
}

// If there are errors, you would typically redisplay the form with the errors
*/
```
