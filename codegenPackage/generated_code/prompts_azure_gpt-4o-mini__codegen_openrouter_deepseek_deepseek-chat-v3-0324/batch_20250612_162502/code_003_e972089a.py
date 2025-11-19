"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: Develop a function in JavaScript that calculates the total duration of the "Especialidad en Ortodoncia y Ortopedia Maxilofacial" program and formats it for display on a webpage.
Generated: DETERMINISTIC_e972089a34038a51
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total duration of the "Especialidad en Ortodoncia y Ortopedia Maxilofacial" program
 * and formats it for display on a webpage.
 * 
 * @param {Object} programData - Contains program duration information
 * @param {number} programData.years - Number of years in the program
 * @param {number} programData.months - Number of months in the program (beyond full years)
 * @param {number} programData.hours - Total hours in the program
 * @returns {string} Formatted duration string for display
 * @throws {Error} If input data is invalid
 */
function formatProgramDuration(programData) {
    // Validate input
    if (!programData || typeof programData !== 'object') {
        throw new Error('Invalid program data: must be an object');
    }

    const { years, months, hours } = programData;

    if (years === undefined || months === undefined || hours === undefined) {
        throw new Error('Invalid program data: missing required properties (years, months, hours)');
    }

    if (typeof years !== 'number' || typeof months !== 'number' || typeof hours !== 'number') {
        throw new Error('Invalid program data: years, months, and hours must be numbers');
    }

    if (years < 0 || months < 0 || hours < 0) {
        throw new Error('Invalid program data: duration values cannot be negative');
    }

    // Calculate total months
    const totalMonths = years * 12 + months;

    // Format the duration string
    let durationString = '';

    if (years > 0) {
        durationString += `${years} año${years !== 1 ? 's' : ''}`;
    }

    if (months > 0) {
        if (durationString.length > 0) {
            durationString += ' y ';
        }
        durationString += `${months} mes${months !== 1 ? 'es' : ''}`;
    }

    if (durationString.length > 0) {
        durationString += ` (${totalMonths} meses)`;
    }

    // Add hours information
    durationString += `, ${hours} horas`;

    return durationString;
}

// Example usage:
// const programData = { years: 2, months: 6, hours: 1200 };
// const formattedDuration = formatProgramDuration(programData);
// console.log(formattedDuration); // "2 años y 6 meses (30 meses), 1200 horas"
```
