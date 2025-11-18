"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Generate a PHP script to handle form submissions for a ticket booking system, storing the submitted data (number of tickets, ticket type, communication method, email, and phone number) in a MySQL database.
Generated: DETERMINISTIC_c70bb85c31a723f7
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ticket Booking System Form Submission Handler

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'ticket_booking_system');
define('DB_USER', 'root');
define('DB_PASS', 'password');

// Establish a connection to the MySQL database
try {
    $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]);
} catch (PDOException $e) {
    // Handle database connection error
    die('Database connection failed: ' . $e->getMessage());
}

// Check if the form is submitted via POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve and sanitize user input
    $number_of_tickets = filter_input(INPUT_POST, 'number_of_tickets', FILTER_VALIDATE_INT);
    $ticket_type = filter_input(INPUT_POST, 'ticket_type', FILTER_SANITIZE_STRING);
    $communication_method = filter_input(INPUT_POST, 'communication_method', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone_number = filter_input(INPUT_POST, 'phone_number', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (
        $number_of_tickets === false || $number_of_tickets <= 0 ||
        empty($ticket_type) || empty($communication_method) ||
        (!$email && empty($phone_number))
    ) {
        // Redirect or display an error message for invalid input
        die('Invalid input. Please fill out the form correctly.');
    }

    try {
        // Prepare the SQL query to insert data into the tickets table
        $stmt = $pdo->prepare(
            'INSERT INTO tickets (number_of_tickets, ticket_type, communication_method, email, phone_number) 
             VALUES (:number_of_tickets, :ticket_type, :communication_method, :email, :phone_number)'
        );

        // Bind parameters to prevent SQL injection
        $stmt->bindParam(':number_of_tickets', $number_of_tickets, PDO::PARAM_INT);
        $stmt->bindParam(':ticket_type', $ticket_type, PDO::PARAM_STR);
        $stmt->bindParam(':communication_method', $communication_method, PDO::PARAM_STR);
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        $stmt->bindParam(':phone_number', $phone_number, PDO::PARAM_STR);

        // Execute the query
        if ($stmt->execute()) {
            // Redirect or display a success message
            echo 'Thank you! Your booking has been successfully submitted.';
        } else {
            // Handle query execution failure
            echo 'An error occurred while processing your booking. Please try again.';
        }
    } catch (PDOException $e) {
        // Handle database query errors
        die('Database error: ' . $e->getMessage());
    }
} else {
    // Redirect or display an error message for unsupported request methods
    die('Invalid request method.');
}
?>
```
