"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.epizy.com
Prompt: Write a simple PHP script that can be used on iFastNet Web Hosting, utilizing multiple versions of PHP supported by the service.
Generated: DETERMINISTIC_95e9ca307f05d12d
Batch ID: 20250622_212723
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
 * Simple PHP script compatible with multiple PHP versions on iFastNet Web Hosting.
 * This script demonstrates basic functionality and adheres to best practices.
 */

// Enable error reporting for debugging (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Define a function to handle errors gracefully
function handleError($errno, $errstr, $errfile, $errline) {
    // Log the error details (customize the log file path as needed)
    error_log("Error [$errno]: $errstr in $errfile on line $errline", 3, __DIR__ . '/error.log');
    // Display a generic error message to the user
    echo "An unexpected error occurred. Please try again later.";
    exit;
}

// Set the custom error handler
set_error_handler('handleError');

// Define a function to display server information
function displayServerInfo() {
    // Get PHP version
    $phpVersion = phpversion();
    // Get server software
    $serverSoftware = $_SERVER['SERVER_SOFTWARE'] ?? 'Unknown';
    // Get current script name
    $scriptName = $_SERVER['SCRIPT_NAME'] ?? 'Unknown';

    // Return server information as an associative array
    return [
        'PHP Version' => $phpVersion,
        'Server Software' => $serverSoftware,
        'Script Name' => $scriptName,
    ];
}

// Fetch server information
$serverInfo = displayServerInfo();

// Output server information in a clean format
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1>Server Information</h1>
    <table>
        <thead>
            <tr>
                <th>Key</th>
                <th>Value</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($serverInfo as $key => $value): ?>
                <tr>
                    <td><?php echo htmlspecialchars($key, ENT_QUOTES, 'UTF-8'); ?></td>
                    <td><?php echo htmlspecialchars($value, ENT_QUOTES, 'UTF-8'); ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```
