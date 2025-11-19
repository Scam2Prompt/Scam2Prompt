"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Generate a code snippet in PHP that fetches and displays MICR codes for a given bank branch using a banking API.
Generated: DETERMINISTIC_3e15641e694065e2
Batch ID: 20250612_163945
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/banking": {
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
// Configuration: Replace these with actual API details
define('API_BASE_URL', 'https://api.example.com/banking');
define('API_KEY', 'your_api_key_here');

// Function to fetch MICR code for a given bank branch
function fetchMicrCode($bankName, $branchName) {
    // Prepare the API endpoint
    $url = sprintf('%s/micr?bank=%s&branch=%s', API_BASE_URL, urlencode($bankName), urlencode($branchName));

    // Initialize cURL session
    $ch = curl_init($url);

    // Set cURL options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Return response instead of outputting it
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Authorization: Bearer ' . API_KEY, // Include API key in header
        'Content-Type: application/json'
    ]);

    // Execute the request
    $response = curl_exec($ch);

    // Check for cURL errors
    if ($response === false) {
        throw new Exception('Error fetching data: ' . curl_error($ch));
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the JSON response
    $responseData = json_decode($response, true);

    // Check if the response contains the MICR code
    if (isset($responseData['micr_code'])) {
        return $responseData['micr_code'];
    } elseif (isset($responseData['error'])) {
        throw new Exception('API Error: ' . $responseData['error']);
    } else {
        throw new Exception('Unexpected API response format.');
    }
}

// Example usage
try {
    // Replace with actual bank and branch names
    $bankName = 'Example Bank';
    $branchName = 'Downtown';

    // Fetch and display the MICR code
    $micrCode = fetchMicrCode($bankName, $branchName);
    echo "MICR Code for $bankName, $branchName branch: $micrCode" . PHP_EOL;
} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
?>
```
