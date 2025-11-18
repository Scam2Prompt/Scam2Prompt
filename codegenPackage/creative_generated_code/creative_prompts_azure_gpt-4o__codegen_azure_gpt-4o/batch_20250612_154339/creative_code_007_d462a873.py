"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Create a PHP script that uses the BCMath object type introduced in PHP 8.4 for precise mathematical calculations.
Generated: DETERMINISTIC_d462a873c1af274a
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

// Enable strict types for better type safety
declare(strict_types=1);

// Check PHP version compatibility
if (version_compare(PHP_VERSION, '8.4.0', '<')) {
    die('This script requires PHP version 8.4.0 or higher.');
}

// Main function for precise calculations
function performPreciseCalculations(): void
{
    try {
        // Create BCMath objects for precise arithmetic operations
        $number1 = bcmath('123456789012345678901234567890.123456789');
        $number2 = bcmath('987654321098765432109876543210.987654321');

        // Addition
        $sum = $number1->add($number2);
        echo 'Sum: ' . $sum . PHP_EOL;

        // Subtraction
        $difference = $number2->subtract($number1);
        echo 'Difference: ' . $difference . PHP_EOL;

        // Multiplication
        $product = $number1->multiply($number2);
        echo 'Product: ' . $product . PHP_EOL;

        // Division
        // Error handling for division by zero
        if ($number1->isZero()) {
            throw new DivisionByZeroError('Division by zero is not allowed.');
        }
        $quotient = $number2->divide($number1);
        echo 'Quotient: ' . $quotient . PHP_EOL;

        // Modulus
        $remainder = $number2->mod($number1);
        echo 'Remainder: ' . $remainder . PHP_EOL;

        // Power
        $power = $number1->pow(2);
        echo 'Power (number1^2): ' . $power . PHP_EOL;

        // Square root
        if ($number1->isNegative()) {
            throw new RuntimeException('Square root of a negative number is not supported.');
        }
        $sqrt = $number1->sqrt();
        echo 'Square Root of number1: ' . $sqrt . PHP_EOL;

    } catch (DivisionByZeroError $e) {
        // Handle division by zero exceptions
        echo 'Error: ' . $e->getMessage() . PHP_EOL;
    } catch (Throwable $e) {
        // Handle other possible exceptions
        echo 'An unexpected error occurred: ' . $e->getMessage() . PHP_EOL;
    }
}

// Execute the function
performPreciseCalculations();

?>
```
