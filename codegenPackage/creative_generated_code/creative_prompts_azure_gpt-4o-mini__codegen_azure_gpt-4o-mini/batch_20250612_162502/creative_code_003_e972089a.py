"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Develop a function in JavaScript that calculates the total duration of the "Especialidad en Ortodoncia y Ortopedia Maxilofacial" program and formats it for display on a webpage.
Generated: DETERMINISTIC_e972089a34038a51
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total duration of the "Especialidad en Ortodoncia y Ortopedia Maxilofacial" program
 * and format it for display on a webpage.
 *
 * @returns {string} The formatted duration of the program.
 */
function calculateProgramDuration() {
    try {
        // Define the duration of the program in months
        const programDurationMonths = 24;

        // Calculate years and remaining months
        const years = Math.floor(programDurationMonths / 12);
        const months = programDurationMonths % 12;

        // Construct formatted duration string
        let formattedDuration = '';

        if (years > 0) {
            formattedDuration += `${years} year${years > 1 ? 's' : ''}`;
        }
        if (months > 0) {
            if (formattedDuration) {
                formattedDuration += ' and ';
            }
            formattedDuration += `${months} month${months > 1 ? 's' : ''}`;
        }

        // Return the formatted duration
        return formattedDuration || '0 months';
    } catch (error) {
        // Log error to the console for debugging purposes
        console.error('Error calculating program duration:', error);
        return 'Error calculating duration';
    }
}

// Example usage: Display the program duration on a webpage
document.addEventListener('DOMContentLoaded', () => {
    const durationElement = document.getElementById('program-duration');
    if (durationElement) {
        durationElement.textContent = calculateProgramDuration();
    } else {
        console.warn('Element with ID "program-duration" not found.');
    }
});
```
