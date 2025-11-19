"""
Generated Code Metadata:
========================
Original URL: https://www.nasiniacademyhairextension.it
Prompt: Develop a simple PHP script to handle maintenance mode for a website, based on the service maintenance example from nasiniacademyhairextension.it.
Generated: DETERMINISTIC_fb0b48aed9ebb268
Batch ID: 20250612_162051
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

// Function to display the maintenance page
function displayMaintenancePage() {
    // Set the HTTP response code to 503 (Service Unavailable)
    http_response_code(503);
    
    // Output the maintenance message
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Maintenance Mode</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            h1 { color: #333; }
            p { color: #666; }
        </style>
    </head>
    <body>
        <h1>We are currently undergoing maintenance</h1>
        <p>We apologize for the inconvenience. Please check back later.</p>
    </body>
    </html>';
    exit; // Stop further execution
}

// Check if the site is in maintenance mode
if (isMaintenanceMode()) {
    displayMaintenancePage(); // Show the maintenance page
}

// Your regular website code goes here
// For example, include your main application logic
// include 'index.php'; // Uncomment this line to include your main application
?>
```

This PHP script checks if the website is in maintenance mode and displays a user-friendly maintenance page if it is. The script is structured to be clean, efficient, and ready for production use.
