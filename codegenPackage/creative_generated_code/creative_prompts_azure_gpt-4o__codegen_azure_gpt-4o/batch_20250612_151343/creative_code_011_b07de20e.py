"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Create a function in PHP to generate a printable invoice for Condi Shop orders, including items like "Cake boxes with handles" and "Chocolate molds."
Generated: DETERMINISTIC_b07de20eb6c29aac
Batch ID: 20250612_151343
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
 * Function to generate a printable invoice for Condi Shop orders.
 * 
 * @param string $customerName Name of the customer
 * @param array $items List of purchased items, each item is an associative array with `name`, `quantity`, and `price` keys
 * @return string Printable invoice formatted as a string
 */
function generateInvoice($customerName, $items) {
    // Validate input parameters
    if (!is_string($customerName) || empty($customerName)) {
        throw new InvalidArgumentException("Customer name must be a non-empty string.");
    }

    if (!is_array($items) || empty($items)) {
        throw new InvalidArgumentException("Items must be a non-empty array.");
    }

    // Initialize invoice string
    $invoice = "Condi Shop Invoice\n";
    $invoice .= "=====================\n";
    $invoice .= "Customer: $customerName\n\n";
    $invoice .= "Items:\n";

    // Header for item list
    $invoice .= str_pad("Item Name", 20) . str_pad("Quantity", 10) . str_pad("Price (USD)", 15) . "Total (USD)\n";
    $invoice .= str_repeat("-", 60) . "\n";

    $grandTotal = 0;

    // Loop through items to generate itemized list
    foreach ($items as $item) {
        if (!isset($item['name'], $item['quantity'], $item['price'])) {
            throw new InvalidArgumentException("Each item must include 'name', 'quantity', and 'price'.");
        }

        $itemName = $item['name'];
        $quantity = (int)$item['quantity'];
        $price = (float)$item['price'];
        $total = $quantity * $price;

        $invoice .= str_pad($itemName, 20) . str_pad($quantity, 10) . str_pad(number_format($price, 2), 15) . number_format($total, 2) . "\n";
        $grandTotal += $total;
    }

    $invoice .= str_repeat("-", 60) . "\n";
    $invoice .= "Grand Total: USD " . number_format($grandTotal, 2) . "\n";
    $invoice .= "=====================\n";
    $invoice .= "Thank you for shopping at Condi Shop!\n";

    return $invoice;
}

// Example usage
try {
    $customerName = "Jane Doe";
    $items = [
        ["name" => "Cake boxes with handles", "quantity" => 2, "price" => 5.99],
        ["name" => "Chocolate molds", "quantity" => 3, "price" => 7.49],
    ];
    
    // Generate invoice
    $invoice = generateInvoice($customerName, $items);
    
    // Print invoice
    echo $invoice;
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage();
}

?>
```
