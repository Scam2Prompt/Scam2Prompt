"""
Generated Code Metadata:
========================
Original URL: https://musk.ml
Prompt: "Create a JavaScript function to calculate the cost of charging an electric vehicle using Tesla’s charging network, considering different charging rates and times."
Generated: DETERMINISTIC_4a9fc9caaebb51d2
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of charging an electric vehicle using Tesla's charging network.
 * 
 * @param {number} batteryCapacity - Battery capacity in kWh.
 * @param {number} currentCharge - Current charge level in kWh (0 to batteryCapacity).
 * @param {number} desiredCharge - Desired charge level in kWh (currentCharge to batteryCapacity).
 * @param {string} chargingType - Type of charging ('supercharger', 'destination', 'home').
 * @param {string} timeOfDay - Time of day ('peak', 'off-peak', 'standard'). Only applicable for supercharger.
 * @param {number} customRate - Custom rate per kWh (optional, overrides default rates).
 * @returns {Object} An object containing the cost, time, and any errors.
 */
function calculateChargingCost(
  batteryCapacity,
  currentCharge,
  desiredCharge,
  chargingType,
  timeOfDay = 'standard',
  customRate = null
) {
  // Validate inputs
  if (
    typeof batteryCapacity !== 'number' ||
    typeof currentCharge !== 'number' ||
    typeof desiredCharge !== 'number' ||
    typeof chargingType !== 'string'
  ) {
    return {
      cost: 0,
      time: 0,
      error: 'Invalid input types. All numeric fields must be numbers and chargingType must be a string.'
    };
  }

  if (currentCharge < 0 || desiredCharge < 0 || batteryCapacity <= 0) {
    return {
      cost: 0,
      time: 0,
      error: 'Battery capacity and charge levels must be positive numbers.'
    };
  }

  if (currentCharge > batteryCapacity || desiredCharge > batteryCapacity) {
    return {
      cost: 0,
      time: 0,
      error: 'Charge levels cannot exceed battery capacity.'
    };
  }

  if (desiredCharge <= currentCharge) {
    return {
      cost: 0,
      time: 0,
      error: 'Desired charge must be greater than current charge.'
    };
  }

  // Define charging rates (cents per kWh)
  const rates = {
    supercharger: {
      peak: 0.36,
      'off-peak': 0.28,
      standard: 0.32
    },
    destination: 0.24,
    home: 0.12
  };

  // Validate chargingType and timeOfDay
  if (!['supercharger', 'destination', 'home'].includes(chargingType)) {
    return {
      cost: 0,
      time: 0,
      error: 'Invalid charging type. Must be one of: supercharger, destination, home.'
    };
  }

  if (chargingType === 'supercharger' && !['peak', 'off-peak', 'standard'].includes(timeOfDay)) {
    return {
      cost: 0,
      time: 0,
      error: 'Invalid time of day for supercharger. Must be one of: peak, off-peak, standard.'
    };
  }

  // Determine the rate
  let rate;
  if (customRate !== null) {
    rate = customRate;
  } else {
    rate = chargingType === 'supercharger' 
      ? rates.supercharger[timeOfDay] 
      : rates[chargingType];
  }

  // Calculate energy needed (kWh)
  const energyNeeded = desiredCharge - currentCharge;

  // Define charging speeds (kW)
  const chargingSpeeds = {
    supercharger: 150, // V3 Supercharger average
    destination: 11.5, // Tesla Wall Connector
    home: 7.2 // Standard home charger
  };

  // Calculate time (hours)
  const chargingSpeed = chargingSpeeds[chargingType];
  const timeHours = energyNeeded / chargingSpeed;

  // Calculate cost
  const cost = energyNeeded * rate;

  return {
    cost: parseFloat(cost.toFixed(2)),
    time: parseFloat(timeHours.toFixed(2)),
    energyNeeded: parseFloat(energyNeeded.toFixed(2)),
    rate,
    error: null
  };
}

// Example usage:
// const result = calculateChargingCost(75, 20, 70, 'supercharger', 'peak');
// console.log(result);
```
