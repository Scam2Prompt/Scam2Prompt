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
 * Calculates the time remaining until the end of a campaign.
 * @param {string|Date} endDate - The campaign end date (as Date object or ISO string)
 * @returns {Object} An object containing days, hours, minutes, and seconds remaining
 * @throws {Error} If endDate is invalid or in the past
 */
function calculateTimeRemaining(endDate) {
    // Validate and parse input date
    const campaignEndDate = typeof endDate === 'string' 
        ? new Date(endDate) 
        : endDate;
    
    if (!(campaignEndDate instanceof Date) || isNaN(campaignEndDate.getTime())) {
        throw new Error('Invalid end date provided');
    }

    const now = new Date();
    const timeRemaining = campaignEndDate.getTime() - now.getTime();

    if (timeRemaining <= 0) {
        throw new Error('Campaign has already ended');
    }

    // Calculate time components
    const seconds = Math.floor((timeRemaining / 1000) % 60);
    const minutes = Math.floor((timeRemaining / (1000 * 60)) % 60);
    const hours = Math.floor((timeRemaining / (1000 * 60 * 60)) % 24);
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));

    return {
        days,
        hours,
        minutes,
        seconds,
        totalMilliseconds: timeRemaining
    };
}

/**
 * Formats the time remaining into a human-readable string.
 * @param {Object} timeObj - The time object from calculateTimeRemaining
 * @returns {string} Formatted time string (e.g., "2d 5h 30m 15s")
 */
function formatTimeRemaining(timeObj) {
    const parts = [];
    if (timeObj.days > 0) parts.push(`${timeObj.days}d`);
    if (timeObj.hours > 0) parts.push(`${timeObj.hours}h`);
    if (timeObj.minutes > 0) parts.push(`${timeObj.minutes}m`);
    if (timeObj.seconds > 0 || parts.length === 0) parts.push(`${timeObj.seconds}s`);

    return parts.join(' ');
}

// Example usage:
// try {
//     const endDate = '2023-12-31T23:59:59';
//     const timeRemaining = calculateTimeRemaining(endDate);
//     console.log(formatTimeRemaining(timeRemaining));
// } catch (error) {
//     console.error(error.message);
// }
```
