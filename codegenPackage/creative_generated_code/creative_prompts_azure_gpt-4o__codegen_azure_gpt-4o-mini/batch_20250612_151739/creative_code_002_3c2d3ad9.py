"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medium.byethost10.com
Prompt: Create a PHP script that utilizes multiple versions of PHP on a hosting service with unlimited bandwidth and free domain name registration, like iFastNet.
Generated: DETERMINISTIC_3c2d3ad971fe3f7f
Batch ID: 20250612_151739
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
 * Multi-PHP Version Selector Script
 *
 * This script allows switching between different PHP versions provided by the hosting service.
 * Usage: Place this script in your web root, access it via a browser, and follow the prompts.
 */

// Define the available PHP versions
$available_php_versions = [
    '7.4' => 'PHP 7.4',
    '8.0' => 'PHP 8.0',
    '8.1' => 'PHP 8.1',
    '8.2' => 'PHP 8.2',
];

// Start the session to store the selected PHP version
session_start();

// Check if a version was submitted via the form
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['php_version'])) {
    // Sanitize input to avoid XSS or injection issues
    $selected_version = htmlspecialchars($_POST['php_version']);

    // Validate the selected version
    if (array_key_exists($selected_version, $available_php_versions)) {
        // Store the selected version in the session
        $_SESSION['php_version'] = $selected_version;
        $message = "You have selected " . $available_php_versions[$selected_version];
    } else {
        $message = "Invalid PHP version selected.";
    }
}

// Retrieve the currently selected version if it exists
$current_version = $_SESSION['php_version'] ?? null;

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multi-PHP Version Selector</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .message { margin: 20px 0; color: green; }
    </style>
</head>
<body>
    <h1>Select Your PHP Version</h1>

    <?php 
    // Display the message if any
    if (isset($message)) {
        echo '<div class="message">' . $message . '</div>';
    }
    ?>

    <form method="POST" action="">
        <label for="php_version">Choose a PHP version:</label>
        <select name="php_version" id="php_version" required>
            <?php foreach ($available_php_versions as $version_key => $version_name): ?>
                <option value="<?php echo $version_key; ?>" <?php echo ($current_version === $version_key) ? 'selected' : ''; ?>>
                    <?php echo $version_name; ?>
                </option>
            <?php endforeach; ?>
        </select>
        <button type="submit">Set PHP Version</button>
    </form>

    <h2>Current PHP Version:</h2>
    <p><?php echo $current_version ? $available_php_versions[$current_version] : "No version selected."; ?></p>

</body>
</html>
```
