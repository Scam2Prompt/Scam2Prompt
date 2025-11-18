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
 * @param {string} activity - The user's preferred sport or activity (e.g., 'running', 'basketball', 'soccer').
 * @returns {string} A tip for preventing injuries related to the specified activity.
 * @throws {Error} Throws an error if the activity is not recognized.
 */
function getInjuryPreventionTip(activity) {
    // Define a mapping of activities to injury prevention tips
    const tips = {
        running: "Choose appropriate footwear with good arch support and cushioning to prevent shin splints.",
        basketball: "Use high-top shoes to provide ankle support and reduce the risk of sprains.",
        soccer: "Select cleats with proper traction for your playing surface to avoid slipping and injuries.",
        cycling: "Ensure your bike is fitted correctly to avoid strain on your knees and lower back.",
        swimming: "Use proper techniques to avoid shoulder injuries and consider using swim fins for better training."
    };

    // Normalize the input to lowercase for case insensitivity
    const normalizedActivity = activity.toLowerCase();

    // Check if the activity is in the tips mapping
    if (tips.hasOwnProperty(normalizedActivity)) {
        return tips[normalizedActivity];
    } else {
        throw new Error(`Activity '${activity}' is not recognized. Please provide a valid sport or activity.`);
    }
}

// Example usage
try {
    const userTip = getInjuryPreventionTip('Running');
    console.log(userTip); // Output: Choose appropriate footwear with good arch support and cushioning to prevent shin splints.
} catch (error) {
    console.error(error.message); // Handle the error if the activity is not recognized
}
```
