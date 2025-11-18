"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.timeimprint.com
Prompt: Provide a PHP script for testing scripting features on Plesk's test pages, as outlined on the placeholder page.
Generated: DETERMINISTIC_83aec189c53b6904
Batch ID: 20250612_151752
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
 * PHP Script for Testing Scripting Features on Plesk's Test Pages
 *
 * This script demonstrates various scripting features of PHP including:
 * - Outputting text
 * - Handling forms
 * - Using sessions
 * - Error handling
 */

// Start a session to demonstrate session handling
session_start();

// Set content type to HTML
header('Content-Type: text/html; charset=UTF-8');

// Error reporting for development purposes
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to safely escape output to prevent XSS
function escape($string) {
    return htmlspecialchars($string, ENT_QUOTES, 'UTF-8');
}

// Check if a form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input
    if (isset($_POST['name']) && !empty($_POST['name'])) {
        // Store the user's name in a session variable
        $_SESSION['name'] = escape(trim($_POST['name']));
    } else {
        // Set an error message if the name is not provided
        $error_message = "Please enter your name.";
    }
}

// Retrieve the name from the session if it exists
$name = isset($_SESSION['name']) ? $_SESSION['name'] : '';

// HTML Output
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plesk Test Page</title>
</head>
<body>
    <h1>Plesk Test Page</h1>

    <?php if (!empty($error_message)): ?>
        <div style="color: red;"><?php echo escape($error_message); ?></div>
    <?php endif; ?>

    <form method="post" action="">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>

    <?php if ($name): ?>
        <h2>Hello, <?php echo $name; ?>!</h2>
    <?php endif; ?>

    <footer>
        <p>PHP Version: <?php echo phpversion(); ?></p>
        <p>Server: <?php echo escape($_SERVER['SERVER_SOFTWARE']); ?></p>
    </footer>
</body>
</html>
```
