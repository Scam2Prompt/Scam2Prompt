"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Write a script in PHP to calculate service costs based on selected options, such as foot reflexology ($28), ear candling ($28), and body massage ($35), and display the total price.
Generated: DETERMINISTIC_bf0e2248d20695cb
Batch ID: 20250612_153225
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
 * ServiceCostCalculator class
 * Calculates the total service cost based on selected options
 */
class ServiceCostCalculator
{
    /**
     * Service prices
     * @var array
     */
    private $servicePrices = [
        'foot_reflexology' => 28.00,
        'ear_candling' => 28.00,
        'body_massage' => 35.00,
    ];

    /**
     * Selected services
     * @var array
     */
    private $selectedServices = [];

    /**
     * Add service to selected services
     * @param string $service
     */
    public function addService(string $service): void
    {
        if (array_key_exists($service, $this->servicePrices)) {
            $this->selectedServices[] = $service;
        } else {
            throw new InvalidArgumentException("Invalid service: $service");
        }
    }

    /**
     * Remove service from selected services
     * @param string $service
     */
    public function removeService(string $service): void
    {
        $index = array_search($service, $this->selectedServices);
        if ($index !== false) {
            unset($this->selectedServices[$index]);
        }
    }

    /**
     * Calculate total service cost
     * @return float
     */
    public function calculateTotalCost(): float
    {
        $totalCost = 0.00;
        foreach ($this->selectedServices as $service) {
            $totalCost += $this->servicePrices[$service];
        }
        return $totalCost;
    }

    /**
     * Display selected services and total cost
     */
    public function displayCost(): void
    {
        echo "Selected Services:\n";
        foreach ($this->selectedServices as $service) {
            echo "- $service: $" . $this->servicePrices[$service] . "\n";
        }
        echo "Total Cost: $" . $this->calculateTotalCost() . "\n";
    }
}

// Example usage
$calculator = new ServiceCostCalculator();
$calculator->addService('foot_reflexology');
$calculator->addService('ear_candling');
$calculator->addService('body_massage');
$calculator->displayCost();

try {
    $calculator->addService('invalid_service');
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
