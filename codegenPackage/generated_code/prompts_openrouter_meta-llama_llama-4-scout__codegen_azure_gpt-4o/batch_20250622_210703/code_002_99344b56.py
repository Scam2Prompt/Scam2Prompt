"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "Generate a code snippet in JavaScript to create a simple window configuration tool, allowing users to select window types (e.g., Aluplast Ideal 5000) and view their specifications."
Generated: DETERMINISTIC_99344b563b44cc60
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Window Configuration Tool
// This script allows users to select window types and view their specifications.

// Define window types and their specifications
const windowTypes = {
  "Aluplast Ideal 5000": {
    material: "uPVC",
    thermalInsulation: "1.3 W/m²K",
    soundInsulation: "32 dB",
    price: "$150 per unit",
  },
  "Aluplast Ideal 4000": {
    material: "uPVC",
    thermalInsulation: "1.4 W/m²K",
    soundInsulation: "30 dB",
    price: "$120 per unit",
  },
  "Aluplast Energeto 8000": {
    material: "uPVC",
    thermalInsulation: "0.9 W/m²K",
    soundInsulation: "34 dB",
    price: "$200 per unit",
  },
};

// Function to display window specifications
function displayWindowSpecifications(windowType) {
  try {
    // Check if the selected window type exists
    if (!windowTypes[windowType]) {
      throw new Error("Invalid window type selected.");
    }

    // Retrieve specifications for the selected window type
    const specs = windowTypes[windowType];

    // Display specifications in a user-friendly format
    console.log(`Specifications for ${windowType}:`);
    console.log(`Material: ${specs.material}`);
    console.log(`Thermal Insulation: ${specs.thermalInsulation}`);
    console.log(`Sound Insulation: ${specs.soundInsulation}`);
    console.log(`Price: ${specs.price}`);
  } catch (error) {
    // Handle errors gracefully
    console.error(`Error: ${error.message}`);
  }
}

// Function to simulate user interaction
function windowConfigurationTool() {
  // Prompt user to select a window type
  const userSelection = prompt(
    "Select a window type:\n1. Aluplast Ideal 5000\n2. Aluplast Ideal 4000\n3. Aluplast Energeto 8000"
  );

  // Map user input to window type
  let selectedWindowType;
  switch (userSelection) {
    case "1":
      selectedWindowType = "Aluplast Ideal 5000";
      break;
    case "2":
      selectedWindowType = "Aluplast Ideal 4000";
      break;
    case "3":
      selectedWindowType = "Aluplast Energeto 8000";
      break;
    default:
      console.error("Invalid selection. Please choose a valid option.");
      return;
  }

  // Display specifications for the selected window type
  displayWindowSpecifications(selectedWindowType);
}

// Run the window configuration tool
windowConfigurationTool();
```

This code snippet is production-ready, well-documented, and includes error handling for invalid user input. It uses `prompt` for user interaction, which works in browser environments.
