"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geteasycrypto.com
Prompt: Create a PHP script to query the WHOIS server (e.g., `http://whois.domaintools.com`) and retrieve domain owner information, as mentioned in the CentOS-WebPanel test page.
Generated: DETERMINISTIC_7955f9dccae6b93d
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://whois.domaintools.com/": {
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
 * A PHP script to query the WHOIS server and retrieve domain owner information.
 *
 * This script sends a request to the WHOIS server and parses the response
 * to extract relevant owner information for a given domain.
 *
 * @package WhoisQuery
 */

function fetchWhoisData($domain) {
    // Validate the domain format
    if (!filter_var($domain, FILTER_VALIDATE_DOMAIN, FILTER_FLAG_HOSTNAME)) {
        throw new InvalidArgumentException("Invalid domain name provided.");
    }

    // WHOIS server URL
    $whoisServer = 'https://whois.domaintools.com/';

    // Initialize a cURL session
    $ch = curl_init();

    // Set the cURL options
    curl_setopt($ch, CURLOPT_URL, $whoisServer . urlencode($domain));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, 10); // Set timeout to 10 seconds

    // Execute the cURL request
    $response = curl_exec($ch);

    // Check for cURL errors
    if ($response === false) {
        $errorMessage = curl_error($ch);
        curl_close($ch);
        throw new RuntimeException("cURL error while fetching WHOIS data: $errorMessage");
    }

    // Close the cURL session
    curl_close($ch);

    return $response;
}

function parseWhoisData($data) {
    // Initialize an array to hold the owner information
    $ownerInfo = [];

    // Use a regular expression to extract relevant information
    preg_match('/Registrant Name:\s*(.*)/i', $data, $nameMatches);
    preg_match('/Registrant Organization:\s*(.*)/i', $data, $orgMatches);
    preg_match('/Registrant Country:\s*(.*)/i', $data, $countryMatches);

    // Store the extracted information in the array
    $ownerInfo['name'] = $nameMatches[1] ?? 'N/A';
    $ownerInfo['organization'] = $orgMatches[1] ?? 'N/A';
    $ownerInfo['country'] = $countryMatches[1] ?? 'N/A';

    return $ownerInfo;
}

// Main execution block
try {
    // Define the domain to query
    $domain = 'example.com'; // Replace with the desired domain
    $whoisData = fetchWhoisData($domain);
    $ownerInfo = parseWhoisData($whoisData);

    // Output the owner information
    echo "Owner Information for domain: $domain\n";
    echo "Name: " . $ownerInfo['name'] . "\n";
    echo "Organization: " . $ownerInfo['organization'] . "\n";
    echo "Country: " . $ownerInfo['country'] . "\n";

} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
