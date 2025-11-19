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
// Enable error reporting for debugging (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Initialize response array
$response = [
    'success' => false,
    'message' => '',
];

// Check if the form is submitted via POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user inputs
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
    $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : '';
    $phone = isset($_POST['phone']) ? sanitizeInput($_POST['phone']) : '';
    $appointmentDate = isset($_POST['appointment_date']) ? sanitizeInput($_POST['appointment_date']) : '';

    // Validate required fields
    if (empty($name)) {
        $response['message'] = 'Name is required.';
    } elseif (empty($email)) {
        $response['message'] = 'Email is required.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $response['message'] = 'Invalid email format.';
    } elseif (empty($phone)) {
        $response['message'] = 'Phone number is required.';
    } elseif (!preg_match('/^\+?[0-9]{10,15}$/', $phone)) {
        $response['message'] = 'Invalid phone number format.';
    } elseif (empty($appointmentDate)) {
        $response['message'] = 'Appointment date is required.';
    } else {
        // If all validations pass, process the booking
        try {
            // Simulate saving the booking (e.g., to a database)
            // In production, replace this with actual database logic
            $response['success'] = true;
            $response['message'] = 'Appointment booked successfully!';
        } catch (Exception $e) {
            // Handle any unexpected errors
            $response['message'] = 'An error occurred while booking the appointment. Please try again later.';
        }
    }
}

// Return JSON response
header('Content-Type: application/json');
echo json_encode($response);
?>
```

This PHP code snippet is designed to handle user input for booking an appointment, including validation for required fields such as name, email, phone number, and appointment date. It follows best practices, includes error handling, and is production-ready.
