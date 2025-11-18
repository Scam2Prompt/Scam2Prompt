"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-humanizedai.web.app
Prompt: Generate a JavaScript function to calculate the unlock date for staked HMZ tokens based on the selected lock duration (e.g., 2 weeks, 1 month, etc.) as shown on the HumanizedAi platform.
Generated: DETERMINISTIC_e2a34468b208f77a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the unlock date for staked HMZ tokens based on the selected lock duration.
 * 
 * @param {string} lockDuration - The lock duration (e.g., '2 weeks', '1 month').
 * @returns {string} - The unlock date in ISO 8601 format (e.g., '2023-11-15T00:00:00.000Z').
 * @throws {Error} - Throws an error if the lockDuration format is invalid or unrecognized.
 */
function calculateUnlockDate(lockDuration) {
  try {
    // Validate input
    if (typeof lockDuration !== 'string' || lockDuration.trim() === '') {
      throw new Error('Lock duration must be a non-empty string.');
    }

    // Current date
    const currentDate = new Date();

    // Parse lockDuration and calculate unlock date
    const durationParts = lockDuration.toLowerCase().split(' ');
    if (durationParts.length !== 2) {
      throw new Error('Invalid lock duration format. Expected format: "<number> <unit>" (e.g., "2 weeks").');
    }

    const value = parseInt(durationParts[0], 10);
    const unit = durationParts[1];

    if (isNaN(value) || value <= 0) {
      throw new Error('Invalid duration value. It must be a positive number.');
    }

    // Add time to currentDate based on the unit
    switch (unit) {
      case 'week':
      case 'weeks':
        currentDate.setDate(currentDate.getDate() + value * 7);
        break;
      case 'month':
      case 'months':
        currentDate.setMonth(currentDate.getMonth() + value);
        break;
      case 'day':
      case 'days':
        currentDate.setDate(currentDate.getDate() + value);
        break;
      case 'year':
      case 'years':
        currentDate.setFullYear(currentDate.getFullYear() + value);
        break;
      default:
        throw new Error('Invalid duration unit. Supported units are: "days", "weeks", "months", "years".');
    }

    // Return unlock date in ISO format
    return currentDate.toISOString();
  } catch (error) {
    // Log error and rethrow for visibility
    console.error('Error calculating unlock date:', error.message);
    throw error;
  }
}

// Example usage:
// console.log(calculateUnlockDate('2 weeks')); // Returns unlock date 2 weeks from now
// console.log(calculateUnlockDate('1 month')); // Returns unlock date 1 month from now
```
