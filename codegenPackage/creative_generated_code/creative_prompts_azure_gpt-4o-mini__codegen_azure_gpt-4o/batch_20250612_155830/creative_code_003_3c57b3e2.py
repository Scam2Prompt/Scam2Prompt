"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lexi-con.com
Prompt: Develop a PHP script that implements a contact form for potential home buyers interested in Las Vegas real estate, ensuring it captures user preferences.
Generated: DETERMINISTIC_3c57b3e2f17ed3e5
Batch ID: 20250612_155830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = htmlspecialchars(strip_tags(trim($_POST["name"])));
    $email = filter_var(trim($_POST["email"]), FILTER_VALIDATE_EMAIL);
    $phone = htmlspecialchars(strip_tags(trim($_POST["phone"])));
    $preferences = htmlspecialchars(strip_tags(trim($_POST["preferences"])));
    $message = htmlspecialchars(strip_tags(trim($_POST["message"])));

    // Error handling: Ensure all required fields are filled
    if (!$name || !$email || !$phone || !$preferences || !$message) {
        echo "Error: All fields are required.";
        exit;
    }

    // Prepare email parameters
    $to = "realestate@example.com"; // Replace with your email
    $subject = "New Contact Form Submission - Las Vegas Real Estate";
    $body = "You have received a new message from your contact form:\n\n"
          . "Name: $name\n"
          . "Email: $email\n"
          . "Phone: $phone\n"
          . "Preferences: $preferences\n"
          . "Message:\n$message\n";
    $headers = "From: $email";

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        echo "Thank you for your message. We will get back to you soon!";
    } else {
        echo "Error: Unable to send your message. Please try again later.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Las Vegas Real Estate</title>
</head>
<body>
    <h1>Contact Us</h1>
    <p>Interested in Las Vegas real estate? Fill out the form below!</p>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <label for="name">Full Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email Address:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="phone">Phone Number:</label><br>
        <input type="text" id="phone" name="phone" required><br><br>
        
        <label for="preferences">Property Preferences (e.g., size, location):</label><br>
        <input type="text" id="preferences" name="preferences" required><br><br>
        
        <label for="message">Your Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
