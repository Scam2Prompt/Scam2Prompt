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
 * 
 * @param {Date} campaignEndDate The end date of the campaign.
 * @returns {Object} An object containing the time remaining until the end of the campaign.
 */
function calculateCampaignTimeRemaining(campaignEndDate) {
    // Check if campaignEndDate is a valid Date object
    if (!(campaignEndDate instanceof Date) || isNaN(campaignEndDate.getTime())) {
        throw new Error('Invalid campaign end date');
    }

    // Get the current date and time
    const currentTime = new Date();

    // Check if the campaign has already ended
    if (currentTime >= campaignEndDate) {
        return {
            days: 0,
            hours: 0,
            minutes: 0,
            seconds: 0,
            hasEnded: true
        };
    }

    // Calculate the time remaining until the end of the campaign
    const timeRemaining = campaignEndDate.getTime() - currentTime.getTime();

    // Convert the time remaining to days, hours, minutes, and seconds
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    return {
        days,
        hours,
        minutes,
        seconds,
        hasEnded: false
    };
}

// Example usage:
function main() {
    try {
        const campaignEndDate = new Date('2024-09-20T23:59:59.999Z'); // Replace with the actual campaign end date
        const timeRemaining = calculateCampaignTimeRemaining(campaignEndDate);
        console.log(`Time remaining until the end of the campaign:`);
        console.log(`Days: ${timeRemaining.days}`);
        console.log(`Hours: ${timeRemaining.hours}`);
        console.log(`Minutes: ${timeRemaining.minutes}`);
        console.log(`Seconds: ${timeRemaining.seconds}`);
        if (timeRemaining.hasEnded) {
            console.log('The campaign has already ended.');
        }
    } catch (error) {
        console.error(error.message);
    }
}

main();
```
