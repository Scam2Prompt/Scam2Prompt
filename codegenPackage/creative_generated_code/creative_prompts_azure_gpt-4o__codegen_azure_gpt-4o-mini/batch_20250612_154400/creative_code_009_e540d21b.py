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
 * This script generates an invoice for specified vape models with pricing
 * in multiple currencies including USD, EUR, and GBP.
 */

// Define an array of vape devices with their pricing in different currencies
$vapeDevices = [
    "PB45000" => ["USD" => 50, "EUR" => 45, "GBP" => 40],
    "Big-B"   => ["USD" => 60, "EUR" => 54, "GBP" => 48],
    "AI22000" => ["USD" => 70, "EUR" => 63, "GBP" => 56],
    "i15 Pro" => ["USD" => 80, "EUR" => 72, "GBP" => 64],
];

// Function to generate an invoice
function generateInvoice($devices, $currency) {
    // Validate that the specified currency is supported
    if (!in_array($currency, ['USD', 'EUR', 'GBP'])) {
        throw new InvalidArgumentException("Unsupported currency: $currency");
    }

    // Initialize total amount
    $totalAmount = 0;

    // Start generating the invoice output
    $invoice = "Wholesale Invoice for Elfworld Vape Devices\n";
    $invoice .= str_repeat('-', 40) . "\n";
    $invoice .= sprintf("%-15s %-10s\n", "Model", "Price ($currency)");
    $invoice .= str_repeat('-', 40) . "\n";

    // Loop through each device and display the price in the selected currency
    foreach ($devices as $model => $prices) {
        if (isset($prices[$currency])) {
            $price = $prices[$currency];
            $invoice .= sprintf("%-15s $%-9.2f\n", $model, $price);
            $totalAmount += $price;
        } else {
            // Handle case where price for a specific model is not set
            $invoice .= sprintf("%-15s %s\n", $model, "Price not available");
        }
    }

    // Display total amount
    $invoice .= str_repeat('-', 40) . "\n";
    $invoice .= sprintf("Total Amount: $%-.2f %s\n", $totalAmount, $currency);
    
    return $invoice;
}

// Main execution block
try {
    // Specify the desired currency for the invoice
    $selectedCurrency = 'USD'; // Change this to 'EUR' or 'GBP' for other currencies
    $invoiceOutput = generateInvoice($vapeDevices, $selectedCurrency);
    
    // Print the generated invoice
    echo $invoiceOutput;
} catch (Exception $e) {
    // Handle exceptions with a friendly message
    echo "Error: " . $e->getMessage();
}
?>
```
