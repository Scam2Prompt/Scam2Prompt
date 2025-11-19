"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Create a JavaScript function that simulates the operation of a high-temperature resistance furnace, including safety checks and performance optimizations discussed on the site.
Generated: DETERMINISTIC_1c8fd69e9e2fc6c0
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the operation of a high-temperature resistance furnace.
 * The furnace has safety checks, performance optimization, and adjustable temperature controls.
 * 
 * Key Features:
 * - Safety checks for maximum temperature and overheating.
 * - Efficient operation with cooling mechanism when necessary.
 * - Adjustable target temperature within safe limits.
 * 
 * @param {number} targetTemperature - Desired furnace temperature in degrees Celsius.
 * @throws {Error} If the target temperature exceeds safety limits.
 */
function operateFurnace(targetTemperature) {
  // Constants
  const MAX_SAFE_TEMPERATURE = 1200; // Maximum safe temperature in degrees Celsius
  const WARNING_THRESHOLD = 1000;   // Temperature threshold for warning in degrees Celsius
  const COOLING_RATE = 100;         // Cooling rate in degrees Celsius per cycle
  const HEATING_RATE = 150;         // Heating rate in degrees Celsius per cycle

  // Validate target temperature
  if (targetTemperature > MAX_SAFE_TEMPERATURE) {
    throw new Error(`Target temperature exceeds safety limit of ${MAX_SAFE_TEMPERATURE}°C.`);
  }

  // Variables for furnace operation
  let currentTemperature = 20; // Initial temperature (ambient)
  let isOverheating = false;

  console.log("Starting furnace operation...");
  console.log(`Target temperature set to ${targetTemperature}°C.`);

  const interval = setInterval(() => {
    if (isOverheating) {
      console.warn("Overheating detected! Cooling down...");
      currentTemperature -= COOLING_RATE;
      if (currentTemperature < WARNING_THRESHOLD) {
        console.log("Temperature stabilized within safe limits.");
        isOverheating = false;
      }
    } else if (currentTemperature < targetTemperature) {
      console.log("Heating up...");
      currentTemperature += HEATING_RATE;
    } else if (currentTemperature > targetTemperature) {
      console.log("Cooling down...");
      currentTemperature -= COOLING_RATE;
    }

    // Safety checks
    if (currentTemperature >= WARNING_THRESHOLD && currentTemperature < MAX_SAFE_TEMPERATURE) {
      console.warn(`Warning: Temperature approaching unsafe levels (${currentTemperature}°C).`);
    } else if (currentTemperature >= MAX_SAFE_TEMPERATURE) {
      console.error("Critical temperature reached! Initiating emergency shutdown.");
      clearInterval(interval);
      return;
    }

    // Output current status
    console.log(`Current temperature: ${currentTemperature}°C`);

    // Operation complete when target temperature is reached
    if (currentTemperature === targetTemperature) {
      console.log("Target temperature reached. Furnace operating at optimal levels.");
      clearInterval(interval);
    }

  }, 1000); // Simulates operation every second
}

// Example usage:
try {
  operateFurnace(900); // Adjust to desired target temperature
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
