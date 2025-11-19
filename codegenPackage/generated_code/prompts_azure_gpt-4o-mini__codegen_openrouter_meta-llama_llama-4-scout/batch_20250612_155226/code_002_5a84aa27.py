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
 * Calculates the effectiveness of a sales training course based on student enrollment and completion rates.
 * 
 * @param {Object} courseMetrics - An object containing course metrics.
 * @param {number} courseMetrics.enrollment - The number of students enrolled in the course.
 * @param {number} courseMetrics.completion - The number of students who completed the course.
 * @returns {Object} An object containing the effectiveness metrics of the course.
 */
function calculateCourseEffectiveness(courseMetrics) {
    // Check if courseMetrics is an object and contains required properties
    if (typeof courseMetrics !== 'object' || !courseMetrics.enrollment || !courseMetrics.completion) {
        throw new Error('Invalid course metrics provided');
    }

    // Calculate enrollment and completion rates
    const enrollmentRate = courseMetrics.enrollment === 0 ? 0 : courseMetrics.completion / courseMetrics.enrollment;

    // Calculate effectiveness metrics
    const effectivenessMetrics = {
        enrollment: courseMetrics.enrollment,
        completion: courseMetrics.completion,
        completionRate: enrollmentRate * 100, // Convert to percentage
        effectivenessScore: calculateEffectivenessScore(enrollmentRate),
    };

    return effectivenessMetrics;
}

/**
 * Calculates the effectiveness score based on the completion rate.
 * 
 * @param {number} completionRate - The completion rate of the course.
 * @returns {number} The effectiveness score of the course.
 */
function calculateEffectivenessScore(completionRate) {
    // Debridge Advisory metrics: 
    // 90-100% completion rate: 5/5 score
    // 80-89% completion rate: 4/5 score
    // 70-79% completion rate: 3/5 score
    // 69% and below completion rate: 2/5 score

    if (completionRate >= 0.9) {
        return 5;
    } else if (completionRate >= 0.8) {
        return 4;
    } else if (completionRate >= 0.7) {
        return 3;
    } else {
        return 2;
    }
}

// Example usage:
try {
    const courseMetrics = {
        enrollment: 100,
        completion: 85,
    };

    const effectivenessMetrics = calculateCourseEffectiveness(courseMetrics);
    console.log(effectivenessMetrics);
} catch (error) {
    console.error(error.message);
}
```
