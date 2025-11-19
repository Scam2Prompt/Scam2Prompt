"""
Generated Code Metadata:
========================
Original URL: https://hingehealth.eu
Prompt: How do I generate a simple health risk assessment tool using JavaScript and relevant health data libraries?
Generated: DETERMINISTIC_1ee313aea32733aa
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Health Risk Assessment Tool
 * This tool calculates a basic health risk score based on user input.
 * It uses BMI (Body Mass Index) as a primary metric for risk assessment.
 * 
 * Dependencies: None (Vanilla JavaScript)
 * Note: For production, consider integrating with health data libraries like WHO or CDC APIs.
 */

// Function to calculate BMI
function calculateBMI(weightKg, heightCm) {
  try {
    if (weightKg <= 0 || heightCm <= 0) {
      throw new Error("Weight and height must be positive numbers.");
    }
    const heightMeters = heightCm / 100; // Convert height to meters
    return (weightKg / (heightMeters ** 2)).toFixed(2); // Return BMI rounded to 2 decimal places
  } catch (error) {
    console.error("Error calculating BMI:", error.message);
    return null;
  }
}

// Function to assess health risk based on BMI
function assessHealthRisk(bmi) {
  if (bmi === null) {
    return "Unable to assess health risk due to invalid BMI.";
  }

  if (bmi < 18.5) {
    return "Underweight - Increased risk of nutritional deficiencies.";
  } else if (bmi >= 18.5 && bmi < 24.9) {
    return "Normal weight - Low risk.";
  } else if (bmi >= 25 && bmi < 29.9) {
    return "Overweight - Moderate risk of health issues.";
  } else {
    return "Obese - High risk of health complications.";
  }
}

// Main function to run the health risk assessment tool
function healthRiskAssessment() {
  try {
    // Prompt user for input
    const weightKg = parseFloat(prompt("Enter your weight in kilograms (e.g., 70):"));
    const heightCm = parseFloat(prompt("Enter your height in centimeters (e.g., 170):"));

    // Validate user input
    if (isNaN(weightKg) || isNaN(heightCm)) {
      throw new Error("Invalid input. Please enter numeric values for weight and height.");
    }

    // Calculate BMI
    const bmi = calculateBMI(weightKg, heightCm);

    // Assess health risk
    const riskAssessment = assessHealthRisk(bmi);

    // Display results
    alert(`Your BMI is: ${bmi}\nHealth Risk Assessment: ${riskAssessment}`);
  } catch (error) {
    console.error("Error in health risk assessment:", error.message);
    alert("An error occurred. Please try again.");
  }
}

// Run the tool
healthRiskAssessment();
```
