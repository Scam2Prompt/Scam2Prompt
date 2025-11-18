"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lisk-snapshot.vercel.app
Prompt: Write code using the `@liskhq/lisk-utils` library (v0.4.0) to create a custom logging mechanism for a Lisk-based application.
Generated: DETERMINISTIC_2a1d28859e2fbc69
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the logger utility from the @liskhq/lisk-utils package
const { createLogger } = require('@liskhq/lisk-utils');

// Define a custom logging mechanism
class CustomLogger {
    constructor(logFilePath = 'logs/app.log', logLevel = 'info') {
        // Initialize the logger with file and console transport
        this.logger = createLogger({
            console: {
                // Log level for console
                level: logLevel,
                // Format for console logs
                format: 'plain',
            },
            file: {
                // Log level for file
                level: logLevel,
                // Path to the log file
                path: logFilePath,
                // Maximum size of the log file in bytes before rotation
                maxFileSize: 10 * 1024 * 1024, // 10 MB
                // Maximum number of rotated log files to keep
                maxFiles: 5,
            },
        });
    }

    // Log an informational message
    info(message, meta = {}) {
        this.logger.info({ message, ...meta });
    }

    // Log a warning message
    warn(message, meta = {}) {
        this.logger.warn({ message, ...meta });
    }

    // Log an error message
    error(message, meta = {}) {
        this.logger.error({ message, ...meta });
    }

    // Log a debug message
    debug(message, meta = {}) {
        this.logger.debug({ message, ...meta });
    }

    // Log a message with a custom level
    log(level, message, meta = {}) {
        if (this.logger[level]) {
            this.logger[level]({ message, ...meta });
        } else {
            // If the level is not recognized, fallback to 'info'
            this.logger.info({ message, ...meta });
        }
    }

    // Add additional metadata to the logger
    attachMeta(meta) {
        this.logger = this.logger.child(meta);
    }

    // Close the logger (useful for process shutdowns)
    close() {
        this.logger.end();
    }
}

// Example usage of the custom logger
function main() {
    try {
        // Create a logger instance
        const logger = new CustomLogger('logs/application.log', 'debug');

        // Log messages
        logger.info('Application started successfully');
        logger.debug('Debugging initialization', { module: 'main' });

        // Simulate a warning
        logger.warn('Low disk space warning', { diskSpace: '500MB' });

        // Simulate an error
        logger.error('Unhandled exception occurred', { stack: 'Stacktrace here...' });

        // Add metadata to all subsequent logs
        logger.attachMeta({ correlationId: '123456789' });
        logger.info('Log entry with attached metadata');

        // Close the logger
        logger.close();
    } catch (err) {
        console.error('Error initializing the logger:', err);
    }
}

// Run the main function
main();
```
