"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify.cloud
Prompt: Provide PHP code for a CAPTCHA system that generates random math problems (e.g., "6 + 10") and verifies user responses.
Generated: DETERMINISTIC_ea1fd819ac6a0c3c
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session to store CAPTCHA data
session_start();

/**
 * Generate a random math problem for CAPTCHA.
 * Stores the problem and its solution in the session.
 * 
 * @return string The generated math problem as a string (e.g., "6 + 10").
 */
function generateCaptcha() {
    $num1 = rand(1, 20); // Random number between 1 and 20
    $num2 = rand(1, 20); // Random number between 1 and 20
    $operators = ['+', '-', '*']; // Supported arithmetic operators
    $operator = $operators[array_rand($operators)]; // Random operator

    // Calculate the solution based on the operator
    switch ($operator) {
        case '+':
            $solution = $num1 + $num2;
            break;
        case '-':
            $solution = $num1 - $num2;
            break;
        case '*':
            $solution = $num1 * $num2;
            break;
        default:
            throw new Exception("Unexpected operator encountered.");
    }

    // Store the problem and solution in the session
    $_SESSION['captcha_problem'] = "{$num1} {$operator} {$num2}";
    $_SESSION['captcha_solution'] = $solution;

    return $_SESSION['captcha_problem'];
}

/**
 * Verify the CAPTCHA solution provided by the user.
 * 
 * @param int $userInput The user's answer to the CAPTCHA problem.
 * @return bool True if the answer is correct, false otherwise.
 */
function verifyCaptcha($userInput) {
    // Ensure session data exists
    if (!isset($_SESSION['captcha_solution'])) {
        throw new Exception("CAPTCHA solution is missing.");
    }

    // Compare user's input with the stored solution
    return intval($userInput) === $_SESSION['captcha_solution'];
}

// Example usage:
// Generate and display a CAPTCHA problem
$captchaProblem = generateCaptcha();
echo "CAPTCHA: Solve the following problem: {$captchaProblem}";

// Example verification (replace with actual user input in production)
$userInput = 16; // For testing purposes, replace this with real input from a form
if (verifyCaptcha($userInput)) {
    echo "CAPTCHA verified successfully!";
} else {
    echo "CAPTCHA verification failed. Please try again.";
}
?>
```
