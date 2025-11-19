"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: "Write a code snippet in JavaScript for a simple calculator to determine tuition fees based on the program and duration of study at an educational institution like Sekolah Quran Indonesia."
Generated: DETERMINISTIC_f1cb0652744012ab
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Tuition Fee Calculator
 * Calculates tuition fees based on the program and duration of study.
 * 
 * Programs and their fees per month:
 * - Quran Studies: $100
 * - Islamic Studies: $150
 * - Arabic Language: $120
 * 
 * Usage:
 * Call `calculateTuitionFee(program, duration)` with the program name and duration in months.
 */

function calculateTuitionFee(program, duration) {
    // Validate input
    if (typeof program !== 'string' || typeof duration !== 'number' || duration <= 0) {
        throw new Error("Invalid input. Program must be a string and duration must be a positive number.");
    }

    // Define tuition fees per program
    const tuitionFees = {
        "Quran Studies": 100,
        "Islamic Studies": 150,
        "Arabic Language": 120
    };

    // Check if the program exists
    if (!tuitionFees[program]) {
        throw new Error(`Invalid program. Available programs are: ${Object.keys(tuitionFees).join(", ")}`);
    }

    // Calculate total tuition fee
    const feePerMonth = tuitionFees[program];
    const totalFee = feePerMonth * duration;

    return totalFee;
}

// Example usage
try {
    const program = "Quran Studies"; // Program name
    const duration = 6; // Duration in months
    const totalFee = calculateTuitionFee(program, duration);
    console.log(`Total tuition fee for ${program} (${duration} months): $${totalFee}`);
} catch (error) {
    console.error(error.message);
}
```
