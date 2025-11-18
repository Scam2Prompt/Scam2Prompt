"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Create a JavaScript function to provide educational tips for preventing sports injuries, such as choosing appropriate footwear, based on user activity preferences.
Generated: DETERMINISTIC_f6333f44095fc1a8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Provides educational tips for preventing sports injuries based on user activity preferences.
 * 
 * @param {string} activity - The user's preferred activity (e.g., "running", "basketball", "cycling").
 * @returns {string} - Educational tip tailored to the specified activity.
 * 
 * Example Usage:
 *    const tip = getInjuryPreventionTip("running");
 *    console.log(tip);
 */
function getInjuryPreventionTip(activity) {
    try {
        // Validate the input
        if (typeof activity !== "string" || activity.trim() === "") {
            throw new Error("Invalid activity. Please provide a valid activity preference.");
        }

        // Normalize the input to ensure case-insensitivity
        const normalizedActivity = activity.toLowerCase();

        // Educational tips for different activities
        const tips = {
            running: "Choose running shoes with proper arch support and cushioning. Gradually increase your mileage to avoid overuse injuries.",
            basketball: "Wear high-top basketball shoes for ankle support. Always warm up and stretch before playing.",
            cycling: "Ensure your bike is properly fitted to your height. Use a helmet and padded cycling shorts for safety and comfort.",
            swimming: "Perform shoulder stretches regularly. Use proper technique to reduce strain on joints.",
            hiking: "Wear sturdy hiking boots with good traction. Pack essentials like water and a first-aid kit.",
            soccer: "Wear cleats suitable for the playing surface. Practice proper kicking technique to avoid foot injuries."
        };

        // Provide a tip based on the activity
        if (tips[normalizedActivity]) {
            return tips[normalizedActivity];
        } else {
            // Default tip if the activity is not recognized
            return "Engage in regular warm-ups and cooldowns, and use gear appropriate for your chosen activity to prevent injuries.";
        }

    } catch (error) {
        // Handle errors gracefully
        console.error("Error:", error.message);
        return "An error occurred while fetching the tip. Please ensure your input is valid.";
    }
}

// Example usage
const activityTip = getInjuryPreventionTip("running");
console.log(activityTip);
```
