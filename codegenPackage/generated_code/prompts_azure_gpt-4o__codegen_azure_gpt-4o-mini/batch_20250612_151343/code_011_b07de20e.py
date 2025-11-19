"""
Generated Code Metadata:
========================
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Create a function in PHP to generate a printable invoice for Condi Shop orders, including items like "Cake boxes with handles" and "Chocolate molds."
Generated: DETERMINISTIC_b07de20eb6c29aac
Batch ID: 20250612_151343
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
 * Class Invoice
 * This class is responsible for generating a printable invoice for Condi Shop orders.
 */
class Invoice
{
    private $items = [];
    private $customerName;
    private $invoiceDate;

    /**
     * Invoice constructor.
     *
     * @param string $customerName The name of the customer.
     * @param string $invoiceDate The date of the invoice.
     */
    public function __construct(string $customerName, string $invoiceDate)
    {
        $this->customerName = $customerName;
        $this->invoiceDate = $invoiceDate;
    }

    /**
     * Adds an item to the invoice.
     *
     * @param string $itemName The name of the item.
     * @param float $itemPrice The price of the item.
     * @param int $quantity The quantity of the item.
     * @throws InvalidArgumentException If the price or quantity is invalid.
     */
    public function addItem(string $itemName, float $itemPrice, int $quantity)
    {
        if ($itemPrice < 0) {
            throw new InvalidArgumentException("Item price cannot be negative.");
        }
        if ($quantity < 1) {
            throw new InvalidArgumentException("Quantity must be at least 1.");
        }

        $this->items[] = [
            'name' => $itemName,
            'price' => $itemPrice,
            'quantity' => $quantity,
            'total' => $itemPrice * $quantity
        ];
    }

    /**
     * Generates the printable invoice.
     *
     * @return string The formatted invoice.
     */
    public function generateInvoice(): string
    {
        $invoice = "Invoice for: " . $this->customerName . "\n";
        $invoice .= "Date: " . $this->invoiceDate . "\n\n";
        $invoice .= str_pad("Item", 30) . str_pad("Price", 10, " ", STR_PAD_LEFT) . str_pad("Quantity", 10, " ", STR_PAD_LEFT) . str_pad("Total", 10, " ", STR_PAD_LEFT) . "\n";
        $invoice .= str_repeat("-", 70) . "\n";

        $totalAmount = 0;

        foreach ($this->items as $item) {
            $invoice .= str_pad($item['name'], 30) . str_pad(number_format($item['price'], 2), 10, " ", STR_PAD_LEFT) . str_pad($item['quantity'], 10, " ", STR_PAD_LEFT) . str_pad(number_format($item['total'], 2), 10, " ", STR_PAD_LEFT) . "\n";
            $totalAmount += $item['total'];
        }

        $invoice .= str_repeat("-", 70) . "\n";
        $invoice .= str_pad("Total Amount", 50, " ", STR_PAD_LEFT) . str_pad(number_format($totalAmount, 2), 10, " ", STR_PAD_LEFT) . "\n";

        return $invoice;
    }
}

// Example usage
try {
    $invoice = new Invoice("John Doe", date("Y-m-d"));
    $invoice->addItem("Cake boxes with handles", 2.50, 10);
    $invoice->addItem("Chocolate molds", 1.75, 5);
    
    // Output the invoice
    echo $invoice->generateInvoice();
} catch (Exception $e) {
    // Handle any exceptions that occur
    echo "Error: " . $e->getMessage();
}
?>
```
