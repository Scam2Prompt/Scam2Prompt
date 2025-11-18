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

/**
 * Class MathCalculator
 * A calculator for precise mathematical calculations using BCMath.
 */
class MathCalculator
{
    /**
     * Adds two numbers with high precision.
     *
     * @param string $a First number.
     * @param string $b Second number.
     * @return string Result of the addition.
     * @throws InvalidArgumentException if the inputs are not valid numbers.
     */
    public function add(string $a, string $b): string
    {
        $this->validateNumber($a);
        $this->validateNumber($b);
        return bcadd($a, $b);
    }

    /**
     * Subtracts two numbers with high precision.
     *
     * @param string $a First number.
     * @param string $b Second number.
     * @return string Result of the subtraction.
     * @throws InvalidArgumentException if the inputs are not valid numbers.
     */
    public function subtract(string $a, string $b): string
    {
        $this->validateNumber($a);
        $this->validateNumber($b);
        return bcsub($a, $b);
    }

    /**
     * Multiplies two numbers with high precision.
     *
     * @param string $a First number.
     * @param string $b Second number.
     * @return string Result of the multiplication.
     * @throws InvalidArgumentException if the inputs are not valid numbers.
     */
    public function multiply(string $a, string $b): string
    {
        $this->validateNumber($a);
        $this->validateNumber($b);
        return bcmul($a, $b);
    }

    /**
     * Divides two numbers with high precision.
     *
     * @param string $a First number.
     * @param string $b Second number.
     * @return string Result of the division.
     * @throws InvalidArgumentException if the inputs are not valid numbers or if division by zero is attempted.
     */
    public function divide(string $a, string $b): string
    {
        $this->validateNumber($a);
        $this->validateNumber($b);
        
        if ($b === '0') {
            throw new InvalidArgumentException('Division by zero is not allowed.');
        }

        return bcdiv($a, $b);
    }

    /**
     * Validates if a string is a valid number for BCMath operations.
     *
     * @param string $number The number to validate.
     * @throws InvalidArgumentException if the input is not a valid number.
     */
    private function validateNumber(string $number): void
    {
        if (!preg_match('/^-?\d+(\.\d+)?$/', $number)) {
            throw new InvalidArgumentException('Invalid number format: ' . $number);
        }
    }
}

// Example usage
try {
    $calculator = new MathCalculator();
    echo "Addition: " . $calculator->add('1.234', '5.678') . PHP_EOL;
    echo "Subtraction: " . $calculator->subtract('10.0', '3.5') . PHP_EOL;
    echo "Multiplication: " . $calculator->multiply('2.5', '4.0') . PHP_EOL;
    echo "Division: " . $calculator->divide('15.0', '3.0') . PHP_EOL;
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
```
