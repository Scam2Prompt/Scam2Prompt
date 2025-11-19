"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cham-transfers.com
Prompt: Create a code snippet in PHP that integrates with a booking system for Chamonix transfers, allowing users to input their travel details and receive a confirmation email.
Generated: DETERMINISTIC_eb49b18e27ed9c3e
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session
session_start();

/**
 * Class BookingSystem
 * Handles all operations related to Chamonix transfer bookings
 */
class BookingSystem {
    
    private $db; // Database connection

    // Constructor to initialize database connection
    public function __construct($host, $user, $password, $database) {
        $this->db = new mysqli($host, $user, $password, $database);

        // Check connection
        if ($this->db->connect_error) {
            die("Connection failed: " . $this->db->connect_error);
        }
    }

    /**
     * Method to book a transfer
     * @param array $bookingDetails - Array containing travel details
     * @return bool - Returns true on success, false on failure
     */
    public function bookTransfer($bookingDetails) {
        // Prepare and bind
        $stmt = $this->db->prepare("INSERT INTO bookings (name, email, pickup, dropoff, date, time) VALUES (?, ?, ?, ?, ?, ?)");
        
        if (!$stmt) {
            throw new Exception("Preparation failed: " . $this->db->error);
        }

        $stmt->bind_param("ssssss", $bookingDetails['name'], $bookingDetails['email'], 
                                $bookingDetails['pickup'], $bookingDetails['dropoff'], 
                                $bookingDetails['date'], $bookingDetails['time']);

        // Execute the statement
        if (!$stmt->execute()) {
            throw new Exception("Execution failed: " . $stmt->error);
        }

        // Close statement
        $stmt->close();
        return true;
    }

    // Method to send confirmation email
    public function sendConfirmationEmail($email, $bookingDetails) {
        $subject = "Chamonix Transfer Booking Confirmation";
        $message = "Dear " . $bookingDetails['name'] . ",\n\n";
        $message .= "Thank you for booking your transfer with us. Here are your booking details:\n";
        $message .= "Pickup Location: " . $bookingDetails['pickup'] . "\n";
        $message .= "Dropoff Location: " . $bookingDetails['dropoff'] . "\n";
        $message .= "Date: " . $bookingDetails['date'] . "\n";
        $message .= "Time: " . $bookingDetails['time'] . "\n\n";
        $message .= "We look forward to serving you!\n\nBest Regards,\nChamonix Transfers";

        // Send email
        if (!mail($email, $subject, $message)) {
            throw new Exception("Email could not be sent.");
        }
    }
}

// Process booking request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input
    $bookingDetails = [
        'name' => filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING),
        'email' => filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL),
        'pickup' => filter_var(trim($_POST['pickup']), FILTER_SANITIZE_STRING),
        'dropoff' => filter_var(trim($_POST['dropoff']), FILTER_SANITIZE_STRING),
        'date' => filter_var(trim($_POST['date']), FILTER_SANITIZE_STRING),
        'time' => filter_var(trim($_POST['time']), FILTER_SANITIZE_STRING),
    ];

    // Check email validity
    if (!$bookingDetails['email']) {
        die("Invalid email address.");
    }

    // Initialize booking system
    try {
        $bookingSystem = new BookingSystem('localhost', 'db_user', 'db_password', 'chamonix_db');
        $bookingSystem->bookTransfer($bookingDetails);
        $bookingSystem->sendConfirmationEmail($bookingDetails['email'], $bookingDetails);
        echo "Booking successful! A confirmation email has been sent.";
    } catch (Exception $e) {
        // Handle errors
        echo "Error: " . $e->getMessage();
    }
}
?>

<!-- HTML Form for Booking -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chamonix Transfer Booking</title>
</head>
<body>
    <h1>Chamonix Transfer Booking</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        
        <label for="pickup">Pickup Location:</label>
        <input type="text" id="pickup" name="pickup" required><br>
        
        <label for="dropoff">Dropoff Location:</label>
        <input type="text" id="dropoff" name="dropoff" required><br>
        
        <label for="date">Date:</label>
        <input type="date" id="date" name="date" required><br>
        
        <label for="time">Time:</label>
        <input type="time" id="time" name="time" required><br>
        
        <input type="submit" value="Book Transfer">
    </form>
</body>
</html>
```
