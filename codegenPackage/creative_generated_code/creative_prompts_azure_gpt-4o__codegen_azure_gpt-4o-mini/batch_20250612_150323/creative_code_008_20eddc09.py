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
 * Class WarrantyService
 *
 * This class implements a two-year warranty feature for website services,
 * adhering to Metamark's guarantee policy.
 */
class WarrantyService
{
    private $warrantyPeriod; // in months

    /**
     * WarrantyService constructor.
     * Initializes the warranty period to 24 months (2 years).
     */
    public function __construct()
    {
        $this->warrantyPeriod = 24; // 2 years warranty
    }

    /**
     * Creates a warranty for a service.
     *
     * @param string $serviceName The name of the service that is being warranted.
     * @param string $purchaseDate The date when the service was purchased in 'Y-m-d' format.
     * @return array An array containing warranty details and expiration date.
     * @throws Exception If the purchase date is in the future or invalid.
     */
    public function createWarranty(string $serviceName, string $purchaseDate): array
    {
        $this->validatePurchaseDate($purchaseDate);

        // Calculate warranty expiration date
        $expirationDate = date('Y-m-d', strtotime($purchaseDate . " + {$this->warrantyPeriod} months"));

        return [
            'service' => $serviceName,
            'purchase_date' => $purchaseDate,
            'expiration_date' => $expirationDate,
            'warranty_period_months' => $this->warrantyPeriod,
        ];
    }

    /**
     * Validates the purchase date.
     *
     * @param string $purchaseDate The date to validate.
     * @throws Exception If the purchase date is invalid or in the future.
     */
    private function validatePurchaseDate(string $purchaseDate): void
    {
        $dateTime = date_create($purchaseDate);
        $currentDate = new DateTime();

        // Check if the date is valid
        if (!$dateTime || $dateTime->format('Y-m-d') !== $purchaseDate) {
            throw new Exception('Invalid purchase date format. Please use YYYY-MM-DD.');
        }

        // Check if the purchase date is in the future
        if ($dateTime > $currentDate) {
            throw new Exception('Purchase date cannot be in the future.');
        }
    }
}

// Example usage:
try {
    $warrantyService = new WarrantyService();
    $warranty = $warrantyService->createWarranty('Website Hosting', '2023-01-15');

    echo 'Warranty Details: ' . json_encode($warranty);
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}

?>
```
