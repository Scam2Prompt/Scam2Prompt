"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omidtak.ir
Prompt: Create a PHP code snippet for connecting to the Saman Kish payment gateway using a token, as explained in the Omidtak tutorial.
Generated: DETERMINISTIC_e701676cbd656ad0
Batch ID: 20250612_163625
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://yourwebsite.com/callback": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.samanbank.ir/payment": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://omidtak.com/tutorials/saman-kish": {
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
 * Saman Kish Payment Gateway Connection
 * This script connects to the Saman Kish payment gateway using a token.
 * 
 * @link https://omidtak.com/tutorials/saman-kish
 */

class SamanKishPaymentGateway
{
    private $apiUrl = 'https://api.samanbank.ir/payment'; // Base URL for the payment gateway
    private $token; // Authentication token

    /**
     * Constructor to initialize the API token.
     *
     * @param string $token The token for authentication.
     */
    public function __construct($token)
    {
        $this->token = $token;
    }

    /**
     * Initiates the payment process.
     *
     * @param array $paymentData Payment data such as amount, order ID, etc.
     * @return array Response from the payment gateway.
     * @throws Exception If the request fails or the response is invalid.
     */
    public function initiatePayment(array $paymentData)
    {
        // Prepare the request payload
        $payload = json_encode($paymentData);

        // Initialize cURL session
        $ch = curl_init($this->apiUrl . '/initiate');

        // Set cURL options
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Content-Type: application/json',
            'Authorization: Bearer ' . $this->token,
        ]);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);

        // Execute the cURL request
        $response = curl_exec($ch);

        // Handle cURL errors
        if (curl_errno($ch)) {
            throw new Exception('cURL Error: ' . curl_error($ch));
        }

        // Close cURL session
        curl_close($ch);

        // Decode response
        $responseData = json_decode($response, true);

        // Check for valid response
        if (json_last_error() !== JSON_ERROR_NONE || !isset($responseData['success'])) {
            throw new Exception('Invalid response from payment gateway.');
        }

        return $responseData;
    }
}

// Usage example
try {
    $token = 'your_api_token_here'; // Replace with your actual token
    $paymentGateway = new SamanKishPaymentGateway($token);

    $paymentData = [
        'amount' => 100000, // Amount in the smallest currency unit (e.g., Rials)
        'order_id' => '123456', // Unique order ID
        'callback_url' => 'https://yourwebsite.com/callback', // Callback URL after payment
    ];

    $response = $paymentGateway->initiatePayment($paymentData);
    print_r($response); // Handle the response as needed

} catch (Exception $e) {
    // Handle exceptions (e.g., log error, notify user)
    echo 'Error: ' . $e->getMessage();
}
```
