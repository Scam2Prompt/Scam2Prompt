"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Write a PHP script using the new "Property Hooks" feature introduced in PHP 8.4 to dynamically modify property access behavior.
Generated: DETERMINISTIC_d854a0e18cf2988e
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

// Example script to demonstrate PHP 8.4's Property Hooks feature.
// This script uses the `__get()` and `__set()` hooks to dynamically modify property access behavior.

class DynamicPropertyHandler
{
    private array $data = []; // Storage for dynamic properties
    
    // Hook for reading properties dynamically
    public function __get(string $name): mixed
    {
        // Check if the property exists in the data array
        if (array_key_exists($name, $this->data)) {
            return $this->data[$name];
        }
        
        // Property does not exist, throw an exception
        throw new Exception("Attempting to access undefined property '$name'.");
    }
    
    // Hook for writing properties dynamically
    public function __set(string $name, mixed $value): void
    {
        // Validate property value (optional, based on requirements)
        if (is_null($value)) {
            throw new Exception("Property '$name' cannot be set to null.");
        }
        
        // Store the value in the data array
        $this->data[$name] = $value;
    }
    
    // Hook for checking if a property is set
    public function __isset(string $name): bool
    {
        return isset($this->data[$name]);
    }
    
    // Hook for unsetting a property
    public function __unset(string $name): void
    {
        if (isset($this->data[$name])) {
            unset($this->data[$name]);
        } else {
            throw new Exception("Attempting to unset an undefined property '$name'.");
        }
    }
}

// Example usage
try {
    $handler = new DynamicPropertyHandler();
    
    // Dynamically setting properties
    $handler->name = "John Doe";
    $handler->age = 30;

    // Accessing dynamic properties
    echo "Name: " . $handler->name . PHP_EOL; // Outputs: Name: John Doe
    echo "Age: " . $handler->age . PHP_EOL; // Outputs: Age: 30

    // Checking if a property is set
    if (isset($handler->name)) {
        echo "Name is set." . PHP_EOL;
    }

    // Unsetting a property
    unset($handler->age);

    // Attempting to access an undefined property (will throw an exception)
    echo $handler->age;
} catch (Exception $e) {
    // Handle errors gracefully
    echo "Error: " . $e->getMessage() . PHP_EOL;
}

?>
```
