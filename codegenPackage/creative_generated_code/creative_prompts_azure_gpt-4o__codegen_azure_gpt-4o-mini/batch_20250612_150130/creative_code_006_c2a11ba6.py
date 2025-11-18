"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masknet.top
Prompt: Write a PHP script to interact with CyberPanel's API for creating new websites and managing DNS records.
Generated: DETERMINISTIC_c2a11ba6a6004a3e
Batch ID: 20250612_150130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-cyberpanel-url.com/api": {
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
 * CyberPanel API Interaction Class.
 *
 * This class provides methods to interact with the CyberPanel API for creating new websites 
 * and managing DNS records.
 */
class CyberPanelAPI
{
    private $apiUrl;
    private $apiKey;

    /**
     * Constructor to initialize API URL and API Key.
     *
     * @param string $apiUrl The base URL for the CyberPanel API.
     * @param string $apiKey Your CyberPanel API key.
     */
    public function __construct($apiUrl, $apiKey)
    {
        $this->apiUrl = rtrim($apiUrl, '/');
        $this->apiKey = $apiKey;
    }

    /**
     * Make a request to the CyberPanel API.
     *
     * @param string $endpoint The API endpoint to call.
     * @param array $data The data to send in the request.
     * @return array The response from the API.
     * @throws Exception If the API request fails.
     */
    public function request($endpoint, $data = [])
    {
        $url = $this->apiUrl . '/' . ltrim($endpoint, '/');
        $data['apiKey'] = $this->apiKey;

        $options = [
            'http' => [
                'header' => "Content-Type: application/json\r\n",
                'method' => 'POST',
                'content' => json_encode($data),
                'ignore_errors' => true,
            ],
        ];

        $context = stream_context_create($options);
        $response = @file_get_contents($url, false, $context);

        if ($response === false) {
            throw new Exception("API request failed: " . $http_response_header[0]);
        }

        return json_decode($response, true);
    }

    /**
     * Create a new website in CyberPanel.
     *
     * @param string $domain The domain name for the new website.
     * @param string $email The owner's email address.
     * @return array The response from the API.
     * @throws Exception If the website creation fails.
     */
    public function createWebsite($domain, $email)
    {
        if (empty($domain) || empty($email)) {
            throw new InvalidArgumentException("Domain and email are required.");
        }

        $data = [
            'domain' => $domain,
            'email' => $email,
        ];

        return $this->request('/createWebsite', $data);
    }

    /**
     * Create a DNS record for a domain.
     *
     * @param string $domain The domain for which to create the DNS record.
     * @param string $type The type of DNS record (A, CNAME, etc.).
     * @param string $value The value of the DNS record.
     * @param int $ttl Optional time-to-live for the DNS record.
     * @return array The response from the API.
     * @throws Exception If the DNS record creation fails.
     */
    public function createDNSRecord($domain, $type, $value, $ttl = 3600)
    {
        if (empty($domain) || empty($type) || empty($value)) {
            throw new InvalidArgumentException("Domain, type, and value are required.");
        }

        $data = [
            'domain' => $domain,
            'type' => $type,
            'value' => $value,
            'ttl' => $ttl,
        ];

        return $this->request('/createDNSRecord', $data);
    }
}

// Example usage:
try {
    $apiUrl = "https://your-cyberpanel-url.com/api";
    $apiKey = "your-api-key";

    $cyberPanel = new CyberPanelAPI($apiUrl, $apiKey);

    // Create a new website
    $websiteResponse = $cyberPanel->createWebsite('example.com', 'admin@example.com');
    print_r($websiteResponse);

    // Create a DNS record
    $dnsResponse = $cyberPanel->createDNSRecord('example.com', 'A', '192.0.2.1');
    print_r($dnsResponse);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

Make sure to replace `your-cyberpanel-url.com` and `your-api-key` with your actual CyberPanel API URL and API key before running the script.
