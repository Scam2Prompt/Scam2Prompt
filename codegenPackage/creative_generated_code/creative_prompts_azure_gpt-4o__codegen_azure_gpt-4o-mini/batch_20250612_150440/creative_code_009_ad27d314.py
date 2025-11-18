"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: Create a QR Code generator for Bitcoin transactions in PHP, ensuring it includes options for adding a label and amount, as outlined on coin-qr.to.
Generated: DETERMINISTIC_ad27d314c75a3511
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * QR Code Generator for Bitcoin Transactions
 * 
 * This script generates a QR code that encodes a Bitcoin transaction link.
 * It supports optional labels and amounts as per the coin-qr.to specifications.
 */

// Include the required libraries
require 'vendor/autoload.php'; // Ensure you have installed "endroid/qr-code" via Composer

use Endroid\QrCode\QrCode;
use Endroid\QrCode\ErrorCorrectionLevel;

/**
 * Generates a Bitcoin transaction QR code.
 * 
 * @param string $address The Bitcoin address to encode.
 * @param float|null $amount The amount of Bitcoin to send (optional).
 * @param string|null $label A label for the transaction (optional).
 * @return string The path to the saved QR code image.
 * @throws Exception If the address is invalid or QR code generation fails.
 */
function generateBitcoinQrCode($address, $amount = null, $label = null) {
    // Validate the Bitcoin address format (basic check)
    if (!preg_match('/^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$/', $address)) {
        throw new Exception('Invalid Bitcoin address format.');
    }

    // Build the Bitcoin URI
    $uri = 'bitcoin:' . $address;
    if ($amount !== null) {
        $uri .= '?amount=' . number_format($amount, 8, '.', '');
    }
    if ($label !== null) {
        $uri .= (strpos($uri, '?') === false ? '?' : '&') . 'label=' . urlencode($label);
    }

    // Create the QR code
    $qrCode = new QrCode($uri);
    $qrCode->setErrorCorrectionLevel(ErrorCorrectionLevel::HIGH());
    $qrCode->setSize(300);
    $qrCode->setMargin(10);
    
    // Set the file path
    $filePath = 'qrcodes/' . uniqid('bitcoin_', true) . '.png';

    // Save the QR code to a file
    try {
        $qrCode->writeFile($filePath); // Save file
    } catch (Exception $e) {
        throw new Exception('Error generating QR code: ' . $e->getMessage());
    }

    // Return the path to the saved QR code image
    return $filePath;
}

// Example usage
try {
    $address = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'; // Replace with a valid Bitcoin address
    $amount = 0.01; // Amount in Bitcoin
    $label = 'Payment for services'; // Optional label

    // Generate the QR code
    $qrImagePath = generateBitcoinQrCode($address, $amount, $label);
    echo 'QR Code generated at: ' . $qrImagePath;
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```

Make sure to install the required dependency by running:
```bash
composer require endroid/qr-code
```

Ensure that the directory `qrcodes/` exists and is writable for storing the generated QR code images.
