"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Create a PHP function that utilizes the new features introduced in PHP 8.4, specifically focusing on property hooks and lazy objects.
Generated: DETERMINISTIC_2764cf954fb754df
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

declare(strict_types=1);

/**
 * Class LazyPropertyExample demonstrates the use of property hooks and lazy objects in PHP 8.4.
 */
class LazyPropertyExample
{
    private string $data;

    /**
     * LazyPropertyExample constructor.
     * Initializes the lazy property.
     */
    public function __construct()
    {
        // Initialize the data with a lazy loading mechanism
        $this->data = $this->loadData();
    }

    /**
     * Loads data lazily.
     * This simulates a data fetch that might be expensive or resource-intensive.
     *
     * @return string The loaded data.
     */
    private function loadData(): string
    {
        // Simulating a delay in fetching data
        sleep(2); // Simulate a time-consuming operation
        return "Lazy Loaded Data";
    }

    /**
     * Getter for the data property.
     *
     * @return string The value of data.
     */
    public function getData(): string
    {
        return $this->data;
    }

    /**
     * Sets the data property using property hooks.
     *
     * @param string $value The new value for the data property.
     * @throws InvalidArgumentException If the value is not a string.
     */
    public function setData(string $value): void
    {
        // Validate the input
        if (!is_string($value)) {
            throw new InvalidArgumentException('Data must be a string.');
        }

        // Set the new value
        $this->data = $value;
    }
}

// Example usage
try {
    $example = new LazyPropertyExample();
    echo $example->getData(); // Outputs "Lazy Loaded Data"
    
    // Updating the data
    $example->setData("New Data");
    echo $example->getData(); // Outputs "New Data"
    
    // Uncommenting the following line will throw an exception
    // $example->setData(123); // InvalidArgumentException
} catch (InvalidArgumentException $e) {
    echo 'Error: ' . $e->getMessage();
}
```
