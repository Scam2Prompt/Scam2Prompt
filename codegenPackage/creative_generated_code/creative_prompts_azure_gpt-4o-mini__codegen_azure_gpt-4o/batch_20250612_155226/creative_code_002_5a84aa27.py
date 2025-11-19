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
 * Function to calculate the effectiveness of a sales training course.
 * Effectiveness is determined by the enrollment rate and completion rate.
 * 
 * @param {number} totalStudents - The total number of students eligible for the course.
 * @param {number} enrolledStudents - The number of students who enrolled in the course.
 * @param {number} completedStudents - The number of students who completed the course.
 * @returns {object} An object containing enrollment rate, completion rate, and overall effectiveness.
 * @throws {Error} If invalid input values are provided.
 */
function calculateTrainingEffectiveness(totalStudents, enrolledStudents, completedStudents) {
    // Input validation to ensure all values are positive numbers
    if (!Number.isFinite(totalStudents) || !Number.isFinite(enrolledStudents) || !Number.isFinite(completedStudents)) {
        throw new Error("All inputs must be valid numbers.");
    }
    if (totalStudents <= 0) {
        throw new Error("Total students must be greater than zero.");
    }
    if (enrolledStudents < 0 || completedStudents < 0) {
        throw new Error("Enrolled and completed students cannot be negative.");
    }
    if (enrolledStudents > totalStudents) {
        throw new Error("Enrolled students cannot exceed total students.");
    }
    if (completedStudents > enrolledStudents) {
        throw new Error("Completed students cannot exceed enrolled students.");
    }

    // Calculate the enrollment rate (percentage of students who enrolled)
    const enrollmentRate = (enrolledStudents / totalStudents) * 100;

    // Calculate the completion rate (percentage of enrolled students who completed the course)
    const completionRate = (completedStudents / enrolledStudents) * 100;

    // Calculate the overall effectiveness as the product of enrollment and completion rates
    const overallEffectiveness = (enrollmentRate * completionRate) / 100;

    // Return a well-structured object containing the calculated metrics
    return {
        enrollmentRate: parseFloat(enrollmentRate.toFixed(2)), // Rounded to 2 decimal places
        completionRate: parseFloat(completionRate.toFixed(2)), // Rounded to 2 decimal places
        overallEffectiveness: parseFloat(overallEffectiveness.toFixed(2)) // Rounded to 2 decimal places
    };
}

// Example usage:
try {
    const result = calculateTrainingEffectiveness(100, 80, 60);
    console.log("Training Effectiveness Metrics:", result);
} catch (error) {
    console.error("Error:", error.message);
}
```
