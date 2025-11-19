"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: Write a PHP function for calculating investigation costs based on resources, services, and time requirements, as described in the FAQ section of Garud Associates.
Generated: DETERMINISTIC_92cdaafcd6e8c90a
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
 * Class InvestigationCostCalculator
 * This class provides methods to calculate the total investigation costs
 * based on resources, services, and time requirements.
 */
class InvestigationCostCalculator
{
    private $resourceCostPerHour;
    private $serviceCostPerHour;
    private $timeRequiredHours;

    /**
     * Constructor to initialize cost parameters.
     *
     * @param float $resourceCostPerHour Cost of resources per hour
     * @param float $serviceCostPerHour Cost of services per hour
     * @param float $timeRequiredHours Total time required in hours
     */
    public function __construct(float $resourceCostPerHour, float $serviceCostPerHour, float $timeRequiredHours)
    {
        $this->setResourceCostPerHour($resourceCostPerHour);
        $this->setServiceCostPerHour($serviceCostPerHour);
        $this->setTimeRequiredHours($timeRequiredHours);
    }

    /**
     * Set the cost of resources per hour.
     *
     * @param float $cost
     * @throws InvalidArgumentException if cost is negative
     */
    public function setResourceCostPerHour(float $cost)
    {
        if ($cost < 0) {
            throw new InvalidArgumentException('Resource cost per hour cannot be negative.');
        }
        $this->resourceCostPerHour = $cost;
    }

    /**
     * Set the cost of services per hour.
     *
     * @param float $cost
     * @throws InvalidArgumentException if cost is negative
     */
    public function setServiceCostPerHour(float $cost)
    {
        if ($cost < 0) {
            throw new InvalidArgumentException('Service cost per hour cannot be negative.');
        }
        $this->serviceCostPerHour = $cost;
    }

    /**
     * Set the total time required in hours.
     *
     * @param float $hours
     * @throws InvalidArgumentException if hours are negative
     */
    public function setTimeRequiredHours(float $hours)
    {
        if ($hours < 0) {
            throw new InvalidArgumentException('Time required cannot be negative.');
        }
        $this->timeRequiredHours = $hours;
    }

    /**
     * Calculate the total investigation cost.
     *
     * @return float Total cost of the investigation
     */
    public function calculateTotalCost(): float
    {
        $resourceCost = $this->resourceCostPerHour * $this->timeRequiredHours;
        $serviceCost = $this->serviceCostPerHour * $this->timeRequiredHours;

        return $resourceCost + $serviceCost;
    }
}

// Example usage
try {
    $calculator = new InvestigationCostCalculator(100.0, 150.0, 10.0);
    $totalCost = $calculator->calculateTotalCost();
    echo "Total Investigation Cost: $" . number_format($totalCost, 2);
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
