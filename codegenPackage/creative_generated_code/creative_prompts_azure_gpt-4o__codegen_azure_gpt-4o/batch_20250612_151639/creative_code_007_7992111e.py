"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syneoshealthls.com
Prompt: Create a PHP script to interact with Plesk's API for adding domains to a hosting account, using the steps outlined in Media Temple's documentation.
Generated: DETERMINISTIC_7992111e05932414
Batch ID: 20250612_151639
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443/enterprise/control/agent.php": {
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
 * Plesk API Integration Script
 * Adds a domain to a hosting account using Plesk's API.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - cURL extension enabled
 */

/**
 * Configuration
 */
$pleskUrl = 'https://your-plesk-server:8443/enterprise/control/agent.php'; // Plesk API endpoint
$pleskUsername = 'api-username'; // API username
$pleskPassword = 'api-password'; // API password

/**
 * Function to send a request to Plesk XML API
 * 
 * @param string $requestXml XML formatted request
 * @return string $responseXml XML formatted response
 * @throws Exception
 */
function sendPleskRequest(string $requestXml): string
{
    $curl = curl_init();

    // Set cURL options
    curl_setopt($curl, CURLOPT_URL, $GLOBALS['pleskUrl']);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, $requestXml);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_HTTPHEADER, [
        'Content-Type: text/xml',
        'HTTP_AUTH_LOGIN: ' . $GLOBALS['pleskUsername'],
        'HTTP_AUTH_PASSWD: ' . $GLOBALS['pleskPassword'],
    ]);

    // Execute request
    $response = curl_exec($curl);

    // Error handling
    if ($response === false) {
        $error = curl_error($curl);
        curl_close($curl);
        throw new Exception('cURL error: ' . $error);
    }

    // Close cURL session
    curl_close($curl);

    return $response;
}

/**
 * Add a domain to Plesk
 * 
 * @param string $domainName Domain name to add
 * @param string $ipAddress IP address to bind the domain to
 * @return void
 * @throws Exception
 */
function addDomainToPlesk(string $domainName, string $ipAddress): void
{
    // XML request to add a domain
    $requestXml = <<<XML
<?xml version="1.0" encoding="UTF-8"?>
<packet>
    <webspace>
        <add>
            <gen_setup>
                <name>{$domainName}</name>
                <ip_address>{$ipAddress}</ip_address>
            </gen_setup>
            <hosting>
                <vrt_hst>
                    <property>
                        <name>ftp_login</name>
                        <value>{$domainName}_ftp</value>
                    </property>
                    <property>
                        <name>ftp_password</name>
                        <value>securepassword123</value>
                    </property>
                </vrt_hst>
            </hosting>
        </add>
    </webspace>
</packet>
XML;

    // Send the request
    $responseXml = sendPleskRequest($requestXml);

    // Validate response
    if (strpos($responseXml, '<status>ok</status>') === false) {
        throw new Exception('Failed to add domain: ' . htmlspecialchars($responseXml));
    }

    echo "Domain '{$domainName}' added successfully.\n";
}

/**
 * Main Script Execution
 */
try {
    // Example usage
    addDomainToPlesk('example.com', '192.168.1.1');
} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage();
    exit(1);
}

?>
```
