"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vfrontier-crew.pages.dev
Prompt: How do I implement JavaScript error handling for applications like vFrontier Crew that require JavaScript to function?
Generated: DETERMINISTIC_150847d98bab96a8
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// vFrontier Crew Error Handling Implementation

/**
 * Custom error class for handling application-specific errors.
 */
class AppError extends Error {
    constructor(message, statusCode) {
        super(message);
        this.statusCode = statusCode;
        this.isOperational = true; // Indicates if the error is operational
        Error.captureStackTrace(this, this.constructor);
    }
}

/**
 * Centralized error handling middleware for Express applications.
 * @param {Object} err - The error object.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 * @param {Object} next - The next middleware function.
 */
function errorHandler(err, req, res, next) {
    const statusCode = err.statusCode || 500;
    const message = err.isOperational ? err.message : 'Something went very wrong!';

    // Log error details for debugging, can be enhanced to log to file or external service
    console.error('Error:', {
        message: err.message,
        stack: err.stack,
    });

    // Send response to client
    res.status(statusCode).json({
        status: 'error',
        statusCode,
        message,
    });
}

/**
 * Function to execute a task that may throw an error.
 * @param {Function} asyncFunc - The asynchronous function to execute.
 */
async function executeWithErrorHandling(asyncFunc) {
    try {
        await asyncFunc();
    } catch (error) {
        // Create a custom error and pass it to the centralized error handler
        if (error instanceof AppError) {
            throw error; // Re-throw operational errors to be handled by middleware
        }
        throw new AppError('An unexpected error occurred', 500); // General error
    }
}

// Example usage of executeWithErrorHandling
async function exampleTask() {
    // Simulate an operation that could throw an error
    throw new AppError('Failed to fetch crew data', 400);
}

// Sample Express setup
const express = require('express');
const app = express();

// Middleware to parse JSON bodies
app.use(express.json());

// Sample route
app.get('/crew', async (req, res, next) => {
    await executeWithErrorHandling(exampleTask);
    res.status(200).json({ message: 'Crew data fetched successfully!' });
});

// Use the centralized error handling middleware
app.use(errorHandler);

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
