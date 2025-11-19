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
  "https://api.paymentgateway.com/v1/charges": {
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
 * Payment Processing Script for Christening Gowns and Outfits
 * 
 * This script integrates with a payment gateway to process orders. It includes handling for free delivery
 * conditions and ensures secure and efficient transactions.
 * 
 * Author: Your Name
 * Date: YYYY-MM-DD
 */

// Configuration
define('FREE_DELIVERY_THRESHOLD', 100.00); // Free delivery for orders >= $100
define('PAYMENT_GATEWAY_API_URL', 'https://api.paymentgateway.com/v1/charges');
define('PAYMENT_GATEWAY_API_KEY', 'your_api_key_here');

// Helper function to calculate delivery cost
function calculateDeliveryCost($orderTotal) {
    return $orderTotal >= FREE_DELIVERY_THRESHOLD ? 0.00 : 10.00; // Flat $10 delivery fee for orders below $100
}

// Helper function to send a POST request to the payment gateway
function sendPaymentRequest($data) {
    $curl = curl_init(PAYMENT_GATEWAY_API_URL);

    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_HTTPHEADER, [
        'Authorization: Bearer ' . PAYMENT_GATEWAY_API_KEY,
        'Content-Type: application/json'
    ]);
    curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));

    $response = curl_exec($curl);

    if (curl_errno($curl)) {
        throw new Exception('Payment gateway error: ' . curl_error($curl));
    }

    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

    curl_close($curl);

    if ($httpCode !== 200) {
        throw new Exception('Payment gateway returned an error response: ' . $response);
    }

    return json_decode($response, true);
}

// Main script logic
try {
    // Example order data (replace with actual order details from your application)
    $order = [
        'customer_name' => 'Jane Doe',
        'order_total' => 120.00,  // Example order total
        'items' => [
            ['name' => 'White Christening Gown', 'price' => 70.00],
            ['name' => 'Blue Christening Outfit', 'price' => 50.00]
        ]
    ];

    // Calculate delivery cost
    $deliveryCost = calculateDeliveryCost($order['order_total']);
    $finalAmount = $order['order_total'] + $deliveryCost;

    // Prepare payment data
    $paymentData = [
        'amount' => $finalAmount * 100, // Convert to cents (required by most payment gateways)
        'currency' => 'USD',
        'description' => 'Order for christening gowns and outfits',
        'customer' => [
            'name' => $order['customer_name'],
            // Include additional customer details such as email, address, etc.
        ]
    ];

    // Send payment request to the gateway
    $response = sendPaymentRequest($paymentData);

    // Handle successful payment response
    if (isset($response['status']) && $response['status'] === 'success') {
        echo "Payment successful! Transaction ID: " . $response['transaction_id'] . "\n";
        echo "Delivery cost: $" . $deliveryCost . "\n";
        echo "Total amount charged: $" . $finalAmount . "\n";
    } else {
        throw new Exception('Payment failed: ' . $response['message']);
    }

} catch (Exception $e) {
    // Handle exceptions and errors
    echo "Error: " . $e->getMessage() . "\n";
    // Log errors for debugging (optional)
    error_log($e->getMessage());
}
?>
```
