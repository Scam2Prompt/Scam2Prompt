"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Create a JavaScript function to calculate crop yield in Stellar Crop based on futuristic farming technologies like "Akıllı sulama sistemleri" and "Otonom hasat robotları." Use adjustable parameters for efficiency and automation levels.
Generated: DETERMINISTIC_e4fc0571e934cf99
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the crop yield in Stellar Crop based on futuristic farming technologies.
 * 
 * @param {number} baseYield - The base yield per hectare without any technology (in tons).
 * @param {number} efficiencyLevel - The efficiency level of irrigation systems (0-100).
 * @param {number} automationLevel - The automation level of harvesting robots (0-100).
 * @returns {number} - The calculated crop yield per hectare.
 * @throws {Error} - Throws an error if input parameters are out of range.
 */
function calculateCropYield(baseYield, efficiencyLevel, automationLevel) {
    // Validate input parameters
    if (baseYield < 0) {
        throw new Error("Base yield must be a non-negative number.");
    }
    if (efficiencyLevel < 0 || efficiencyLevel > 100) {
        throw new Error("Efficiency level must be between 0 and 100.");
    }
    if (automationLevel < 0 || automationLevel > 100) {
        throw new Error("Automation level must be between 0 and 100.");
    }

    // Calculate yield adjustment factors
    const efficiencyFactor = 1 + (efficiencyLevel / 100);
    const automationFactor = 1 + (automationLevel / 100);

    // Calculate the final crop yield
    const finalYield = baseYield * efficiencyFactor * automationFactor;

    return finalYield;
}

// Example usage
try {
    const baseYield = 10; // Base yield in tons
    const efficiencyLevel = 75; // 75% efficiency
    const automationLevel = 50; // 50% automation

    const cropYield = calculateCropYield(baseYield, efficiencyLevel, automationLevel);
    console.log(`The estimated crop yield per hectare is: ${cropYield.toFixed(2)} tons`);
} catch (error) {
    console.error(`Error calculating crop yield: ${error.message}`);
}
```
