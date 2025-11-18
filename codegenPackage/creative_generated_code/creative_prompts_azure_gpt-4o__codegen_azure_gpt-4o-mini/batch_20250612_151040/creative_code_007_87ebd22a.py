"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitebody.com.br
Prompt: Create JavaScript code to calculate and display the equivalent hours of traditional workouts for a 20-minute electrostimulation training session on a fitness studio website.
Generated: DETERMINISTIC_87ebd22aeeb05bea
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the equivalent hours of traditional workouts
 * based on a 20-minute electrostimulation training session.
 * 
 * @param {number} electroSessionMinutes - The duration of the electrostimulation session in minutes.
 * @returns {number} The equivalent hours of traditional workouts.
 */
function calculateEquivalentWorkoutHours(electroSessionMinutes) {
    // Define the conversion ratio: 20 minutes of electrostimulation is equivalent to 1 hour of traditional workout
    const conversionRatio = 60 / 20;

    // Calculate equivalent hours
    const equivalentHours = (electroSessionMinutes * conversionRatio) / 60;

    return equivalentHours;
}

/**
 * Function to display the equivalent workout hours on the webpage.
 */
function displayEquivalentWorkoutHours() {
    // Get the duration of the electrostimulation session (20 minutes)
    const electroSessionMinutes = 20;

    try {
        // Calculate equivalent hours
        const equivalentHours = calculateEquivalentWorkoutHours(electroSessionMinutes);

        // Get the display element (assumed to be present in the HTML)
        const displayElement = document.getElementById('equivalent-workout-hours');

        // Check if display element exists
        if (!displayElement) {
            throw new Error('Display element for equivalent workout hours not found.');
        }

        // Display the result
        displayElement.textContent = `Equivalent hours of traditional workout: ${equivalentHours.toFixed(2)} hours`;
    } catch (error) {
        console.error('Error displaying equivalent workout hours:', error);
        // Optionally, display an error message to the user
        const displayElement = document.getElementById('equivalent-workout-hours');
        if (displayElement) {
            displayElement.textContent = 'Error calculating equivalent workout hours.';
        }
    }
}

// Run the display function on page load
document.addEventListener('DOMContentLoaded', () => {
    displayEquivalentWorkoutHours();
});
```
