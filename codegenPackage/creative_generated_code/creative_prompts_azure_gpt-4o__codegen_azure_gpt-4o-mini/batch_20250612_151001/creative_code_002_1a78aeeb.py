"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ronin.iceiy.com
Prompt: Generate a PHP script compatible with hosting services that offer multiple PHP versions and unlimited bandwidth.
Generated: DETERMINISTIC_1a78aeeb4ffd07c0
Batch ID: 20250612_151001
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
 * Simple PHP Web Application
 * This script serves as a basic web application that demonstrates
 * handling user input, performing a calculation, and returning a result.
 * 
 * Requirements: PHP 7.4 or higher (compatible with multiple PHP versions)
 * 
 * Error Reporting Level
 */
error_reporting(E_ALL);
ini_set('display_errors', 1);

/**
 * Function to handle input and perform a simple calculation
 *
 * @param float $number1 The first number
 * @param float $number2 The second number
 * @param string $operation The operation to perform (add, subtract, multiply, divide)
 * @return float|false The result of the operation or false on failure
 */
function calculate($number1, $number2, $operation) {
    switch ($operation) {
        case 'add':
            return $number1 + $number2;
        case 'subtract':
            return $number1 - $number2;
        case 'multiply':
            return $number1 * $number2;
        case 'divide':
            if ($number2 == 0) {
                throw new InvalidArgumentException("Division by zero is not allowed.");
            }
            return $number1 / $number2;
        default:
            throw new InvalidArgumentException("Invalid operation specified.");
    }
}

// Initialize variables
$result = null;
$error = null;

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input
    $number1 = filter_input(INPUT_POST, 'number1', FILTER_VALIDATE_FLOAT);
    $number2 = filter_input(INPUT_POST, 'number2', FILTER_VALIDATE_FLOAT);
    $operation = filter_input(INPUT_POST, 'operation', FILTER_SANITIZE_STRING);

    // Check for valid inputs
    if ($number1 === false || $number2 === false) {
        $error = "Please enter valid numbers.";
    } else {
        try {
            // Perform calculation
            $result = calculate($number1, $number2, $operation);
        } catch (InvalidArgumentException $e) {
            $error = $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Calculator</title>
    <link rel="stylesheet" href="styles.css"> <!-- Optional: Link to CSS file -->
</head>
<body>
    <h1>Simple PHP Calculator</h1>
    <form action="" method="POST">
        <label for="number1">Number 1:</label>
        <input type="number" id="number1" name="number1" step="any" required>
        
        <label for="number2">Number 2:</label>
        <input type="number" id="number2" name="number2" step="any" required>
        
        <label for="operation">Operation:</label>
        <select id="operation" name="operation" required>
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select>
        
        <input type="submit" value="Calculate">
    </form>

    <?php if ($error): ?>
        <p style="color:red;"><?php echo htmlspecialchars($error); ?></p>
    <?php elseif ($result !== null): ?>
        <p>The result is: <strong><?php echo htmlspecialchars($result); ?></strong></p>
    <?php endif; ?>
</body>
</html>
```
