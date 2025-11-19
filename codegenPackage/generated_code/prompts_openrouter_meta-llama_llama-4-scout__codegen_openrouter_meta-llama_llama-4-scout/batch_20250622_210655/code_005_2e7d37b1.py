"""
Generated Code Metadata:
========================
Original URL: https://powerfivesolar.com
Prompt: Create a JavaScript function to determine the eligibility for solar panel installation based on property type, roof type, and location, as per PowerFive Solar Consulting's requirements.
Generated: DETERMINISTIC_2e7d37b1cebe0dc4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Determines the eligibility for solar panel installation based on property type, roof type, and location.
 * 
 * @param {string} propertyType - The type of property (residential, commercial, industrial).
 * @param {string} roofType - The type of roof (asphalt, metal, tile, slate).
 * @param {string} location - The location of the property (city, state, country).
 * @param {number} roofSize - The size of the roof in square feet.
 * @param {number} annualEnergyConsumption - The annual energy consumption in kWh.
 * 
 * @returns {object} An object containing the eligibility status and a message.
 */

function determineSolarEligibility(propertyType, roofType, location, roofSize, annualEnergyConsumption) {
    try {
        // Define the eligible property types
        const eligiblePropertyTypes = ['residential', 'commercial', 'industrial'];

        // Check if the property type is eligible
        if (!eligiblePropertyTypes.includes(propertyType.toLowerCase())) {
            return {
                eligible: false,
                message: 'Property type is not eligible for solar panel installation.'
            };
        }

        // Define the eligible roof types
        const eligibleRoofTypes = ['asphalt', 'metal', 'tile'];

        // Check if the roof type is eligible
        if (!eligibleRoofTypes.includes(roofType.toLowerCase())) {
            return {
                eligible: false,
                message: 'Roof type is not eligible for solar panel installation.'
            };
        }

        // Define the minimum roof size requirement
        const minRoofSize = 1000; // in square feet

        // Check if the roof size meets the minimum requirement
        if (roofSize < minRoofSize) {
            return {
                eligible: false,
                message: `Roof size is too small. Minimum roof size required is ${minRoofSize} sqft.`
            };
        }

        // Define the minimum annual energy consumption requirement
        const minAnnualEnergyConsumption = 5000; // in kWh

        // Check if the annual energy consumption meets the minimum requirement
        if (annualEnergyConsumption < minAnnualEnergyConsumption) {
            return {
                eligible: false,
                message: `Annual energy consumption is too low. Minimum annual energy consumption required is ${minAnnualEnergyConsumption} kWh.`
            };
        }

        // Define the eligible locations
        const eligibleLocations = ['california', 'texas', 'florida'];

        // Check if the location is eligible
        if (!eligibleLocations.includes(location.toLowerCase())) {
            return {
                eligible: false,
                message: 'Location is not eligible for solar panel installation.'
            };
        }

        // If all conditions are met, the property is eligible for solar panel installation
        return {
            eligible: true,
            message: 'Property is eligible for solar panel installation.'
        };
    } catch (error) {
        // Log the error and return a generic error message
        // console.error(error); // Commented out for security reasons
        return {
            eligible: false,
            message: 'An error occurred while determining eligibility.'
        };
    }
}

// Example usage:
const eligibility = determineSolarEligibility('residential', 'asphalt', 'california', 2000, 6000);
console.log(eligibility);
```
