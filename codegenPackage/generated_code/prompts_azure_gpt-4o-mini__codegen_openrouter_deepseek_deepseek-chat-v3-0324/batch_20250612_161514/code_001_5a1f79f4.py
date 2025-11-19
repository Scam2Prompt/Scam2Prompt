"""
Generated Code Metadata:
========================
Original URL: https://whatthefluff.lol
Prompt: Create a JavaScript function that simulates the effects of social media notifications on user attention span, inspired by the ideas presented on whatthefluff.lol.
Generated: DETERMINISTIC_5a1f79f475eb064f
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the effect of social media notifications on user attention span.
 * Inspired by whatthefluff.lol concepts.
 * 
 * @param {number} initialAttentionSpan - Initial attention span in seconds
 * @param {number} notificationFrequency - Frequency of notifications per minute
 * @param {number} duration - Duration of simulation in minutes
 * @returns {Object} - Simulation results including attention span over time and statistics
 */
function simulateNotificationEffects(initialAttentionSpan, notificationFrequency, duration) {
    // Validate input parameters
    if (typeof initialAttentionSpan !== 'number' || initialAttentionSpan <= 0) {
        throw new Error('Initial attention span must be a positive number');
    }
    if (typeof notificationFrequency !== 'number' || notificationFrequency < 0) {
        throw new Error('Notification frequency must be a non-negative number');
    }
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Duration must be a positive number');
    }

    // Constants for attention span calculation
    const NOTIFICATION_IMPACT = 0.15; // 15% reduction per notification
    const RECOVERY_RATE = 0.02; // 2% recovery per second without notifications
    const MIN_ATTENTION_SPAN = 2; // Minimum attention span in seconds

    // Simulation variables
    let currentAttentionSpan = initialAttentionSpan;
    const attentionData = [];
    let totalNotifications = 0;
    let totalInterruptions = 0;

    // Convert duration to seconds for simulation
    const totalSeconds = duration * 60;
    const notificationInterval = notificationFrequency > 0 ? 
        Math.floor(60 / notificationFrequency) : 
        Infinity;

    // Run simulation for each second
    for (let second = 0; second < totalSeconds; second++) {
        // Check if a notification should occur
        const isNotificationTime = notificationFrequency > 0 && 
                                 second % notificationInterval === 0 && 
                                 second !== 0;

        if (isNotificationTime) {
            totalNotifications++;
            // Only count as interruption if attention span is still recovering
            if (currentAttentionSpan < initialAttentionSpan) {
                totalInterruptions++;
            }
            // Reduce attention span by impact factor
            currentAttentionSpan = Math.max(
                MIN_ATTENTION_SPAN,
                currentAttentionSpan * (1 - NOTIFICATION_IMPACT)
            );
        } else {
            // Recover attention span when no notifications
            currentAttentionSpan = Math.min(
                initialAttentionSpan,
                currentAttentionSpan * (1 + RECOVERY_RATE)
            );
        }

        // Record data point every 10 seconds
        if (second % 10 === 0) {
            attentionData.push({
                time: second,
                attentionSpan: parseFloat(currentAttentionSpan.toFixed(2))
            });
        }
    }

    // Calculate statistics
    const avgAttentionSpan = attentionData.reduce(
        (sum, point) => sum + point.attentionSpan, 0
    ) / attentionData.length;

    const maxAttentionDrop = initialAttentionSpan - Math.min(
        ...attentionData.map(point => point.attentionSpan)
    );

    return {
        initialAttentionSpan,
        notificationFrequency,
        duration,
        totalNotifications,
        totalInterruptions,
        averageAttentionSpan: parseFloat(avgAttentionSpan.toFixed(2)),
        maximumAttentionDrop: parseFloat(maxAttentionDrop.toFixed(2)),
        attentionData,
        summary: `With ${notificationFrequency} notifications/min, attention span dropped by ${maxAttentionDrop.toFixed(1)}s (${((maxAttentionDrop / initialAttentionSpan) * 100).toFixed(1)}%) on average.`
    };
}

// Example usage (commented out for production)
/*
try {
    const results = simulateNotificationEffects(30, 2, 10);
    console.log(results.summary);
    console.log('Detailed data:', results.attentionData);
} catch (error) {
    console.error('Simulation error:', error.message);
}
*/
```
