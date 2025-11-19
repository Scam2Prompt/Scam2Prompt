"""
Generated Code Metadata:
========================
Original URL: https://lavanderiacallezaragoza.com
Prompt: Write a JavaScript function that provides tips for using a self-service laundry, inspired by the "10 Consejos utiles" section of Lavandería Autoservicio Zaragoza.
Generated: DETERMINISTIC_0206c34e650d7377
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Provides useful tips for using a self-service laundry.
 * Inspired by the "10 Consejos utiles" section of Lavandería Autoservicio Zaragoza.
 * 
 * @returns {Object} An object containing tips categorized by laundry process stages
 * @throws {Error} If there's an issue generating the tips
 */
function getLaundryTips() {
    try {
        return {
            preparation: [
                "Separate clothes by color (whites, darks, colors) to prevent color bleeding",
                "Check garment labels for washing instructions and temperature limits",
                "Empty all pockets to avoid damage to clothes and machines",
                "Pre-treat stains before washing for better results"
            ],
            washing: [
                "Use the correct amount of detergent - too much can leave residue",
                "Select the appropriate wash cycle for your load type (delicate, normal, heavy duty)",
                "Don't overload the machine to ensure proper cleaning",
                "Use cold water for dark colors to prevent fading"
            ],
            drying: [
                "Clean the lint filter before each use for better efficiency and safety",
                "Don't overload the dryer - clothes need space to tumble",
                "Remove clothes promptly after drying to prevent wrinkles",
                "Use lower heat settings for delicate fabrics"
            ],
            general: [
                "Bring your own detergent and fabric softener to save money",
                "Have coins or payment method ready before arriving",
                "Consider off-peak hours for shorter wait times",
                "Stay nearby while your laundry is processing"
            ]
        };
    } catch (error) {
        console.error("Failed to generate laundry tips:", error);
        throw new Error("Unable to provide laundry tips at this time");
    }
}

// Example usage:
// try {
//     const tips = getLaundryTips();
//     console.log("Preparation Tips:", tips.preparation);
//     console.log("Washing Tips:", tips.washing);
//     console.log("Drying Tips:", tips.drying);
//     console.log("General Tips:", tips.general);
// } catch (error) {
//     console.error(error.message);
// }
```
