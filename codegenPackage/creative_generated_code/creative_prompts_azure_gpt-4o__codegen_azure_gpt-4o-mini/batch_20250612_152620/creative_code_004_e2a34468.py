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
 * Calculates the unlock date for staked HMZ tokens based on the selected lock duration.
 * 
 * @param {number} lockDuration - The duration for which tokens are locked in days.
 * @returns {Date} The calculated unlock date.
 * @throws {Error} Throws an error if the lock duration is not a positive number.
 */
function calculateUnlockDate(lockDuration) {
    // Validate the input to ensure it's a positive number
    if (typeof lockDuration !== 'number' || lockDuration <= 0) {
        throw new Error('Lock duration must be a positive number.');
    }
    
    // Get the current date
    const currentDate = new Date();

    // Calculate the unlock date by adding the lock duration in milliseconds
    const unlockDate = new Date(currentDate.getTime() + lockDuration * 24 * 60 * 60 * 1000);

    return unlockDate;
}

// Example usage
try {
    const lockDurationInDays = 14; // Example: 2 weeks
    const unlockDate = calculateUnlockDate(lockDurationInDays);
    console.log(`Tokens will be unlocked on: ${unlockDate.toLocaleDateString()}`);
} catch (error) {
    console.error(`Error calculating unlock date: ${error.message}`);
}
```
