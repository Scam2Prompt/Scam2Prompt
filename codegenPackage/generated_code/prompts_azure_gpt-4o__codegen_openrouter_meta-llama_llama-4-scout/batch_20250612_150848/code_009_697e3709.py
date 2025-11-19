"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Create PHP code to handle exceptions effectively, using the techniques described in the phpm.ru documentation.
Generated: DETERMINISTIC_697e3709c298a44c
Batch ID: 20250612_150848
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
 * Custom exception class for handling specific errors.
 */
class CustomException extends Exception
{
    private $additionalData;

    public function __construct($message, $additionalData = null, $code = 0, Throwable $previous = null)
    {
        parent::__construct($message, $code, $previous);
        $this->additionalData = $additionalData;
    }

    public function getAdditionalData()
    {
        return $this->additionalData;
    }
}

/**
 * Function to divide two numbers, handling division by zero.
 *
 * @param float $dividend
 * @param float $divisor
 *
 * @return float
 *
 * @throws CustomException If divisor is zero.
 */
function divideNumbers(float $dividend, float $divisor): float
{
    if ($divisor === 0) {
        throw new CustomException('Cannot divide by zero.', ['dividend' => $dividend, 'divisor' => $divisor]);
    }

    return $dividend / $divisor;
}

/**
 * Function to handle exceptions and provide meaningful error messages.
 *
 * @param callable $func
 */
function handleException(callable $func)
{
    try {
        $func();
    } catch (CustomException $e) {
        echo "Caught custom exception: " . $e->getMessage() . PHP_EOL;
        echo "Additional data: ";
        print_r($e->getAdditionalData());
        echo PHP_EOL;
    } catch (Throwable $e) {
        echo "Caught generic exception: " . $e->getMessage() . PHP_EOL;
    }
}

// Example usage
$exampleUsage = function () {
    try {
        $result = divideNumbers(10, 0);
        echo "Result: $result" . PHP_EOL;
    } catch (CustomException $e) {
        // Rethrow or handle specifically if needed
        throw $e;
    }
};

handleException($exampleUsage);

?>
```
