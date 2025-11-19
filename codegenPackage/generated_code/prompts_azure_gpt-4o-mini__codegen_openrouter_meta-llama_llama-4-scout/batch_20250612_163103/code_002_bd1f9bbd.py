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
 * Logs the time and reason when a domain is not accessible.
 */

// Configuration
$logFile = 'domain_accessibility.log';
$domain = 'example.com'; // replace with the domain to check
$timeout = 5; // seconds

/**
 * Checks if a domain is accessible.
 *
 * @param string $domain The domain to check.
 * @param int $timeout The timeout in seconds.
 *
 * @return bool True if the domain is accessible, false otherwise.
 */
function isDomainAccessible($domain, $timeout) {
    $ch = curl_init($domain);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);
    curl_setopt($ch, CURLOPT_HEADER, true);
    curl_setopt($ch, CURLOPT_NOBODY, true);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    return $httpCode >= 200 && $httpCode < 300;
}

/**
 * Logs a message to the log file.
 *
 * @param string $message The message to log.
 */
function logMessage($message) {
    global $logFile;
    $timestamp = date('Y-m-d H:i:s');
    $logEntry = "$timestamp - $message\n";
    file_put_contents($logFile, $logEntry, FILE_APPEND);
}

// Check if the domain is accessible
if (!isDomainAccessible($domain, $timeout)) {
    // Multilingual messages (reflecting STRATO page)
    $reasons = [
        'en' => 'The domain is currently not accessible.',
        'de' => 'Die Domain ist derzeit nicht erreichbar.',
        'fr' => 'Le domaine est actuellement inaccessible.',
        'es' => 'El dominio no es accesible en este momento.',
    ];

    // Log the time and reason
    $reason = $reasons['en']; // default to English
    $locale = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2); // simple locale detection
    if (isset($reasons[$locale])) {
        $reason = $reasons[$locale];
    }
    logMessage("Domain $domain not accessible. Reason: $reason");
}

?>
```
