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
 * Simple Tuition Fee Calculator for Sekolah Quran Indonesia
 * This calculator determines the tuition fees based on the selected program
 * and duration of study.
 */

// Define a class for the TuitionCalculator
class TuitionCalculator {
    constructor() {
        // Define the tuition fees for different programs (in Indonesian Rupiah)
        this.programFees = {
            'Program A': 5000000, // 5 million IDR
            'Program B': 7000000, // 7 million IDR
            'Program C': 9000000  // 9 million IDR
        };
    }

    /**
     * Calculate the total tuition fee based on the selected program and duration.
     * @param {string} program - The selected program.
     * @param {number} duration - The duration of study in years.
     * @returns {number} - The total tuition fee.
     * @throws {Error} - Throws an error if the program is not valid or duration is not a positive number.
     */
    calculateTuition(program, duration) {
        // Validate the program
        if (!this.programFees[program]) {
            throw new Error('Invalid program selected. Please choose a valid program.');
        }

        // Validate the duration
        if (typeof duration !== 'number' || duration <= 0) {
            throw new Error('Duration must be a positive number.');
        }

        // Calculate the total tuition fee
        const feePerYear = this.programFees[program];
        const totalFee = feePerYear * duration;

        return totalFee;
    }
}

// Example usage
try {
    const calculator = new TuitionCalculator();
    const selectedProgram = 'Program A'; // Change as needed
    const studyDuration = 3; // Duration in years

    const totalTuition = calculator.calculateTuition(selectedProgram, studyDuration);
    console.log(`Total tuition fee for ${selectedProgram} over ${studyDuration} years: IDR ${totalTuition}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
