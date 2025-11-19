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
 * Function to calculate the total duration of the "Especialidad en Ortodoncia y Ortopedia Maxilofacial" program.
 * Duration is predefined as a constant value, but the function can be extended to accept dynamic inputs if needed.
 * The formatted duration is returned as a string for display on a webpage.
 */

// Define the program duration in months (constant)
const PROGRAM_DURATION_MONTHS = 36; // Example: 3 years = 36 months

/**
 * Converts the program duration into years and months
 * and formats it as a human-readable string.
 * 
 * @returns {string} Formatted duration string (e.g., "3 years and 0 months").
 */
function getFormattedProgramDuration() {
  try {
    // Calculate years and remaining months
    const years = Math.floor(PROGRAM_DURATION_MONTHS / 12);
    const months = PROGRAM_DURATION_MONTHS % 12;

    // Build the formatted duration string
    let formattedDuration = `${years} year${years !== 1 ? 's' : ''}`;
    if (months > 0) {
      formattedDuration += ` and ${months} month${months !== 1 ? 's' : ''}`;
    }

    return formattedDuration;
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error("An error occurred while calculating the program duration:", error);
    return "Duration unavailable"; // Fallback message
  }
}

// Example usage: Display the duration on a webpage
document.addEventListener("DOMContentLoaded", () => {
  try {
    // Get the element where the duration will be displayed
    const durationElement = document.getElementById("program-duration");

    if (durationElement) {
      // Calculate and set the formatted duration
      durationElement.textContent = getFormattedProgramDuration();
    } else {
      console.warn("Element with ID 'program-duration' not found on the page.");
    }
  } catch (error) {
    console.error("An error occurred while displaying the program duration:", error);
  }
});

/**
 * Note:
 * Ensure the webpage includes an element with the ID "program-duration"
 * where the program duration will be displayed.
 * Example:
 * <div id="program-duration"></div>
 */
```
