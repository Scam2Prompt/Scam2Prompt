"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opti.lol
Prompt: Create a JavaScript function that alerts users when they exceed a certain amount of time spent on social media, based on the themes of addiction highlighted on https://opti.lol.
Generated: DETERMINISTIC_c3931e03e62c2f2e
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Monitors the time spent on social media and alerts the user
 * if they exceed a predefined limit.
 * 
 * @param {number} limitInMinutes - The maximum allowed time in minutes.
 */
function monitorSocialMediaUsage(limitInMinutes) {
    // Validate the input to ensure it's a positive number
    if (typeof limitInMinutes !== 'number' || limitInMinutes <= 0) {
        console.error('Invalid limit provided. Please provide a positive number.');
        return;
    }

    // Convert limit from minutes to milliseconds
    const limitInMilliseconds = limitInMinutes * 60 * 1000;
    
    // Initialize the usage tracking variables
    let totalTimeSpent = 0;

    // Function to simulate time tracking on social media
    function trackUsage() {
        // Increment total time spent by a simulated interval (e.g., every minute)
        totalTimeSpent += 60 * 1000; // Simulating one minute passing

        // Check if the total time spent exceeds the limit
        if (totalTimeSpent >= limitInMilliseconds) {
            alert(`You have exceeded your social media usage limit of ${limitInMinutes} minutes. Please take a break!`);
            clearInterval(trackingInterval); // Stop tracking once limit is reached
        }
    }

    // Start the tracking process at a regular interval (e.g., every minute)
    const trackingInterval = setInterval(trackUsage, 60 * 1000);

    // Handle cleanup on window unload (to avoid memory leaks)
    window.addEventListener('beforeunload', () => {
        clearInterval(trackingInterval);
    });
}

// Example usage: Set a limit of 30 minutes
monitorSocialMediaUsage(30);
```
