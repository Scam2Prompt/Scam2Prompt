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
session_start();

/**
 * Generates a random math problem.
 * The generated problem will be a simple addition or subtraction.
 *
 * @return string The math problem as a string (e.g., "6 + 10").
 */
function generateMathProblem() {
    $num1 = rand(1, 20);
    $num2 = rand(1, 20);
    $operator = rand(0, 1) == 0 ? '+' : '-'; // Randomly choose between addition and subtraction
    $_SESSION['captcha_answer'] = ($operator === '+') ? ($num1 + $num2) : ($num1 - $num2);
    
    return "$num1 $operator $num2";
}

/**
 * Validates the user's answer against the generated CAPTCHA answer.
 *
 * @param int $userAnswer The answer submitted by the user.
 * @return bool True if the answer is correct, false otherwise.
 */
function validateCaptcha($userAnswer) {
    if (!isset($_SESSION['captcha_answer'])) {
        throw new Exception("CAPTCHA answer not set in session.");
    }

    return (int)$userAnswer === $_SESSION['captcha_answer'];
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if the answer is provided
    if (isset($_POST['captcha_answer'])) {
        try {
            $userAnswer = $_POST['captcha_answer'];
            
            if (validateCaptcha($userAnswer)) {
                echo "CAPTCHA passed!";
                // Proceed with the form submission or further processing
            } else {
                echo "Incorrect CAPTCHA answer. Please try again.";
            }
        } catch (Exception $e) {
            echo "Error: " . $e->getMessage();
        }
    }
}

// Generate a new CAPTCHA problem
$mathProblem = generateMathProblem();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CAPTCHA System</title>
</head>
<body>
    <h1>CAPTCHA Verification</h1>
    <form method="POST" action="">
        <label for="captcha"><?php echo $mathProblem; ?> = ?</label>
        <input type="text" name="captcha_answer" id="captcha" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
