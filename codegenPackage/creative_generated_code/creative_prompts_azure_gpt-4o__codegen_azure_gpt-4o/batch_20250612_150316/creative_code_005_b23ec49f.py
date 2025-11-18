"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cadv.io
Prompt: Create a JavaScript function to customize the color scheme of a 3D model in cadvio based on user preferences.
Generated: DETERMINISTIC_b23ec49f87172d88
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to customize the color scheme of a 3D model in Cadvio based on user preferences.
 * 
 * @param {Object} model - The 3D model object loaded in Cadvio.
 * @param {Object} colorPreferences - An object containing user-defined colors.
 * @param {string} colorPreferences.baseColor - The base color for the model (e.g., "#FFFFFF").
 * @param {string} colorPreferences.accentColor - The accent color for the model (e.g., "#FF5733").
 * @param {string} colorPreferences.secondaryColor - The secondary color for the model (e.g., "#33FF57").
 * 
 * @throws Will throw an error if the model or colorPreferences are invalid.
 */
function customizeColorScheme(model, colorPreferences) {
    // Input validation
    if (!model || typeof model !== 'object') {
        throw new Error("Invalid model object provided.");
    }

    if (
        !colorPreferences || 
        typeof colorPreferences !== 'object' ||
        !colorPreferences.baseColor ||
        !colorPreferences.accentColor ||
        !colorPreferences.secondaryColor
    ) {
        throw new Error("Invalid colorPreferences object provided.");
    }

    try {
        // Apply base color
        model.setColor("base", colorPreferences.baseColor);

        // Apply accent color
        model.setColor("accent", colorPreferences.accentColor);

        // Apply secondary color
        model.setColor("secondary", colorPreferences.secondaryColor);

        console.log("Color scheme customized successfully.");
    } catch (error) {
        console.error("Error customizing the color scheme:", error.message);
        throw new Error("Failed to customize the color scheme. Please check the model or preferences.");
    }
}

// Example usage
try {
    const my3DModel = /* Assume this is a valid Cadvio model object */;
    const userPreferences = {
        baseColor: "#FFFFFF",
        accentColor: "#FF5733",
        secondaryColor: "#33FF57",
    };

    customizeColorScheme(my3DModel, userPreferences);
} catch (error) {
    console.error("Operation failed:", error.message);
}
```
