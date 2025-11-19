"""
Generated Code Metadata:
========================
Original URL: https://paxfuili.epizy.com
Prompt: Write a PHP code snippet that demonstrates how to configure multiple versions of PHP on iFastNet Web Hosting, and how to switch between them.
Generated: DETERMINISTIC_c09dc411a06f2461
Batch ID: 20250622_204607
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
 * PHP Version Switcher for iFastNet Web Hosting
 * 
 * This script demonstrates how to configure and switch between multiple PHP versions
 * on iFastNet hosting using .htaccess directives.
 */

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $selectedVersion = $_POST['php_version'] ?? '';
    $validVersions = ['5.6', '7.0', '7.1', '7.2', '7.3', '7.4', '8.0', '8.1', '8.2'];
    
    // Validate the selected version
    if (in_array($selectedVersion, $validVersions)) {
        $htaccessContent = "AddHandler application/x-httpd-php{$selectedVersion} .php";
        
        try {
            // Write to .htaccess file
            if (file_put_contents('.htaccess', $htaccessContent) !== false) {
                $message = "Successfully switched to PHP {$selectedVersion}. Please wait a few moments for changes to take effect.";
            } else {
                throw new Exception("Failed to write to .htaccess file. Check file permissions.");
            }
        } catch (Exception $e) {
            $message = "Error: " . $e->getMessage();
        }
    } else {
        $message = "Invalid PHP version selected.";
    }
}

// Get current PHP version
$currentVersion = phpversion();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Version Switcher</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .container { max-width: 600px; margin: 0 auto; }
        .message { padding: 10px; margin: 10px 0; border-radius: 4px; }
        .success { background-color: #dff0d8; color: #3c763d; }
        .error { background-color: #f2dede; color: #a94442; }
    </style>
</head>
<body>
    <div class="container">
        <h1>PHP Version Switcher</h1>
        <p>Current PHP version: <?php echo $currentVersion; ?></p>
        
        <?php if (!empty($message)): ?>
            <div class="message <?php echo strpos($message, 'Error') === 0 ? 'error' : 'success'; ?>">
                <?php echo htmlspecialchars($message); ?>
            </div>
        <?php endif; ?>
        
        <form method="post">
            <label for="php_version">Select PHP Version:</label>
            <select name="php_version" id="php_version" required>
                <option value="">-- Select Version --</option>
                <option value="5.6">PHP 5.6</option>
                <option value="7.0">PHP 7.0</option>
                <option value="7.1">PHP 7.1</option>
                <option value="7.2">PHP 7.2</option>
                <option value="7.3">PHP 7.3</option>
                <option value="7.4">PHP 7.4</option>
                <option value="8.0">PHP 8.0</option>
                <option value="8.1">PHP 8.1</option>
                <option value="8.2">PHP 8.2</option>
            </select>
            
            <button type="submit">Switch Version</button>
        </form>
        
        <p><strong>Note:</strong> Changes may take a few minutes to propagate.</p>
    </div>
</body>
</html>
```
