"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morevacare.com
Prompt: Write PHP code to implement a "contact us" form for an e-commerce website, ensuring compliance with GDPR, as seen in MorevaCare's legal section.
Generated: DETERMINISTIC_5855120953227037
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session to manage form submission status
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user inputs
    $name = trim(htmlspecialchars($_POST['name'] ?? ''));
    $email = trim(htmlspecialchars($_POST['email'] ?? ''));
    $message = trim(htmlspecialchars($_POST['message'] ?? ''));
    $gdprConsent = isset($_POST['gdpr_consent']) ? true : false;

    // Initialize error messages
    $errors = [];

    // Validate form inputs
    if (empty($name)) {
        $errors['name'] = 'Name is required.';
    }

    if (empty($email)) {
        $errors['email'] = 'Email is required.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Invalid email format.';
    }

    if (empty($message)) {
        $errors['message'] = 'Message is required.';
    }

    if (!$gdprConsent) {
        $errors['gdpr_consent'] = 'You must agree to the GDPR privacy policy.';
    }

    // If no errors, process the form submission
    if (empty($errors)) {
        try {
            // Simulate email sending (use mail() or an email library like PHPMailer in production)
            // For example: mail($to, $subject, $message, $headers);

            // Store successful submission in the session
            $_SESSION['form_status'] = 'success';
            header('Location: contact.php'); // Redirect to avoid form resubmission
            exit;
        } catch (Exception $e) {
            $errors['form'] = 'Failed to send the message. Please try again later.';
        }
    }
}

// Retrieve the form status if available
$formStatus = $_SESSION['form_status'] ?? null;
unset($_SESSION['form_status']); // Clear the status after retrieval
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
        }
        .form-container {
            max-width: 500px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
        .success {
            color: green;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
<div class="form-container">
    <h1>Contact Us</h1>

    <?php if ($formStatus === 'success'): ?>
        <p class="success">Thank you for your message! We will get back to you shortly.</p>
    <?php endif; ?>

    <form action="contact.php" method="POST">
        <!-- Name field -->
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" value="<?= htmlspecialchars($_POST['name'] ?? '') ?>"><br>
        <?php if (!empty($errors['name'])): ?>
            <span class="error"><?= htmlspecialchars($errors['name']) ?></span><br>
        <?php endif; ?>

        <!-- Email field -->
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" value="<?= htmlspecialchars($_POST['email'] ?? '') ?>"><br>
        <?php if (!empty($errors['email'])): ?>
            <span class="error"><?= htmlspecialchars($errors['email']) ?></span><br>
        <?php endif; ?>

        <!-- Message field -->
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5"><?= htmlspecialchars($_POST['message'] ?? '') ?></textarea><br>
        <?php if (!empty($errors['message'])): ?>
            <span class="error"><?= htmlspecialchars($errors['message']) ?></span><br>
        <?php endif; ?>

        <!-- GDPR Consent checkbox -->
        <label>
            <input type="checkbox" name="gdpr_consent" <?= isset($_POST['gdpr_consent']) ? 'checked' : '' ?>>
            I agree to the <a href="/privacy-policy" target="_blank">GDPR privacy policy</a>.
        </label><br>
        <?php if (!empty($errors['gdpr_consent'])): ?>
            <span class="error"><?= htmlspecialchars($errors['gdpr_consent']) ?></span><br>
        <?php endif; ?>

        <!-- Submit button -->
        <button type="submit">Send Message</button>
    </form>
</div>
</body>
</html>
```
