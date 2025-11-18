"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssupport.42web.io
Prompt: Generate a PHP script compatible with iFastNet hosting that leverages multiple PHP versions for backward compatibility.
Generated: DETERMINISTIC_8f65d28349eee51d
Batch ID: 20250612_154420
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
 * iFastNet Multi-Version PHP Compatibility Script
 *
 * This script demonstrates how to switch between different versions of PHP
 * on iFastNet hosting while ensuring backward compatibility for your application.
 * It uses the .htaccess file to manage PHP versioning and includes error handling
 * for any potential issues that may arise during execution.
 */

// Set the desired PHP version (7.4, 8.0, or 8.1)
$desiredPhpVersion = '8.0';

// Function to set the PHP version
function setPhpVersion($version) {
    // Validate the PHP version to ensure it's one of the supported versions
    $supportedVersions = ['7.4', '8.0', '8.1'];
    if (!in_array($version, $supportedVersions)) {
        throw new InvalidArgumentException("Unsupported PHP version: $version");
    }

    // Create the .htaccess content to select the PHP version
    $htaccessContent = "<?php\n" .
                       "    # Use the following line to set the PHP version\n" .
                       "    AddHandler application/x-httpd-php$version .php\n" .
                       "?>";

    // Write to the .htaccess file
    if (file_put_contents('.htaccess', $htaccessContent) === false) {
        throw new RuntimeException('Failed to write to .htaccess file.');
    }
}

// Error handling using try-catch
try {
    setPhpVersion($desiredPhpVersion);
    echo "PHP version set to $desiredPhpVersion successfully.";
} catch (InvalidArgumentException $e) {
    // Log the exception message for debugging
    error_log($e->getMessage());
    echo "Error: " . $e->getMessage();
} catch (RuntimeException $e) {
    // Log the exception message for debugging
    error_log($e->getMessage());
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    // Catch any other unexpected exceptions
    error_log($e->getMessage());
    echo "An unexpected error occurred: " . $e->getMessage();
}

// Note: This script requires the appropriate permissions to write to the .htaccess file.
// Ensure that your application has the necessary permissions set on your iFastNet hosting account.
?>
```
