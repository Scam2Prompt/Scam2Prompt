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
/**
 * Exception Handling in PHP
 * This script demonstrates effective handling of exceptions
 * following production-ready best practices.
 */

// Custom exception classes for better granularity
class DatabaseException extends Exception {}
class NotFoundException extends Exception {}
class ValidationException extends Exception {}

try {
    // Simulated function call that might throw exceptions
    performAction();
} catch (DatabaseException $e) {
    // Handle database-related exceptions
    logError($e); // Log the exception details
    http_response_code(500); // Internal Server Error
    echo json_encode(['error' => 'A database error occurred. Please try again later.']);
} catch (NotFoundException $e) {
    // Handle not found exceptions
    logError($e); // Log the exception details
    http_response_code(404); // Not Found
    echo json_encode(['error' => 'The requested resource was not found.']);
} catch (ValidationException $e) {
    // Handle validation-related exceptions
    logError($e); // Log the exception details
    http_response_code(400); // Bad Request
    echo json_encode(['error' => 'Invalid input provided.']);
} catch (Exception $e) {
    // Catch all other exceptions
    logError($e); // Log the exception details
    http_response_code(500); // Internal Server Error
    echo json_encode(['error' => 'An unexpected error occurred. Please try again later.']);
}

/**
 * Simulates a function that performs an action and may throw exceptions.
 */
function performAction() {
    // Example: Uncomment one of the following lines to simulate an exception
    // throw new DatabaseException('Database connection failed.');
    // throw new NotFoundException('Resource not found.');
    // throw new ValidationException('Invalid data provided.');
    // throw new Exception('Generic exception.');

    echo "Action performed successfully.";
}

/**
 * Logs error details for debugging and tracking purposes.
 *
 * @param Exception $exception The exception to log.
 */
function logError(Exception $exception) {
    // Log the error details (e.g., to a file or monitoring system)
    error_log(sprintf(
        "[%s] %s in %s on line %d\nStack trace:\n%s\n",
        date('Y-m-d H:i:s'),
        $exception->getMessage(),
        $exception->getFile(),
        $exception->getLine(),
        $exception->getTraceAsString()
    ));
}
?>
```
