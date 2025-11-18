"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://job4chat.crediblejobs.in
Prompt: Generate code using JavaScript to calculate the salary range (₹30,000 to ₹40,000) based on user input for "Experience" and "Last Drawn Salary," and display additional benefits like "Night Shift Allowance" and "Transport Allowance."
Generated: DETERMINISTIC_8563606b02242ef2
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate and display salary range and additional benefits
 * based on user input for "Experience" and "Last Drawn Salary".
 * The salary range is capped between ₹30,000 to ₹40,000.
 */

// Function to calculate salary range
function calculateSalaryRange(experience, lastDrawnSalary) {
  try {
    // Validate inputs
    if (typeof experience !== 'number' || typeof lastDrawnSalary !== 'number') {
      throw new Error('Experience and Last Drawn Salary must be valid numbers.');
    }
    if (experience < 0 || lastDrawnSalary < 0) {
      throw new Error('Experience and Last Drawn Salary cannot be negative.');
    }

    // Base salary calculation logic
    let baseSalary = lastDrawnSalary + experience * 1000;

    // Ensure salary falls within range ₹30,000 to ₹40,000
    let adjustedSalary = Math.max(30000, Math.min(baseSalary, 40000));

    return adjustedSalary;
  } catch (error) {
    console.error('Error calculating salary range:', error.message);
    return null; // Return null in case of error
  }
}

// Function to display additional benefits
function displayBenefits() {
  return {
    nightShiftAllowance: '₹3,000',
    transportAllowance: '₹2,000',
  };
}

// Main function to handle user input and display results
function main() {
  // Example user inputs
  const userExperience = prompt('Enter your years of experience (as a number):');
  const lastDrawnSalary = prompt('Enter your last drawn salary (as a number):');

  // Parse inputs
  const experience = parseFloat(userExperience);
  const salary = parseFloat(lastDrawnSalary);

  // Calculate salary range
  const finalSalary = calculateSalaryRange(experience, salary);

  if (finalSalary !== null) {
    console.log('Calculated Salary Range:', `₹${finalSalary}`);
    const benefits = displayBenefits();
    console.log('Additional Benefits:');
    console.log('Night Shift Allowance:', benefits.nightShiftAllowance);
    console.log('Transport Allowance:', benefits.transportAllowance);
  } else {
    console.log('Failed to calculate salary range due to invalid input.');
  }
}

// Run the program
main();
```
