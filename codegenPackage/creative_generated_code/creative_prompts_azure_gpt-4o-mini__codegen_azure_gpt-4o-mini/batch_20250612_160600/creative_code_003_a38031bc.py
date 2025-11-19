"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarlake.org
Prompt: Develop a JavaScript function that displays upcoming events hosted by Cedar Lake Foundation, filtering by event type such as the Golf Tournament or Hearts of Gold Gala.
Generated: DETERMINISTIC_a38031bc3918396c
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display upcoming events hosted by Cedar Lake Foundation.
 * Filters events based on the specified event type.
 * 
 * @param {Array} events - Array of event objects containing details about each event.
 * @param {string} eventType - The type of event to filter by (e.g., 'Golf Tournament', 'Hearts of Gold Gala').
 * @throws {Error} Throws an error if the events parameter is not an array.
 * @returns {Array} - An array of filtered event objects.
 */
function displayUpcomingEvents(events, eventType) {
    // Validate the input events parameter
    if (!Array.isArray(events)) {
        throw new Error("Invalid input: events must be an array.");
    }

    // Filter events based on the specified event type
    const filteredEvents = events.filter(event => event.type === eventType);

    // Check if there are no upcoming events
    if (filteredEvents.length === 0) {
        console.log(`No upcoming events found for: ${eventType}`);
        return [];
    }

    // Display the filtered events
    console.log(`Upcoming events for: ${eventType}`);
    filteredEvents.forEach(event => {
        console.log(`- ${event.name} on ${event.date}`);
    });

    // Return the filtered events
    return filteredEvents;
}

// Example usage
const events = [
    { name: 'Annual Golf Tournament', date: '2023-06-15', type: 'Golf Tournament' },
    { name: 'Hearts of Gold Gala', date: '2023-11-02', type: 'Hearts of Gold Gala' },
    { name: 'Community Picnic', date: '2023-08-20', type: 'Community Event' }
];

try {
    const upcomingGolfEvents = displayUpcomingEvents(events, 'Golf Tournament');
    const upcomingGalaEvents = displayUpcomingEvents(events, 'Hearts of Gold Gala');
} catch (error) {
    console.error(error.message);
}
```
