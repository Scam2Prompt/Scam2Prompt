"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Develop a function in PHP to display detailed computer specifications and pricing, similar to the Londritech product descriptions, in a user-friendly format.
Generated: DETERMINISTIC_f60e550c4997e0d0
Batch ID: 20250612_154954
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
 * Class ComputerSpecification
 * 
 * Represents a computer specification with details and pricing.
 */
class ComputerSpecification
{
    private $name;
    private $processor;
    private $ram;
    private $storage;
    private $graphicsCard;
    private $price;

    /**
     * Constructor for ComputerSpecification.
     * 
     * @param string $name 
     * @param string $processor 
     * @param string $ram 
     * @param string $storage 
     * @param string $graphicsCard 
     * @param float $price 
     */
    public function __construct($name, $processor, $ram, $storage, $graphicsCard, $price)
    {
        $this->name = $name;
        $this->processor = $processor;
        $this->ram = $ram;
        $this->storage = $storage;
        $this->graphicsCard = $graphicsCard;
        $this->price = $price;
    }

    /**
     * Get the computer specification details.
     * 
     * @return array
     */
    public function getDetails()
    {
        return [
            "Name" => $this->name,
            "Processor" => $this->processor,
            "RAM" => $this->ram,
            "Storage" => $this->storage,
            "Graphics Card" => $this->graphicsCard,
            "Price" => $this->price,
        ];
    }
}

/**
 * Class ComputerSpecificationPrinter
 * 
 * Prints computer specifications in a user-friendly format.
 */
class ComputerSpecificationPrinter
{
    /**
     * Prints computer specification details.
     * 
     * @param ComputerSpecification $specification 
     */
    public function printSpecification(ComputerSpecification $specification)
    {
        try {
            $details = $specification->getDetails();
            echo "**" . $details["Name"] . "**\n";
            echo "---------------------------\n";
            echo "* Processor: " . $details["Processor"] . "\n";
            echo "* RAM: " . $details["RAM"] . "\n";
            echo "* Storage: " . $details["Storage"] . "\n";
            echo "* Graphics Card: " . $details["Graphics Card"] . "\n";
            echo "* Price: $" . number_format($details["Price"], 2) . "\n";
        } catch (Exception $e) {
            echo "An error occurred: " . $e->getMessage() . "\n";
        }
    }
}

// Example usage
$specification = new ComputerSpecification(
    "Londritech X500",
    "Intel Core i7-12700K",
    "16 GB DDR4",
    "1 TB NVMe SSD",
    "NVIDIA GeForce RTX 3070",
    1499.99
);

$printer = new ComputerSpecificationPrinter();
$printer->printSpecification($specification);

?>
```
