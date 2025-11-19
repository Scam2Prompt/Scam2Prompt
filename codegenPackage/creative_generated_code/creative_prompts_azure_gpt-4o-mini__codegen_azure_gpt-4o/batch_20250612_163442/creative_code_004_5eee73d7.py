"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-today.rf.gd
Prompt: What are the specific steps to enable multiple PHP versions on iFastNet Web Hosting?
Generated: DETERMINISTIC_5eee73d788580af1
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Script to check and switch PHP versions on iFastNet Web Hosting

// Step 1: Define the desired PHP version
$desiredPHPVersion = '8.1'; // Change this to the version you want (e.g., '7.4', '8.0', etc.)

// Step 2: Check the current PHP version
$currentPHPVersion = phpversion();

// Log the current PHP version
echo "Current PHP Version: $currentPHPVersion\n";

// Step 3: Verify if the desired PHP version is available
$availableVersions = ['7.2', '7.4', '8.0', '8.1']; // Example list of available PHP versions on iFastNet

if (!in_array($desiredPHPVersion, $availableVersions)) {
    // If the desired version is not available, show an error and exit
    echo "Error: Desired PHP version $desiredPHPVersion is not available on this hosting.\n";
    exit;
}

// Step 4: Check if the current PHP version matches the desired version
if ($currentPHPVersion === $desiredPHPVersion) {
    echo "The desired PHP version $desiredPHPVersion is already active.\n";
    exit;
}

// Step 5: Set the PHP version by creating or modifying the `.htaccess` file
$htaccessFilePath = $_SERVER['DOCUMENT_ROOT'] . '/.htaccess'; // Path to the .htaccess file
$phpHandlerLine = "AddHandler application/x-httpd-php$desiredPHPVersion .php\n"; // Handler for the desired PHP version

try {
    // Read the current contents of the .htaccess file if it exists
    $htaccessContent = file_exists($htaccessFilePath) ? file_get_contents($htaccessFilePath) : '';

    // Replace any existing PHP version handler with the new desired version
    $updatedContent = preg_replace(
        '/AddHandler\s+application\/x-httpd-php\d+\s+.php/', 
        $phpHandlerLine, 
        $htaccessContent
    );

    // If no handler exists, add the new one
    if (!$updatedContent) {
        $updatedContent = $htaccessContent . $phpHandlerLine;
    }

    // Write the updated content back to the .htaccess file
    file_put_contents($htaccessFilePath, $updatedContent);

    echo "PHP version successfully switched to $desiredPHPVersion. Please allow a few minutes for changes to take effect.\n";
} catch (Exception $e) {
    // Handle errors related to file operations
    echo "Error: Failed to update .htaccess file - " . $e->getMessage() . "\n";
    exit;
}
?>
```
