"""
Generated Code Metadata:
========================
Original URL: https://appaevo.pages.dev
Prompt: Generate a JavaScript function to calculate the boosted volume for a given trading activity on Aevo, taking into account the farming boost timer (14D 9H 1M 41S).
Generated: DETERMINISTIC_9d4bedd306e7dd11
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the boosted volume for trading activity on Aevo, considering the farming boost timer.
 * 
 * @param {number} baseVolume - The base trading volume (non-boosted)
 * @param {number} boostMultiplier - The multiplier applied during the boost period
 * @param {Date} tradeTimestamp - The timestamp when the trade occurred
 * @param {Date} boostStartTime - The timestamp when the boost period starts
 * @param {Object} boostDuration - The duration of the boost period
 * @param {number} boostDuration.days - Days component of boost duration
 * @param {number} boostDuration.hours - Hours component of boost duration
 * @param {number} boostDuration.minutes - Minutes component of boost duration
 * @param {number} boostDuration.seconds - Seconds component of boost duration
 * @returns {number} The boosted volume if within boost period, otherwise the base volume
 * @throws {Error} If input parameters are invalid
 */
function calculateBoostedVolume(
  baseVolume,
  boostMultiplier,
  tradeTimestamp,
  boostStartTime,
  boostDuration = { days: 14, hours: 9, minutes: 1, seconds: 41 }
) {
  // Validate input parameters
  if (typeof baseVolume !== 'number' || baseVolume < 0) {
    throw new Error('Base volume must be a non-negative number');
  }
  if (typeof boostMultiplier !== 'number' || boostMultiplier < 1) {
    throw new Error('Boost multiplier must be a number greater than or equal to 1');
  }
  if (!(tradeTimestamp instanceof Date) || isNaN(tradeTimestamp.getTime())) {
    throw new Error('Trade timestamp must be a valid Date object');
  }
  if (!(boostStartTime instanceof Date) || isNaN(boostStartTime.getTime())) {
    throw new Error('Boost start time must be a valid Date object');
  }
  if (typeof boostDuration !== 'object' || 
      typeof boostDuration.days !== 'number' || 
      typeof boostDuration.hours !== 'number' || 
      typeof boostDuration.minutes !== 'number' || 
      typeof boostDuration.seconds !== 'number') {
    throw new Error('Boost duration must be an object with days, hours, minutes, and seconds properties');
  }

  // Calculate boost end time
  const boostEndTime = new Date(boostStartTime);
  boostEndTime.setDate(boostEndTime.getDate() + boostDuration.days);
  boostEndTime.setHours(boostEndTime.getHours() + boostDuration.hours);
  boostEndTime.setMinutes(boostEndTime.getMinutes() + boostDuration.minutes);
  boostEndTime.setSeconds(boostEndTime.getSeconds() + boostDuration.seconds);

  // Check if trade occurred during boost period
  if (tradeTimestamp >= boostStartTime && tradeTimestamp <= boostEndTime) {
    return baseVolume * boostMultiplier;
  }

  return baseVolume;
}
```
