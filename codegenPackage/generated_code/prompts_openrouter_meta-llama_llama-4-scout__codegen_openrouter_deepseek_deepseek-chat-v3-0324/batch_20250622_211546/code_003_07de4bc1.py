"""
Generated Code Metadata:
========================
Original URL: https://btc5000.epizy.com
Prompt: Generate a PHP code snippet that demonstrates how to configure and use multiple versions of PHP on iFastNet Web Hosting.
Generated: DETERMINISTIC_07de4bc149f556f8
Batch ID: 20250622_211546
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
 * This script demonstrates how to configure and use multiple PHP versions
 * on iFastNet hosting by modifying the .htaccess file.
 */

// Check if the script is being accessed directly
if (php_sapi_name() === 'cli') {
    exit('This script should be run via a web browser, not CLI.');
}

// Define available PHP versions (adjust based on iFastNet's offerings)
$availableVersions = [
    'php5.6' => 'PHP 5.6',
    'php7.0' => 'PHP 7.0',
    'php7.1' => 'PHP 7.1',
    'php7.2' => 'PHP 7.2',
    'php7.3' => 'PHP 7.3',
    'php7.4' => 'PHP 7.4',
    'php8.0' => 'PHP 8.0',
    'php8.1' => 'PHP 8.1'
];

// Handle form submission to switch PHP version
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['php_version'])) {
    $selectedVersion = $_POST['php_version'];
    
    // Validate the selected version
    if (!array_key_exists($selectedVersion, $availableVersions)) {
        die('Invalid PHP version selected.');
    }

    // .htaccess content to switch PHP version
    $htaccessContent = <<<HTACCESS
# PHP version switcher
AddHandler application/x-httpd-{$selectedVersion} .php
HTACCESS;

    // Write to .htaccess file
    try {
        if (file_put_contents('.htaccess', $htaccessContent) === false) {
            throw new Exception('Failed to write to .htaccess file.');
        }
        $successMessage = "PHP version switched to {$availableVersions[$selectedVersion]} successfully!";
    } catch (Exception $e) {
        die("Error: " . $e->getMessage());
    }
}

// Get current PHP version from .htaccess if exists
$currentVersion = null;
if (file_exists('.htaccess')) {
    $htaccess = file_get_contents('.htaccess');
    if (preg_match('/AddHandler application\/x-httpd-(php\d\.\d)/', $htaccess, $matches)) {
        $currentVersion = $matches[1];
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Version Switcher</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .success { color: green; margin: 10px 0; }
        .current { font-weight: bold; margin: 15px 0; }
    </style>
</head>
<body>
    <h1>PHP Version Switcher</h1>
    
    <?php if (isset($successMessage)): ?>
        <div class="success"><?php echo htmlspecialchars($successMessage); ?></div>
    <?php endif; ?>
    
    <div class="current">
        Current PHP Version: <?php echo phpversion(); ?>
        <?php if ($currentVersion): ?>
            (Configured: <?php echo $availableVersions[$currentVersion] ?? 'Unknown'; ?>)
        <?php endif; ?>
    </div>
    
    <form method="post">
        <label for="php_version">Select PHP Version:</label>
        <select name="php_version" id="php_version" required>
            <?php foreach ($availableVersions as $version => $label): ?>
                <option value="<?php echo htmlspecialchars($version); ?>"
                    <?php if ($currentVersion === $version) echo 'selected'; ?>>
                    <?php echo htmlspecialchars($label); ?>
                </option>
            <?php endforeach; ?>
        </select>
        <button type="submit">Switch Version</button>
    </form>
    
    <p><small>Note: Changes may take a few minutes to take effect.</small></p>
</body>
</html>
```
