"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Construct a code snippet in PHP that sends an email confirmation to customers after they book a boat through Coastal Boat Rentals' online system.
Generated: DETERMINISTIC_6a24fd1e07b2a1af
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Sends a confirmation email to customers after booking a boat.
 *
 * @param string $customerEmail The email address of the customer.
 * @param string $customerName The name of the customer.
 * @param string $boatDetails Details of the booked boat.
 * @param string $bookingDate The date of the booking.
 * @return bool True on success, false on failure.
 */
function sendBookingConfirmationEmail($customerEmail, $customerName, $boatDetails, $bookingDate) {
    // Validate email address
    if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
        throw new InvalidArgumentException("Invalid email address provided.");
    }

    // Subject of the email
    $subject = "Your Boat Booking Confirmation";

    // Email body content
    $message = "
    <html>
    <head>
        <title>Booking Confirmation</title>
    </head>
    <body>
        <h2>Dear $customerName,</h2>
        <p>Thank you for booking with Coastal Boat Rentals!</p>
        <p>You have successfully booked the following boat:</p>
        <p><strong>Boat Details:</strong> $boatDetails</p>
        <p><strong>Booking Date:</strong> $bookingDate</p>
        <p>We look forward to seeing you!</p>
        <p>Best regards,<br>Coastal Boat Rentals Team</p>
    </body>
    </html>
    ";

    // Set the content-type header for sending HTML email
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= "From: noreply@coastalboatrentals.com" . "\r\n";

    // Attempt to send the email and handle any errors
    if (!mail($customerEmail, $subject, $message, $headers)) {
        error_log("Failed to send email to $customerEmail.");
        return false; // Email sending failed
    }

    return true; // Email sent successfully
}

// Example usage
try {
    $customerEmail = "customer@example.com";
    $customerName = "John Doe";
    $boatDetails = "Luxury Yacht - Model XYZ";
    $bookingDate = "2023-10-15";

    if (sendBookingConfirmationEmail($customerEmail, $customerName, $boatDetails, $bookingDate)) {
        echo "Confirmation email sent successfully.";
    } else {
        echo "There was a problem sending the confirmation email.";
    }
} catch (Exception $e) {
    // Log the exception message
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage();
}
?>
```
