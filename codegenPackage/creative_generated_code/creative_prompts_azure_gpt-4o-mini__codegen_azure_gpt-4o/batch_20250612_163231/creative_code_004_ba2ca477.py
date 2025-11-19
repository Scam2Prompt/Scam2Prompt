"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-ss.com
Prompt: Write a JavaScript code that dynamically displays the specifications and modifications of the Cobalt SS, including features like the limited slip differential and Brembo brakes, based on user input.
Generated: DETERMINISTIC_ba2ca4771ddce168
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure (to be included in your index.html):
// <div id="car-details"></div>
// <input type="text" id="user-input" placeholder="Enter feature (e.g., 'brakes')">
// <button onclick="displaySpecifications()">Show Details</button>

// JavaScript code begins

// Car specifications data
const cobaltSSSpecifications = {
  overview: {
    model: "Cobalt SS",
    manufacturer: "Chevrolet",
    type: "Sport Compact",
    productionYears: "2005–2010",
  },
  features: {
    engine: "2.0L Turbocharged Inline-4",
    horsepower: 260,
    torque: "260 lb-ft",
    drivetrain: "Front-Wheel Drive (FWD)",
    limitedSlipDifferential: true,
    brakes: "Brembo Performance Brakes",
    suspension: "Sport-Tuned Suspension",
  },
  modifications: [
    "Cold air intake upgrade",
    "Performance exhaust system",
    "ECU tune for increased horsepower",
    "Upgraded turbocharger",
    "Aftermarket wheels and tires",
  ],
};

/**
 * Function to dynamically display car specifications and modifications
 * based on user input.
 */
function displaySpecifications() {
  const userInput = document.getElementById("user-input").value.trim().toLowerCase();
  const carDetailsDiv = document.getElementById("car-details");
  carDetailsDiv.innerHTML = ""; // Clear previous output

  try {
    if (!userInput) {
      // Display general overview if no specific input is provided
      carDetailsDiv.innerHTML = `
        <h3>Chevrolet Cobalt SS - Overview</h3>
        <p><strong>Model:</strong> ${cobaltSSSpecifications.overview.model}</p>
        <p><strong>Manufacturer:</strong> ${cobaltSSSpecifications.overview.manufacturer}</p>
        <p><strong>Type:</strong> ${cobaltSSSpecifications.overview.type}</p>
        <p><strong>Production Years:</strong> ${cobaltSSSpecifications.overview.productionYears}</p>
      `;
    } else if (cobaltSSSpecifications.features[userInput]) {
      // Display specific feature if it exists
      const featureValue = cobaltSSSpecifications.features[userInput];
      carDetailsDiv.innerHTML = `
        <h3>Feature Details</h3>
        <p><strong>${capitalize(userInput)}:</strong> ${featureValue}</p>
      `;
    } else if (userInput === "modifications") {
      // Display list of modifications
      carDetailsDiv.innerHTML = `
        <h3>Available Modifications</h3>
        <ul>
          ${cobaltSSSpecifications.modifications.map((mod) => `<li>${mod}</li>`).join("")}
        </ul>
      `;
    } else {
      // Handle invalid input
      carDetailsDiv.innerHTML = "<p style='color: red;'>Invalid input. Please try again.</p>";
    }
  } catch (error) {
    // Error handling
    console.error("An error occurred while displaying specifications:", error);
    carDetailsDiv.innerHTML = "<p style='color: red;'>An error occurred. Please try again later.</p>";
  }
}

/**
 * Utility function to capitalize the first letter of a string.
 * @param {string} str - The string to capitalize.
 * @returns {string} - The capitalized string.
 */
function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

// JavaScript code ends
```
