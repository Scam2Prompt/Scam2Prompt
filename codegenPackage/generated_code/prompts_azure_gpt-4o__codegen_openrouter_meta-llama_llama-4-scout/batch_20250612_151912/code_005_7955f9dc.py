"""
Generated Code Metadata:
========================
Original URL: https://geteasycrypto.com
Prompt: Create a PHP script to query the WHOIS server (e.g., `http://whois.domaintools.com`) and retrieve domain owner information, as mentioned in the CentOS-WebPanel test page.
Generated: DETERMINISTIC_7955f9dccae6b93d
Batch ID: 20250612_151912
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
 * WHOIS Query Script
 *
 * Queries the WHOIS server and retrieves domain owner information.
 *
 * @author [Your Name]
 */

// Configuration
$WHOIS_SERVER = 'whois.domaintools.com';
$TIMEOUT = 10; // seconds

/**
 * Queries the WHOIS server and retrieves domain information.
 *
 * @param string $domain The domain to query.
 *
 * @return string The WHOIS response.
 */
function queryWhois($domain) {
    // Validate domain
    if (!filter_var($domain, FILTER_VALIDATE_DOMAIN)) {
        throw new Exception("Invalid domain: $domain");
    }

    // Create socket
    $fp = fsockopen($WHOIS_SERVER, 43, $errno, $errstr, $TIMEOUT);
    if (!$fp) {
        throw new Exception("Failed to connect to WHOIS server: $errstr ($errno)");
    }

    // Send query
    fwrite($fp, $domain . "\r\n");

    // Get response
    $response = '';
    while (!feof($fp)) {
        $response .= fgets($fp);
    }

    // Close socket
    fclose($fp);

    return $response;
}

// Example usage
$domain = 'example.com';

try {
    $whoisInfo = queryWhois($domain);
    echo "WHOIS Information for $domain:\n";
    echo $whoisInfo;
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

?>
```
