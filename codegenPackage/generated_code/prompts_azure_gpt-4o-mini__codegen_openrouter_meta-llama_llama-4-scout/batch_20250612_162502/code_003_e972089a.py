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
 * Calculates the total duration of the "Especialidad en Ortodoncia y Ortopedia Maxilofacial" program.
 * 
 * @param {Array<Object>} programDetails - Program details containing course information.
 * @param {string} programDetails[].name - Course name.
 * @param {number} programDetails[].durationInMonths - Course duration in months.
 * 
 * @returns {string} The total duration of the program in years and months, formatted for display.
 */
function calculateProgramDuration(programDetails) {
    try {
        // Validate input
        if (!Array.isArray(programDetails) || programDetails.length === 0) {
            throw new Error('Invalid program details');
        }

        // Calculate total duration in months
        let totalDurationInMonths = programDetails.reduce((acc, current) => {
            if (typeof current.durationInMonths !== 'number' || current.durationInMonths <= 0) {
                throw new Error(`Invalid duration for course: ${current.name}`);
            }
            return acc + current.durationInMonths;
        }, 0);

        // Convert total duration to years and months
        const years = Math.floor(totalDurationInMonths / 12);
        const remainingMonths = totalDurationInMonths % 12;

        // Format duration for display
        let durationString = '';
        if (years > 0) {
            durationString += `${years} año${years > 1 ? 's' : ''}`;
        }
        if (remainingMonths > 0) {
            if (durationString.length > 0) {
                durationString += ' y ';
            }
            durationString += `${remainingMonths} mes${remainingMonths > 1 ? 'es' : ''}`;
        }

        return durationString;
    } catch (error) {
        console.error('Error calculating program duration:', error.message);
        return 'Duración no disponible';
    }
}

// Example usage:
const programDetails = [
    { name: 'Curso 1', durationInMonths: 6 },
    { name: 'Curso 2', durationInMonths: 12 },
    { name: 'Curso 3', durationInMonths: 3 },
];

const duration = calculateProgramDuration(programDetails);
console.log(duration);

// For use in a webpage, you can use the following example:
// const programDurationElement = document.getElementById('program-duration');
// programDurationElement.textContent = calculateProgramDuration(programDetails);
```
