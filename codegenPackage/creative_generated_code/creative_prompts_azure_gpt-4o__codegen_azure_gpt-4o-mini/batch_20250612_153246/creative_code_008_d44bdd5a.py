"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Write a script in PHP to generate repair guarantees for diesel turbo services, including customer details, repair specifics, and warranty terms.
Generated: DETERMINISTIC_d44bdd5a8e8a6dc3
Batch ID: 20250612_153246
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
 * Class RepairGuarantee
 * A class to generate repair guarantees for diesel turbo services.
 */
class RepairGuarantee {
    private $customerName;
    private $customerEmail;
    private $repairDetails;
    private $warrantyPeriod;

    /**
     * Constructor to initialize customer and repair details.
     *
     * @param string $customerName Customer's full name.
     * @param string $customerEmail Customer's email address.
     * @param string $repairDetails Details of the repair performed.
     * @param int $warrantyPeriod Warranty period in months.
     */
    public function __construct($customerName, $customerEmail, $repairDetails, $warrantyPeriod) {
        $this->setCustomerName($customerName);
        $this->setCustomerEmail($customerEmail);
        $this->setRepairDetails($repairDetails);
        $this->setWarrantyPeriod($warrantyPeriod);
    }

    /**
     * Set customer name.
     *
     * @param string $customerName
     * @throws InvalidArgumentException if the name is empty.
     */
    public function setCustomerName($customerName) {
        if (empty($customerName)) {
            throw new InvalidArgumentException('Customer name cannot be empty.');
        }
        $this->customerName = $customerName;
    }

    /**
     * Set customer email.
     *
     * @param string $customerEmail
     * @throws InvalidArgumentException if the email is invalid.
     */
    public function setCustomerEmail($customerEmail) {
        if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException('Invalid email format.');
        }
        $this->customerEmail = $customerEmail;
    }

    /**
     * Set repair details.
     *
     * @param string $repairDetails
     * @throws InvalidArgumentException if the details are empty.
     */
    public function setRepairDetails($repairDetails) {
        if (empty($repairDetails)) {
            throw new InvalidArgumentException('Repair details cannot be empty.');
        }
        $this->repairDetails = $repairDetails;
    }

    /**
     * Set warranty period.
     *
     * @param int $warrantyPeriod
     * @throws InvalidArgumentException if the period is not a positive integer.
     */
    public function setWarrantyPeriod($warrantyPeriod) {
        if (!is_int($warrantyPeriod) || $warrantyPeriod <= 0) {
            throw new InvalidArgumentException('Warranty period must be a positive integer.');
        }
        $this->warrantyPeriod = $warrantyPeriod;
    }

    /**
     * Generate the repair guarantee document.
     *
     * @return string
     */
    public function generateGuarantee() {
        $expiryDate = date('Y-m-d', strtotime("+{$this->warrantyPeriod} months"));
        $guarantee = "Repair Guarantee\n";
        $guarantee .= "Customer Name: {$this->customerName}\n";
        $guarantee .= "Customer Email: {$this->customerEmail}\n";
        $guarantee .= "Repair Details: {$this->repairDetails}\n";
        $guarantee .= "Warranty Period: {$this->warrantyPeriod} months\n";
        $guarantee .= "Warranty Expiry Date: {$expiryDate}\n";

        return $guarantee;
    }
}

// Usage example
try {
    // Create a new RepairGuarantee instance
    $guarantee = new RepairGuarantee(
        'John Doe',
        'johndoe@example.com',
        'Repaired turbocharger on 2008 diesel engine.',
        12
    );

    // Generate and print the guarantee
    echo $guarantee->generateGuarantee();
} catch (InvalidArgumentException $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage();
}
?>
```
