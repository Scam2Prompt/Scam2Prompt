"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zendesk-metamask.rf.gd
Prompt: Write a PHP script to configure and test SSL certificates on iFastNet hosting with multiple PHP versions.
Generated: DETERMINISTIC_c7a102db89204536
Batch ID: 20250612_151514
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
 * SSL Configuration and Testing Script for iFastNet Hosting
 * 
 * This script tests the SSL certificate setup on iFastNet hosting,
 * supporting multiple PHP versions. It checks the validity and 
 * expiration of the SSL certificate for a given domain.
 * 
 * Requirements:
 * - PHP 7.0 or newer
 * - OpenSSL extension enabled
 * 
 * Usage:
 * You can run this script from the command line or web browser by passing the domain name as a query parameter.
 */

// Function to test SSL certificate for the given domain
function testSSLConfiguration($domain) {
    // Validate domain input
    if (filter_var($domain, FILTER_VALIDATE_DOMAIN, FILTER_FLAG_HOSTNAME) === false) {
        throw new Exception("Invalid domain format: $domain");
    }

    // Connect to the domain and fetch SSL certificate details
    $port = 443; // Default HTTPS port
    $timeout = 30; // Timeout for connection attempts
    $streamContext = stream_context_create([
        "ssl" => [
            "capture_peer_cert" => true
        ]
    ]);

    $client = @stream_socket_client(
        "ssl://$domain:$port",
        $errorCode,
        $errorMessage,
        $timeout,
        STREAM_CLIENT_CONNECT,
        $streamContext
    );

    if (!$client) {
        throw new Exception("Failed to connect to $domain on port $port - $errorMessage ($errorCode)");
    }

    // Get SSL certificate details
    $params = stream_context_get_params($client);
    $certificate = $params['options']['ssl']['peer_certificate'] ?? null;

    if (!$certificate) {
        throw new Exception("Unable to retrieve the SSL certificate from $domain.");
    }

    // Extract and return SSL certificate details
    $certInfo = openssl_x509_parse($certificate);
    return [
        "domain" => $domain,
        "subject" => $certInfo["subject"] ?? null,
        "issuer" => $certInfo["issuer"] ?? null,
        "validFrom" => isset($certInfo["validFrom_time_t"]) ? date("Y-m-d H:i:s", $certInfo["validFrom_time_t"]) : null,
        "validTo" => isset($certInfo["validTo_time_t"]) ? date("Y-m-d H:i:s", $certInfo["validTo_time_t"]) : null,
        "isValid" => time() < ($certInfo["validTo_time_t"] ?? 0)
    ];
}

// Main script execution
try {
    // Get domain from user input
    $domain = $_GET['domain'] ?? $argv[1] ?? null;

    if (!$domain) {
        throw new Exception("Please provide a domain name as input.");
    }

    // Check SSL details
    $sslDetails = testSSLConfiguration($domain);

    // Output results
    header('Content-Type: application/json');
    echo json_encode([
        "status" => "success",
        "data" => $sslDetails
    ], JSON_PRETTY_PRINT);
} catch (Exception $ex) {
    // Handle errors gracefully
    header('Content-Type: application/json');
    echo json_encode([
        "status" => "error",
        "message" => $ex->getMessage()
    ], JSON_PRETTY_PRINT);
}
```
