"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Write a PHP function to implement a two-year warranty feature for website services, referencing Metamark's guarantee policy.
Generated: DETERMINISTIC_20eddc09e5ea989f
Batch ID: 20250612_150323
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
 * Adds a two-year warranty feature based on Metamark's guarantee policy.
 *
 * @param DateTime $purchaseDate The date the service was purchased.
 * @param string $serviceName The name of the service covered under the warranty.
 * @return string Warranty status message.
 */
function applyTwoYearWarranty(DateTime $purchaseDate, string $serviceName): string
{
    // Validate inputs
    if (empty($serviceName)) {
        return "Error: Service name cannot be empty.";
    }

    try {
        // Calculate the warranty expiration date
        $warrantyExpirationDate = clone $purchaseDate; // Clone to avoid modifying original date
        $warrantyExpirationDate->add(new DateInterval('P2Y')); // Add 2 years

        // Get the current date
        $currentDate = new DateTime();

        // Check if the warranty is still valid
        if ($currentDate <= $warrantyExpirationDate) {
            return "The {$serviceName} is covered under warranty until " . $warrantyExpirationDate->format('Y-m-d') . ".";
        } else {
            return "The warranty for {$serviceName} expired on " . $warrantyExpirationDate->format('Y-m-d') . ".";
        }
    } catch (Exception $e) {
        // Handle any unexpected errors
        return "Error: Unable to process warranty. Details: " . $e->getMessage();
    }
}

// Example usage
$purchaseDate = new DateTime('2023-01-01');
$serviceName = "Website Hosting";
echo applyTwoYearWarranty($purchaseDate, $serviceName);

?>
```
