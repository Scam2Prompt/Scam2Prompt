"""
Generated Code Metadata:
========================
Original URL: https://rothschild.de.com
Prompt: Create a PHP code snippet that logs the time and reason when a domain is not accessible, reflecting the multilingual message seen on the STRATO page.
Generated: DETERMINISTIC_bd1f9bbda00d0492
Batch ID: 20250612_163103
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
 * Domain Accessibility Logger
 * 
 * This script logs the time and reason when a domain is not accessible.
 * It reflects the multilingual message seen on the STRATO page.
 * 
 * Usage: Call the logDomainAccessibility function with the domain and reason.
 */

// Define the log file path
define('LOG_FILE', 'domain_accessibility.log');

/**
 * Logs the domain accessibility issue to a log file.
 *
 * @param string $domain The domain that is not accessible.
 * @param string $reason The reason for the inaccessibility.
 * @return void
 */
function logDomainAccessibility($domain, $reason) {
    // Validate input
    if (empty($domain) || empty($reason)) {
        throw new InvalidArgumentException('Domain and reason must not be empty.');
    }

    // Prepare the log message
    $timestamp = date('Y-m-d H:i:s');
    $logMessage = sprintf("[%s] Domain: %s - Reason: %s\n", $timestamp, $domain, $reason);

    // Attempt to write to the log file
    try {
        if (file_put_contents(LOG_FILE, $logMessage, FILE_APPEND | LOCK_EX) === false) {
            throw new RuntimeException('Failed to write to log file.');
        }
    } catch (Exception $e) {
        // Handle any exceptions that occur during logging
        error_log('Logging error: ' . $e->getMessage());
    }
}

// Example usage
try {
    logDomainAccessibility('example.com', 'Domain is not reachable due to DNS issues.');
} catch (Exception $e) {
    // Handle any exceptions that occur during the logging process
    echo 'Error: ' . $e->getMessage();
}
?>
```
