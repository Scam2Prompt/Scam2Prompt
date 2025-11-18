"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Demonstrate how to use PHP's "Lazy Objects" feature introduced in version 8.4 to optimize object creation.
Generated: DETERMINISTIC_de0c7623e794a288
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Ensure you are using PHP 8.4 or newer for the Lazy Objects feature.

// Example demonstrating Lazy Objects in PHP 8.4

// Define a class with expensive initialization logic
class ExpensiveObject
{
    private array $data;

    public function __construct()
    {
        // Simulate expensive initialization, e.g., loading data from an external source
        echo "Initializing ExpensiveObject...\n";
        $this->data = [];
        for ($i = 0; $i < 1000000; $i++) {
            $this->data[] = $i;
        }
    }

    public function getData(): array
    {
        return $this->data;
    }
}

// Create a lazy version of the object using the new Lazy Objects feature
$lazyObject = ExpensiveObject::createLazy(function () {
    // The callback provides the initialization logic for the lazy object
    return new ExpensiveObject();
});

// At this point, the object is not initialized yet.

// Accessing a method or property forces initialization
echo "Accessing lazy object...\n";
$data = $lazyObject->getData(); // This triggers initialization of the object

// The object is now fully initialized
echo "Lazy object initialized and data retrieved: " . count($data) . " items.\n";

?>
```
