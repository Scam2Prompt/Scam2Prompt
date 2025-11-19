"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rothschild.de.com
Prompt: Create a PHP code snippet that logs the time and reason when a domain is not accessible, reflecting the multilingual message seen on the STRATO page.
Generated: DETERMINISTIC_bd1f9bbda00d0492
Batch ID: 20250612_163103
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * PHP Script to log the time and reason when a domain is not accessible.
 * The log message mimics the multilingual message seen on the STRATO page.
 */

// Log file path
define('LOG_FILE', __DIR__ . '/domain_access_log.txt');

/**
 * Function to check if a domain is accessible.
 *
 * @param string $domain URL of the domain to check.
 * @return bool Returns true if accessible, false otherwise.
 */
function isDomainAccessible(string $domain): bool
{
    $headers = @get_headers($domain);
    return $headers && strpos($headers[0], '200 OK') !== false;
}

/**
 * Function to log inaccessible domain details.
 *
 * @param string $domain URL of the domain.
 * @param string $reason Reason for inaccessibility.
 */
function logDomainInaccessibility(string $domain, string $reason): void
{
    $timestamp = date('Y-m-d H:i:s');
    $logMessage = sprintf("[%s] Domain '%s' is not accessible. Reason: %s\n", $timestamp, $domain, $reason);

    // Append the log message to the file.
    file_put_contents(LOG_FILE, $logMessage, FILE_APPEND | LOCK_EX);
}

// Example domain to check.
$domain = 'https://example.com';

try {
    if (!isDomainAccessible($domain)) {
        $messageEN = "This domain is not reachable at the moment.";
        $messageDE = "Diese Domain ist momentan nicht erreichbar.";
        $messageFR = "Ce domaine n'est pas accessible pour le moment.";
        $reason = "$messageEN | $messageDE | $messageFR";

        logDomainInaccessibility($domain, $reason);
    }
} catch (Exception $e) {
    // Log unexpected errors.
    logDomainInaccessibility($domain, 'Unexpected error: ' . $e->getMessage());
}
?>
```
