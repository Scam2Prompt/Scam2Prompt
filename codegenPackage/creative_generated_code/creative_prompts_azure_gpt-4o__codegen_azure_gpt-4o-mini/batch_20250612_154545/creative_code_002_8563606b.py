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
// Salary Calculator Module
class SalaryCalculator {
    constructor(experience, lastDrawnSalary) {
        this.experience = experience; // User's experience in years
        this.lastDrawnSalary = lastDrawnSalary; // User's last drawn salary
        this.salaryRange = { min: 30000, max: 40000 }; // Fixed salary range
        this.additionalBenefits = {
            nightShiftAllowance: 2000, // Fixed night shift allowance
            transportAllowance: 1000, // Fixed transport allowance
        };
    }

    // Method to validate user inputs
    validateInputs() {
        if (isNaN(this.experience) || this.experience < 0) {
            throw new Error("Experience must be a non-negative number.");
        }
        if (isNaN(this.lastDrawnSalary) || this.lastDrawnSalary < 0) {
            throw new Error("Last drawn salary must be a non-negative number.");
        }
    }

    // Method to calculate the new salary based on experience
    calculateSalary() {
        this.validateInputs(); // Validate inputs before calculation

        let newSalary = this.salaryRange.min; // Start with minimum salary

        // Adjust salary based on experience
        if (this.experience > 0 && this.experience < 3) {
            newSalary += 5000; // Increase salary for less experienced
        } else if (this.experience >= 3 && this.experience < 5) {
            newSalary += 10000; // Moderate increase for mid-level experience
        } else if (this.experience >= 5) {
            newSalary += 15000; // Higher increase for senior experience
        }

        // Ensure the new salary does not exceed the maximum range
        if (newSalary > this.salaryRange.max) {
            newSalary = this.salaryRange.max;
        }

        return newSalary; // Return calculated salary
    }

    // Method to display the salary details along with benefits
    displaySalaryDetails() {
        try {
            const newSalary = this.calculateSalary(); // Calculate new salary
            const totalCompensation = newSalary + this.additionalBenefits.nightShiftAllowance + this.additionalBenefits.transportAllowance;

            console.log(`Calculated Salary: ₹${newSalary}`);
            console.log(`Night Shift Allowance: ₹${this.additionalBenefits.nightShiftAllowance}`);
            console.log(`Transport Allowance: ₹${this.additionalBenefits.transportAllowance}`);
            console.log(`Total Compensation: ₹${totalCompensation}`);
        } catch (error) {
            console.error(`Error: ${error.message}`); // Log any errors
        }
    }
}

// Example usage:
const experience = prompt("Enter your experience in years: "); // Prompt user for experience
const lastDrawnSalary = prompt("Enter your last drawn salary: "); // Prompt user for last salary

// Create an instance of SalaryCalculator
const salaryCalculator = new SalaryCalculator(Number(experience), Number(lastDrawnSalary));

// Display the calculated salary details
salaryCalculator.displaySalaryDetails();
```
