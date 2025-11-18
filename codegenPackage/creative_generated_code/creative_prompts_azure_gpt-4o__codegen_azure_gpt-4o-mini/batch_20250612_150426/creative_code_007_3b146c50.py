"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomchromeextension.flazio.com
Prompt: Develop a script to monitor and log the activities performed by the Phantom Chrome Extension for productivity analytics.
Generated: DETERMINISTIC_3b146c500214dbf9
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Phantom Chrome Extension Activity Logger
// This script monitors and logs user activities performed by the Phantom Chrome Extension for productivity analytics.

const activityLog = [];
const logFileName = 'activity_log.json';

// Function to log activities
function logActivity(activity) {
    const timestamp = new Date().toISOString();
    const logEntry = {
        timestamp,
        activity,
    };

    // Push the new log entry to the activityLog array
    activityLog.push(logEntry);
    console.log(`Logged activity: ${activity}`);

    // Persist the log to a file
    saveLogToFile();
}

// Function to save log to a file
function saveLogToFile() {
    try {
        // Convert the activity log to a JSON string
        const logData = JSON.stringify(activityLog, null, 2);
        
        // Use the Chrome API to download the log file
        const blob = new Blob([logData], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        
        // Create a temporary link element for the download
        const a = document.createElement('a');
        a.href = url;
        a.download = logFileName;
        document.body.appendChild(a);
        a.click();
        
        // Clean up
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    } catch (error) {
        console.error('Error saving log to file:', error);
    }
}

// Example usage of logging activities
// This function can be called on various user interactions
function onUserAction(action) {
    if (typeof action === 'string' && action.trim() !== '') {
        logActivity(action);
    } else {
        console.warn('Invalid action. Action must be a non-empty string.');
    }
}

// Initialize the logger
function initLogger() {
    console.log('Phantom Chrome Extension Activity Logger Initialized');
}

// Entry point of the script
initLogger();

// Simulating user actions for demonstration
setTimeout(() => onUserAction('User clicked on the extension icon'), 2000);
setTimeout(() => onUserAction('User navigated to settings'), 4000);
setTimeout(() => onUserAction('User logged out'), 6000);
```

This code provides a simple activity logger for the Phantom Chrome Extension, capturing user actions and saving them to a JSON file. It includes error handling and input validation for robustness.
