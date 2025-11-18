"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Write a script in PHP to generate a wholesale invoice for Elfworld vape devices, including models PB45000, Big-B, AI22000, and i15 Pro, with pricing in multiple currencies like USD, EUR, and GBP.
Generated: DETERMINISTIC_e540d21bc2c95d42
Batch ID: 20250612_154400
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
 * Wholesale Invoice Generator for Elfworld Vape Devices
 * 
 * This script generates an invoice for Elfworld vape devices in multiple currencies.
 * Models include: PB45000, Big-B, AI22000, and i15 Pro.
 * Supports pricing in USD, EUR, and GBP.
 * 
 * Author: [Your Name]
 * Version: 1.0
 */

// Define constant pricing for devices in USD
const PRICING_USD = [
    "PB45000" => 50.00,
    "Big-B"   => 35.00,
    "AI22000" => 45.00,
    "i15 Pro" => 25.00
];

// Currency exchange rates (subject to fluctuations; update as needed)
const EXCHANGE_RATES = [
    "USD_TO_EUR" => 0.93, // 1 USD = 0.93 EUR
    "USD_TO_GBP" => 0.82  // 1 USD = 0.82 GBP
];

/**
 * Function to calculate pricing in multiple currencies
 * 
 * @param float $priceUSD Price in USD
 * @return array Pricing in USD, EUR, and GBP
 */
function calculatePricing($priceUSD) {
    return [
        "USD" => number_format($priceUSD, 2),
        "EUR" => number_format($priceUSD * EXCHANGE_RATES["USD_TO_EUR"], 2),
        "GBP" => number_format($priceUSD * EXCHANGE_RATES["USD_TO_GBP"], 2)
    ];
}

/**
 * Function to generate wholesale invoice
 * 
 * @param array $orderDetails Array of ordered models and quantities
 * @return string Formatted invoice
 */
function generateInvoice($orderDetails) {
    $invoice = "---- Wholesale Invoice ----\n";
    $invoice .= "Elfworld Vape Devices\n\n";

    $invoice .= "Model       Quantity  Price (USD)  Price (EUR)  Price (GBP)\n";
    $invoice .= "---------------------------------------------------------\n";
    
    $totalPriceUSD = 0;

    foreach ($orderDetails as $model => $quantity) {
        // Validate model exists in pricing
        if (!isset(PRICING_USD[$model])) {
            return "Error: Model '$model' not found in pricing details.\n";
        }
        
        $priceUSD = PRICING_USD[$model] * $quantity;
        $pricing = calculatePricing($priceUSD);

        $invoice .= sprintf(
            "%-10s %-8d $%-12s €%-11s £%-10s\n",
            $model, $quantity, $pricing["USD"], $pricing["EUR"], $pricing["GBP"]
        );

        $totalPriceUSD += $priceUSD;
    }

    $totalPricing = calculatePricing($totalPriceUSD);
    $invoice .= "---------------------------------------------------------\n";
    $invoice .= sprintf(
        "Total:              $%-12s €%-11s £%-10s\n",
        $totalPricing["USD"], $totalPricing["EUR"], $totalPricing["GBP"]
    );

    return $invoice;
}

/**
 * Example Usage
 */

// Define example order details (model => quantity)
$orderDetails = [
    "PB45000" => 100,
    "Big-B"   => 200,
    "AI22000" => 150,
    "i15 Pro" => 300
];

// Generate the invoice
try {
    $invoice = generateInvoice($orderDetails);
    echo $invoice;
} catch (Exception $e) {
    // Handle any unforeseen errors gracefully
    echo "An error occurred while generating the invoice: " . $e->getMessage();
}
?>
```
