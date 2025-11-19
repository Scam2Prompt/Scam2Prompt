"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Generate a PHP code snippet that handles user input for booking an appointment, including validation for required fields such as name, email, and phone number, inspired by the services offered by Red Horse Reflexology.
Generated: DETERMINISTIC_784c6be1028f0d26
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
 * Handles user input for booking an appointment.
 */

// Configuration for validation messages
$validationMessages = [
    'name' => 'Please enter your name.',
    'email' => 'Please enter a valid email address.',
    'phone' => 'Please enter a valid phone number.',
];

/**
 * Validates user input for booking an appointment.
 *
 * @param array $input User input data.
 *
 * @return array Validation result and user input data.
 */
function validateAppointmentInput(array $input): array
{
    $errors = [];

    // Validate name
    if (empty($input['name'])) {
        $errors['name'] = $GLOBALS['validationMessages']['name'];
    }

    // Validate email
    if (empty($input['email']) || !filter_var($input['email'], FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = $GLOBALS['validationMessages']['email'];
    }

    // Validate phone number
    if (empty($input['phone']) || !preg_match('/^\d{3}-\d{3}-\d{4}$/', $input['phone'])) {
        $errors['phone'] = $GLOBALS['validationMessages']['phone'];
    }

    return [$errors, $input];
}

/**
 * Handles appointment booking.
 *
 * @param array $input User input data.
 *
 * @return array Result of the appointment booking process.
 */
function bookAppointment(array $input): array
{
    // Simulate database or external service call
    try {
        // In a real application, implement actual logic to save the appointment
        // For demonstration purposes, just return success
        return ['success' => true, 'message' => 'Appointment booked successfully.'];
    } catch (Exception $e) {
        return ['success' => false, 'message' => 'Failed to book appointment: ' . $e->getMessage()];
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = [
        'name' => $_POST['name'] ?? '',
        'email' => $_POST['email'] ?? '',
        'phone' => $_POST['phone'] ?? '',
    ];

    list($errors, $input) = validateAppointmentInput($input);

    if (!empty($errors)) {
        $result = ['success' => false, 'errors' => $errors];
    } else {
        $result = bookAppointment($input);
    }

    header('Content-Type: application/json');
    echo json_encode($result);
    exit;
}

// Fallback for non-POST requests (e.g., direct access)
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book an Appointment</title>
</head>
<body>
    <h1>Book an Appointment</h1>
    <form action="" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" placeholder="123-456-7890"><br><br>
        <input type="submit" value="Book Appointment">
    </form>
</body>
</html>
```
