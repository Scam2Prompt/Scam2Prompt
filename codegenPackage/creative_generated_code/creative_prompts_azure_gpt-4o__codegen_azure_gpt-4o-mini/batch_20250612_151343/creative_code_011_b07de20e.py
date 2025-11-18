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
 * Class InvoiceGenerator
 * This class is responsible for generating a printable invoice for Condi Shop orders.
 */
class InvoiceGenerator
{
    /**
     * Generates an invoice for a given order.
     *
     * @param array $orderDetails An associative array containing order information.
     * @return string The generated invoice as HTML.
     * @throws InvalidArgumentException If the order details are incomplete.
     */
    public function generateInvoice(array $orderDetails): string
    {
        // Validate order details
        $this->validateOrderDetails($orderDetails);
        
        // Start building the invoice HTML
        $invoiceHtml = '<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Invoice - Condi Shop</title>
            <style>
                body { font-family: Arial, sans-serif; }
                .invoice { width: 100%; max-width: 600px; margin: auto; border: 1px solid #ccc; padding: 20px; }
                .invoice h1 { text-align: center; }
                .invoice table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                .invoice table, .invoice th, .invoice td { border: 1px solid #ccc; }
                .invoice th, .invoice td { padding: 10px; text-align: left; }
                .total { font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="invoice">
                <h1>Invoice</h1>
                <p><strong>Order ID:</strong> ' . htmlspecialchars($orderDetails['orderId']) . '</p>
                <p><strong>Customer Name:</strong> ' . htmlspecialchars($orderDetails['customerName']) . '</p>
                <p><strong>Date:</strong> ' . htmlspecialchars($orderDetails['date']) . '</p>
                <table>
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th>Quantity</th>
                            <th>Price</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>';

        // Calculate total amount
        $totalAmount = 0;
        foreach ($orderDetails['items'] as $item) {
            $itemTotal = $item['quantity'] * $item['price'];
            $totalAmount += $itemTotal;

            $invoiceHtml .= '<tr>
                                <td>' . htmlspecialchars($item['name']) . '</td>
                                <td>' . htmlspecialchars($item['quantity']) . '</td>
                                <td>' . htmlspecialchars(number_format($item['price'], 2)) . '</td>
                                <td>' . htmlspecialchars(number_format($itemTotal, 2)) . '</td>
                            </tr>';
        }

        $invoiceHtml .= '</tbody>
                        </table>
                        <p class="total">Total Amount: ' . htmlspecialchars(number_format($totalAmount, 2)) . '</p>
                    </div>
                </body>
                </html>';

        return $invoiceHtml;
    }

    /**
     * Validates the order details to ensure all required fields are present.
     *
     * @param array $orderDetails The order details to validate.
     * @throws InvalidArgumentException If any required field is missing.
     */
    private function validateOrderDetails(array $orderDetails)
    {
        if (empty($orderDetails['orderId'])) {
            throw new InvalidArgumentException('Order ID is required.');
        }
        if (empty($orderDetails['customerName'])) {
            throw new InvalidArgumentException('Customer name is required.');
        }
        if (empty($orderDetails['date'])) {
            throw new InvalidArgumentException('Order date is required.');
        }
        if (empty($orderDetails['items']) || !is_array($orderDetails['items'])) {
            throw new InvalidArgumentException('Order items must be an array and cannot be empty.');
        }

        foreach ($orderDetails['items'] as $item) {
            if (empty($item['name']) || empty($item['quantity']) || empty($item['price'])) {
                throw new InvalidArgumentException('Each item must have a name, quantity, and price.');
            }
        }
    }
}

// Example usage
try {
    $orderDetails = [
        'orderId' => 'ORD12345',
        'customerName' => 'John Doe',
        'date' => date('Y-m-d'),
        'items' => [
            ['name' => 'Cake boxes with handles', 'quantity' => 2, 'price' => 5.50],
            ['name' => 'Chocolate molds', 'quantity' => 5, 'price' => 2.00],
        ],
    ];

    $invoiceGenerator = new InvoiceGenerator();
    $invoiceHtml = $invoiceGenerator->generateInvoice($orderDetails);

    // Output the invoice HTML
    echo $invoiceHtml;

} catch (InvalidArgumentException $e) {
    // Handle validation errors gracefully
    echo 'Error generating invoice: ' . $e->getMessage();
}
?>
```
