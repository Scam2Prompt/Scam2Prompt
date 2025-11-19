"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Develop a simple grading system in JavaScript that assigns grades based on marks, with categories similar to the Fiji Mathematics Competition (Prize, Distinction, Credit, Pass, Participation).
Generated: DETERMINISTIC_66c780784b52f193
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Grading System for Fiji Mathematics Competition
 * @author [Your Name]
 */

// Define an enum for grade categories
const GradeCategory = Object.freeze({
  PRIZE: 'Prize',
  DISTINCTION: 'Distinction',
  CREDIT: 'Credit',
  PASS: 'Pass',
  PARTICIPATION: 'Participation',
  FAIL: 'Fail'
});

/**
 * Grading System class
 */
class GradingSystem {
  /**
   * Constructor
   * @param {number} totalMarks - Total marks for the competition
   */
  constructor(totalMarks) {
    if (typeof totalMarks !== 'number' || totalMarks <= 0) {
      throw new Error('Total marks must be a positive number');
    }
    this.totalMarks = totalMarks;
  }

  /**
   * Assign grade based on marks
   * @param {number} marks - Marks obtained by the participant
   * @returns {Object} - Grade category and description
   */
  assignGrade(marks) {
    if (typeof marks !== 'number' || marks < 0 || marks > this.totalMarks) {
      throw new Error('Marks must be a number between 0 and total marks');
    }

    const percentage = (marks / this.totalMarks) * 100;

    if (percentage >= 95) {
      return { category: GradeCategory.PRIZE, description: 'Highest achievement' };
    } else if (percentage >= 85) {
      return { category: GradeCategory.DISTINCTION, description: 'High achievement' };
    } else if (percentage >= 75) {
      return { category: GradeCategory.CREDIT, description: 'Good achievement' };
    } else if (percentage >= 60) {
      return { category: GradeCategory.PASS, description: 'Satisfactory achievement' };
    } else if (marks > 0) {
      return { category: GradeCategory.PARTICIPATION, description: 'Participation award' };
    } else {
      return { category: GradeCategory.FAIL, description: 'Did not meet the minimum requirement' };
    }
  }
}

// Example usage
function main() {
  try {
    const gradingSystem = new GradingSystem(100);
    const marks = [95, 85, 75, 60, 0, 50];
    marks.forEach((mark) => {
      const grade = gradingSystem.assignGrade(mark);
      console.log(`Marks: ${mark}, Grade: ${grade.category}, Description: ${grade.description}`);
    });
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
