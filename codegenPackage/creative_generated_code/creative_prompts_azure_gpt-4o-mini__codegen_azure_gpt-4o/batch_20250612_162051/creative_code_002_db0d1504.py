"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bda.mcupr.ac.th
Prompt: Write a JavaScript function that simulates the display of various Buddha images, including the Wednesday Night Buddha and Friday Buddha, as detailed on the BDA MCU webpage.
Generated: DETERMINISTIC_db0d150481302ff5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the display of various Buddha images based on the day of the week.
 * Each day has a specific Buddha image associated with it.
 * Includes Wednesday night Buddha and Friday Buddha.
 */

// Function to display Buddha images
function displayBuddhaImage(day) {
  // Map of Buddha images associated with each day
  const buddhaImages = {
    monday: "Monday Buddha - Representing peace and calm",
    tuesday: "Tuesday Buddha - Reflecting the Reclining Buddha",
    wednesday: "Wednesday Buddha (Day) - Standing Buddha holding an alms bowl",
    wednesdayNight: "Wednesday Buddha (Night) - Reclining Buddha",
    thursday: "Thursday Buddha - Meditation Buddha",
    friday: "Friday Buddha - Buddha contemplating with hands crossed",
    saturday: "Saturday Buddha - Buddha protected by the Naga (serpent)"
  };

  // Normalize the input to lower case for matching
  const normalizedDay = day.toLowerCase();

  // Validate the input and display the corresponding Buddha image
  if (normalizedDay === "wednesday night") {
    console.log(buddhaImages.wednesdayNight);
  } else if (buddhaImages[normalizedDay]) {
    console.log(buddhaImages[normalizedDay]);
  } else {
    // Error handling for invalid day input
    console.error(
      "Invalid day provided. Please enter a valid day of the week (e.g., 'Monday', 'Wednesday night', etc.)."
    );
  }
}

// Example Usage:
// Display Buddha images for different days of the week
displayBuddhaImage("Monday"); // Output: Monday Buddha - Representing peace and calm
displayBuddhaImage("Wednesday"); // Output: Wednesday Buddha (Day) - Standing Buddha holding an alms bowl
displayBuddhaImage("Wednesday night"); // Output: Wednesday Buddha (Night) - Reclining Buddha
displayBuddhaImage("Friday"); // Output: Friday Buddha - Buddha contemplating with hands crossed
displayBuddhaImage("InvalidDay"); // Error: Invalid day provided...
```
