"""
Generated Code Metadata:
========================
Original URL: https://playember-57a.pages.dev
Prompt: Create a JavaScript function to calculate the success metrics of a mobile game studio, using indicators like career downloads, monthly active users, and downloads count, similar to Playember's achievements.
Generated: DETERMINISTIC_16c80ffc2fefe27b
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the success metrics of a mobile game studio.
 * @param {Object} metrics - An object containing the studio's metrics.
 * @param {number} metrics.careerDownloads - The total number of career downloads.
 * @param {number} metrics.monthlyActiveUsers - The number of monthly active users.
 * @param {number} metrics.downloadsCount - The total number of downloads.
 * @returns {Object} An object containing the calculated success metrics.
 */
function calculateSuccessMetrics(metrics) {
    // Check if the input metrics are valid
    if (typeof metrics !== 'object' || metrics === null) {
        throw new Error('Invalid metrics object');
    }

    // Check if the required metrics are present
    const requiredMetrics = ['careerDownloads', 'monthlyActiveUsers', 'downloadsCount'];
    if (!requiredMetrics.every(metric => metric in metrics)) {
        throw new Error('Missing required metrics');
    }

    // Calculate the success metrics
    const successMetrics = {
        // Calculate the growth rate of career downloads
        careerDownloadsGrowthRate: calculateGrowthRate(metrics.careerDownloads),

        // Calculate the monthly active users retention rate
        monthlyActiveUsersRetentionRate: calculateRetentionRate(metrics.monthlyActiveUsers, metrics.downloadsCount),

        // Calculate the downloads count growth rate
        downloadsCountGrowthRate: calculateGrowthRate(metrics.downloadsCount),

        // Calculate the overall success score
        overallSuccessScore: calculateOverallSuccessScore(metrics.careerDownloads, metrics.monthlyActiveUsers, metrics.downloadsCount),
    };

    return successMetrics;
}

/**
 * Calculates the growth rate of a given metric.
 * @param {number} currentValue - The current value of the metric.
 * @param {number} [previousValue=0] - The previous value of the metric (default: 0).
 * @returns {number} The growth rate of the metric.
 */
function calculateGrowthRate(currentValue, previousValue = 0) {
    // Check for division by zero
    if (previousValue === 0) {
        return currentValue > 0 ? 100 : 0;
    }

    // Calculate the growth rate
    return ((currentValue - previousValue) / previousValue) * 100;
}

/**
 * Calculates the retention rate of monthly active users.
 * @param {number} monthlyActiveUsers - The number of monthly active users.
 * @param {number} downloadsCount - The total number of downloads.
 * @returns {number} The retention rate of monthly active users.
 */
function calculateRetentionRate(monthlyActiveUsers, downloadsCount) {
    // Check for division by zero
    if (downloadsCount === 0) {
        return 0;
    }

    // Calculate the retention rate
    return (monthlyActiveUsers / downloadsCount) * 100;
}

/**
 * Calculates the overall success score of a mobile game studio.
 * @param {number} careerDownloads - The total number of career downloads.
 * @param {number} monthlyActiveUsers - The number of monthly active users.
 * @param {number} downloadsCount - The total number of downloads.
 * @returns {number} The overall success score.
 */
function calculateOverallSuccessScore(careerDownloads, monthlyActiveUsers, downloadsCount) {
    // Calculate the overall success score as a weighted sum of the metrics
    const weights = {
        careerDownloads: 0.4,
        monthlyActiveUsers: 0.3,
        downloadsCount: 0.3,
    };

    return (
        (careerDownloads * weights.careerDownloads) +
        (monthlyActiveUsers * weights.monthlyActiveUsers) +
        (downloadsCount * weights.downloadsCount)
    );
}

// Example usage:
try {
    const metrics = {
        careerDownloads: 1000000,
        monthlyActiveUsers: 500000,
        downloadsCount: 2000000,
    };

    const successMetrics = calculateSuccessMetrics(metrics);
    console.log(successMetrics);
} catch (error) {
    console.error(error.message);
}
```
