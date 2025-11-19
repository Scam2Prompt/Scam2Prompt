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
/**
 * Contact Form for Las Vegas Real Estate
 * This script processes a contact form for potential home buyers, capturing user preferences
 */

// Start the session
session_start();

// Define constants for form validation
define('NAME_MIN_LENGTH', 2);
define('NAME_MAX_LENGTH', 50);
define('EMAIL_REGEX', '/^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$/');
define('PHONE_REGEX', '/^\+?[0-9]{10,15}$/');

// Initialize error array
$errors = [];

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate name
    $name = trim($_POST['name']);
    if (strlen($name) < NAME_MIN_LENGTH || strlen($name) > NAME_MAX_LENGTH) {
        $errors['name'] = 'Name must be between ' . NAME_MIN_LENGTH . ' and ' . NAME_MAX_LENGTH . ' characters.';
    }

    // Validate email
    $email = trim($_POST['email']);
    if (!preg_match(EMAIL_REGEX, $email)) {
        $errors['email'] = 'Invalid email format.';
    }

    // Validate phone
    $phone = trim($_POST['phone']);
    if (!preg_match(PHONE_REGEX, $phone)) {
        $errors['phone'] = 'Invalid phone number format.';
    }

    // Capture user preferences
    $preferences = isset($_POST['preferences']) ? $_POST['preferences'] : [];

    // Check if there are any errors
    if (empty($errors)) {
        // Process the contact form (e.g., send email or save to database)
        $to = 'info@lasvegasrealestate.com'; // Change to your email
        $subject = 'New Contact Form Submission';
        $message = "Name: $name\nEmail: $email\nPhone: $phone\nPreferences:\n" . implode(", ", $preferences);
        $headers = "From: $email\r\nReply-To: $email\r\n";

        // Attempt to send the email
        if (mail($to, $subject, $message, $headers)) {
            $_SESSION['success'] = 'Your message has been sent successfully!';
            header('Location: thank_you.php'); // Redirect to thank you page
            exit;
        } else {
            $errors['form'] = 'There was an error sending your message. Please try again later.';
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Las Vegas Real Estate</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to a CSS file for styling -->
</head>
<body>
    <h1>Contact Us</h1>
    <?php if (!empty($errors)): ?>
        <div class="error-messages">
            <ul>
                <?php foreach ($errors as $error): ?>
                    <li><?php echo htmlspecialchars($error); ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
    <?php endif; ?>

    <form action="" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required>

        <fieldset>
            <legend>Your Preferences:</legend>
            <label><input type="checkbox" name="preferences[]" value="Single Family Home"> Single Family Home</label>
            <label><input type="checkbox" name="preferences[]" value="Condo"> Condo</label>
            <label><input type="checkbox" name="preferences[]" value="Townhouse"> Townhouse</label>
            <label><input type="checkbox" name="preferences[]" value="Investment Property"> Investment Property</label>
        </fieldset>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
