"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopias-program-rewards.mydiscussion.net
Prompt: Write a PHP script to verify SSL installation on a domain hosted by iFastNet.
Generated: DETERMINISTIC_418fb81617b61a93
Batch ID: 20250612_153314
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
 * SSL Verification Script for iFastNet Hosted Domain
 * 
 * This script checks if an SSL certificate is properly installed on a given domain.
 *
 * Usage:
 * 1. Save the script as ssl_verification.php.
 * 2. Run the script in the CLI or access it via a web browser.
 * 3. Provide the domain name as a parameter.
 */

// Function to validate the domain name format
function validateDomain($domain) {
    return filter_var($domain, FILTER_VALIDATE_DOMAIN, FILTER_FLAG_HOSTNAME);
}

// Function to check SSL certificate details
function checkSSL($domain) {
    $sslDetails = [];

    // Establish a connection to retrieve certificate information
    $streamContext = stream_context_create([
        "ssl" => [
            "capture_peer_cert" => true,
            "verify_peer" => false,
            "verify_peer_name" => false,
        ]
    ]);

    try {
        // Open a secure connection to the domain
        $client = @stream_socket_client(
            "ssl://{$domain}:443",
            $errno,
            $errstr,
            30,
            STREAM_CLIENT_CONNECT,
            $streamContext
        );

        // Check if the connection succeeded
        if (!$client) {
            throw new Exception("Unable to connect to domain (SSL): $errstr ($errno)");
        }

        // Extract SSL certificate information
        $contextOptions = stream_context_get_options($client);
        if (isset($contextOptions['ssl']['peer_certificate'])) {
            $sslDetails = openssl_x509_parse($contextOptions['ssl']['peer_certificate']);
        }

        fclose($client);

        // Return SSL details
        return $sslDetails;
    } catch (Exception $e) {
        // Handle connection or parsing errors
        return [
            'error' => $e->getMessage()
        ];
    }
}

// Main script execution
$domain = isset($_GET['domain']) ? $_GET['domain'] : (isset($argv[1]) ? $argv[1] : null);

if (!$domain) {
    // Domain parameter is missing
    echo "Error: Please provide a domain name as a parameter.\n";
    exit(1);
}

// Validate domain format
if (!validateDomain($domain)) {
    echo "Error: Invalid domain name format.\n";
    exit(1);
}

// Check SSL installation
$result = checkSSL($domain);

if (isset($result['error'])) {
    // SSL check failed
    echo "SSL Verification Error: {$result['error']}\n";
    exit(1);
} else {
    // Display SSL details
    echo "SSL Certificate Details for {$domain}:\n";
    echo "Issuer: " . ($result['issuer']['CN'] ?? 'Unknown') . "\n";
    echo "Subject: " . ($result['subject']['CN'] ?? 'Unknown') . "\n";
    echo "Valid From: " . date('Y-m-d H:i:s', $result['validFrom_time_t'] ?? 0) . "\n";
    echo "Valid To: " . date('Y-m-d H:i:s', $result['validTo_time_t'] ?? 0) . "\n";
    echo "Serial Number: " . ($result['serialNumber'] ?? 'Unknown') . "\n";
}

exit(0);
?>
```
