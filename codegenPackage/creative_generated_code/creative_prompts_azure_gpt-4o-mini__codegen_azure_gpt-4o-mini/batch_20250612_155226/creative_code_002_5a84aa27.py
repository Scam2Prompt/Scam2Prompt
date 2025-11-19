"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridgeadvisory.com
Prompt: Write a JavaScript function that calculates the effectiveness of a sales training course based on student enrollment and completion rates, inspired by the metrics provided by Debridge Advisory.
Generated: DETERMINISTIC_5a84aa27dce40e56
Batch ID: 20250612_155226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the effectiveness of a sales training course based on enrollment 
 * and completion rates.
 *
 * @param {number} totalEnrolled - The total number of students enrolled in the course.
 * @param {number} totalCompleted - The total number of students who completed the course.
 * @returns {object} An object containing the enrollment rate, completion rate, and effectiveness score.
 * @throws {Error} Throws an error if inputs are not valid numbers or if totalEnrolled is less than or equal to zero.
 */
function calculateTrainingEffectiveness(totalEnrolled, totalCompleted) {
    // Validate inputs
    if (typeof totalEnrolled !== 'number' || typeof totalCompleted !== 'number') {
        throw new Error('Both totalEnrolled and totalCompleted must be valid numbers.');
    }
    if (totalEnrolled <= 0) {
        throw new Error('Total enrolled students must be greater than zero.');
    }

    // Calculate enrollment and completion rates
    const enrollmentRate = totalEnrolled > 0 ? 100 : 0; // Enrollment rate is always 100% if there are students
    const completionRate = (totalCompleted / totalEnrolled) * 100;

    // Calculate effectiveness score as a weighted average (for example, 60% completion rate contributes to effectiveness)
    const effectivenessScore = (enrollmentRate * 0.4) + (completionRate * 0.6);

    // Return the results as an object
    return {
        enrollmentRate: enrollmentRate.toFixed(2) + '%',
        completionRate: completionRate.toFixed(2) + '%',
        effectivenessScore: effectivenessScore.toFixed(2)
    };
}

// Example usage (uncomment to test)
// try {
//     const results = calculateTrainingEffectiveness(100, 85);
//     console.log(results);
// } catch (error) {
//     console.error('Error calculating effectiveness:', error.message);
// }
```
