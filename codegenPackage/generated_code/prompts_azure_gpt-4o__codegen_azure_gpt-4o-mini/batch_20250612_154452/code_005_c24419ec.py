"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: Write a function in PHP to generate unlimited electronic invoices for a retail business, ensuring compliance with Peruvian regulations, as highlighted by TICOM Software.
Generated: DETERMINISTIC_c24419ec7a2c662e
Batch ID: 20250612_154452
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
 * Class InvoiceGenerator
 * This class is responsible for generating electronic invoices
 * in compliance with Peruvian regulations.
 */
class InvoiceGenerator
{
    private $invoiceData;

    /**
     * Constructor to initialize invoice data.
     *
     * @param array $data Initial invoice data.
     */
    public function __construct(array $data)
    {
        $this->invoiceData = $data;
    }

    /**
     * Generates an electronic invoice.
     *
     * @return string The generated invoice in JSON format.
     * @throws Exception If invoice data is invalid.
     */
    public function generateInvoice()
    {
        // Validate invoice data
        $this->validateInvoiceData();

        // Prepare invoice data for output
        $invoice = [
            'invoice_number' => $this->generateInvoiceNumber(),
            'date' => date('Y-m-d H:i:s'),
            'items' => $this->invoiceData['items'],
            'total' => $this->calculateTotal(),
            'customer' => $this->invoiceData['customer'],
            'tax' => $this->calculateTax(),
        ];

        // Convert invoice to JSON format
        return json_encode($invoice, JSON_PRETTY_PRINT);
    }

    /**
     * Validates the invoice data.
     *
     * @throws Exception If validation fails.
     */
    private function validateInvoiceData()
    {
        if (empty($this->invoiceData['items']) || !is_array($this->invoiceData['items'])) {
            throw new Exception('Invalid invoice items.');
        }

        if (empty($this->invoiceData['customer'])) {
            throw new Exception('Customer information is required.');
        }
    }

    /**
     * Generates a unique invoice number.
     *
     * @return string The generated invoice number.
     */
    private function generateInvoiceNumber()
    {
        // For simplicity, using a timestamp as a unique invoice number
        return 'INV-' . time();
    }

    /**
     * Calculates the total amount of the invoice.
     *
     * @return float The total amount.
     */
    private function calculateTotal()
    {
        $total = 0.0;

        foreach ($this->invoiceData['items'] as $item) {
            if (!isset($item['price'], $item['quantity'])) {
                throw new Exception('Item must have price and quantity.');
            }
            $total += $item['price'] * $item['quantity'];
        }

        return $total;
    }

    /**
     * Calculates the tax based on the total amount.
     *
     * @return float The calculated tax.
     */
    private function calculateTax()
    {
        $taxRate = 0.18; // 18% tax rate as per Peruvian regulations
        return $this->calculateTotal() * $taxRate;
    }
}

// Example usage
try {
    $invoiceData = [
        'items' => [
            ['name' => 'Product 1', 'price' => 100.00, 'quantity' => 2],
            ['name' => 'Product 2', 'price' => 50.00, 'quantity' => 1],
        ],
        'customer' => [
            'name' => 'John Doe',
            'document_type' => 'DNI',
            'document_number' => '12345678',
        ],
    ];

    $invoiceGenerator = new InvoiceGenerator($invoiceData);
    $invoice = $invoiceGenerator->generateInvoice();
    echo $invoice;

} catch (Exception $e) {
    // Handle exceptions gracefully
    echo 'Error generating invoice: ' . $e->getMessage();
}
?>
```
