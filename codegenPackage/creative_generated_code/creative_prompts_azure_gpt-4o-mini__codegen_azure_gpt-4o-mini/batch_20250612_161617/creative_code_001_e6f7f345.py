"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imaginrayones.com
Prompt: Write a PHP script that utilizes Plesk's features for managing DNS settings.
Generated: DETERMINISTIC_e6f7f34510dc05ba
Batch ID: 20250612_161617
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443": {
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
 * PHP script to manage DNS settings using Plesk API.
 *
 * This script demonstrates how to add, update, and delete DNS records
 * using Plesk's API. Ensure that the Plesk API is enabled and accessible.
 */

// Plesk API configuration
define('PLESK_HOST', 'https://your-plesk-server:8443'); // Replace with your Plesk server URL
define('PLESK_USERNAME', 'your-username'); // Replace with your Plesk username
define('PLESK_PASSWORD', 'your-password'); // Replace with your Plesk password

/**
 * Makes a request to the Plesk API.
 *
 * @param string $method The HTTP method (GET, POST, etc.)
 * @param string $endpoint The API endpoint to hit
 * @param array|null $data Optional data to send with the request
 * @return array|null The response from the API or null on failure
 * @throws Exception if the request fails or if the response is invalid
 */
function pleskApiRequest($method, $endpoint, $data = null)
{
    $url = PLESK_HOST . $endpoint;
    $options = [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPAUTH => CURLAUTH_BASIC,
        CURLOPT_USERPWD => PLESK_USERNAME . ':' . PLESK_PASSWORD,
        CURLOPT_SSL_VERIFYPEER => false, // Disable SSL verification for local testing
        CURLOPT_TIMEOUT => 30,
    ];

    switch (strtoupper($method)) {
        case 'POST':
            $options[CURLOPT_POST] = true;
            if ($data) {
                $options[CURLOPT_POSTFIELDS] = $data;
                $options[CURLOPT_HTTPHEADER] = ['Content-Type: application/xml'];
            }
            break;
        case 'GET':
            // No additional options needed for GET
            break;
        default:
            throw new Exception("Unsupported HTTP method: $method");
    }

    $ch = curl_init();
    curl_setopt_array($ch, $options);
    $response = curl_exec($ch);

    if ($response === false) {
        throw new Exception('Curl error: ' . curl_error($ch));
    }

    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode !== 200) {
        throw new Exception("API request failed with HTTP code: $httpCode. Response: $response");
    }

    return simplexml_load_string($response);
}

/**
 * Adds a DNS record.
 *
 * @param string $domain The domain for which to add the record
 * @param string $type The type of DNS record (e.g., A, CNAME)
 * @param string $host The hostname for the record
 * @param string $value The value for the record
 * @param int $ttl The time-to-live for the record
 * @return void
 * @throws Exception if the API request fails
 */
function addDnsRecord($domain, $type, $host, $value, $ttl = 3600)
{
    $xmlData = <<<XML
<packet>
    <dns>
        <add>
            <domain>$domain</domain>
            <type>$type</type>
            <host>$host</host>
            <value>$value</value>
            <ttl>$ttl</ttl>
        </add>
    </dns>
</packet>
XML;

    pleskApiRequest('POST', '/api/v2/dns', $xmlData);
}

/**
 * Updates an existing DNS record.
 *
 * @param int $recordId The ID of the DNS record to update
 * @param string $type The type of DNS record (e.g., A, CNAME)
 * @param string $host The hostname for the record
 * @param string $value The new value for the record
 * @param int $ttl The time-to-live for the record
 * @return void
 * @throws Exception if the API request fails
 */
function updateDnsRecord($recordId, $type, $host, $value, $ttl = 3600)
{
    $xmlData = <<<XML
<packet>
    <dns>
        <update>
            <id>$recordId</id>
            <type>$type</type>
            <host>$host</host>
            <value>$value</value>
            <ttl>$ttl</ttl>
        </update>
    </dns>
</packet>
XML;

    pleskApiRequest('POST', '/api/v2/dns', $xmlData);
}

/**
 * Deletes a DNS record.
 *
 * @param int $recordId The ID of the DNS record to delete
 * @return void
 * @throws Exception if the API request fails
 */
function deleteDnsRecord($recordId)
{
    $xmlData = <<<XML
<packet>
    <dns>
        <delete>
            <id>$recordId</id>
        </delete>
    </dns>
</packet>
XML;

    pleskApiRequest('POST', '/api/v2/dns', $xmlData);
}

// Example usage:

try {
    // Add a new DNS record
    addDnsRecord('example.com', 'A', 'www', '192.0.2.1');

    // Update the DNS record
    updateDnsRecord(1, 'A', 'www', '192.0.2.2'); // Replace 1 with the actual record ID

    // Delete the DNS record
    deleteDnsRecord(1); // Replace 1 with the actual record ID
} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage();
}
?>
```
