"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Develop a JavaScript function to calculate the total cost of a course, including the 76-week Graduate Diploma of Management (Learning) program for $18,000.
Generated: DETERMINISTIC_2be3bdb8054a8a70
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a course.
 * 
 * @param {number} courseDuration - The duration of the course in weeks.
 * @param {number} courseCostPerWeek - The cost of the course per week.
 * @returns {number} The total cost of the course.
 */
function calculateCourseCost(courseDuration, courseCostPerWeek) {
    // Check if course duration and cost per week are valid numbers
    if (typeof courseDuration !== 'number' || typeof courseCostPerWeek !== 'number') {
        throw new Error('Course duration and cost per week must be numbers');
    }
    
    // Check if course duration and cost per week are positive
    if (courseDuration <= 0 || courseCostPerWeek <= 0) {
        throw new Error('Course duration and cost per week must be positive');
    }

    // Calculate the total cost of the course
    const totalCost = courseDuration * courseCostPerWeek;

    return totalCost;
}

/**
 * Calculates the total cost of the 76-week Graduate Diploma of Management (Learning) program.
 * 
 * @returns {number} The total cost of the Graduate Diploma of Management (Learning) program.
 */
function calculateGraduateDiplomaCost() {
    const courseDuration = 76; // weeks
    const courseCostPerWeek = 18000 / 76; // $18,000 for 76 weeks

    return calculateCourseCost(courseDuration, courseCostPerWeek);
}

// Example usage:
try {
    const graduateDiplomaCost = calculateGraduateDiplomaCost();
    console.log(`The total cost of the Graduate Diploma of Management (Learning) program is: $${graduateDiplomaCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
