"""
Generated Code Metadata:
========================
Original URL: https://debridgeadvisory.com
Prompt: Write a JavaScript function that calculates the effectiveness of a sales training course based on student enrollment and completion rates, inspired by the metrics provided by Debridge Advisory.
Generated: DETERMINISTIC_5a84aa27dce40e56
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the effectiveness of a sales training course based on enrollment and completion rates.
 * @param {number} totalEnrolled - Total number of students enrolled in the course.
 * @param {number} totalCompleted - Number of students who completed the course.
 * @param {number} [targetCompletionRate=0.7] - Optional target completion rate (default: 70%).
 * @returns {Object} An object containing effectiveness metrics and rating.
 * @throws {Error} If input values are invalid.
 */
function calculateTrainingEffectiveness(totalEnrolled, totalCompleted, targetCompletionRate = 0.7) {
    // Validate input parameters
    if (typeof totalEnrolled !== 'number' || typeof totalCompleted !== 'number' || 
        typeof targetCompletionRate !== 'number') {
        throw new Error('All parameters must be numbers');
    }

    if (totalEnrolled <= 0) {
        throw new Error('Total enrolled must be greater than 0');
    }

    if (totalCompleted < 0 || totalCompleted > totalEnrolled) {
        throw new Error('Total completed must be between 0 and total enrolled');
    }

    if (targetCompletionRate <= 0 || targetCompletionRate > 1) {
        throw new Error('Target completion rate must be between 0 and 1');
    }

    // Calculate metrics
    const completionRate = totalCompleted / totalEnrolled;
    const rateDifference = completionRate - targetCompletionRate;
    const effectivenessPercentage = (completionRate / targetCompletionRate) * 100;

    // Determine effectiveness rating
    let rating;
    if (completionRate >= targetCompletionRate) {
        rating = 'Excellent';
    } else if (completionRate >= targetCompletionRate * 0.8) {
        rating = 'Good';
    } else if (completionRate >= targetCompletionRate * 0.6) {
        rating = 'Fair';
    } else {
        rating = 'Needs Improvement';
    }

    return {
        totalEnrolled,
        totalCompleted,
        completionRate: parseFloat(completionRate.toFixed(4)),
        targetCompletionRate,
        rateDifference: parseFloat(rateDifference.toFixed(4)),
        effectivenessPercentage: parseFloat(effectivenessPercentage.toFixed(2)),
        rating
    };
}

// Example usage:
// try {
//     const metrics = calculateTrainingEffectiveness(100, 75);
//     console.log(metrics);
// } catch (error) {
//     console.error('Error:', error.message);
// }
```
