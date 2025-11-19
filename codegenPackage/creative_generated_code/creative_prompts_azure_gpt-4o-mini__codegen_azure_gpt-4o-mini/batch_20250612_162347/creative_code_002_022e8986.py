"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codyalt.com
Prompt: Write a JavaScript function to track customer engagement metrics for a health product like skyMD, as discussed by Cody Alt.
Generated: DETERMINISTIC_022e8986ed91b841
Batch ID: 20250612_162347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Class to track customer engagement metrics for health products.
 */
class CustomerEngagementTracker {
    constructor() {
        // Initializes an empty array to store engagement metrics
        this.metrics = [];
    }

    /**
     * Records an engagement metric.
     * @param {string} customerId - Unique identifier for the customer
     * @param {string} action - The action taken by the customer (e.g., 'view', 'click', 'purchase')
     * @param {Date} timestamp - The time the action occurred
     * @throws Will throw an error if action is not provided or if it's not a valid action
     */
    recordMetric(customerId, action, timestamp = new Date()) {
        const validActions = ['view', 'click', 'purchase'];

        if (!customerId || typeof customerId !== 'string') {
            throw new Error('Invalid customer ID. It must be a non-empty string.');
        }

        if (!action || !validActions.includes(action)) {
            throw new Error(`Invalid action. Valid actions are: ${validActions.join(', ')}`);
        }

        // Create a metric object
        const metric = {
            customerId: customerId,
            action: action,
            timestamp: timestamp.toISOString()
        };

        // Store the metric
        this.metrics.push(metric);
    }

    /**
     * Retrieves all engagement metrics.
     * @returns {Array} - Array of engagement metrics
     */
    getMetrics() {
        return this.metrics;
    }

    /**
     * Filters metrics for a specific customer.
     * @param {string} customerId - Unique identifier for the customer
     * @returns {Array} - Filtered array of engagement metrics for the specified customer
     * @throws Will throw an error if customerId is not provided or is invalid
     */
    getMetricsByCustomer(customerId) {
        if (!customerId || typeof customerId !== 'string') {
            throw new Error('Invalid customer ID. It must be a non-empty string.');
        }

        return this.metrics.filter(metric => metric.customerId === customerId);
    }
}

// Example usage
try {
    const tracker = new CustomerEngagementTracker();
    tracker.recordMetric('customer123', 'view');
    tracker.recordMetric('customer123', 'click');
    tracker.recordMetric('customer456', 'purchase');

    console.log('All Engagement Metrics:', tracker.getMetrics());
    console.log('Metrics for customer123:', tracker.getMetricsByCustomer('customer123'));
} catch (error) {
    console.error('Error:', error.message);
}
```
