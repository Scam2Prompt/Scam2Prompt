"""
Generated Code Metadata:
========================
Original URL: https://metaimsklogi.imweb.me
Prompt: How can I implement a maintenance mode for my website using PHP?
Generated: DETERMINISTIC_722900175864960b
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// maintenance.php

// Start the session to manage user state
session_start();

// Define a constant for maintenance mode
define('MAINTENANCE_MODE', true);

// Function to check if the site is in maintenance mode
function isMaintenanceMode() {
    return MAINTENANCE_MODE;
}

// Function to display a maintenance message
function displayMaintenanceMessage() {
    // Set the HTTP response code to 503 (Service Unavailable)
    http_response_code(503);
    
    // Display a user-friendly maintenance message
    echo "<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Maintenance Mode</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            h1 { color: #ff0000; }
        </style>
    </head>
    <body>
        <h1>We'll be back soon!</h1>
        <p>Our website is currently undergoing maintenance. Please check back later.</p>
    </body>
    </html>";
    exit; // Terminate the script after displaying the message
}

// Check if the site is in maintenance mode
if (isMaintenanceMode()) {
    // If the user is not an admin, display the maintenance message
    if (!isset($_SESSION['is_admin']) || $_SESSION['is_admin'] !== true) {
        displayMaintenanceMessage();
    }
}

// Your regular website code goes here
// For example, include your main application logic or routing
// include 'app.php'; // Uncomment this line to include your main application logic

?>
```

### Usage Instructions:
1. Set the `MAINTENANCE_MODE` constant to `true` to enable maintenance mode.
2. Ensure that you set a session variable `$_SESSION['is_admin']` to `true` for admin users who should bypass the maintenance message.
3. Place this code at the top of your PHP files to enforce maintenance mode across your website.
