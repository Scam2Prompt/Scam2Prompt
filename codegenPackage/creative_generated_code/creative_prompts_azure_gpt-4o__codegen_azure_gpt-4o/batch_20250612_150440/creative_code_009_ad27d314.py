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

// Import the Composer autoload file (make sure to install phpqrcode via Composer before running: composer require chillerlan/php-qrcode)
require_once 'vendor/autoload.php';

use chillerlan\QRCode\QRCode;
use chillerlan\QRCode\QROptions;

/**
 * Generates a QR Code for a Bitcoin transaction.
 * Includes optional parameters for label and amount.
 *
 * @param string $bitcoinAddress The recipient's Bitcoin address
 * @param float|null $amount The amount to send (optional)
 * @param string|null $label A label for the transaction (optional)
 * @return string The path to the generated QR Code image
 * @throws Exception If any validation fails
 */
function generateBitcoinQrCode(string $bitcoinAddress, ?float $amount = null, ?string $label = null): string
{
    // Validate Bitcoin address (basic validation for demonstration purposes)
    if (empty($bitcoinAddress) || !preg_match('/^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$/', $bitcoinAddress)) {
        throw new Exception('Invalid Bitcoin address.');
    }

    // Build the Bitcoin URI
    $bitcoinUri = 'bitcoin:' . $bitcoinAddress;

    // Add optional parameters to the URI
    $queryParams = [];
    if ($amount !== null) {
        if ($amount <= 0) {
            throw new Exception('Amount must be greater than 0.');
        }
        // Format the amount to 8 decimal places (Bitcoin standard)
        $queryParams['amount'] = number_format($amount, 8, '.', '');
    }
    if ($label !== null) {
        $queryParams['label'] = urlencode($label);
    }

    if (!empty($queryParams)) {
        $bitcoinUri .= '?' . http_build_query($queryParams);
    }

    // Set QR Code options
    $options = new QROptions([
        'version'    => 5, // QR Code version
        'outputType' => QRCode::OUTPUT_IMAGE_PNG, // Output format
        'eccLevel'   => QRCode::ECC_L, // Error correction level
        'scale'      => 5, // Size of each pixel
    ]);

    // Generate the QR Code
    $qrcode = new QRCode($options);

    // Define the output file path
    $outputFile = __DIR__ . '/bitcoin_qr_' . time() . '.png';

    // Save the QR Code as an image file
    $qrcode->render($bitcoinUri, $outputFile);

    // Return the output file path
    return $outputFile;
}

// Example usage
try {
    $bitcoinAddress = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'; // Replace with a valid Bitcoin address
    $amount = 0.05; // Optional amount in BTC
    $label = 'Donation'; // Optional label

    $qrCodePath = generateBitcoinQrCode($bitcoinAddress, $amount, $label);
    echo "QR Code generated successfully! View it here: $qrCodePath" . PHP_EOL;
} catch (Exception $e) {
    // Error handling
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
?>
```

### Notes:
1. Before running this code, install the `phpqrcode` library with Composer: `composer require chillerlan/php-qrcode`.
2. Ensure your server has write permissions for the directory where the QR Code image will be saved.
3. This script performs simple validation for the Bitcoin address. For production, consider using a library for full Bitcoin address validation if needed.
