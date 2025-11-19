"""
Generated Code Metadata:
========================
Original URL: https://davivihnasd1.webcindario.com
Prompt: Write a PHP script to check if a URL has been requested and display a custom message, inspired by the functionality on davivihnasd1.webcindario.com.
Generated: DETERMINISTIC_0cbf0183d6634517
Batch ID: 20250612_151415
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
 * URL Request Checker with Custom Message Display
 * 
 * This script checks if a specific URL has been requested and displays a custom message.
 * Inspired by davivihnasd1.webcindario.com functionality.
 */

// Start session to track URL requests
session_start();

// Configuration
$targetUrl = 'requested-url'; // The URL to check for
$customMessage = 'This is a custom message displayed when the URL is requested!';
$messageDuration = 5; // Duration in seconds to display the message

// Check if the target URL matches the current request
if (isset($_SERVER['REQUEST_URI']) && strpos($_SERVER['REQUEST_URI'], $targetUrl) !== false) {
    // Set session flag to show message
    $_SESSION['show_custom_message'] = true;
    $_SESSION['message_expiry'] = time() + $messageDuration;
    
    // Redirect to avoid URL parameters in address bar
    header('Location: ' . strtok($_SERVER['REQUEST_URI'], '?'));
    exit();
}

// Check if we should display the message
$showMessage = isset($_SESSION['show_custom_message']) 
               && $_SESSION['show_custom_message'] 
               && time() < $_SESSION['message_expiry'];

// Clear message if expired
if ($showMessage && time() >= $_SESSION['message_expiry']) {
    unset($_SESSION['show_custom_message']);
    unset($_SESSION['message_expiry']);
    $showMessage = false;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Request Checker</title>
    <style>
        .custom-message {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px;
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            z-index: 1000;
            animation: fadeIn 0.5s, fadeOut 0.5s <?php echo $messageDuration - 0.5; ?>s;
        }
        
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        
        @keyframes fadeOut {
            from {opacity: 1;}
            to {opacity: 0;}
        }
    </style>
</head>
<body>
    <?php if ($showMessage): ?>
        <div class="custom-message">
            <?php echo htmlspecialchars($customMessage, ENT_QUOTES, 'UTF-8'); ?>
        </div>
        
        <?php 
        // Clear the message after displaying
        unset($_SESSION['show_custom_message']);
        unset($_SESSION['message_expiry']);
        ?>
    <?php endif; ?>
    
    <h1>Welcome to the URL Request Checker</h1>
    <p>Visit <a href="<?php echo htmlspecialchars($targetUrl, ENT_QUOTES, 'UTF-8'); ?>">this link</a> to see the custom message.</p>
</body>
</html>
```
