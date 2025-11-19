"""
Generated Code Metadata:
========================
Original URL: https://job4chat.crediblejobs.in
Prompt: Generate code using JavaScript to calculate the salary range (₹30,000 to ₹40,000) based on user input for "Experience" and "Last Drawn Salary," and display additional benefits like "Night Shift Allowance" and "Transport Allowance."
Generated: DETERMINISTIC_8563606b02242ef2
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SalaryCalculator class to handle salary calculations based on user input
class SalaryCalculator {
    constructor(experience, lastDrawnSalary) {
        this.experience = experience; // User's experience in years
        this.lastDrawnSalary = lastDrawnSalary; // User's last drawn salary
        this.salaryRange = { min: 30000, max: 40000 }; // Defined salary range
        this.benefits = {
            nightShiftAllowance: 2000, // Fixed night shift allowance
            transportAllowance: 1500 // Fixed transport allowance
        };
    }

    // Method to calculate the new salary based on experience and last drawn salary
    calculateSalary() {
        try {
            // Validate inputs
            this.validateInputs();

            // Calculate new salary based on experience and last drawn salary
            let newSalary = this.lastDrawnSalary + (this.experience * 1000);
            newSalary = Math.max(this.salaryRange.min, Math.min(newSalary, this.salaryRange.max));

            return newSalary;
        } catch (error) {
            console.error("Error calculating salary:", error.message);
            return null; // Return null in case of an error
        }
    }

    // Method to validate user inputs
    validateInputs() {
        if (typeof this.experience !== 'number' || this.experience < 0) {
            throw new Error("Experience must be a non-negative number.");
        }
        if (typeof this.lastDrawnSalary !== 'number' || this.lastDrawnSalary < 0) {
            throw new Error("Last drawn salary must be a non-negative number.");
        }
    }

    // Method to get total benefits
    getTotalBenefits() {
        return this.benefits.nightShiftAllowance + this.benefits.transportAllowance;
    }

    // Method to display the salary and benefits
    displaySalaryAndBenefits() {
        const newSalary = this.calculateSalary();
        if (newSalary !== null) {
            const totalBenefits = this.getTotalBenefits();
            console.log(`New Salary: ₹${newSalary}`);
            console.log(`Total Benefits: ₹${totalBenefits}`);
            console.log(`Total Compensation: ₹${newSalary + totalBenefits}`);
        }
    }
}

// Example usage
const experience = 5; // User input for experience
const lastDrawnSalary = 28000; // User input for last drawn salary

const salaryCalculator = new SalaryCalculator(experience, lastDrawnSalary);
salaryCalculator.displaySalaryAndBenefits();
```
