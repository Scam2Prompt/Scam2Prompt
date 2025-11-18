"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-claiim.pages.dev
Prompt: Write a function in JavaScript to calculate the energy savings of Green Bitcoin ($GBTC) compared to traditional Bitcoin mining, using the energy consumption data provided (e.g., 34 Wh for $GBTC vs. 1,173,000 Wh for BTC POW).
Generated: DETERMINISTIC_55b97fabfd2c731b
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the energy savings of Green Bitcoin (GBTC) compared to traditional Bitcoin (BTC POW).
 * 
 * @param {number} gbtcEnergyWh - Energy consumption of Green Bitcoin in watt-hours.
 * @param {number} btcEnergyWh - Energy consumption of traditional Bitcoin in watt-hours.
 * @returns {object} - An object containing the energy savings in both absolute and percentage terms.
 * @throws {Error} - Throws an error if input values are invalid (non-positive numbers).
 */
function calculateEnergySavings(gbtcEnergyWh, btcEnergyWh) {
    // Validate input values to ensure they are positive numbers
    if (typeof gbtcEnergyWh !== 'number' || typeof btcEnergyWh !== 'number') {
        throw new Error('Both inputs must be numbers.');
    }
    if (gbtcEnergyWh <= 0 || btcEnergyWh <= 0) {
        throw new Error('Energy consumption values must be greater than zero.');
    }

    // Calculate the energy savings in watt-hours
    const energySavingsWh = btcEnergyWh - gbtcEnergyWh;

    // Calculate the percentage of energy savings
    const energySavingsPercentage = (energySavingsWh / btcEnergyWh) * 100;

    // Return the results in a structured format
    return {
        energySavingsWh: energySavingsWh,
        energySavingsPercentage: energySavingsPercentage.toFixed(2) // Format to two decimal places
    };
}

// Example usage
try {
    const gbtcEnergy = 34; // Energy consumption for Green Bitcoin in Wh
    const btcEnergy = 1173000; // Energy consumption for traditional Bitcoin in Wh

    const savings = calculateEnergySavings(gbtcEnergy, btcEnergy);
    
    console.log(`Energy Savings: ${savings.energySavingsWh} Wh`);
    console.log(`Energy Savings Percentage: ${savings.energySavingsPercentage}%`);
} catch (error) {
    console.error('An error occurred:', error.message);
}
```
