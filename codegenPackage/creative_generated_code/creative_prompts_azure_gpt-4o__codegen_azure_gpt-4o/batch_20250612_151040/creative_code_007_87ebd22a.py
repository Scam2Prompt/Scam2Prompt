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
 * Calculate and display the equivalent hours of traditional workouts
 * for a 20-minute electrostimulation training session.
 * This script assumes a fixed multiplier for conversion based on fitness industry standards.
 */

// Constant multiplier: How many hours of traditional workout a 20-minute EMS session equates to
const EMS_TO_TRADITIONAL_WORKOUT_RATIO = 4; // Example: 1 EMS session = 4 hours traditional workout

/**
 * Calculates the equivalent hours of traditional workouts.
 * @param {number} emsMinutes - Duration of the EMS session in minutes.
 * @return {number} Equivalent traditional workout hours.
 */
function calculateEquivalentWorkoutHours(emsMinutes) {
  if (emsMinutes <= 0) {
    throw new Error("EMS session duration must be a positive number.");
  }
  return (emsMinutes / 20) * EMS_TO_TRADITIONAL_WORKOUT_RATIO;
}

/**
 * Displays the calculated workout equivalence on the website.
 * @param {number} emsMinutes - Duration of the EMS session in minutes.
 */
function displayEquivalentWorkoutHours(emsMinutes) {
  try {
    const equivalentHours = calculateEquivalentWorkoutHours(emsMinutes);
    const message = `A ${emsMinutes}-minute electrostimulation training session is equivalent to approximately ${equivalentHours.toFixed(
      2
    )} hours of traditional workouts.`;

    // Display the message in a designated HTML element (e.g., div with ID 'workoutDisplay')
    const displayElement = document.getElementById("workoutDisplay");
    if (!displayElement) {
      throw new Error("Display element with ID 'workoutDisplay' not found.");
    }
    displayElement.textContent = message;
  } catch (error) {
    console.error("Error displaying workout equivalence:", error.message);
    alert("An error occurred while calculating the workout equivalence. Please try again.");
  }
}

// Example usage: calculate for a 20-minute EMS session
document.addEventListener("DOMContentLoaded", () => {
  const emsMinutes = 20; // You can dynamically change this value based on user input
  displayEquivalentWorkoutHours(emsMinutes);
});
```

**Note**: Ensure your HTML includes an element with the ID `workoutDisplay` for the script to function correctly. For example:

```html
<div id="workoutDisplay"></div>
```
