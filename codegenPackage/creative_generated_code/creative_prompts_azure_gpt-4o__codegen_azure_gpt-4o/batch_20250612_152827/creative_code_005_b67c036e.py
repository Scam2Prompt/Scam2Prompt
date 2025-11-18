"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imaginrayones.com
Prompt: Write a PHP script to verify server configuration using Plesk's SSI test page.
Generated: DETERMINISTIC_b67c036e6d0dddb3
Batch ID: 20250612_152827
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-server-ip-or-domain/plesk-stat/test/ssi/test.html": {
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
 * Script to verify server configuration using Plesk's SSI (Server Side Includes) test page.
 * This script fetches the Plesk SSI test page and displays whether the server configuration is correct.
 * 
 * Author: Professional Software Developer
 * Date: YYYY-MM-DD
 */

try {
    // Define the URL for the Plesk SSI test page
    $pleskTestPageUrl = "http://your-server-ip-or-domain/plesk-stat/test/ssi/test.html";

    // Initialize a cURL session
    $curl = curl_init();

    // Set cURL options
    curl_setopt($curl, CURLOPT_URL, $pleskTestPageUrl); // URL to fetch
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);   // Return response as a string
    curl_setopt($curl, CURLOPT_FOLLOWLOCATION, true);   // Follow redirects if necessary
    curl_setopt($curl, CURLOPT_TIMEOUT, 10);            // Set a timeout for the request

    // Execute the cURL request
    $response = curl_exec($curl);

    // Check for cURL errors
    if (curl_errno($curl)) {
        throw new Exception("cURL error: " . curl_error($curl));
    }

    // Get the HTTP response status code
    $httpStatusCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

    // Close the cURL session
    curl_close($curl);

    // Validate the HTTP status code and response content
    if ($httpStatusCode === 200 && strpos($response, "SSI test page") !== false) {
        echo "Server configuration is correct. Successfully fetched the Plesk SSI test page.";
    } else {
        echo "Server configuration error. Unable to verify the Plesk SSI test page.";
    }
} catch (Exception $e) {
    // Handle any exceptions
    echo "An error occurred while verifying server configuration: " . $e->getMessage();
}
?>
```
