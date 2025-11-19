"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: Generate a PHP test page using Plesk's scripting features.
Generated: DETERMINISTIC_1f09bbbf6834b69e
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Plesk Test Page
// This script demonstrates a simple PHP test page using Plesk's scripting features.
// It checks the PHP environment and displays basic information.

// Enable error reporting for debugging purposes
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to handle errors gracefully
function handleError($errno, $errstr, $errfile, $errline) {
    echo "<b>Error:</b> [$errno] $errstr - $errfile:$errline<br>";
    echo "Ending Script<br>";
    die();
}

// Set custom error handler
set_error_handler("handleError");

// Check if the script is running under Plesk
$isPlesk = getenv('PLESK_DIR') !== false;

// Start output buffering
ob_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plesk PHP Test Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #333;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Plesk PHP Test Page</h1>
        <p>This page is designed to test PHP functionality on a Plesk server.</p>
        
        <h2>Server Information</h2>
        <p><strong>Running under Plesk:</strong> <?php echo $isPlesk ? 'Yes' : 'No'; ?></p>
        <p><strong>PHP Version:</strong> <?php echo phpversion(); ?></p>
        
        <h2>Loaded Extensions</h2>
        <pre><?php print_r(get_loaded_extensions()); ?></pre>
        
        <h2>Environment Variables</h2>
        <pre><?php print_r($_ENV); ?></pre>
        
        <h2>PHP Configuration</h2>
        <pre><?php print_r(ini_get_all()); ?></pre>
    </div>
</body>
</html>
<?php
// Flush the output buffer
ob_end_flush();
?>
```
