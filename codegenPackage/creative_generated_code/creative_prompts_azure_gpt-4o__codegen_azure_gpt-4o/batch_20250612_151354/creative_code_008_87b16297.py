"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Develop a PHP script to integrate payment processing for annual membership fees (e.g., S/195) as outlined in the Enacip website's pricing model.
Generated: DETERMINISTIC_87b1629742193764
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// payment_processor.php

/**
 * Payment Processing Script for Annual Membership Fees
 * This script integrates payment processing for annual membership fees (S/195).
 * It uses a hypothetical payment gateway API for demonstration purposes.
 * 
 * Ensure you configure the API credentials and other parameters appropriately.
 */

// Load necessary configurations
require_once 'config.php'; // Contains payment gateway credentials and configurations

/**
 * Process Payment for Annual Membership Fee
 *
 * @param string $name Full name of the payer
 * @param string $email Email address of the payer
 * @param string $cardNumber Credit card number
 * @param string $expiryDate Credit card expiry date (MM/YY)
 * @param string $cvv Credit card CVV code
 * @return array Response containing payment result and message
 */
function processMembershipFee($name, $email, $cardNumber, $expiryDate, $cvv) {
    // Define the membership fee
    $membershipFee = 195.00; // S/195 in PEN currency
    
    // Validate inputs
    if (empty($name) || empty($email) || empty($cardNumber) || empty($expiryDate) || empty($cvv)) {
        return [
            'success' => false,
            'message' => 'All fields are required.'
        ];
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return [
            'success' => false,
            'message' => 'Invalid email address.'
        ];
    }

    // Simulate a payment gateway API request
    $paymentGatewayUrl = PAYMENT_GATEWAY_URL; // URL of the payment gateway
    $apiKey = PAYMENT_GATEWAY_API_KEY; // API key for authentication
    
    // Prepare payment data
    $paymentData = [
        'amount' => $membershipFee,
        'currency' => 'PEN',
        'payer_name' => $name,
        'payer_email' => $email,
        'card_number' => $cardNumber,
        'card_expiry' => $expiryDate,
        'card_cvv' => $cvv,
    ];

    // Use cURL for API call
    $ch = curl_init($paymentGatewayUrl);

    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($paymentData));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . $apiKey
    ]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    // Handle API response
    if ($httpCode === 200) { // HTTP 200 indicates success
        $responseData = json_decode($response, true);
        if ($responseData['status'] === 'success') {
            return [
                'success' => true,
                'message' => 'Payment processed successfully.'
            ];
        } else {
            return [
                'success' => false,
                'message' => 'Payment failed: ' . $responseData['message']
            ];
        }
    } else {
        return [
            'success' => false,
            'message' => 'Error processing payment. HTTP Code: ' . $httpCode
        ];
    }
}

// Example Usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = htmlspecialchars($_POST['name'] ?? '');
    $email = htmlspecialchars($_POST['email'] ?? '');
    $cardNumber = htmlspecialchars($_POST['card_number'] ?? '');
    $expiryDate = htmlspecialchars($_POST['expiry_date'] ?? '');
    $cvv = htmlspecialchars($_POST['cvv'] ?? '');

    $result = processMembershipFee($name, $email, $cardNumber, $expiryDate, $cvv);

    header('Content-Type: application/json');
    echo json_encode($result);
    exit();
}
?>
```
