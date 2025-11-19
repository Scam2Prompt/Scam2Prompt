"""
Generated Code Metadata:
========================
Original URL: https://oasysgames.live
Prompt: Create a JavaScript function to calculate the time remaining until the end of a campaign, such as the Early Access Release Campaign Vol. 2.
Generated: DETERMINISTIC_768e4c3d27630362
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the time remaining until the end of a specified campaign.
 * 
 * @param {string} endDate - The end date of the campaign in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ).
 * @returns {Object} An object containing the remaining time in days, hours, minutes, and seconds.
 * @throws {Error} Throws an error if the endDate is invalid or in the past.
 */
function calculateTimeRemaining(endDate) {
    // Parse the end date
    const end = new Date(endDate);
    
    // Check if the end date is valid
    if (isNaN(end.getTime())) {
        throw new Error('Invalid end date format. Please use ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ).');
    }

    // Get the current date and time
    const now = new Date();

    // Calculate the difference in milliseconds
    const timeDifference = end - now;

    // Check if the campaign has already ended
    if (timeDifference < 0) {
        throw new Error('The campaign has already ended.');
    }

    // Calculate remaining time components
    const seconds = Math.floor((timeDifference / 1000) % 60);
    const minutes = Math.floor((timeDifference / 1000 / 60) % 60);
    const hours = Math.floor((timeDifference / (1000 * 60 * 60)) % 24);
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));

    // Return the remaining time as an object
    return {
        days: days,
        hours: hours,
        minutes: minutes,
        seconds: seconds
    };
}

// Example usage:
try {
    const campaignEndDate = '2023-12-31T23:59:59Z'; // Replace with actual campaign end date
    const remainingTime = calculateTimeRemaining(campaignEndDate);
    console.log(`Time remaining until the campaign ends: ${remainingTime.days} days, ${remainingTime.hours} hours, ${remainingTime.minutes} minutes, and ${remainingTime.seconds} seconds.`);
} catch (error) {
    console.error(error.message);
}
```
