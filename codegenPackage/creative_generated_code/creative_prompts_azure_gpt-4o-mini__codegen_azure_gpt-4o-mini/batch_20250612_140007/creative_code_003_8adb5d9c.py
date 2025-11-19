"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorgeouschristeninggowns.com.au
Prompt: Develop a PHP script that integrates with a payment gateway to process orders for christening gowns and outfits, ensuring free delivery conditions are met.
Generated: DETERMINISTIC_8adb5d9cc0a0c1f7
Batch ID: 20250612_140007
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.paymentgateway.com/process": {
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
// Payment Gateway Integration for Processing Orders of Christening Gowns and Outfits

// Include required libraries (e.g., for the payment gateway)
// require 'vendor/autoload.php'; // Uncomment if using Composer for libraries

/**
 * Configurations for the payment gateway
 */
define('PAYMENT_GATEWAY_URL', 'https://api.paymentgateway.com/process');
define('API_KEY', 'your_api_key_here'); // Your payment gateway API key
define('FREE_DELIVERY_THRESHOLD', 100.00); // Minimum order amount for free delivery

/**
 * Function to process the order payment
 *
 * @param float $orderAmount The total amount of the order
 * @param string $paymentMethod The payment method chosen by the user
 * @return array Response from the payment gateway
 * @throws Exception If payment processing fails
 */
function processPayment(float $orderAmount, string $paymentMethod): array {
    // Validate order amount
    if ($orderAmount <= 0) {
        throw new Exception('Invalid order amount. Must be greater than zero.');
    }

    // Prepare payment data
    $paymentData = [
        'amount' => $orderAmount,
        'currency' => 'USD',
        'payment_method' => $paymentMethod,
        'api_key' => API_KEY
    ];

    // Initialize cURL session
    $ch = curl_init(PAYMENT_GATEWAY_URL);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($paymentData));

    // Execute payment request
    $response = curl_exec($ch);

    // Check for cURL errors
    if ($response === false) {
        curl_close($ch);
        throw new Exception('Payment processing failed: ' . curl_error($ch));
    }

    // Close cURL session
    curl_close($ch);

    // Decode JSON response
    $responseData = json_decode($response, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new Exception('Failed to decode payment gateway response.');
    }

    return $responseData;
}

/**
 * Function to calculate delivery charges based on order amount
 *
 * @param float $orderAmount The total amount of the order
 * @return float Delivery charges
 */
function calculateDeliveryCharges(float $orderAmount): float {
    return $orderAmount >= FREE_DELIVERY_THRESHOLD ? 0.00 : 10.00; // Fixed delivery charge of $10.00
}

// Example usage
try {
    // Simulate order amount and payment method
    $orderAmount = 120.00; // Get the total amount from the order details
    $paymentMethod = 'credit_card'; // Example payment method

    // Process payment
    $paymentResponse = processPayment($orderAmount, $paymentMethod);
    
    // Check payment response status
    if ($paymentResponse['status'] === 'success') {
        // Calculate delivery charges
        $deliveryCharges = calculateDeliveryCharges($orderAmount);
        
        // Process successful order (e.g., save to database, send confirmation)
        echo "Payment successful! Delivery Charges: $" . number_format($deliveryCharges, 2);
    } else {
        echo "Payment failed: " . $paymentResponse['message'];
    }
} catch (Exception $e) {
    // Handle exceptions and log errors
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage();
}
?>
```
