"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://barbudogrowler.cl
Prompt: Provide example code in PHP for integrating a WhatsApp API to enable customer inquiries directly from the "Barbudo Growler" website. Include functionality for sending automated responses based on predefined queries.
Generated: DETERMINISTIC_51a9dcf39aa20b5a
Batch ID: 20250612_152321
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.whatsapp.com/send": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://barbudo-growler.com/menu": {
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
// WhatsApp API Integration for "Barbudo Growler" Website
// This script handles customer inquiries and sends automated responses based on predefined queries.

// Load Composer's autoloader (if using external libraries)
require 'vendor/autoload.php';

// Configuration for WhatsApp API
define('WHATSAPP_API_URL', 'https://api.whatsapp.com/send');
define('WHATSAPP_API_TOKEN', 'your_api_token_here'); // Replace with actual token
define('BUSINESS_PHONE_NUMBER', '1234567890'); // Replace with your business phone number

// Predefined queries and responses
$automatedResponses = [
    'hours' => 'Our business hours are from 12 PM to 10 PM, Monday through Saturday.',
    'location' => 'We are located at 123 Brew Street, Beer City.',
    'menu' => 'Visit our website at https://barbudo-growler.com/menu to see our menu.',
    'default' => 'Thank you for reaching out to Barbudo Growler! Please provide more details about your inquiry.',
];

/**
 * Sends a response to the customer via WhatsApp API.
 *
 * @param string $customerNumber Customer's phone number in international format.
 * @param string $message Message to be sent.
 * @return void
 */
function sendWhatsAppMessage($customerNumber, $message)
{
    $payload = [
        'to' => $customerNumber,
        'type' => 'text',
        'text' => ['body' => $message],
    ];

    $headers = [
        'Authorization: Bearer ' . WHATSAPP_API_TOKEN,
        'Content-Type: application/json',
    ];

    // Initialize CURL
    $ch = curl_init(WHATSAPP_API_URL);

    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    curl_close($ch);

    // Error handling
    if ($httpCode !== 200) {
        error_log('Failed to send WhatsApp message. Response: ' . $response);
    }
}

/**
 * Handles incoming customer queries and sends appropriate responses.
 *
 * @param string $customerNumber Customer's phone number.
 * @param string $query The customer's query.
 * @return void
 */
function handleCustomerInquiry($customerNumber, $query)
{
    global $automatedResponses;

    // Match predefined queries to responses
    $responseMessage = $automatedResponses[strtolower($query)] ?? $automatedResponses['default'];

    // Send the response message
    sendWhatsAppMessage($customerNumber, $responseMessage);
}

// Example usage (replace with actual request handling logic)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $customerNumber = $_POST['customer_number'] ?? null; // Customer's phone number
    $query = $_POST['query'] ?? ''; // Customer's query

    if (!empty($customerNumber) && !empty($query)) {
        handleCustomerInquiry($customerNumber, $query);
    } else {
        error_log('Invalid customer inquiry data.');
    }
}
?>
```
