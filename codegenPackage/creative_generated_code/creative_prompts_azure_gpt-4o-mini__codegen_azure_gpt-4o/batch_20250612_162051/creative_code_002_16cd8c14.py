"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahlrentacar.com.tr
Prompt: Can you provide a code snippet that demonstrates how to handle SSL certificate verification in cURL requests?
Generated: DETERMINISTIC_16cd8c14a4a1cc80
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/endpoint": {
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
 * Making an HTTPS request using cURL with SSL certificate verification enabled.
 * Ensures proper handling of SSL certificates to prevent MITM attacks.
 */

// URL to request
$url = 'https://example.com/api/endpoint';

// Path to your trusted CA certificate bundle file (usually provided by your system or server)
$caCertificatePath = '/path/to/cacert.pem';

try {
    // Initialize cURL session
    $ch = curl_init();

    if ($ch === false) {
        throw new Exception('Failed to initialize cURL.');
    }

    // Set cURL options
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Return response as a string
    curl_setopt($ch, CURLOPT_TIMEOUT, 30);         // Set timeout for the request

    // Enable SSL certificate verification
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true); // Verify the peer's SSL certificate
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);    // Verify the hostname matches the certificate
    curl_setopt($ch, CURLOPT_CAINFO, $caCertificatePath); // Specify the path to the certificate bundle

    // Execute the cURL request
    $response = curl_exec($ch);

    // Check if an error occurred
    if ($response === false) {
        $errorMessage = curl_error($ch);
        curl_close($ch); // Clean up on error
        throw new Exception("cURL Error: $errorMessage");
    }

    // Get HTTP status code
    $httpStatusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Close the cURL session
    curl_close($ch);

    // Check HTTP status code for success (200 OK)
    if ($httpStatusCode !== 200) {
        throw new Exception("Request failed with HTTP status code $httpStatusCode.");
    }

    // Print response (or handle it as needed)
    echo "Response:\n$response";

} catch (Exception $e) {
    // Handle exceptions
    echo "Error: " . $e->getMessage();
}
?>
```
