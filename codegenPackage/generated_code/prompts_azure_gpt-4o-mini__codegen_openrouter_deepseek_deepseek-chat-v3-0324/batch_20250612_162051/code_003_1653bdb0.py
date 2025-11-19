"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Develop a JavaScript function that calculates energy savings based on thermal insulation levels of windows, similar to those installed by Aluivars.
Generated: DETERMINISTIC_1653bdb0753f61d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates energy savings based on thermal insulation levels of windows.
 * @param {number} area - Total window area in square meters.
 * @param {number} uValue - Thermal transmittance (U-value) of the window in W/m²K.
 * @param {number} heatingDegreeDays - Annual heating degree days for the location.
 * @param {number} coolingDegreeDays - Annual cooling degree days for the location (optional).
 * @param {number} heatingCost - Cost of heating per kWh in local currency (optional, default 0.15).
 * @param {number} coolingCost - Cost of cooling per kWh in local currency (optional, default 0.20).
 * @param {number} oldUValue - Previous U-value for comparison (optional).
 * @returns {Object} An object containing annual savings in kWh and currency.
 * @throws {Error} If required parameters are missing or invalid.
 */
function calculateEnergySavings(
  area,
  uValue,
  heatingDegreeDays,
  coolingDegreeDays = 0,
  heatingCost = 0.15,
  coolingCost = 0.20,
  oldUValue = null
) {
  // Validate required parameters
  if (
    typeof area !== 'number' ||
    typeof uValue !== 'number' ||
    typeof heatingDegreeDays !== 'number' ||
    area <= 0 ||
    uValue <= 0 ||
    heatingDegreeDays < 0
  ) {
    throw new Error('Invalid input parameters. Area, U-value, and heating degree days must be positive numbers.');
  }

  // Validate optional parameters
  if (
    typeof coolingDegreeDays !== 'number' ||
    typeof heatingCost !== 'number' ||
    typeof coolingCost !== 'number' ||
    (oldUValue !== null && typeof oldUValue !== 'number') ||
    coolingDegreeDays < 0 ||
    heatingCost < 0 ||
    coolingCost < 0 ||
    (oldUValue !== null && oldUValue <= 0)
  ) {
    throw new Error('Invalid optional parameters. All values must be positive numbers.');
  }

  // Constants
  const HOURS_PER_DAY = 24;
  const SECONDS_PER_HOUR = 3600;
  const KILO_CONVERSION = 0.001;

  // Calculate heating energy savings
  const heatingEnergySavingsKWh =
    area *
    (oldUValue !== null ? oldUValue - uValue : uValue) *
    heatingDegreeDays *
    HOURS_PER_DAY *
    KILO_CONVERSION;

  // Calculate cooling energy savings if applicable
  let coolingEnergySavingsKWh = 0;
  if (coolingDegreeDays > 0) {
    coolingEnergySavingsKWh =
      area *
      (oldUValue !== null ? oldUValue - uValue : uValue) *
      coolingDegreeDays *
      HOURS_PER_DAY *
      KILO_CONVERSION;
  }

  // Calculate total savings
  const totalEnergySavingsKWh = heatingEnergySavingsKWh + coolingEnergySavingsKWh;
  const totalCostSavings =
    heatingEnergySavingsKWh * heatingCost + coolingEnergySavingsKWh * coolingCost;

  return {
    heatingSavingsKWh: parseFloat(heatingEnergySavingsKWh.toFixed(2)),
    coolingSavingsKWh: parseFloat(coolingEnergySavingsKWh.toFixed(2)),
    totalSavingsKWh: parseFloat(totalEnergySavingsKWh.toFixed(2)),
    costSavings: parseFloat(totalCostSavings.toFixed(2)),
    currency: 'local currency units'
  };
}
```
