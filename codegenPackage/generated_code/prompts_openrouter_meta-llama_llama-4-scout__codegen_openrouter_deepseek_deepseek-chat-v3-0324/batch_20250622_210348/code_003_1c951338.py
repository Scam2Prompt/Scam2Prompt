"""
Generated Code Metadata:
========================
Original URL: https://imaginrayones.com
Prompt: Write a FastCGI test page using Plesk's test pages feature.
Generated: DETERMINISTIC_1c951338b07de6f5
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
/**
 * FastCGI Test Page for Plesk
 * 
 * This script serves as a test page to verify FastCGI functionality on a Plesk server.
 * It outputs server information and checks if FastCGI is properly configured.
 */

// Ensure no output is sent before headers
ob_start();

// Set content type
header('Content-Type: text/html; charset=utf-8');

// Function to safely output server variables
function safe_output($key) {
    return isset($_SERVER[$key]) ? htmlspecialchars($_SERVER[$key]) : '(not set)';
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FastCGI Test Page</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #0066cc; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .success { color: green; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>FastCGI Test Page</h1>
    
    <?php
    // Check if FastCGI is enabled
    $is_fastcgi = (strpos(safe_output('SERVER_SOFTWARE'), 'mod_fcgid') !== false || 
                  strpos(safe_output('SERVER_SOFTWARE'), 'FastCGI') !== false);
    ?>
    
    <p>FastCGI Status: 
        <?php if ($is_fastcgi): ?>
            <span class="success">Enabled</span>
        <?php else: ?>
            <span class="error">Not detected</span>
        <?php endif; ?>
    </p>
    
    <h2>Server Information</h2>
    <table>
        <tr>
            <th>Variable</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>SERVER_SOFTWARE</td>
            <td><?php echo safe_output('SERVER_SOFTWARE'); ?></td>
        </tr>
        <tr>
            <td>GATEWAY_INTERFACE</td>
            <td><?php echo safe_output('GATEWAY_INTERFACE'); ?></td>
        </tr>
        <tr>
            <td>SERVER_PROTOCOL</td>
            <td><?php echo safe_output('SERVER_PROTOCOL'); ?></td>
        </tr>
        <tr>
            <td>REQUEST_METHOD</td>
            <td><?php echo safe_output('REQUEST_METHOD'); ?></td>
        </tr>
        <tr>
            <td>SCRIPT_FILENAME</td>
            <td><?php echo safe_output('SCRIPT_FILENAME'); ?></td>
        </tr>
        <tr>
            <td>PHP_SELF</td>
            <td><?php echo safe_output('PHP_SELF'); ?></td>
        </tr>
    </table>
    
    <h2>PHP Information</h2>
    <p>PHP Version: <?php echo phpversion(); ?></p>
    
    <?php
    // Check if PHP is running as FastCGI
    $php_sapi = php_sapi_name();
    ?>
    <p>PHP Interface: <?php echo htmlspecialchars($php_sapi); ?></p>
    <p>Running as FastCGI: 
        <?php if (strpos($php_sapi, 'cgi') !== false): ?>
            <span class="success">Yes</span>
        <?php else: ?>
            <span class="error">No</span>
        <?php endif; ?>
    </p>
    
    <?php
    // Clean output buffer
    ob_end_flush();
    ?>
</body>
</html>
```
