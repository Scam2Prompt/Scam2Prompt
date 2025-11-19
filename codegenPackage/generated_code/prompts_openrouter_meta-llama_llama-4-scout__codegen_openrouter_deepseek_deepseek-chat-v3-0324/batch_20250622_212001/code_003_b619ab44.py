"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Write a PHP code snippet to store ticket booking form data in a MySQL database, including fields for email address, phone number, and preferred communication method.
Generated: DETERMINISTIC_b619ab448c362936
Batch ID: 20250622_212001
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
 * Ticket Booking Form Submission Handler
 * 
 * This script processes the ticket booking form submission and stores the data in a MySQL database.
 * It includes validation for required fields and proper error handling.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'ticket_booking');
define('DB_TABLE', 'bookings');

// Enable error reporting for debugging (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Initialize response array
$response = [
    'success' => false,
    'message' => '',
    'errors' => []
];

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    $response['message'] = 'Invalid request method.';
    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}

// Validate required fields
$requiredFields = ['email', 'phone', 'communication_method'];
foreach ($requiredFields as $field) {
    if (empty($_POST[$field])) {
        $response['errors'][$field] = 'This field is required.';
    }
}

// Validate email format
if (!empty($_POST['email']) && !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
    $response['errors']['email'] = 'Please enter a valid email address.';
}

// Validate phone number (basic validation)
if (!empty($_POST['phone']) && !preg_match('/^[0-9]{10,15}$/', $_POST['phone'])) {
    $response['errors']['phone'] = 'Please enter a valid phone number (10-15 digits).';
}

// If there are validation errors, return them
if (!empty($response['errors'])) {
    $response['message'] = 'Please correct the errors below.';
    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}

try {
    // Create database connection
    $conn = new PDO(
        "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME,
        DB_USER,
        DB_PASS
    );
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Prepare SQL statement
    $stmt = $conn->prepare("
        INSERT INTO " . DB_TABLE . " 
        (email, phone, communication_method, created_at) 
        VALUES (:email, :phone, :communication_method, NOW())
    ");

    // Bind parameters
    $stmt->bindParam(':email', $_POST['email']);
    $stmt->bindParam(':phone', $_POST['phone']);
    $stmt->bindParam(':communication_method', $_POST['communication_method']);

    // Execute the statement
    if ($stmt->execute()) {
        $response['success'] = true;
        $response['message'] = 'Your booking has been submitted successfully!';
    } else {
        $response['message'] = 'There was an error processing your booking. Please try again.';
    }

} catch (PDOException $e) {
    // Log the error (in production, you would log to a file or error tracking system)
    error_log("Database error: " . $e->getMessage());
    
    $response['message'] = 'A database error occurred. Please try again later.';
} finally {
    // Close connection
    $conn = null;
}

// Return JSON response
header('Content-Type: application/json');
echo json_encode($response);
?>
```
