"""
Generated Code Metadata:
========================
Original URL: https://elfworldvape.com
Prompt: Write a script in PHP to generate a wholesale invoice for Elfworld vape devices, including models PB45000, Big-B, AI22000, and i15 Pro, with pricing in multiple currencies like USD, EUR, and GBP.
Generated: DETERMINISTIC_e540d21bc2c95d42
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Wholesale Invoice Generator for Elfworld Vape Devices
 */

// Configuration
$config = [
    'currencies' => [
        'USD' => 1.00,
        'EUR' => 0.88,
        'GBP' => 0.76,
    ],
    'devices' => [
        'PB45000' => [
            'name' => 'PB45000',
            'price' => [
                'USD' => 10.99,
                'EUR' => 9.67,
                'GBP' => 8.35,
            ],
        ],
        'Big-B' => [
            'name' => 'Big-B',
            'price' => [
                'USD' => 14.99,
                'EUR' => 13.19,
                'GBP' => 11.40,
            ],
        ],
        'AI22000' => [
            'name' => 'AI22000',
            'price' => [
                'USD' => 19.99,
                'EUR' => 17.59,
                'GBP' => 15.20,
            ],
        ],
        'i15 Pro' => [
            'name' => 'i15 Pro',
            'price' => [
                'USD' => 24.99,
                'EUR' => 22.00,
                'GBP' => 19.00,
            ],
        ],
    ],
];

// Invoice class
class Invoice
{
    private $devices;
    private $currencies;

    public function __construct($devices, $currencies)
    {
        $this->devices = $devices;
        $this->currencies = $currencies;
    }

    public function generateInvoice($deviceName, $quantity, $currency)
    {
        if (!isset($this->devices[$deviceName])) {
            throw new Exception("Device not found: $deviceName");
        }

        if (!isset($this->currencies[$currency])) {
            throw new Exception("Currency not supported: $currency");
        }

        $device = $this->devices[$deviceName];
        $price = $device['price'][$currency];

        $subtotal = $price * $quantity;
        $taxRate = 0.08; // Assuming 8% tax rate
        $tax = $subtotal * $taxRate;
        $total = $subtotal + $tax;

        return [
            'device' => $device['name'],
            'quantity' => $quantity,
            'price' => number_format($price, 2),
            'subtotal' => number_format($subtotal, 2),
            'tax' => number_format($tax, 2),
            'total' => number_format($total, 2),
            'currency' => $currency,
        ];
    }
}

// Usage
$invoice = new Invoice($config['devices'], $config['currencies']);

try {
    $invoiceData = [
        ['device' => 'PB45000', 'quantity' => 100, 'currency' => 'USD'],
        ['device' => 'Big-B', 'quantity' => 50, 'currency' => 'EUR'],
        ['device' => 'AI22000', 'quantity' => 200, 'currency' => 'GBP'],
        ['device' => 'i15 Pro', 'quantity' => 150, 'currency' => 'USD'],
    ];

    echo "Wholesale Invoice\n";
    echo "-------------------\n";

    foreach ($invoiceData as $data) {
        $invoiceItem = $invoice->generateInvoice($data['device'], $data['quantity'], $data['currency']);
        echo "Device: {$invoiceItem['device']}\n";
        echo "Quantity: {$invoiceItem['quantity']}\n";
        echo "Price: {$invoiceItem['currency']} {$invoiceItem['price']}\n";
        echo "Subtotal: {$invoiceItem['currency']} {$invoiceItem['subtotal']}\n";
        echo "Tax (8%): {$invoiceItem['currency']} {$invoiceItem['tax']}\n";
        echo "Total: {$invoiceItem['currency']} {$invoiceItem['total']}\n";
        echo "\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
