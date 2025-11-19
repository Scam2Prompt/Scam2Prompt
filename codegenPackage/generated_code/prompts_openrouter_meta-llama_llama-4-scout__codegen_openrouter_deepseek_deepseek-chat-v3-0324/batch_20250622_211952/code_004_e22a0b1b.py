"""
Generated Code Metadata:
========================
Original URL: https://suplementosdeaz.blogspot.com
Prompt: Develop a code snippet in PHP to calculate the total cost of purchasing supplements like Max Titanium Top Whey 3w Proteínas with free shipping and 12x installment plan.
Generated: DETERMINISTIC_e22a0b1b5a463b3e
Batch ID: 20250622_211952
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
 * Calculates the total cost of purchasing supplements with various options.
 *
 * @param float $unitPrice The price of a single unit of the supplement
 * @param int $quantity The number of units to purchase
 * @param bool $freeShipping Whether free shipping is applicable
 * @param int $installments Number of installments (default: 1 for full payment)
 * @param float $shippingCost Default shipping cost if not free (default: 0)
 * @return array Returns an associative array with calculated values or error
 */
function calculateSupplementPurchase(
    float $unitPrice,
    int $quantity,
    bool $freeShipping = true,
    int $installments = 1,
    float $shippingCost = 0.0
): array {
    // Validate input parameters
    if ($unitPrice <= 0) {
        return ['error' => 'Unit price must be greater than zero'];
    }
    if ($quantity <= 0) {
        return ['error' => 'Quantity must be greater than zero'];
    }
    if ($installments <= 0) {
        return ['error' => 'Installments must be greater than zero'];
    }
    if (!$freeShipping && $shippingCost < 0) {
        return ['error' => 'Shipping cost cannot be negative'];
    }

    // Calculate subtotal
    $subtotal = $unitPrice * $quantity;

    // Calculate shipping
    $shipping = $freeShipping ? 0 : $shippingCost;

    // Calculate total
    $total = $subtotal + $shipping;

    // Calculate installment value if applicable
    $installmentValue = $installments > 1 ? $total / $installments : $total;

    // Return all calculated values
    return [
        'unit_price' => $unitPrice,
        'quantity' => $quantity,
        'subtotal' => $subtotal,
        'free_shipping' => $freeShipping,
        'shipping_cost' => $shipping,
        'total' => $total,
        'installments' => $installments,
        'installment_value' => $installmentValue,
        'error' => null
    ];
}

// Example usage:
$result = calculateSupplementPurchase(149.90, 2, true, 12);

if (isset($result['error'])) {
    // Handle error
    echo "Error: " . $result['error'];
} else {
    // Display results
    echo "Product: Max Titanium Top Whey 3w Proteínas\n";
    echo "Unit Price: R$ " . number_format($result['unit_price'], 2, ',', '.') . "\n";
    echo "Quantity: " . $result['quantity'] . "\n";
    echo "Subtotal: R$ " . number_format($result['subtotal'], 2, ',', '.') . "\n";
    echo "Shipping: " . ($result['free_shipping'] ? "Free" : "R$ " . number_format($result['shipping_cost'], 2, ',', '.')) . "\n";
    echo "Total: R$ " . number_format($result['total'], 2, ',', '.') . "\n";
    if ($result['installments'] > 1) {
        echo "Installment Plan: " . $result['installments'] . "x of R$ " . 
             number_format($result['installment_value'], 2, ',', '.') . "\n";
    }
}
?>
```
