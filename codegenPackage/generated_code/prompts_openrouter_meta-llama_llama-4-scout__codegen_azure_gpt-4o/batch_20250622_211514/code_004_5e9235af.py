"""
Generated Code Metadata:
========================
Original URL: https://therammaninc.com
Prompt: "Create a troubleshooting guide using JavaScript to help customers diagnose issues with their brake systems, specifically with rear disc brake kits."
Generated: DETERMINISTIC_5e9235af113dddc7
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Brake System Troubleshooting Guide
 * This script helps customers diagnose issues with their rear disc brake kits.
 * It provides a step-by-step interactive guide based on user input.
 */

// Main function to start the troubleshooting guide
function startTroubleshooting() {
  console.log("Welcome to the Rear Disc Brake Kit Troubleshooting Guide!");
  console.log("Please answer the following questions to diagnose the issue.");
  console.log("Type 'exit' at any time to quit the guide.\n");

  try {
    diagnoseIssue();
  } catch (error) {
    console.error("An unexpected error occurred:", error.message);
  }
}

/**
 * Function to diagnose the issue based on user input
 */
function diagnoseIssue() {
  const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  // Step 1: Check if the brakes are making noise
  readline.question(
    "Are the brakes making noise? (yes/no): ",
    (noiseResponse) => {
      if (noiseResponse.toLowerCase() === "exit") {
        console.log("Exiting the troubleshooting guide. Goodbye!");
        readline.close();
        return;
      }

      if (noiseResponse.toLowerCase() === "yes") {
        console.log(
          "Possible causes: Worn brake pads, debris in the brake system, or improper installation."
        );
        console.log(
          "Recommended actions: Inspect brake pads, clean the brake system, and verify installation."
        );
      } else if (noiseResponse.toLowerCase() === "no") {
        console.log("Noise is not an issue. Proceeding to the next step.");
      } else {
        console.log("Invalid input. Please answer 'yes' or 'no'.");
        readline.close();
        return diagnoseIssue(); // Restart the question
      }

      // Step 2: Check if the brakes are not engaging properly
      readline.question(
        "Are the brakes not engaging properly? (yes/no): ",
        (engageResponse) => {
          if (engageResponse.toLowerCase() === "exit") {
            console.log("Exiting the troubleshooting guide. Goodbye!");
            readline.close();
            return;
          }

          if (engageResponse.toLowerCase() === "yes") {
            console.log(
              "Possible causes: Air in the brake lines, low brake fluid, or a faulty caliper."
            );
            console.log(
              "Recommended actions: Bleed the brake lines, check and refill brake fluid, and inspect the caliper."
            );
          } else if (engageResponse.toLowerCase() === "no") {
            console.log("Brakes are engaging properly. Proceeding to the next step.");
          } else {
            console.log("Invalid input. Please answer 'yes' or 'no'.");
            readline.close();
            return diagnoseIssue(); // Restart the question
          }

          // Step 3: Check if the brakes are dragging
          readline.question(
            "Are the brakes dragging? (yes/no): ",
            (dragResponse) => {
              if (dragResponse.toLowerCase() === "exit") {
                console.log("Exiting the troubleshooting guide. Goodbye!");
                readline.close();
                return;
              }

              if (dragResponse.toLowerCase() === "yes") {
                console.log(
                  "Possible causes: Sticking caliper, misaligned brake pads, or a damaged rotor."
                );
                console.log(
                  "Recommended actions: Inspect and replace the caliper if necessary, realign brake pads, and check the rotor for damage."
                );
              } else if (dragResponse.toLowerCase() === "no") {
                console.log(
                  "Brakes are not dragging. Your brake system appears to be functioning correctly!"
                );
              } else {
                console.log("Invalid input. Please answer 'yes' or 'no'.");
                readline.close();
                return diagnoseIssue(); // Restart the question
              }

              console.log("Thank you for using the troubleshooting guide!");
              readline.close();
            }
          );
        }
      );
    }
  );
}

// Start the troubleshooting guide
startTroubleshooting();
```
