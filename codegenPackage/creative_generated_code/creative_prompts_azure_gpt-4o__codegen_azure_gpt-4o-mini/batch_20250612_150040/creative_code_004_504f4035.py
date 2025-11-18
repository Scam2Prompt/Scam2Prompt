"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Write a PHP script that generates a QR code for a USDT wallet address and ensures the QR code works across blockchain formats such as ERC-20, TRC-20, BEP-20, Omni, and BEP-2.
Generated: DETERMINISTIC_504f403569ca69f3
Batch ID: 20250612_150040
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
 * QR Code Generator for a USDT Wallet Address
 *
 * This script generates a QR code for various blockchain formats of USDT
 * including ERC-20, TRC-20, BEP-20, Omni, and BEP-2.
 *
 * Requirements:
 * - PHP GD library for image creation
 * - Composer for QR Code library (e.g., endroid/qr-code)
 */

// Autoload Composer dependencies
require 'vendor/autoload.php';

use Endroid\QrCode\QrCode;
use Endroid\QrCode\ErrorCorrectionLevel;
use Endroid\QrCode\LabelAlignment;

function generateQRCode($address, $blockchain) {
    // Validate the blockchain type
    $validBlockchains = ['ERC20', 'TRC20', 'BEP20', 'Omni', 'BEP2'];
    if (!in_array($blockchain, $validBlockchains)) {
        throw new InvalidArgumentException('Invalid blockchain type provided');
    }

    // Construct the URI based on the blockchain type
    switch ($blockchain) {
        case 'ERC20':
            $uri = "ethereum:$address?amount=0.00&label=USDT"; // Ethereum format
            break;
        case 'TRC20':
            $uri = "tron:$address?amount=0.00&label=USDT"; // Tron format
            break;
        case 'BEP20':
            $uri = "binance:$address?amount=0.00&label=USDT"; // Binance Smart Chain format
            break;
        case 'Omni':
            $uri = "omni:$address?amount=0.00&label=USDT"; // Omni Layer format
            break;
        case 'BEP2':
            $uri = "bep2:$address?amount=0.00&label=USDT"; // BEP2 format
            break;
        default:
            throw new InvalidArgumentException('Invalid blockchain type provided');
    }

    // Generate the QR code
    $qrCode = new QrCode($uri);
    $qrCode->setErrorCorrectionLevel(new ErrorCorrectionLevel(ErrorCorrectionLevel::HIGH));
    $qrCode->setSize(300);
    $qrCode->setMargin(10);

    // Create a unique filename for the QR code
    $filename = 'qrcodes/' . $blockchain . '_USDT_' . md5($address) . '.png';

    // Ensure the directory exists
    if (!is_dir('qrcodes')) {
        mkdir('qrcodes', 0755, true);
    }

    // Save the QR code to a file
    try {
        $qrCode->writeFile($filename);
        return $filename; // Return the path to the generated QR code
    } catch (Exception $e) {
        throw new RuntimeException('Failed to create QR code: ' . $e->getMessage());
    }
}

// Example usage
try {
    $address = 'YourWalletAddressHere'; // Replace with actual wallet address
    $blockchain = 'ERC20'; // Change to desired blockchain type
    $qrCodePath = generateQRCode($address, $blockchain);
    echo "QR Code generated successfully: " . $qrCodePath;
} catch (Exception $e) {
    // Handle any errors that occur during the QR code generation
    echo 'Error: ' . $e->getMessage();
}

?>
```

Make sure to install the required `endroid/qr-code` library via Composer before running this script:
```bash
composer require endroid/qr-code
```
