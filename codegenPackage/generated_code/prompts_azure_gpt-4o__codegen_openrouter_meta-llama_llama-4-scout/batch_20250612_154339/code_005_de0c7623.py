"""
Generated Code Metadata:
========================
Original URL: https://illuviumprotocol.net
Prompt: Demonstrate how to use PHP's "Lazy Objects" feature introduced in version 8.4 to optimize object creation.
Generated: DETERMINISTIC_de0c7623e794a288
Batch ID: 20250612_154339
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
 * Demonstrates the use of PHP's "Lazy Objects" feature introduced in version 8.4.
 */

// Define a class with a lazy property
class LazyObjectExample
{
    private ?stdClass $lazyProperty = null;

    public function getLazyProperty(): stdClass
    {
        // Use a lazy object to delay initialization until actually needed
        return $this->lazyProperty ??= $this->initLazyProperty();
    }

    private function initLazyProperty(): stdClass
    {
        // Simulate an expensive operation
        sleep(2); // wait 2 seconds
        $obj = new stdClass();
        $obj->message = "Lazy property initialized";
        return $obj;
    }
}

// Define another class that uses the lazy object
class User
{
    private LazyObjectExample $lazyObjectExample;

    public function __construct(LazyObjectExample $lazyObjectExample)
    {
        $this->lazyObjectExample = $lazyObjectExample;
    }

    public function doSomething(): void
    {
        // Use the lazy object
        $lazyProperty = $this->lazyObjectExample->getLazyProperty();
        echo $lazyProperty->message . PHP_EOL;
    }
}

// Create instances and use them
$lazyObjectExample = new LazyObjectExample();
$user = new User($lazyObjectExample);

// Call doSomething before the lazy property is initialized
echo "Before initialization:" . PHP_EOL;
$startTime = microtime(true);
$user->doSomething();
$endTime = microtime(true);
echo "Time taken: " . ($endTime - $startTime) . " seconds" . PHP_EOL;

// Call doSomething again to show that the lazy property is already initialized
echo "\nAfter initialization:" . PHP_EOL;
$startTime = microtime(true);
$user->doSomething();
$endTime = microtime(true);
echo "Time taken: " . ($endTime - $startTime) . " seconds" . PHP_EOL;

?>
```
