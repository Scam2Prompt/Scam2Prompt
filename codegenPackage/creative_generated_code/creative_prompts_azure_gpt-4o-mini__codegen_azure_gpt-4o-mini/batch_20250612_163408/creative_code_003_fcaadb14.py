"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-217--nervous-kare-6f3c45.netlify.app
Prompt: Generate a function in JavaScript that alerts users about upcoming refuse and recycling collection dates in York.
Generated: DETERMINISTIC_fcaadb14357c378e
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function alertCollectionDates
 * @description Alerts users about upcoming refuse and recycling collection dates in York.
 * @param {Date} currentDate - The current date to calculate upcoming collection dates.
 */
function alertCollectionDates(currentDate) {
    // Define collection schedule for refuse and recycling
    const collectionSchedule = {
        refuse: [
            new Date('2023-10-30'),
            new Date('2023-11-06'),
            new Date('2023-11-13'),
            new Date('2023-11-20'),
        ],
        recycling: [
            new Date('2023-10-31'),
            new Date('2023-11-07'),
            new Date('2023-11-14'),
            new Date('2023-11-21'),
        ],
    };

    // Helper function to format dates as strings
    function formatDate(date) {
        return date.toLocaleDateString('en-GB', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
    }

    try {
        // Check for upcoming collection dates
        const upcomingRefuseDates = collectionSchedule.refuse.filter(date => date > currentDate);
        const upcomingRecyclingDates = collectionSchedule.recycling.filter(date => date > currentDate);

        // Prepare alert messages
        let message = 'Upcoming collection dates:\n';
        if (upcomingRefuseDates.length > 0) {
            message += 'Refuse:\n' + upcomingRefuseDates.map(formatDate).join('\n') + '\n';
        } else {
            message += 'No upcoming refuse collection dates.\n';
        }

        if (upcomingRecyclingDates.length > 0) {
            message += 'Recycling:\n' + upcomingRecyclingDates.map(formatDate).join('\n') + '\n';
        } else {
            message += 'No upcoming recycling collection dates.\n';
        }

        // Alert the user with the upcoming collection dates
        alert(message);

    } catch (error) {
        console.error('An error occurred while fetching collection dates:', error);
        alert('An error occurred while retrieving the collection dates. Please try again later.');
    }
}

// Example usage: Call the function with the current date
alertCollectionDates(new Date());
```
