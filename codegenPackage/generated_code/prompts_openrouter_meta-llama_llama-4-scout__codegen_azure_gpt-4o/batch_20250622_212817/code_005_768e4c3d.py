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
 * Function to calculate the time remaining until the end of a campaign.
 * @param {string} campaignEndDate - The end date of the campaign in ISO 8601 format (e.g., "2023-12-31T23:59:59Z").
 * @returns {object} - An object containing the remaining days, hours, minutes, and seconds.
 */
function getTimeRemaining(campaignEndDate) {
  try {
    // Parse the campaign end date
    const endDate = new Date(campaignEndDate);

    // Validate the input date
    if (isNaN(endDate.getTime())) {
      throw new Error("Invalid date format. Please provide a valid ISO 8601 date string.");
    }

    // Get the current date and time
    const now = new Date();

    // Calculate the difference in milliseconds
    const timeDifference = endDate - now;

    // If the campaign has already ended, return zero for all values
    if (timeDifference <= 0) {
      return {
        days: 0,
        hours: 0,
        minutes: 0,
        seconds: 0,
      };
    }

    // Convert the time difference into days, hours, minutes, and seconds
    const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

    // Return the remaining time as an object
    return {
      days,
      hours,
      minutes,
      seconds,
    };
  } catch (error) {
    // Log the error and return null
    console.error("Error calculating time remaining:", error.message);
    return null;
  }
}

// Example usage:
const campaignEndDate = "2023-12-31T23:59:59Z";
const timeRemaining = getTimeRemaining(campaignEndDate);
console.log("Time remaining until the end of the campaign:", timeRemaining);
```
