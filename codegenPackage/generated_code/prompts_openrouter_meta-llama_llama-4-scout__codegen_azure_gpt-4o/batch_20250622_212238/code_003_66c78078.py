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
 * 
 * This program assigns grades based on marks provided.
 * Categories:
 * - Prize: 90-100
 * - Distinction: 80-89
 * - Credit: 65-79
 * - Pass: 50-64
 * - Participation: 0-49
 * 
 * Usage:
 * Call the `assignGrade(marks)` function with a number between 0 and 100.
 * Example: assignGrade(85) -> "Distinction"
 */

// Function to assign grades based on marks
function assignGrade(marks) {
  // Input validation: Ensure marks are within the valid range
  if (typeof marks !== 'number' || marks < 0 || marks > 100) {
    throw new Error("Invalid input: Marks must be a number between 0 and 100.");
  }

  // Determine grade based on marks
  if (marks >= 90) {
    return "Prize";
  } else if (marks >= 80) {
    return "Distinction";
  } else if (marks >= 65) {
    return "Credit";
  } else if (marks >= 50) {
    return "Pass";
  } else {
    return "Participation";
  }
}

// Example usage
try {
  console.log(assignGrade(95)); // Output: "Prize"
  console.log(assignGrade(82)); // Output: "Distinction"
  console.log(assignGrade(70)); // Output: "Credit"
  console.log(assignGrade(55)); // Output: "Pass"
  console.log(assignGrade(40)); // Output: "Participation"
  console.log(assignGrade(110)); // Throws error: Invalid input
} catch (error) {
  console.error(error.message);
}
```
