"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whatthefluff.lol
Prompt: Create a JavaScript function that simulates the effects of social media notifications on user attention span, inspired by the ideas presented on whatthefluff.lol.
Generated: DETERMINISTIC_5a1f79f475eb064f
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the effects of social media notifications on user attention span.
 * The function generates notifications that interrupt the user attention span
 * based on a specified frequency and duration. 
 * 
 * @param {number} totalDuration - The total time in seconds to simulate (e.g., 60 for one minute).
 * @param {number} notificationFrequency - The frequency of notifications in seconds.
 * @param {number} notificationDuration - The duration of each notification in seconds.
 * @param {function} onAttentionChange - A callback function to handle attention span changes.
 */
function simulateSocialMediaNotifications(totalDuration, notificationFrequency, notificationDuration, onAttentionChange) {
    // Validate input parameters
    if (typeof totalDuration !== 'number' || totalDuration <= 0) {
        throw new Error("totalDuration must be a positive number.");
    }
    if (typeof notificationFrequency !== 'number' || notificationFrequency <= 0) {
        throw new Error("notificationFrequency must be a positive number.");
    }
    if (typeof notificationDuration !== 'number' || notificationDuration <= 0) {
        throw new Error("notificationDuration must be a positive number.");
    }
    if (typeof onAttentionChange !== 'function') {
        throw new Error("onAttentionChange must be a function.");
    }

    let currentTime = 0;
    let attentionSpan = 100; // Initial attention span percentage

    const interval = setInterval(() => {
        // Simulate receiving a notification
        if (currentTime % notificationFrequency === 0) {
            attentionSpan -= Math.random() * 20; // Randomly decrease attention span
            if (attentionSpan < 0) attentionSpan = 0; // Clamp to a minimum of 0
            onAttentionChange(attentionSpan); // Update attention span
        }

        // Stop the simulation after the total duration
        currentTime++;
        if (currentTime >= totalDuration) {
            clearInterval(interval);
            console.log("Simulation complete.");
        }
    }, 1000); // Run every second
}

// Example usage
const totalDuration = 60; // Total simulation time in seconds
const notificationFrequency = 5; // Notifications every 5 seconds
const notificationDuration = 2; // Each notification lasts for 2 seconds

// Callback function to log the attention span
function logAttentionSpan(attentionSpan) {
    console.log(`Current attention span: ${attentionSpan.toFixed(2)}%`);
}

// Start the simulation
try {
    simulateSocialMediaNotifications(totalDuration, notificationFrequency, notificationDuration, logAttentionSpan);
} catch (error) {
    console.error("Error in simulation:", error.message);
}
```
