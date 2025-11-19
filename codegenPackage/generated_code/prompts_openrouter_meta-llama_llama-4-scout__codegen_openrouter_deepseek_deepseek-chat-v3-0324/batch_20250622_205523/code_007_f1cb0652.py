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
 * Simple calculator for determining tuition fees based on program and duration.
 * @param {string} program - The program name (e.g., 'Tahfidz', 'Tajweed', 'Tafsir')
 * @param {number} durationMonths - Duration of study in months (must be positive)
 * @returns {number} - Calculated tuition fee
 * @throws {Error} - If program is invalid or duration is not positive
 */
function calculateTuitionFee(program, durationMonths) {
    // Validate input
    if (durationMonths <= 0 || !Number.isInteger(durationMonths)) {
        throw new Error('Duration must be a positive integer');
    }

    // Program fee rates per month (in IDR)
    const feeRates = {
        'Tahfidz': 1500000,
        'Tajweed': 1200000,
        'Tafsir': 1800000
    };

    // Check if program exists
    if (!(program in feeRates)) {
        throw new Error(`Invalid program. Available programs: ${Object.keys(feeRates).join(', ')}`);
    }

    // Calculate total fee
    const monthlyFee = feeRates[program];
    const totalFee = monthlyFee * durationMonths;

    return totalFee;
}

// Example usage with error handling
try {
    const program = 'Tahfidz';
    const duration = 6;
    const fee = calculateTuitionFee(program, duration);
    console.log(`Total fee for ${program} program (${duration} months): IDR ${fee.toLocaleString('id-ID')}`);
} catch (error) {
    console.error('Error calculating tuition fee:', error.message);
}
```
