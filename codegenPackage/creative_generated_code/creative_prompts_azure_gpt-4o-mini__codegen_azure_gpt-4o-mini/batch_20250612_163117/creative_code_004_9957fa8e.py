"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hometymex.co.za
Prompt: Construct a PHP script that performs a soft credit check for HomeTyme's pre-approval process without affecting the user's credit score.
Generated: DETERMINISTIC_9957fa8ea80e7480
Batch ID: 20250612_163117
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hometyme.com/soft_credit_check": {
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
 * HomeTyme Soft Credit Check Script
 *
 * This script performs a soft credit check for users applying for pre-approval
 * without affecting their credit score. It utilizes a hypothetical credit check API.
 */

// Define constants for API configuration
define('API_URL', 'https://api.hometyme.com/soft_credit_check');
define('API_KEY', 'your_api_key_here'); // Replace with your actual API key

/**
 * Function to perform a soft credit check
 *
 * @param string $userEmail The email of the user requesting the credit check
 * @param string $userSSN The social security number of the user
 * @return array The response from the credit check API
 * @throws Exception If the API call fails or returns an error
 */
function performSoftCreditCheck($userEmail, $userSSN) {
    // Validate input
    if (empty($userEmail) || empty($userSSN)) {
        throw new InvalidArgumentException('User email and SSN are required.');
    }

    // Prepare the data for the API request
    $data = [
        'email' => $userEmail,
        'ssn' => $userSSN,
        'action' => 'soft_check'
    ];

    // Initialize cURL for API request
    $ch = curl_init(API_URL);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . API_KEY
    ]);

    // Execute the API call
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    // Check for cURL errors
    if (curl_errno($ch)) {
        throw new RuntimeException('cURL error: ' . curl_error($ch));
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the API response
    $responseData = json_decode($response, true);

    // Check for API errors
    if ($httpCode !== 200 || isset($responseData['error'])) {
        throw new RuntimeException('API error: ' . ($responseData['error'] ?? 'Unknown error'));
    }

    return $responseData;
}

// Example usage: Perform a soft credit check
try {
    $email = 'user@example.com'; // Replace with user input
    $ssn = '123-45-6789'; // Replace with user input (ensure you handle this data securely)

    $creditCheckResult = performSoftCreditCheck($email, $ssn);
    echo "Credit check successful. Data: " . json_encode($creditCheckResult);
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . $e->getMessage();
}
?>
```
