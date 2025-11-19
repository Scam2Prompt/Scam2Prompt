"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Develop a code example in PHP for creating a simple email sending functionality, similar to the "Send a Message" feature on the website, using a mail server for sending emails to the counselor.
Generated: DETERMINISTIC_f6082f6ef29002a4
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
 * Simple Email Sending Functionality in PHP
 * 
 * This script handles sending emails to a counselor using PHP's mail() function.
 * Includes basic validation and error handling.
 */

// Configuration
$to = 'counselor@example.com'; // Counselor's email address
$subjectPrefix = 'Message from Website: '; // Prefix for email subject

// Function to sanitize input data
function sanitizeInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

// Function to send email
function sendEmail($to, $subject, $message, $headers) {
    if (mail($to, $subject, $message, $headers)) {
        return true;
    } else {
        return false;
    }
}

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Initialize variables
    $name = $email = $subject = $message = '';
    $errors = [];
    
    // Validate and sanitize inputs
    if (empty($_POST['name'])) {
        $errors[] = 'Name is required';
    } else {
        $name = sanitizeInput($_POST['name']);
    }
    
    if (empty($_POST['email'])) {
        $errors[] = 'Email is required';
    } else {
        $email = sanitizeInput($_POST['email']);
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors[] = 'Invalid email format';
        }
    }
    
    if (empty($_POST['subject'])) {
        $errors[] = 'Subject is required';
    } else {
        $subject = sanitizeInput($_POST['subject']);
    }
    
    if (empty($_POST['message'])) {
        $errors[] = 'Message is required';
    } else {
        $message = sanitizeInput($_POST['message']);
    }
    
    // If no errors, proceed to send email
    if (empty($errors)) {
        // Prepare email headers
        $headers = "From: $name <$email>\r\n";
        $headers .= "Reply-To: $email\r\n";
        $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
        
        $fullSubject = $subjectPrefix . $subject;
        
        // Send email
        if (sendEmail($to, $fullSubject, $message, $headers)) {
            $success = 'Your message has been sent successfully!';
        } else {
            $errors[] = 'Failed to send message. Please try again later.';
        }
    }
}

// HTML form (could be in a separate file)
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Counselor</title>
    <style>
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Send a Message to Counselor</h1>
    
    <?php if (!empty($errors)): ?>
        <div class="error">
            <ul>
                <?php foreach ($errors as $error): ?>
                    <li><?php echo $error; ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
    <?php endif; ?>
    
    <?php if (isset($success)): ?>
        <div class="success"><?php echo $success; ?></div>
    <?php endif; ?>
    
    <form method="post" action="">
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" value="<?php echo isset($name) ? $name : ''; ?>" required>
        </div>
        
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="<?php echo isset($email) ? $email : ''; ?>" required>
        </div>
        
        <div>
            <label for="subject">Subject:</label>
            <input type="text" id="subject" name="subject" value="<?php echo isset($subject) ? $subject : ''; ?>" required>
        </div>
        
        <div>
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="5" required><?php echo isset($message) ? $message : ''; ?></textarea>
        </div>
        
        <button type="submit">Send Message</button>
    </form>
</body>
</html>
```
