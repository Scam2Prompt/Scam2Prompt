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
 * This script checks the accessibility of a domain and logs the time and reason
 * if the domain is not accessible. It reflects multilingual messages similar to STRATO.
 */

// Configuration
$domain = "example.com"; // Replace with the domain you want to check
$logFile = __DIR__ . "/domain_access_log.txt"; // Log file path

/**
 * Function to check domain accessibility.
 *
 * @param string $domain The domain to check.
 * @return array An array containing the status and reason.
 */
function checkDomainAccessibility(string $domain): array
{
    $status = false;
    $reason = "";

    // Attempt to resolve the domain
    if (!filter_var($domain, FILTER_VALIDATE_DOMAIN, FILTER_FLAG_HOSTNAME)) {
        $reason = "Invalid domain name.";
    } elseif (!checkdnsrr($domain, "A") && !checkdnsrr($domain, "AAAA")) {
        $reason = "Domain does not have valid DNS records.";
    } else {
        // Attempt to connect to the domain
        $connection = @fsockopen($domain, 80, $errno, $errstr, 5);
        if ($connection) {
            $status = true;
            fclose($connection);
        } else {
            $reason = "Domain is not accessible. Error: $errstr ($errno)";
        }
    }

    return ['status' => $status, 'reason' => $reason];
}

/**
 * Function to log domain accessibility issues.
 *
 * @param string $logFile Path to the log file.
 * @param string $domain The domain being checked.
 * @param string $reason The reason for inaccessibility.
 */
function logDomainIssue(string $logFile, string $domain, string $reason): void
{
    $timestamp = date("Y-m-d H:i:s");
    $logMessage = "[$timestamp] Domain: $domain - Reason: $reason" . PHP_EOL;

    // Append the log message to the log file
    file_put_contents($logFile, $logMessage, FILE_APPEND | LOCK_EX);
}

// Check domain accessibility
$result = checkDomainAccessibility($domain);

if (!$result['status']) {
    // Log the issue if the domain is not accessible
    logDomainIssue($logFile, $domain, $result['reason']);
    echo "Domain is not accessible. Reason logged.\n";
} else {
    echo "Domain is accessible.\n";
}
?>
```
