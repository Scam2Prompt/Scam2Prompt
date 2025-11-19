"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pneusml.com
Prompt: Develop a PHP script that allows users to submit a request for a tire inspection and alignment service, similar to the services offered by Pneus ML.
Generated: DETERMINISTIC_a9b4a5061e641ec9
Batch ID: 20250612_163224
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
 * Tire Inspection and Alignment Service Request Script
 * 
 * This script allows users to submit a request for tire inspection and alignment services.
 * It handles form submission, validates input, and sends a confirmation email to the user.
 */

// Start the session to use session variables
session_start();

// Define constants for email configuration
define('ADMIN_EMAIL', 'admin@pneusml.com');
define('SUCCESS_MESSAGE', 'Your request has been submitted successfully. We will contact you shortly.');
define('ERROR_MESSAGE', 'There was an error processing your request. Please try again later.');

// Initialize variables
$name = '';
$email = '';
$phone = '';
$service_date = '';
$message = '';
$success = false;

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $service_date = filter_input(INPUT_POST, 'service_date', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Invalid email format'); // Early exit for invalid email
    }
    
    // Check for required fields
    if (empty($name) || empty($email) || empty($phone) || empty($service_date)) {
        die('All fields are required'); // Early exit for missing fields
    }

    // Prepare email content
    $subject = "New Tire Inspection and Alignment Request";
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n";
    $email_content .= "Phone: $phone\n";
    $email_content .= "Service Date: $service_date\n";
    $email_content .= "Message: $message\n";

    // Attempt to send email
    if (mail(ADMIN_EMAIL, $subject, $email_content)) {
        $success = true;
        $_SESSION['success_message'] = SUCCESS_MESSAGE;
    } else {
        $_SESSION['error_message'] = ERROR_MESSAGE;
    }
}

// Redirect to the form page
header('Location: request_form.php');
exit;

?>

<!-- HTML Form to request service -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tire Inspection Request</title>
</head>
<body>

<?php
// Display success or error message
if (isset($_SESSION['success_message'])) {
    echo "<p style='color: green;'>".$_SESSION['success_message']."</p>";
    unset($_SESSION['success_message']);
} elseif (isset($_SESSION['error_message'])) {
    echo "<p style='color: red;'>".$_SESSION['error_message']."</p>";
    unset($_SESSION['error_message']);
}
?>

<form action="" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required value="<?php echo htmlspecialchars($name); ?>"><br>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required value="<?php echo htmlspecialchars($email); ?>"><br>

    <label for="phone">Phone:</label>
    <input type="text" id="phone" name="phone" required value="<?php echo htmlspecialchars($phone); ?>"><br>

    <label for="service_date">Preferred Service Date:</label>
    <input type="date" id="service_date" name="service_date" required value="<?php echo htmlspecialchars($service_date); ?>"><br>

    <label for="message">Message:</label>
    <textarea id="message" name="message"><?php echo htmlspecialchars($message); ?></textarea><br>

    <button type="submit">Submit Request</button>
</form>

</body>
</html>
```
