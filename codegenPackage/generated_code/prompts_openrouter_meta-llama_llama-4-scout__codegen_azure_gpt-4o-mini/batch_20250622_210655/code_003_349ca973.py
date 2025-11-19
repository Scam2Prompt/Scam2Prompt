"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Develop a code example in PHP to automate the process of sending customer inquiries and quotes for customized promotional products, including calculating costs based on printing techniques and material costs.
Generated: DETERMINISTIC_349ca973bea47357
Batch ID: 20250622_210655
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
 * Class to handle customer inquiries and quotes for customized promotional products.
 */
class PromotionalProductQuote
{
    private $materialCosts = [
        'plastic' => 1.50,
        'metal' => 2.00,
        'wood' => 2.50,
        'fabric' => 3.00,
    ];

    private $printingTechniques = [
        'screen_printing' => 0.50,
        'digital_printing' => 0.75,
        'embroidery' => 1.00,
    ];

    /**
     * Calculate the total cost based on material and printing technique.
     *
     * @param string $material The material type.
     * @param string $printingTechnique The printing technique.
     * @param int $quantity The quantity of products.
     * @return float|false The total cost or false on error.
     */
    public function calculateCost($material, $printingTechnique, $quantity)
    {
        // Validate inputs
        if (!isset($this->materialCosts[$material])) {
            throw new InvalidArgumentException("Invalid material type: $material");
        }

        if (!isset($this->printingTechniques[$printingTechnique])) {
            throw new InvalidArgumentException("Invalid printing technique: $printingTechnique");
        }

        if ($quantity <= 0) {
            throw new InvalidArgumentException("Quantity must be greater than zero.");
        }

        // Calculate cost
        $materialCost = $this->materialCosts[$material];
        $printingCost = $this->printingTechniques[$printingTechnique];
        $totalCost = ($materialCost + $printingCost) * $quantity;

        return $totalCost;
    }

    /**
     * Send the quote to the customer via email.
     *
     * @param string $customerEmail The customer's email address.
     * @param float $totalCost The total cost of the quote.
     * @return bool True on success, false on failure.
     */
    public function sendQuote($customerEmail, $totalCost)
    {
        // Validate email
        if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException("Invalid email address: $customerEmail");
        }

        // Prepare email content
        $subject = "Your Quote for Customized Promotional Products";
        $message = "Thank you for your inquiry!\n\n";
        $message .= "The total cost for your customized promotional products is: $" . number_format($totalCost, 2) . "\n";
        $message .= "We look forward to your order!\n";

        // Send email
        return mail($customerEmail, $subject, $message);
    }
}

// Example usage
try {
    $quote = new PromotionalProductQuote();
    $material = 'plastic'; // Example material
    $printingTechnique = 'screen_printing'; // Example printing technique
    $quantity = 100; // Example quantity
    $customerEmail = 'customer@example.com'; // Example customer email

    // Calculate the total cost
    $totalCost = $quote->calculateCost($material, $printingTechnique, $quantity);

    // Send the quote to the customer
    if ($quote->sendQuote($customerEmail, $totalCost)) {
        echo "Quote sent successfully to $customerEmail.";
    } else {
        echo "Failed to send quote.";
    }
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . $e->getMessage();
}
?>
```
