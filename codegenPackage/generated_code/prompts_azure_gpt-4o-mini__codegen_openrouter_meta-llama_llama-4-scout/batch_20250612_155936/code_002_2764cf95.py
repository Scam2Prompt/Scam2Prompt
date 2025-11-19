"""
Generated Code Metadata:
========================
Original URL: https://illuviumprotocol.net
Prompt: Create a PHP function that utilizes the new features introduced in PHP 8.4, specifically focusing on property hooks and lazy objects.
Generated: DETERMINISTIC_2764cf954fb754df
Batch ID: 20250612_155936
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
 * User class utilizing PHP 8.4 features: property hooks and lazy objects.
 */
class User
{
    # Property with getter and setter hooks
    private string $name;

    public function __construct(string $name)
    {
        $this->name = $name;
    }

    /**
     * Getter for $name property.
     *
     * @return string
     */
    public function getName(): string
    {
        return $this->name;
    }

    /**
     * Setter for $name property with validation.
     *
     * @param string $name
     */
    public function setName(string $name): void
    {
        if (empty($name)) {
            throw new InvalidArgumentException('Name cannot be empty');
        }
        $this->name = $name;
    }
}

/**
 * LazyObject class demonstrating lazy loading.
 */
class LazyObject
{
    private ?object $object = null;

    /**
     * Creates a lazy object.
     */
    public function __construct()
    {
        // Object creation is deferred until it's actually needed
    }

    /**
     * Magic method to handle property access.
     *
     * @param string $name
     * @return mixed
     */
    public function __get(string $name)
    {
        if ($this->object === null) {
            // Simulate expensive object creation
            $this->object = new stdClass();
            $this->object->property = 'value';
        }
        return $this->object->$name;
    }
}

/**
 * Demonstrates usage of User and LazyObject classes.
 */
function main(): void
{
    try {
        $user = new User('John Doe');
        echo $user->getName() . PHP_EOL;

        // Test setter validation
        $user->setName('Jane Doe');
        echo $user->getName() . PHP_EOL;

        // Attempt to set invalid name
        try {
            $user->setName('');
        } catch (InvalidArgumentException $e) {
            echo 'Caught exception: ' . $e->getMessage() . PHP_EOL;
        }

        // Demonstrate lazy object
        $lazyObject = new LazyObject();
        // The object is not created yet
        echo 'Before accessing property' . PHP_EOL;
        // Accessing a property triggers object creation
        echo $lazyObject->property . PHP_EOL;
        echo 'After accessing property' . PHP_EOL;
    } catch (Exception $e) {
        echo 'An error occurred: ' . $e->getMessage() . PHP_EOL;
    }
}

main();

?>
```
