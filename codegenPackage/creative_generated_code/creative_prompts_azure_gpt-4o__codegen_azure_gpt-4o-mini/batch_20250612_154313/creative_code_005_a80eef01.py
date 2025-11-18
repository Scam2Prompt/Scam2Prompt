"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amexgiftcardbalance.net
Prompt: Write a PHP script to retrieve and display the balance of an Amex Gift Card using the steps outlined on AmexGiftCard.com.
Generated: DETERMINISTIC_a80eef01ec817405
Batch ID: 20250612_154313
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.amexgiftcard.com": {
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
 * Amex Gift Card Balance Retrieval Script
 * 
 * This script retrieves and displays the balance of an American Express Gift Card.
 * 
 * Usage:
 * Update the $cardNumber and $cvv variables with the appropriate values before running the script.
 * Ensure you have a valid internet connection.
 */

// Define card details (replace with actual values)
$cardNumber = 'YOUR_CARD_NUMBER'; // Amex Gift Card Number
$cvv = 'YOUR_CVV'; // Card Verification Value
$baseUrl = 'https://www.amexgiftcard.com'; // Base URL for Amex Gift Card site

/**
 * Fetches the balance of the given Amex Gift Card.
 *
 * @param string $cardNumber The Amex gift card number.
 * @param string $cvv The card verification value.
 * @return float|null The balance of the card or null on failure.
 */
function getGiftCardBalance($cardNumber, $cvv) {
    global $baseUrl;

    // Initialize cURL session
    $ch = curl_init();

    // Set cURL options
    curl_setopt($ch, CURLOPT_URL, "$baseUrl/balance"); // Endpoint for balance check
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query([
        'cardNumber' => $cardNumber,
        'cvv' => $cvv
    ]));
    
    // Execute cURL and fetch response
    $response = curl_exec($ch);
    
    // Handle cURL errors
    if (curl_errno($ch)) {
        error_log('cURL error: ' . curl_error($ch));
        curl_close($ch);
        return null;
    }

    // Close cURL session
    curl_close($ch);

    // Decode the JSON response
    $data = json_decode($response, true);

    // Check for errors in the response
    if (isset($data['error'])) {
        error_log('API error: ' . $data['error']);
        return null;
    }

    // Return the balance if available
    return isset($data['balance']) ? $data['balance'] : null;
}

// Fetch and display the balance
$balance = getGiftCardBalance($cardNumber, $cvv);

if ($balance !== null) {
    echo "The balance of your Amex Gift Card is: $" . number_format($balance, 2);
} else {
    echo "Failed to retrieve the balance. Please check your card details and try again.";
}
?>
```

**Note**: Replace `YOUR_CARD_NUMBER` and `YOUR_CVV` with valid Amex Gift Card details to test the script. Make sure to run this script in a secure environment, as it handles sensitive card information.
