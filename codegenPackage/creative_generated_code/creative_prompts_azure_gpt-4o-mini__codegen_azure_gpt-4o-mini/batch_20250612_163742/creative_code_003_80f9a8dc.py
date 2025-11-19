"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dropcoin.lol
Prompt: Create a JavaScript function that alerts users when they exceed a certain amount of time spent on social media, in line with the ideas presented on Dropcoin regarding digital addiction.
Generated: DETERMINISTIC_80f9a8dc7167e18e
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Monitors the time spent on social media and alerts the user if they exceed a specified limit.
 * 
 * @param {number} timeLimit - The time limit (in minutes) for social media usage.
 * @param {string} alertMessage - The message to display in the alert when the limit is exceeded.
 */
function monitorSocialMediaUsage(timeLimit, alertMessage) {
    // Check if the provided time limit is a valid number
    if (typeof timeLimit !== 'number' || timeLimit <= 0) {
        console.error('Invalid time limit. Please provide a positive number.');
        return;
    }

    // Initialize the timer variable
    let totalTimeSpent = 0;

    // Function to track time spent on social media
    function trackTime() {
        totalTimeSpent += 1; // Increment the time spent every minute

        // Check if the total time spent exceeds the limit
        if (totalTimeSpent >= timeLimit) {
            alert(alertMessage); // Alert the user
            clearInterval(timer); // Stop the timer
        }
    }

    // Start a timer that tracks the time every minute
    const timer = setInterval(trackTime, 60000); // 60000 ms = 1 minute

    // Function to stop the timer (e.g., when the user logs off)
    function stopTracking() {
        clearInterval(timer);
        console.log('Social media usage tracking has been stopped.');
    }

    // Return the stop function in case the user needs to stop tracking manually
    return stopTracking;
}

// Example usage:
const stopUsageTracking = monitorSocialMediaUsage(30, 'You have exceeded your 30-minute limit on social media. Please take a break!');

// To stop tracking manually, call:
// stopUsageTracking();
```
