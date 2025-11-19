"""
Generated Code Metadata:
========================
Original URL: https://rothschild.de.com
Prompt: Create a PHP code snippet that logs the time and reason when a domain is not accessible, reflecting the multilingual message seen on the STRATO page.
Generated: DETERMINISTIC_bd1f9bbda00d0492
Batch ID: 20250612_163103
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php

/**
 * DomainAccessLogger
 * 
 * A utility class to log domain accessibility checks with timestamps and reasons.
 * Supports multilingual error messages similar to STRATO's page.
 */
class DomainAccessLogger {
    /**
     * @var string Path to the log file
     */
    private $logFile;

    /**
     * @var array Multilingual error messages
     */
    private $errorMessages = [
        'en' => [
            'dns_error' => 'DNS resolution failed',
            'timeout' => 'Connection timed out',
            'http_error' => 'HTTP error occurred',
            'ssl_error' => 'SSL certificate error'
        ],
        'de' => [
            'dns_error' => 'DNS-Auflösung fehlgeschlagen',
            'timeout' => 'Verbindung zeitüberschritten',
            'http_error' => 'HTTP-Fehler aufgetreten',
            'ssl_error' => 'SSL-Zertifikatsfehler'
        ]
    ];

    /**
     * Constructor
     * 
     * @param string $logFile Path to the log file
     */
    public function __construct($logFile = 'domain_access.log') {
        $this->logFile = $logFile;
    }

    /**
     * Check if a domain is accessible
     * 
     * @param string $domain Domain to check
     * @param string $lang Language for error messages (en/de)
     * @return bool True if accessible, false otherwise
     */
    public function checkDomainAccessibility($domain, $lang = 'en') {
        if (!array_key_exists($lang, $this->errorMessages)) {
            $lang = 'en';
        }

        // Remove http/https prefix if present
        $cleanDomain = preg_replace('#^https?://#', '', $domain);

        // Check DNS first
        if (!gethostbyname($cleanDomain)) {
            $this->logFailure($cleanDomain, 'dns_error', $lang);
            return false;
        }

        // Initialize cURL
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "http://" . $cleanDomain);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
        curl_setopt($ch, CURLOPT_TIMEOUT, 10);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_MAXREDIRS, 3);
        curl_setopt($ch, CURLOPT_USERAGENT, 'DomainAccessChecker/1.0');

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $error = curl_error($ch);
        curl_close($ch);

        // Check for cURL errors
        if ($error) {
            if (strpos($error, 'timed out') !== false) {
                $this->logFailure($cleanDomain, 'timeout', $lang);
            } elseif (strpos($error, 'SSL') !== false) {
                $this->logFailure($cleanDomain, 'ssl_error', $lang);
            } else {
                $this->logFailure($cleanDomain, 'http_error', $lang);
            }
            return false;
        }

        // Check HTTP status code
        if ($httpCode >= 400) {
            $this->logFailure($cleanDomain, 'http_error', $lang);
            return false;
        }

        return true;
    }

    /**
     * Log domain access failure
     * 
     * @param string $domain Domain that failed
     * @param string $errorType Type of error
     * @param string $lang Language for error message
     */
    private function logFailure($domain, $errorType, $lang = 'en') {
        $timestamp = date('Y-m-d H:i:s');
        $message = $this->errorMessages[$lang][$errorType] ?? $this->errorMessages['en'][$errorType];

        $logEntry = sprintf(
            "[%s] Domain '%s' inaccessible. Reason: %s\n",
            $timestamp,
            $domain,
            $message
        );

        file_put_contents($this->logFile, $logEntry, FILE_APPEND);
    }
}

// Example usage:
// $logger = new DomainAccessLogger();
// $logger->checkDomainAccessibility('example.com', 'de');
// $logger->checkDomainAccessibility('nonexistentdomain.abc', 'en');

?>
```
