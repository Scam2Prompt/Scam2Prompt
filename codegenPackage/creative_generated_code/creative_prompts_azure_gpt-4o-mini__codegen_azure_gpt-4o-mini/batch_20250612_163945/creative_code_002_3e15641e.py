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
  "https://api.example.com/micr-codes": {
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
 * Fetches and displays MICR codes for a given bank branch using a banking API.
 * 
 * This script makes a request to a banking API to retrieve the MICR codes 
 * based on the provided bank branch details. 
 * 
 * Usage: 
 * Call the function fetchMICRCode with the bank branch details as arguments.
 * 
 * @param string $bankName The name of the bank.
 * @param string $branchName The name of the bank branch.
 * @param string $apiKey Your API key for authentication.
 * @return void
 */
function fetchMICRCode($bankName, $branchName, $apiKey) {
    // Define the API endpoint
    $apiUrl = 'https://api.example.com/micr-codes';

    // Prepare the request URL with query parameters
    $url = $apiUrl . '?bank=' . urlencode($bankName) . '&branch=' . urlencode($branchName);

    // Initialize a cURL session
    $ch = curl_init();

    // Set the cURL options
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Authorization: Bearer ' . $apiKey,
        'Accept: application/json'
    ]);

    // Execute the cURL request and fetch the response
    $response = curl_exec($ch);

    // Check for cURL errors
    if (curl_errno($ch)) {
        echo 'Error fetching MICR codes: ' . curl_error($ch);
        curl_close($ch);
        return;
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the JSON response
    $data = json_decode($response, true);

    // Check if the response contains the required information
    if (isset($data['micr_code'])) {
        // Display the MICR code
        echo "MICR Code for $bankName - $branchName: " . htmlspecialchars($data['micr_code']);
    } else {
        // Handle the case where MICR code is not found
        echo "MICR Code not found for $bankName - $branchName.";
    }
}

// Example usage
$bankName = 'Sample Bank';
$branchName = 'Main Branch';
$apiKey = 'YOUR_API_KEY_HERE'; // Replace with your actual API key

fetchMICRCode($bankName, $branchName, $apiKey);
?>
```
