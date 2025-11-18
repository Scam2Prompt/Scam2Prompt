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
// Database configuration
$host = 'localhost'; // Database host
$db = 'ticket_booking'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

// Create a new PDO instance
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input data
    $numTickets = filter_input(INPUT_POST, 'num_tickets', FILTER_VALIDATE_INT);
    $ticketType = filter_input(INPUT_POST, 'ticket_type', FILTER_SANITIZE_STRING);
    $communicationMethod = filter_input(INPUT_POST, 'communication_method', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);

    // Check for validation errors
    if ($numTickets === false || $numTickets <= 0) {
        die("Invalid number of tickets.");
    }
    if (empty($ticketType)) {
        die("Ticket type is required.");
    }
    if (empty($communicationMethod)) {
        die("Communication method is required.");
    }
    if ($email === false) {
        die("Invalid email address.");
    }
    if (empty($phone)) {
        die("Phone number is required.");
    }

    // Prepare the SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO ticket_bookings (num_tickets, ticket_type, communication_method, email, phone) VALUES (:num_tickets, :ticket_type, :communication_method, :email, :phone)");

    // Bind parameters
    $stmt->bindParam(':num_tickets', $numTickets, PDO::PARAM_INT);
    $stmt->bindParam(':ticket_type', $ticketType);
    $stmt->bindParam(':communication_method', $communicationMethod);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':phone', $phone);

    // Execute the statement and handle success/failure
    try {
        $stmt->execute();
        echo "Ticket booking successfully submitted!";
    } catch (PDOException $e) {
        // Handle execution errors
        die("Error submitting the booking: " . $e->getMessage());
    }
}
?>

<!-- Simple HTML form for ticket booking -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ticket Booking Form</title>
</head>
<body>
    <h1>Book Your Tickets</h1>
    <form method="POST" action="">
        <label for="num_tickets">Number of Tickets:</label>
        <input type="number" id="num_tickets" name="num_tickets" required min="1">
        
        <label for="ticket_type">Ticket Type:</label>
        <input type="text" id="ticket_type" name="ticket_type" required>
        
        <label for="communication_method">Communication Method:</label>
        <select id="communication_method" name="communication_method" required>
            <option value="email">Email</option>
            <option value="phone">Phone</option>
        </select>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="phone">Phone Number:</label>
        <input type="text" id="phone" name="phone" required>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
