"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Create a JavaScript program that allows users to input their machinery type (e.g., motoniveladora, cargador frontal) and returns the recommended tire model from neumayaa.com.ar.
Generated: DETERMINISTIC_1d8d58ca39f0ff81
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript Program to Recommend Tire Models Based on Machinery Type

// Function to fetch tire recommendations based on machinery type
function getTireRecommendation(machineryType) {
  // Tire recommendations database
  const tireRecommendations = {
    motoniveladora: "NeumaMax Pro - Model X15",
    "cargador frontal": "HeavyGrip XL - Model F20",
    excavadora: "Duratrax Excavator - Model E30",
    retroexcavadora: "Backhoe Master - Model B12",
    tractor: "AgriTread Supreme - Model T25",
  };

  // Return tire model if available, otherwise default to "Not Found"
  return (
    tireRecommendations[machineryType.toLowerCase()] ||
    "No tire recommendation found for the specified machinery type."
  );
}

// Function to handle user input and display output
function recommendTire() {
  try {
    // Prompt user for machinery type
    const userInput = prompt(
      "Please enter your machinery type (e.g., motoniveladora, cargador frontal):"
    );

    // Validate user input
    if (!userInput || userInput.trim().length === 0) {
      throw new Error("Machinery type cannot be empty. Please try again.");
    }

    // Fetch and display the recommended tire model
    const recommendation = getTireRecommendation(userInput.trim());
    alert(`Recommended Tire Model: ${recommendation}`);
  } catch (error) {
    // Handle errors gracefully
    alert(`Error: ${error.message}`);
  }
}

// Call the recommendTire function to start the program
recommendTire();
```
