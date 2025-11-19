"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Write a code snippet in PHP to integrate a payment gateway with an e-commerce platform for a menuiserie distribution company, handling transactions for products like volets roulants and portails."
Generated: DETERMINISTIC_854135dc0c3ba4cc
Batch ID: 20250622_205436
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paymentgateway.com/v1/transactions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
// Payment Gateway Integration for Menuiserie Distribution Company

// Configuration for the payment gateway
define('PAYMENT_GATEWAY_URL', 'https://api.paymentgateway.com/v1/transactions');
define('API_KEY', 'your_api_key_here'); // Replace with your actual API key

/**
 * Function to process payment
 *
 * @param string $orderId The unique order ID
 * @param float $amount The transaction amount
 * @param string $currency The currency code (e.g., 'EUR')
 * @param string $customerEmail The customer's email address
 * @return array Response from the payment gateway
 */
function processPayment($orderId, $amount, $currency, $customerEmail) {
    // Prepare the payload for the payment gateway
    $payload = [
        'order_id' => $orderId,
        'amount' => $amount,
        'currency' => $currency,
        'customer_email' => $customerEmail
    ];

    // Initialize cURL session
    $ch = curl_init(PAYMENT_GATEWAY_URL);

    // Set cURL options
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . API_KEY
    ]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    // Execute the request
    $response = curl_exec($ch);

    // Check for cURL errors
    if (curl_errno($ch)) {
        $errorMessage = curl_error($ch);
        curl_close($ch);
        return [
            'success' => false,
            'message' => 'Payment processing failed: ' . $errorMessage
        ];
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the response
    $decodedResponse = json_decode($response, true);

    // Handle response errors
    if (isset($decodedResponse['error'])) {
        return [
            'success' => false,
            'message' => 'Payment processing failed: ' . $decodedResponse['error']['message']
        ];
    }

    // Return the successful response
    return [
        'success' => true,
        'data' => $decodedResponse
    ];
}

// Example usage
$orderId = 'ORDER12345';
$amount = 150.00; // Example amount for volets roulants or portails
$currency = 'EUR';
$customerEmail = 'customer@example.com';

$result = processPayment($orderId, $amount, $currency, $customerEmail);

if ($result['success']) {
    // Payment successful
    echo "Payment processed successfully. Transaction details:\n";
    print_r($result['data']);
} else {
    // Payment failed
    echo "Error: " . $result['message'] . "\n";
}
?>
```
