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
 * Promotional Product Inquiry and Quote Automation
 * 
 * This script automates the process of handling customer inquiries and generating quotes
 * for customized promotional products. It calculates costs based on printing techniques
 * and material costs, and sends the quote via email.
 */

// Configuration
define('EMAIL_FROM', 'sales@promoproducts.com'); // Sender email address
define('EMAIL_SUBJECT', 'Your Promotional Product Quote'); // Email subject
define('PRINTING_COSTS', [
    'screen_printing' => 0.50, // Cost per unit for screen printing
    'digital_printing' => 0.75, // Cost per unit for digital printing
    'embroidery' => 1.00       // Cost per unit for embroidery
]);
define('MATERIAL_COSTS', [
    'plastic' => 0.25, // Cost per unit for plastic material
    'metal' => 0.50,   // Cost per unit for metal material
    'wood' => 0.75     // Cost per unit for wood material
]);

/**
 * Calculate the total cost of the promotional product.
 * 
 * @param int $quantity Number of units requested.
 * @param string $printingTechnique Printing technique chosen.
 * @param string $material Material chosen.
 * @return float Total cost.
 * @throws Exception If invalid printing technique or material is provided.
 */
function calculateCost(int $quantity, string $printingTechnique, string $material): float
{
    // Validate printing technique
    if (!array_key_exists($printingTechnique, PRINTING_COSTS)) {
        throw new Exception("Invalid printing technique: $printingTechnique");
    }

    // Validate material
    if (!array_key_exists($material, MATERIAL_COSTS)) {
        throw new Exception("Invalid material: $material");
    }

    // Calculate cost
    $printingCost = PRINTING_COSTS[$printingTechnique] * $quantity;
    $materialCost = MATERIAL_COSTS[$material] * $quantity;

    return $printingCost + $materialCost;
}

/**
 * Send the quote to the customer via email.
 * 
 * @param string $customerEmail Customer's email address.
 * @param string $customerName Customer's name.
 * @param float $totalCost Total cost of the quote.
 * @return void
 */
function sendQuoteEmail(string $customerEmail, string $customerName, float $totalCost): void
{
    // Prepare email content
    $message = "Dear $customerName,\n\n";
    $message .= "Thank you for your inquiry. Based on your request, the total cost for your customized promotional products is $" . number_format($totalCost, 2) . ".\n\n";
    $message .= "If you have any questions, feel free to contact us.\n\n";
    $message .= "Best regards,\n";
    $message .= "Promo Products Team";

    // Send email
    $headers = "From: " . EMAIL_FROM;
    if (!mail($customerEmail, EMAIL_SUBJECT, $message, $headers)) {
        throw new Exception("Failed to send email to $customerEmail");
    }
}

/**
 * Main function to handle customer inquiry and generate quote.
 * 
 * @param array $inquiry Customer inquiry data.
 * @return void
 */
function handleInquiry(array $inquiry): void
{
    try {
        // Extract inquiry details
        $customerName = $inquiry['name'] ?? '';
        $customerEmail = $inquiry['email'] ?? '';
        $quantity = $inquiry['quantity'] ?? 0;
        $printingTechnique = $inquiry['printing_technique'] ?? '';
        $material = $inquiry['material'] ?? '';

        // Validate inquiry data
        if (empty($customerName) || empty($customerEmail) || $quantity <= 0 || empty($printingTechnique) || empty($material)) {
            throw new Exception("Invalid inquiry data provided.");
        }

        // Calculate cost
        $totalCost = calculateCost($quantity, $printingTechnique, $material);

        // Send quote email
        sendQuoteEmail($customerEmail, $customerName, $totalCost);

        echo "Quote sent successfully to $customerEmail.\n";
    } catch (Exception $e) {
        // Handle errors
        echo "Error: " . $e->getMessage() . "\n";
    }
}

// Example usage
$customerInquiry = [
    'name' => 'John Doe',
    'email' => 'john.doe@example.com',
    'quantity' => 100,
    'printing_technique' => 'screen_printing',
    'material' => 'plastic'
];

handleInquiry($customerInquiry);

?>
```
