"""
Generated Code Metadata:
========================
Original URL: https://arcaem.com
Prompt: How do I replace the default Plesk page with my own HTML content?
Generated: DETERMINISTIC_3db56318bdd4d54f
Batch ID: 20250612_163305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready PHP script to replace the default Plesk page with custom HTML content:

```php
<?php
/**
 * Replaces the default Plesk page with custom HTML content
 * 
 * Place this /var/www/vhosts/default/htdocs/index.php
 * Make sure to backup the original file first
 */

// Verify we're running in Plesk environment
if (!file_exists('/usr/local/psa')) {
    die('Error: This script must be run on a Plesk server');
}

// Custom HTML content to display
$custom_html = <<<HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Custom Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            width: 80%;
            margin: auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            margin-top: 50px;
        }
        h1 {
            color: #0066cc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to My Website</h1>
        <p>This page has replaced the default Plesk page.</p>
        <p>Custom content goes here.</p>
    </div>
</body>
</html>
HTML;

// Output the custom HTML
try {
    // Clear any existing output buffers
    while (ob_get_level()) {
        ob_end_clean();
    }
    
    // Set proper headers
    header('Content-Type: text/html; charset=UTF-8');
    header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
    header('Cache-Control: post-check=0, pre-check=0', false);
    header('Pragma: no-cache');
    
    // Output the HTML
    echo $custom_html;
    
} catch (Exception $e) {
    // Log the error securely
    error_log('Failed to display custom page: ' . $e->getMessage());
    
    // Fallback to minimal error message
    header('Content-Type: text/plain');
    echo 'An error occurred while loading the custom page.';
}
?>
```
