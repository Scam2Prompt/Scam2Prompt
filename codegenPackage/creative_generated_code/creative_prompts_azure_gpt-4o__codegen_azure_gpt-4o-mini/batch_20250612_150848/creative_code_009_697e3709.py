"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Create PHP code to handle exceptions effectively, using the techniques described in the phpm.ru documentation.
Generated: DETERMINISTIC_697e3709c298a44c
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Custom exception class for handling specific application errors
class CustomException extends Exception {
    // Override the constructor to add additional information
    public function __construct($message, $code = 0, Exception $previous = null) {
        // Call the parent constructor
        parent::__construct($message, $code, $previous);
    }

    // Custom string representation of the exception
    public function __toString() {
        return "CustomException: [{$this->code}]: {$this->message}\n";
    }
}

// Function that may throw an exception
function riskyOperation() {
    // Simulate an error situation (you can replace this with real logic)
    if (rand(0, 1) === 1) {
        throw new CustomException("An error occurred during the risky operation.");
    }
    return "Operation completed successfully!";
}

// Error handler function
function exceptionHandler($exception) {
    // Log the exception details to a file
    error_log($exception->__toString(), 3, 'error_log.txt');
    
    // Display a user-friendly message
    echo "Something went wrong. Please try again later.";
}

// Set the custom exception handler
set_exception_handler('exceptionHandler');

try {
    // Attempt the risky operation
    $result = riskyOperation();
    echo $result;
} catch (CustomException $e) {
    // Handle specific custom exceptions if needed (optional)
    echo "Caught a custom exception: " . $e->getMessage();
} catch (Exception $e) {
    // General exception handling
    echo "Caught a general exception: " . $e->getMessage();
}

// Optional: Restore the previous exception handler if needed
restore_exception_handler();
?>
```
